-- Ryan Moro, moro@ualberta.ca - Feb 2, 2020

-- users: email, name, pwd, city, gender
insert into users values ('weezyfbaby@gmail.com', 'Lil Wayne', 'G04T', 'New Orleans, LA', 'M');
insert into users values ('henowshe@yahoo.com', 'Caitlyn Jenner', '8DEZ', 'Mount Kisco, NY', 'T');
insert into users values ('dirtylean@live.ca', 'Future Saclown', '8008', 'Atlanta, GA', 'M');
insert into users values ('yougetone@outlook.com', 'Oprah Winfrey', '1BBW', 'Mississippi, MI', 'F');
insert into users values ('smoovCrim@gmail.com', 'Micheal Jackson', 'H3H3', 'Gary, IN, ', 'M');
insert into users values ('daycare@live.com', 'Jeffery Epstein', 'SKRT', 'Brooklyn, NY', 'M');
insert into users values ('291islife@hotmail.com', 'Davood Rafiei', 'TECR', 'Edmonton, AB', 'M');
insert into users values ('maga@hotmail.ca', 'Donald Trump', 'GOLF', 'Queens', 'M');
insert into users values ('blackMamba@hotmail.com', 'Kobe Bryant', 'BALS', 'Edmonton, KY', 'M');

-- products: pid, description
insert into products values ('GF00', 'Gucci Flip Flops');
insert into products values ('TB55', 'Teddy Bear');
insert into products values ('JJ39', 'Soul');
insert into products values ('UE69', 'Lean Cup');
insert into products values ('HH39', 'Concert ticket');
insert into products values ('VV20', 'Sex change voucher');
insert into products values ('XBX9', 'Xbox');
insert into products values ('PS44', 'PS4');
insert into products values ('D449', 'data');
insert into products values ('H119', 'speeding ticket');
insert into products values ('H00T', 'Vase');
insert into products values ('1CEY', 'Luigi chain');
insert into products values ('NNNN', 'NOTHING');

-- sales: sid, lister (email), pid, end date, description, condition, registered price
insert into sales values ('S01', 'daycare@live.com', 'PS44',datetime('now', '+3 days'), 'I dont use this pS4 anymore, cool kids play xbox', 'Used', 150);
insert into sales values ('S02', 'daycare@live.com', 'XBX9', datetime('now', '+2 days'), 'I play xboX with all my lil friends', 'Mint', 220);
insert into sales values ('S03', 'henowshe@yahoo.com', 'VV20', datetime('now', '+1 days'), 'I highly recommend this place, voucher', 'New', 200);
insert into sales values ('S04', 'dirtylean@live.ca', 'GF00', datetime('now', '+5 days'), 'i fucked my bitch wearing these', 'Used', 999);
insert into sales values ('S05', 'smoovCrim@gmail.com', 'TB55', datetime('now', '+8 days'), 'brand new teddy bear smells like candy', 'Mint', 1);
insert into sales values ('S06', 'yougetone@outlook.com', 'JJ39', datetime('now', '-1 days'), 'selling this for fame', 'Used', 1400);
insert into sales values ('S07', 'weezyfbaby@gmail.com', 'UE69', datetime('now', '-9 days'), 'Used this since i was 8 but still works', 'Used', 350);
insert into sales values ('S08', 'smoovCrim@gmail.com', 'HH39', datetime('now', '-6 days'), 'Hologram concert ticket', 'New', 99);
insert into sales values ('S09', '291islife@hotmail.com', 'D449', datetime('now', '+1 days'), 'good data 4 u', 'Used', 69);
insert into sales values ('S10', 'weezyfbaby@gmail.com', 'H119', datetime('now', '+6 days'), 'pay for my ticket pls', 'Used', 350);
insert into sales values ('S11', 'smoovCrim@gmail.com', 'D449', datetime('now', '+3 days'), 'my diary', 'New', 999999);
insert into sales values ('S12', 'smoovCrim@gmail.com', 'XBX9', datetime('now', '+1 days'), 'xBoX 720', 'New', 420);
insert into sales values ('S13', 'smoovCrim@gmail.com', 'PS44', datetime('now', '+1 days'), 'ps4', 'New', 30);
insert into sales values ('S14', 'dirtylean@live.ca', 'PS44', datetime('now', '+1 days'), 'ps4', 'New', 30);
insert into sales values ('S15', 'dirtylean@live.ca', 'H00T', datetime('now', '+1 days'), 'its a b0ng', 'Used', 3);
insert into sales values ('S16', 'dirtylean@live.ca', '1CEY', datetime('now', '+1 days'), 'its fake', 'Used', 7000);
insert into sales values ('S17', 'dirtylean@live.ca', 'JJ39', datetime('now', '+1 days'), 'ree', 'Used', 7000);
insert into sales values ('S18', 'dirtylean@live.ca', 'H119', datetime('now', '+4 days'), 'ree', 'Used', 7000);
insert into sales values ('S19', 'dirtylean@live.ca', 'H119', datetime('now', '+2 days'), 'ree', 'Used', 7000);


-- bids: bid, bidder (email), sid, bid placed date, amount
insert into bids values ('B01', 'weezyfbaby@gmail.com', 'S09', '2020-01-20', 40.00);
insert into bids values ('B02', '291islife@hotmail.com', 'S04', '2020-01-27', 100.00);
insert into bids values ('B03', 'weezyfbaby@gmail.com', 'S03', '2020-01-30', 260.00);
insert into bids values ('B04', '291islife@hotmail.com', 'S08', '2020-01-04', 430.00);
insert into bids values ('B05', 'dirtylean@live.ca', 'S08', '2020-01-04', 430.00);
insert into bids values ('B06', 'weezyfbaby@gmail.com', 'S07', '2020-01-04', 430.00);
insert into bids values ('B07', 'yougetone@outlook.com', 'S07', '2020-01-04', 530.00);
insert into bids values ('B08', 'yougetone@outlook.com', 'S01', '2020-01-04', 10.00); 
insert into bids values ('B09', 'yougetone@outlook.com', 'S12', '2020-01-04', 530.00);
insert into bids values ('B10', 'yougetone@outlook.com', 'S15', '2020-01-04', 530.00);
insert into bids values ('B11', 'yougetone@outlook.com', 'S16', '2020-01-04', 8177.00);
insert into bids values ('B12', 'dirtylean@live.ca', 'S13', '2020-01-04', 8177.00);
insert into bids values ('B13', 'dirtylean@live.ca', 'S02', '2020-01-04', 1.00);
insert into bids values ('B14', 'dirtylean@live.ca', 'S12', '2020-01-04', 8177.00);
insert into bids values ('B15', 'blackMamba@hotmail.com', 'S10', '2020-01-04', 8177.00);

-- reviews: reviewer (email), (email), rating, review text, review date
insert into reviews values ('maga@hotmail.ca', 'daycare@live.com', 10.0, 'my bff i miss his smile', '2020-01-15');
insert into reviews values ('smoovCrim@gmail.com', 'daycare@live.com', 1.0, 'this dude poached my clients', '2020-01-31');
insert into reviews values ('henowshe@yahoo.com', 'daycare@live.com', 9.9, 'upstanding citizen', '2019-11-14');
insert into reviews values ('weezyfbaby@gmail.com', 'maga@hotmail.ca', 9.0, 'this guy has bars', '2020-01-13');
insert into reviews values ('smoovCrim@gmail.com', 'maga@hotmail.ca', 2.0, 'i died before he was president so i cant rly say', '2020-01-11');
insert into reviews values ('henowshe@yahoo.com', 'maga@hotmail.ca', 10.0, 'very supportive guy', '2020-01-10');
insert into reviews values ('henowshe@yahoo.com', 'weezyfbaby@gmail.com', 10.0, 'undeniable goat', '2019-10-11');
insert into reviews values ('smoovCrim@gmail.com', 'weezyfbaby@gmail.com', 10.0, 'i wish i was this talented', '2019-08-10');
insert into reviews values ('dirtylean@live.ca', 'weezyfbaby@gmail.com', 10.0, 'this guy made me possible', '2020-01-13');
insert into reviews values ('dirtylean@live.ca', '291islife@hotmail.com', 9.0, 'i cant read but this guy knows what hes talking about', '2020-01-01');
insert into reviews values ('smoovCrim@gmail.com', '291islife@hotmail.com', 6.0, 'hehe i come to class just for his smile hehe', '2020-01-11');
insert into reviews values ('yougetone@outlook.com', '291islife@hotmail.com', 2.0, 'he lost to me in the hotdog eating contest', '2020-01-02');
insert into reviews values ('dirtylean@live.ca', 'henowshe@yahoo.com', 2.0, 'loved his her? cameo on south park', '2020-02-01');
insert into reviews values ('maga@hotmail.ca', 'henowshe@yahoo.com', 9.0, 'couldnt ask for a better fmoather in law for Kanye', '2019-02-13');
insert into reviews values ('henowshe@yahoo.com', 'henowshe@yahoo.com', 10.0, 'so brave, im the best', '2020-01-23');
insert into reviews values ('henowshe@yahoo.com', 'dirtylean@live.ca', 1.0, 'say no to drugs', '2020-01-13');
insert into reviews values ('maga@hotmail.ca', 'dirtylean@live.ca', 1.0, 'big fan of the urban community', '2019-09-13');
insert into reviews values ('weezyfbaby@gmail.com', 'dirtylean@live.ca', 3.0, 'who?', '2020-01-19');
insert into reviews values ('henowshe@yahoo.com', 'smoovCrim@gmail.com', 10.0, 'good ticklr', '2019-10-11');

-- previews: preview id, pid, reviewer (email), rating, review text, review date
insert into previews values ('1', 'VV20', 'daycare@live.com', 1.8, 'they didnt let me use it for my son', '2019-07-20');
insert into previews values ('2', 'UE69', 'yougetone@outlook.com', 9.5, 'very good, i can also use it to drink molasses', '2019-09-13');
insert into previews values ('3', 'GF00', 'daycare@live.com', 6.9, 'sick, these are very hip with the youth', '2019-12-04');
insert into previews values ('4', 'GF00', 'smoovCrim@gmail.com', 9.9, 'fresh flops', '2019-12-04');
insert into previews values ('5', 'GF00', 'smoovCrim@gmail.com', 1.9, 'these are from china', '2018-12-04');
insert into previews values ('6', 'XBX9', 'smoovCrim@gmail.com', 9.9, 'got paid to write this review', '2019-12-04');
insert into previews values ('7', 'XBX9', 'smoovCrim@gmail.com', 9.9, 'got paid to write this review', '2019-12-04');
insert into previews values ('8', 'PS44', 'smoovCrim@gmail.com', 8.0, 'got paid to write this review', '2018-12-04');
insert into previews values ('9', 'PS44', 'smoovCrim@gmail.com', 10.0, 'got paid to write this review', '2018-12-04');

insert into previews values ('10', 'JJ39', 'smoovCrim@gmail.com', 10.0, 'got paid to write this review', '2018-12-04');
insert into previews values ('11', 'JJ39', 'smoovCrim@gmail.com', 10.0, 'got paid to write this review', '2018-12-04');
insert into previews values ('12','1CEY','smoovCrim@gmail.com','5.0','sick as fk','2020-03-05');

-- endorses: rid, endorser (email)
insert into endorses values ('1', '291islife@hotmail.com');
insert into endorses values ('6', 'yougetone@outlook.com');
insert into endorses values ('9', 'smoovCrim@gmail.com');

