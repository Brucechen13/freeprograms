import pymysql
import json
#Activity表结构 id, title, content, time, city，price，useid
class Activity:
    def __init__(self, conn):
        self._conn = conn
    
    def addActivity(self, useId, title, content, time, city, price):
        if self.getUser(phoneNumber) == None:
            try:            
                with self._conn.cursor() as cursor:
                    # 执行sql语句，插入记录
                    sql = 'INSERT INTO activities (title, content, time, city，price，useid) VALUES (%s, %s,%s, %s,%s, %s)'
                    cursor.execute(sql, (title, content, time, city, price, useId))
                    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                    self._conn.commit()
                    return json.dumps({'success':'ok'})
            except Exception:
                return json.dumps({'err':'未知错误'})
            #finally:
            #    self        ._conn.close();
        else:
            return json.dumps({'err':'手机号已经注册'})
