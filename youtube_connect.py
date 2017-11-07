import datetime
import pymysql as Mariadb


#connect database
conn = Mariadb.connect(host = "localhost", user = "dmine", passwd = "dmineScrapy", db = "dyoutube")
c = conn.cursor()
	
c.execute("USE dyoutube")

def getdata():
	#execute the query
	c.execute("INSERT INTO channel(channel_id, channel_name, description, created_at, subscribers_count, video_count, views_count, country) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (channel_id, channel_name, description, created_at, subscribers_count, video_count, views_count, country))
	
	conn.commit()
	
def read_db():
		c.execute('SELECT * FROM channel')
		for row in c.fetchall(): #to get the result output
			print(row) #print the result


read_db()			
c.close()
conn.close()
