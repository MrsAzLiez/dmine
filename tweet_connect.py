#!/usr/bin/python
import datetime
import pymysql as mariadb


#connect database
conn = mariadb.connect(host = "localhost", user = "dmine", passwd = "dmineScrapy", db = "tweet")
c = conn.cursor()
        
c.execute("USE tweet")

def getdata(tweet):
#execute the query
        c.execute("INSERT INTO tweet(tweet_id, author, username, body, lang, created_at, retweets, replies, fav_count) VALUES (%s,%s,%s,%s,%s,%s)",(tweet_id, author, username, body, lang, created_at, retweets, replies, fav_count))
        

        conn.commit()
def read_db():

        c.execute("SELECT * FROM tweet")
        for row in c.fetchall(): #to get the result output
                print(row), #print the result

read_db()			
c.close()
conn.close()
