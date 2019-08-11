import sqlite3
import os.path




class SqliteWrapper:
    def __init__(self):
        self.__conn = None
        self.__cursor = None

    def __del__(self):
        self.close()

    def connect(self, dbfile):
        self.close()
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR,dbfile)
        self.__conn =sqlite3.connect(db_path)
        self.__cursor = self.__conn.cursor()

    def close(self):
        if self.__cursor:
            self.__cursor.close()
            self.__cursor = None

        if self.__conn:
            self.__conn.close()
            self.__conn = None


    def select(self, sql):
        self.__cursor.execute(sql)
        rst= self.__cursor.fetchall()
        return rst


    def execute(self, sql):
        self.__cursor.execute(sql)
        self.__conn.commit()
