from config import *
import psycopg2


class PgsqlConnect:
    """数据库连接"""

    def __init__(self, dbname, user, password, host, port):

        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        self.cursor = self.conn.cursor()

    def execute_sql(self):

        sql = SQL
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        self.conn.commit()
        self.conn.close()

        print(result)

