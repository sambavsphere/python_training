import psycopg2

def db_connect():
	con = psycopg2.connect(user="postgres",password="9959409986",host="localhost",port=5432,database="Test")
	cur= con.cursor()
	return con,cur

def browse(id=None):
	query = "select * from emp"
	if id:
		query = query+" where id={0}".format(id)
	con,cur = db_connect()
	cur.execute(query)
	return cur.fetchall()

if __name__ == "__main__":
	print browse()
	print "*"*30
	print browse(1)



