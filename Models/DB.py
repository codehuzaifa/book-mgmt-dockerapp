import os
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


class DB(object):
	"""Initialize mysql database """
	table = ""

	def __init__(self, app):
		app.config["MYSQL_DATABASE_HOST"] = os.environ.get("MYSQL_DATABASE_HOST", "mysql_db");
		app.config["MYSQL_DATABASE_USER"] = os.environ.get("MYSQL_DATABASE_USER", "lms_user");
		app.config["MYSQL_DATABASE_PASSWORD"] = os.environ.get("MYSQL_DATABASE_PASSWORD", "lms_password");
		app.config["MYSQL_DATABASE_DB"] = os.environ.get("MYSQL_DATABASE_DB", "lms");

		self.mysql = MySQL(app, cursorclass=DictCursor)

	def cur(self):
		return self.mysql.get_db().cursor()

	def query(self, q):
		h = self.cur()
	
		if (len(self.table)>0):
			q = q.replace("@table", self.table)

		h.execute(q)

		return h

	def commit(self):
		self.query("COMMIT;")
