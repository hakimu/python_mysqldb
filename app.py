import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
import MySQLdb

@newrelic.agent.background_task()
def caller():
	db = MySQLdb.connect(host='localhost',db='test')
	cursor = db.cursor()
	cursor.execute("""SELECT * FROM user""")
	db.close()

caller()


