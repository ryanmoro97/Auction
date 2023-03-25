--1 List all products with some active sales associated to them.
--pid, descr, #reviews, avg(rating), #active sales
--sort by #active sales DESC



SELECT p.pid as pid, p.descr,count(pr.pid) --, ROUND(AVG(pr.rating), 2)
FROM products p, previews pr
LEFT OUTER JOIN sales s ON p.pid=s.pid
WHERE p.pid = pr.pid

GROUP BY p.pid



SELECT p.pid, COUNT(*)
FROM products p, sales s 
WHERE p.pid = s.pid
AND datetime(edate) > datetime('now')
--WHERE datetime('now') > datetime(s.edate, '+1 days')
GROUP BY p.pid;


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


--the sale description, 
--the maximum bid (if there is a bid on the item) or 
--    the reserved price (if there is no bid on the item), 
--and the number of days, hours and minutes left until the sale expires

SELECT s.descr, strftime('%s',edate) - strftime('%s','now')
FROM products p1, sales s 
WHERE p1.pid = s.pid
AND datetime(edate) > datetime('now')



SELECT s.sid FROM sales s WHERE s.pid LIKE ?
AND datetime(s.edate) > datetime('now')
ORDER BY datetime(s.edate);


SELECT s.sid, s.descr, p.descr 
FROM sales s, products p 
WHERE s.pid = p.pid 


SELECT rating, text 
FROM reviews 
WHERE reviewee = ?

--usersales = all sids associated with email
--ordered by remaining time on sale
 

SELECT sid, edate 
 FROM sales 
 WHERE lister LIKE "smoovcrim@gmail.com"
 ORDER BY edate

 '''
 SELECT sid, edate 
 FROM sales 
 WHERE lister = ?
 ORDER BY edate
 ''', (email,)


 SELECT p.descr, COUNT(*), AVG(pr.rating)
 FROM products p, previews pr, sales s
 WHERE s.sid = "S01"
 AND s.pid = p.pid 
 AND p.pid = pr.pid

SELECT s.sid, datetime(s.edate), datetime('now')
FROM sales s WHERE s.pid LIKE "XBX9"
AND datetime(s.edate) > datetime('now')
ORDER BY datetime(s.edate);

SELECT p.descr, COUNT(*), AVG(pr.rating)
FROM products p, previews pr, sales s
WHERE s.pid = "H119"
AND s.pid = p.pid 
AND p.pid = pr.pid

SELECT p.descr, COUNT(*)
FROM products p, sales s
WHERE s.pid = "H119"
AND s.pid = p.pid 

SELECT sid
FROM sales 
WHERE LOWER(lister) = "youtgetone@outlook.com"
AND datetime(edate) > datetime('now')
ORDER BY edate;