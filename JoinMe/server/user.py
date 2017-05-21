import pymysql
#User表结构 id, phone, password, username, gender，age，address，career
class User:
    _conn = None 
    def __init__(self, conn):
        self._conn = conn
        
    def registerUser(self, phoneNumber, password):
        try:
            with self._conn.cursor() as cursor:
                # 执行sql语句，插入记录
                sql = 'INSERT INTO users (phoneno, password) VALUES (%s, %s)'
                cursor.execute(sql, (phoneNumber, password))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            self._conn.commit()
        finally:
            self._conn.close();     
    
    def getUser(self, phoneNumber):
        try:
            with self._conn.cursor() as cursor:
                sql = 'select * from users where phoneno = %s'
                cursor.execute(sql, (phoneNumber))
                result = cursor.fetchone()            
                self._conn.commit()
                return result
        finally:
            print('final')
            self._conn.close();     
global conn
# 创建连接
def conMysql():
    global conn
    conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', passwd='123456', db='test', charset='utf8')
conMysql()
user = User(conn)
print(user.getUser('18840884702'))