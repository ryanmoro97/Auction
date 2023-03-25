import sqlite3
import time
import getpass
import string
import sys
from datetime import date
from operator import itemgetter
import re

conn = None
cur = None
username = None

# main loop of program, setup database and go to login screen
def main():
    global conn, cur
    # get db
    path ='./' + get_dbname()
    connect(path)
    # main menu
    login_screen()
    conn.commit()
    conn.close()
    return

# db name should be provided as command line arg
# if not provided, prompt to enter it 
def get_dbname():
    if(len(sys.argv) == 2):
        return sys.argv[1]
    else:
        return input("No database file provided. Enter it now: ")

# connect to the specified database
def connect(path):
    global conn, cur
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    conn.commit()
    return

# main menu: allow users to sign in, register or exit
def login_screen():
    while(True):
        print('\nOptions:\n'
                  +'Sign in (s)\n'
                  +'Register (r)\n'
                  +'Exit program (e)\n')
        action = input("Select an option: ").lower()
        if(action == 's'):
            login()
        elif(action == 'r'):
            register()
        elif(action == 'e'):
            break
        else:
            print("Invalid command, try again\n")

# function called if user wants to log in
def login():
    global username
    cnt = 0
    while True:
        print("If you wish to exit type e on the username")
        username = input("Username: ")
        if (username == 'e'):
            return
        # echo free input for pwd assuming console allows echo free input
        pwd = getpass.getpass("Password: ", None)
        #make sure user or pwd is not empty
        if not (username.strip() and pwd.strip()):
            print("Missing information, try again")
            continue
        loginInfo = username + " " + pwd
        #check if valid login 
        if chkInfo(loginInfo, 'l') == False:
            cnt += 1
            print("Invalid username or password.  Try again")
            if cnt == 3:
                val = input("Consider registering? (y/n)")
                if val.lower() == 'y':
                    register()
                    return
                else:
                    cnt = 0
        else:
            print("Successful login\n")
            loggedIn()
            break
    return

# function called if users wants to register
def register():
    global conn, cur, username
    while True:
        print("Please enter the following information to register:")
        print("to exit type e on the email input\n")
        username = input("Email: ")
        if (username == 'e'):
            return
        pwd = getpass.getpass("Password: ", None).strip()
        if not (username and pwd):
            print("Invalid: Username and password cannot be blank")
            continue
        #check if email is valid format
        regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
        if not re.search(regex,username):
            print("Invalid email, try again")
            continue
        regInfo = username + " " + pwd
        if not chkInfo(regInfo, "r"):
            print("Username is taken.  Try again\n")
            val = input("Consider logging in with that email? (y/n)")
            if val.lower() == 'y':
                login()
                return
            continue
        # get valid gender
        while(True):
            gender = input("gender (M, F, O): ").strip()
            if gender.lower() not in "m, f, o":
                print("Invalid: Gender must be one of M,F,O")
                continue
            if not gender:
                print("Gender cannot be left blank, try again")
            break
        # get valid city/prov
        while(True):
            city = input("City: ").strip()
            prov = input("Province abbreviation: ").upper().strip()
            if not (city and prov):
                print("Invalid: Must enter a city and province")
                continue
            city = city + ", " + prov
            break
        # get valid name
        while(True):
            name = input("Name: ").strip()
            if not name:
                print("Invalid: Name cannot be left blank")
                continue
            break
        print("Successful registration. Logging in now\n")
        cur.execute("INSERT INTO users (email, name, pwd, city, gender) \
                    VALUES(?,?,?,?,?);", (username, name, pwd, city, gender))
        conn.commit()
        break
    loggedIn()
    return

# function to check if login or register information is correct
#inputs: info - "email pwd", type - "r" for registering users, "l" for logging in
def chkInfo(info, type):
    global conn, cur
    inf = info.split()
    username = inf[0]
    pwd = inf[1]
    if type == "r":
      # check if username is taken
        cur.execute("SELECT * FROM users WHERE email LIKE ?;",(username,))
        if len(cur.fetchall()) != 0:
            return False
    elif type == "l":
        #check if the user & pwd exists 
        cur.execute("SELECT * FROM users WHERE email LIKE ? and pwd=? ;",(username,pwd))
        if len(cur.fetchall()) != 1:
            return False
    return True

# function for logged in users
def loggedIn():
    print("You Have logged in successfully")
    print("\nCongrats!!!\n")
    logged_in = True
    while(logged_in):
        print('\nOptions:\n'
              +'List products (l)\n'
              +'Search for sale (s)\n'
              +'Post a sale (p)\n'
              +'Search for user (u)\n'
              +'Logout (q)\n')
        opt = input('Select an option : ').lower()
        if opt == 'q':
            logged_in = False
        elif opt.lower() == 'l':
            list_prod()
        elif opt.lower() == 's':
            search_sale()
        elif opt.lower() == 'p':
            post_sale()
        elif opt.lower() == 'u':
            search_user()
        else:
            print('Please enter a valid option\n')
    return

# list products with active sales and provide options for these products
def list_prod():
    global conn, cur
    get_active_products()
    while(True):
        pid = input('\nOptions:\n'
                 +'Enter a pid ("XXXX")\n'
                 +'Display product list (l)\n'
                 +'Return to user menu: (q)\n').strip()
        if(pid == 'q'):
            break
        if(pid == 'l'):
            get_active_products()
        #check pid validity 
        cur.execute("SELECT pid FROM products;")
        pids = [item[0] for item in cur.fetchall()]
        if pid not in pids:
            print("Product ID does not exist, try again")
            continue
        while(True):
            opt = input('\nOptions:\n'
                    +'Write a review (w)\n'
                    +'List all reviews (l)\n'
                    +'List active sales (s)\n'
                    +'Return to list menu (q)\n')
            if opt.lower() == 'w':
                write_preview(pid)
            elif opt.lower() == 'l':
                list_review(pid)
            elif opt.lower() == 's':
                list_sales(pid)
            elif opt.lower() == 'q':
                break
            else:
                print("Invalid command, please try again\n")
        return

# print info for any products associated to an active sale
# pid, desc, no_rev, avg_rating, no_active_sales
def get_active_products():
    global conn, cur
    cur.execute(
        '''
          SELECT ppid, descr, prcount, pravg, activesales FROM
            (SELECT p.pid as ppid, p.descr as descr, count(pr.pid) as prcount, ROUND(AVG(pr.rating), 2) as pravg
            FROM products p LEFT OUTER JOIN previews pr on p.pid = pr.pid
            GROUP BY p.pid, p.descr)
          LEFT OUTER JOIN
            (SELECT p1.pid as p1id, COUNT(*) as activesales
            FROM products p1, sales s 
            WHERE p1.pid = s.pid
            AND datetime(edate) > datetime('now')
            GROUP BY p1.pid)
          ON ppid = p1id
          WHERE activesales NOT NULL
          ORDER BY activesales DESC;
        '''
    )
    products = cur.fetchall()
    print("(PID, description, review count, average rating, active sales)")
    for product in products:
        print(product)
    return

# submit a product review for specified pid
def write_preview(pid):
    global conn, cur, username 
    while(True):
        text = input("Enter your review for product " + pid + "\n").strip()
        if not text:
            print("Must enter product review, try again")
            continue 
        break
    rating = 0
    while(True):
        rating = input("Enter a rating for this product from 1-5\n").strip()
        if not rating:
            print("Must enter a rating, try again")
            continue
        if(1 > int(rating) or int(rating) > 5):
            print("Invalid rating")
            continue
        print("Review successfully entered")
        break
    cur.execute("SELECT COUNT(*) FROM previews")
    rid = cur.fetchone()[0]+1
    cur.execute("SELECT datetime('now')")
    date = cur.fetchone()[0]
    cur.execute("INSERT INTO previews (rid, pid, reviewer, rating, rtext, rdate) \
                        VALUES(?,?,?,?,?,?);", (rid, pid, username, rating, text, date))
    conn.commit()
    return

# list all ratings+reviews for specified pid
def list_review(pid):
    global conn, cur
    cur.execute('SELECT rtext, rating, rid FROM previews WHERE pid=:id', {"id":pid})
    rows = cur.fetchall()
    print("Product reviews for " + pid)
    if len(rows) == 0:
        print("No reviews for this product")
    for row in rows:
        print(str(row[1]) + '/5 ' + str(row[0]))
    return

# find all active sales associated to specified pid
# call follow up options for displayed sales 
def list_sales(pid):
    global conn, cur, username
    # list all active sales associated to pid
    cur.execute('''SELECT s.sid FROM sales s WHERE s.pid=?
                      AND datetime(s.edate) > datetime('now')
                      ORDER BY datetime(s.edate);''',(pid,))
    # return list of sids
    sids = [item[0] for item in cur.fetchall()]
    if len(sids) == 0:
        print("No sales associated to this product. Returning to product list menu")
        return
    print('Sale ID, Description, Max Bid, Time Left')
    for sid in sids:
        get_sid_details(sid)
    
    # select an sid from the list
    validSid = False
    while not validSid:
        sid = input('\nSelect an sid for more details and options\n'
                    +'Or return to product list (q)\n')
        if sid.lower() == 'q':
            break
        elif sid in sids:
            validSid = True
            sale_follow_up(sid)
        else:
            print("Invalid selection, try again")
            continue
    return

# for a sid - get additional detailed information and print it out
def get_sid_details(sid):
    global conn, cur
    # print out info here
    cur.execute(''' SELECT s.descr, b.amt, (julianday(s.edate)-julianday('now'))
                    FROM sales s, (SELECT s.sid, CASE count(bid)
                                        WHEN 0 THEN rprice
                                        ELSE max(amount)
                                        END amt
                          FROM sales s LEFT OUTER JOIN bids b on s.sid=b.sid
                          GROUP BY s.sid) b
                    WHERE s.sid=b.sid
                    AND s.sid=?;
                 ''', (sid,))
    row=cur.fetchone()
    time_left = row[2]
    days = int(time_left//1)
    time_left -= days
    time_left *= 24
    hrs = int((time_left)//1)
    time_left -= hrs
    time_left *= 60
    mts = int((time_left)//1)

    print(sid, row[0], str(row[1]), str(days)+' Days '+str(hrs)+' Hours '
          +str(mts)+' Minutes', sep=', ')
    return


# search for sale listings with keywords in sales.descr and products.descr from associated products
# if no results, return to search menu 
# if matches, provide sales follow up options
def search_sale():
    global conn, cur
    while(True):
        keywords = input('\nEnter one or more space separated keywords\n'
                    + 'Return to product menu (q)\n')
        if keywords.lower() == 'q':
            return
        keywords = keywords.lower().split()
        # get all sid,descr and associated pid
        cur.execute(''' 
            SELECT s.sid, s.descr, p.descr 
            FROM sales s LEFT OUTER JOIN products p 
            ON s.pid = p.pid
            WHERE datetime(s.edate) > datetime('now'); 
            ''')
        rows = cur.fetchall()
        # create list of sids and full descr
        sids = []
        for row in rows:
            sid = row[0]
            descr = row[1].lower()
            if row[2] != None:
                descr += " " + row[2].lower()
            sids.append((sid,descr))
        # get number of keyword hits for each sid in full descr
        # order by most keyword hits 
        sid_hits = []
        for sid,descr in sids: 
            hits = 0
            for key in keywords:
                hits += descr.count(key)
            if hits != 0:
                sid_hits.append((sid, hits))
        sid_hits.sort(key=itemgetter(1), reverse = True)
        # check if no matches
        if len(sid_hits) == 0:
            print("No matches, returning to search\n")
            continue
        # show more info for each sid from search
        print('Sale ID, Description, Max Bid, Time Left')
        for sid,hits in sid_hits:
            get_sid_details(sid)
        # select an sid to show available options 
        validSid = False
        while not validSid:
            sid = input('\nSelect an sid for more details and options\n'
                        +'Or return to search (q)\n')
            if sid.lower() == 'q':
                break
            for sid_hit in sid_hits:
                if sid == sid_hit[0]:
                    validSid = True
                    sale_follow_up(sid)
            if not validSid:
                print("Invalid selection, try again")
        if not validSid: 
            continue
        return

# create a sale to place into auction
def post_sale():
    global conn, cur, username
    print('Please enter the following information:\n')
    while True:
        descr = input('Description: ').strip()
        cond = input('Condition: ').strip()
        if not (descr and cond):
            print("Must enter a description and condition, try again")
            continue
        end_date = input('End date (yyyy-mm-dd): ')
        end_time = input('End time (hh:mm:ss): ')
        edate = end_date + ' ' + end_time
        if not re.search("[0-9]{4}-([1][0-2]|[0][1-9])-([0][1-9]|[1-2][0-9]|[3][0-1]) ([0-1][0-9]|[21-23]):([0-5][0-9]):([0-5][0-9])", edate):
            print("Invalid date format, try again")
            continue
        cur.execute("SELECT datetime('now')")
        cdate = cur.fetchone()[0]
        if edate < cdate:
            print('End date must be in the future.')
        else:
            break
    pid = input('Product id (optional): ').strip()
    if pid:
        cur.execute("SELECT pid FROM products;")
        pids = [item[0] for item in cur.fetchall()]
        if pid not in pids:        
            # product doesnt exist in database, get optional descr
            pdescr = input("Product does not exist in catalog, enter a description (optional): ")
            if pdescr:
                cur.execute("INSERT INTO products (pid,descr) VALUES (?,?)",(pid,pdescr))
                conn.commit()
    else:
        pid = None
    rprice = input('Reserve price (optional): ')
    if not rprice:
        rprice = None     
    # get next sid
    cur.execute('SELECT sid FROM sales;')
    used_sid = cur.fetchall()
    num = len(used_sid) + 1
    valid = False
    while not valid:
        valid = True
        if num < 10:
            sid = 's' + '0' + str(num)
        else:
            sid = 's' + str(num)
        for s in used_sid:
            if sid == s[0]:
                valid = False
        num += 1
    cur.execute('INSERT INTO sales (sid, lister, pid, edate, descr, \
                cond, rprice) VALUES(?,?,?,?,?,?,?);', 
                (sid, username, pid, edate, descr, cond, rprice))
    conn.commit()
    print('Sale added successfully!')
    return

# search for keywords in user email or name 
# for any hits display users.email, name, city 
# provide follow up options to perform with matches
def search_user():
    global conn, cur
    while(True):
        keywords = input('\nEnter one or more space separated keywords\n'
                    + 'Return to product menu (q)\n')
        if keywords.lower() == 'q':
            return
        keywords = keywords.lower().split()
        # get appropriate values to compare keywords against
        cur.execute("SELECT email, name, city FROM users")
        rows = cur.fetchall()
        #create list of email + "," + name, city 
        users = []
        for row in rows:
            descr = row[0].lower() + "," + row[1].lower()
            city = row[2]
            users.append((descr,city))
        #find all users with keyword hits
        user_hits = []
        for descr,city in users: 
            hits = 0
            for key in keywords:
                hits += descr.count(key)
            if hits != 0:
                user_hits.append((descr, city))
        # check if no matches
        if len(user_hits) == 0:
            print("No matches, returning to search\n")
            continue
        # display all users with keyword matches
        validEmails = []
        for user in user_hits:
            email, name = user[0].split(',')
            city = user[1]
            validEmails.append(email)
            print("Email: ", email, ", Name: ", name, ", City: ", city)
        # select a valid user from the list of users who had matches
        validUser = False
        while not validUser:
            email = input('\nSelect an email for more details and options\n'
                        +'Or return to search (q)\n').lower()
            if email == 'q':
                break
            elif email not in validEmails:
                print("Invalid selection, try again")
                continue
            validUser = True
        if not validUser:
            continue
        # display options to preform on selected user
        opt = input('\nOptions:\n'
                +'Write a review on user (w)\n'
                +'List users active sale listings (l)\n'
                +'List reviews of this user (r)\n'
                +'Return to list menu (q)\n')
        if opt.lower() == 'w':
            write_user_review(email)
        elif opt.lower() == 'l':
            sales_of_seller(email)
        elif opt.lower() == 'r':
            reviews_of_seller(email)
        elif opt.lower() == 'q':
            break
        else:
            print("Invalid command, please try again\n")
    return

# additional options to perform on a selected sale
def sale_follow_up(sid):
    global conn, cur, username
    cur.execute(''' SELECT s.lister, r.num, r.rating, s.descr,
                     s.edate, s.cond, b.amt
                     FROM sales s , (SELECT lister, count(rating) as num,
                                     avg(rating) as rating
                                     FROM (SELECT DISTINCT lister
                                           FROM sales) LEFT OUTER JOIN reviews
                                     ON lister=reviewee
                                     GROUP BY lister) r, 
                     (SELECT s.sid, CASE count(bid)
                                    WHEN 0 THEN rprice
                                    ELSE max(amount)
                                    END amt
                      FROM sales s LEFT OUTER JOIN bids b on s.sid=b.sid
                      GROUP BY s.sid) b
                      WHERE s.lister=r.lister
                      AND s.sid=?
                      AND s.sid=b.sid;
                 ''', (sid,))
    
    result = cur.fetchone()
    print('Lister, Lister Reviews, Description, End Date, Condition, Max Bid, Product info')
    lister = result[0]
    if result[1] == 0:
        lister_review = 'Lister has no reviews'
    else:
        lister_review = str(result[1])+' reviews: '+str(round(result[2], 2))+'/5'
    # attatch associated product info 
    cur.execute(''' SELECT p.descr, COUNT(*), AVG(pr.rating)
                FROM products p, previews pr, sales s
                WHERE s.sid = ?
                AND s.pid = p.pid 
                AND p.pid = pr.pid;''',(sid,))
    pinfo = cur.fetchall()
    if(pinfo[0][0] == None):
        pinfo = "Product is not reviewed"
    else:
        pinfo = "%s, %d ratings, avg: %s/5" % (pinfo[0][0], pinfo[0][1],round(pinfo[0][2],2))
    # display all info on sale and provide additonal options
    print(lister, lister_review, result[3], result[4], result[5], result[6], pinfo, sep=', ')
    while(True):
        print('\nOptions:\n'
            +'Place a bid (b)\n'
            +'List active sales of the seller (s)\n'
            +'List reviews of seller (r)\n'
            +'Or (q) to return')
        opt = input('Select an option: ').lower()
        if opt == 'q':
            return
        elif opt == 'b':
            place_bid(sid)
        elif opt == 's':
            sales_of_seller(lister)
        elif opt == 'r':
            reviews_of_seller(lister)
        else:
            print("Invalid selection, try again")
    return

# post a bid on a selected sale
def place_bid(sid):
    global conn, cur, username
    # find current max bid on sale or reserved price if sale has no bids
    cur.execute(''' SELECT CASE count(bid)
                           WHEN 0 THEN rprice
                           ELSE max(amount)
                           END max
                    FROM sales s LEFT OUTER JOIN bids b on s.sid=b.sid
                    WHERE s.sid=?
                    GROUP BY s.sid;    
                ''', (sid,))
    max_bid = cur.fetchone()[0]
    if max_bid == None:
        max_bid = 0
    # enter new bid
    while True:
        amt = input('\nEnter a bid amount (XXX)\n'
                    +'Or (q) to return\n').strip()
        if amt.lower() == 'q':
            break
        try:
            amt = float(amt)
        except:
            print('Bid must be a number')
            continue
        if amt <= max_bid:
            print('Bid must be greater than %.1f' %max_bid)
        else:
            cur.execute("SELECT datetime('now')")
            bdate = cur.fetchone()[0]
            cur.execute('SELECT bid FROM bids;')
            used_bid = cur.fetchall()
            num = len(used_bid) + 1
            valid = False
            while not valid:
                valid = True
                if num < 10:
                    bid = 'b' + '0' + str(num)
                else:
                    bid = 'b' + str(num)
                for b in used_bid:
                    if bid == b[0]:
                        valid = False
                num += 1
            cur.execute('INSERT INTO bids (bid, bidder, sid, bdate, amount) VALUES(?,?,?,?,?);', 
                        (bid, username, sid, bdate, amt))
            print('Bid added successfully!')
            conn.commit()                
            return

# get additional info for all sales from a specified user and provide options for the sales
def sales_of_seller(email):
    global conn, cur
    #usersales = all sids associated with seller ordered by remaining time on sale
    cur.execute( '''
                SELECT sid
                FROM sales 
                WHERE lister LIKE ?
                AND datetime(edate) > datetime('now')
                ORDER BY edate;
                ''', (email,))
    usersales = cur.fetchall()
    if len(usersales) == 0:
        print("No sales listed by this user")
        return
    # get sale info for all listings by specified user
    print('Sale ID, Description, Max Bid, Time Left')
    for sid in usersales:
        get_sid_details(sid[0])    
    # select an sid to display more options for that sale
    validSid = False
    while not validSid:
        sid = input('\nSelect an sid for more details and options\n'
                    +'Or return to search (q)\n')
        if sid.lower() == 'q':
            break
        for sale in usersales:
            if sid == sale[0]:
                validSid = True
                sale_follow_up(sid)
                break
        if not validSid:
            print("Invalid selection, try again")
    return

#show all reviews written about the seller
def reviews_of_seller(email):
    global conn, cur
    cur.execute('''
                SELECT rating, rtext 
                FROM reviews 
                WHERE LOWER(reviewee) = ?;
                ''', (email,))
    reviews = cur.fetchall()
    if len(reviews) == 0:
        print("This user has no reviews")    
    for review in reviews:
        rating = review[0]
        rtext = review[1]
        print(rating, "/5, ", rtext)
    return

# enter a review on a specified user
def write_user_review(email):
    global conn, cur, username
    cur.execute('''
                SELECT * FROM reviews 
                WHERE reviewee =?
                AND reviewer=?
                ''', (email,username))
    if len(cur.fetchall()) == 1:
        print("You cannot review this user more than once, returning to user search")
        return
    rtext = input("Enter a review: ")
    while(True):
        rating = input("Enter a rating for this user from 1-5\n")
        if(1 > int(rating) or int(rating) > 5):
            print("Invalid rating")
            continue
        print("Review successfully entered")
        break
    cur.execute("SELECT datetime('now')")
    rdate = cur.fetchone()[0]
    cur.execute("INSERT INTO reviews (reviewer, reviewee, rating, rtext, rdate) VALUES (?, ?, ?, ?, ?)",
                (username, email, rating, rtext, rdate))
    conn.commit()
    return

main()