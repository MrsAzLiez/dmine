import pymysql as Mariadb
#import Mariadb


conn = Mariadb.connect(host = "localhost", user = "dmine", passwd = "dmineScrapy", db = "dReddit")
c = conn.cursor()
	
c.execute("USE dReddit")

def getdata(post, comment):
	c.execute("INSERT INTO post(post_id, title, subreddit, score, author) VALUES (%s, %s, %s, %s, %s,)",(post_id, title, subreddit, score, author))
	
	conn.commit()
	
	c.execute("INSERT INTO comment(comment_id, author, body, score) VALUES (%s,%s, %s, %s, %s)",(comment_id, author, body, score))
	
	conn.commit()
	
def read_db():
		c.execute('SELECT * FROM post')
		for row in c.fetchall():
			print(row)

read_db()			
c.close()
conn.close()