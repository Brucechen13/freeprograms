import pymysql
import json
#Activity表结构 id, title, content, time, city，price，useid
#活动分享数，评论数，关注数
class Activity:
    def __init__(self, conn):
        self._conn = conn
    
    def addActivity(self, useId, title, content, starttime, endtime, city, price):
        try:            
            with self._conn.cursor() as cursor:
                # 执行sql语句，插入记录
                sql = 'INSERT INTO activities (title, content, starttime, endtime, city, price, useid) VALUES (%s, %s,%s, %s, %s,%s, %s)'
                cursor.execute(sql, (title, content, starttime, endtime, city, price, useId))
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                self._conn.commit()
                return json.dumps({'success':'ok'})
        except Exception as e:
            return json.dumps({'err':str(e)})
    def showActivity(self, curTime, start, end):
        try:
            with self._conn.cursor() as cursor:
                sql = "SELECT * FROM activities where starttime>Now() order by starttime limit %s, %s"
                cursor.execute(sql, (start, end))
                result = cursor.fetchall()            
                self._conn.commit()  
                return result
        except Exception as e:
            return json.dumps({'err':str(e)})
    def showLatestActivity(self, curTime):
        try:
            with self._conn.cursor() as cursor:
                sql = "SELECT * FROM activities where starttime>Now() starttime>%s and order by starttime"
                cursor.execute(sql, (curTime))
                result = cursor.fetchall()            
                self._conn.commit()  
                return result
        except Exception as e:
            return json.dumps({'err':str(e)})
    def shareActivity(self, actid):
        try:
            with self._conn.cursor() as cursor:
                sql = "SELECT * FROM activities where starttime>Now() order by starttime"
                cursor.execute(sql)        
                self._conn.commit()  
                return json.dumps({'success':'ok'})
        except Exception as e:
            return json.dumps({'err':str(e)})        

#conn = pymysql.connect(host='127.0.0.1', port=3305, user='root', passwd='123456', db='test', charset='utf8')
#act = Activity(conn)
#print(act.addActivity(1, '123', '456', '2017/6/1', '2017/6/2', 'beij', 'free'))
#print((act.getActivity()))