import datetime
import pymysql as Mariadb



#connect database
conn = Mariadb.connect(host = "localhost", user = "dmine", passwd = "dmineScrapy", db = "imgur")
c = conn.cursor()
	
c.execute("USE imgur")

def getdata():
	#execute the query
	c.execute("INSERT INTO post(post_id, author, title, description, link, topic, points, score, ups, downs, comment_count, tags, nsfw) VALUES(' ',' ',' ',' ',' ')", (post_id, author, title, description, link, topic, points, score, ups, downs, comment_count, tags, nsfw))
	c.execute("INSERT INTO comment(comment_id, parent_id, body, author, datetime, deleted, points, vote, downs, ups) VALUES(' ',' ',')", (comment_id, parent_id, body, author, datetime, deleted, points, vote, downs, ups))

	conn.commit()
	
def read_db():
		c.execute('SELECT * FROM channel')
		for row in c.fetchall(): #to get the result output
			print(row) #print the result


read_db()			
c.close()
conn.close()
