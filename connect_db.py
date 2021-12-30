import psycopg2


class DbCNH:

    def __init__(self):
        self.conn = psycopg2.connect(dbname='cnh', user='postgres', password='Dfkkf-123', host='192.168.19.128')
        self.cur = self.conn.cursor()

    def select(self, query):
        self.cur.execute(query)
        return self.cur.fetchone()

    def insert(self, query, row):
        self.cur.execute(query, row)
        self.conn.commit()
