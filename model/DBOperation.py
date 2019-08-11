import model.SqliteWrapper as sw


class DBOpeation:
    def __init__(self):
        self.dbFile="purchasing.db"
        self.sw=sw.SqliteWrapper()

    def getAllItems(self):
        self.sw.connect(self.dbFile)
        sql="select * from  item"
        rows=self.sw.select(sql)
        self.sw.close()
        rtn={}
        for i in range(len(rows)):
            rtn[i]=list(rows[i])
        return rtn


    def update(self,table,colNames,colVals,colID):

        self.sw.connect(self.dbFile)
        sql="update "+table+" set "
        for i in range(len(colNames)):
            sql=sql+colNames[i]+"='"+colVals[i]+"', "
        sql=sql[:-2]
        sql=sql+" where ID="+str(colID)
        print(sql)
        self.sw.execute(sql)
        self.sw.close()

    def insert(self,table, colNames,colVals):
        self.sw.connect(self.dbFile)
        sql="insert into "+table+"("
        for i in range(len(colNames)):
            sql=sql+colNames[i]+","
        sql=sql[:-1]+") values ("
        for i in range(len(colNames)):
            sql=sql+"'"+str(colVals[i])+"',"
        sql = sql[:-1] + ")"
        print(sql)
        self.sw.execute(sql)
        self.sw.close()
