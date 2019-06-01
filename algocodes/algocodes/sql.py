import mysql.connector

MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456q'
MYSQL_PORT = '3306'
MYSQL_DB = 'algocodes'

def __init__():
    cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
    cur = cnx.cursor(buffered=True)

def _check_sql(cls):
    global cnx, cur
    try:
        sql = "show tables;"
        cur.execute(sql)
        cnx.commit()
    except mysql.connector.Error:
        cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB)
        cur = cnx.cursor(buffered=True)

class Sql:
    @classmethod
    def create_table(cls):
        _check_sql(cls)
        sql = "CREATE TABLE IF NOT EXISTS leetcode(problem_id int not null,problem_title varchar(255) not null, problem_content text not null, problem_acc int not null, problem_submit int not null, problem_level int not null);"
        cur.execute(sql)
        cnx.commit()

    @classmethod
    def create_table_arxiv(cls):
        _check_sql(cls)
        sql = "CREATE TABLE IF NOT EXISTS arxiv(paper_title varchar(255) not null, paper_content text not null, paper_author varchar(255) not null, paper_time varchar(255) not null, paper_subject varchar(255) not null, paper_pdfurl varchar(255) not null );"
        cur.execute(sql)
        cnx.commit()


    @classmethod
    def insert_problem(cls, id, title, content, acc, submit, level):
        _check_sql(cls)
        sql = 'INSERT INTO leetcode (`problem_id`, `problem_title`, `problem_content`, `problem_acc`, `problem_submit`, `problem_level`) VALUES (%(id)s, %(title)s, %(content)s, %(acc)s, %(submit)s, %(level)s)'
        value = {
            'id': id,
            'title': title,
            'content': content,
            'acc': acc,
            'submit':submit,
            'level':level
        }
        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def get_paper(cls, title, time):
        _check_sql(cls)
        sql = 'SELECT * FROM arxiv WHERE paper_title=%(title)s AND paper_time=%(time)s'
        value = {
            'title':title,
            'time':time
        }
        cur.execute(sql, value)
        return cur.fetchall()


    @classmethod
    def insert_paper(cls, title, author, content, time, subject, pdfurl):
        _check_sql(cls)
        if len(Sql.get_paper(title, time)) != 0:
               return
        sql = 'INSERT INTO arxiv (`paper_title`, `paper_content`, `paper_author`, `paper_time`, `paper_subject`, `paper_pdfurl`) VALUES (%(title)s, %(content)s, %(author)s, %(time)s, %(subject)s, %(pdfurl)s)'
        value = {
            'time': time,
            'title': title,
            'content': content,
            'author': author,
            'subject':subject,
            'pdfurl':pdfurl
        }
        cur.execute(sql, value)
        cnx.commit()


    @classmethod
    def get_page(cls, curPage):
        _check_sql(cls)
        sql = 'SELECT * FROM leetcode order by problem_id limit %(page)s, 20'
        value = {
            'page': curPage
        }
        cur.execute(sql, value)
        print(cur)
        return cur.fetchall()

    @classmethod
    def select_id(cls, name_id):
        _check_sql(cls)
        sql = "SELECT * FROM leetcode WHERE problem_id=%(name_id)s"
        value = {
            'name_id': name_id
        }
        cur.execute(sql, value)
        return cur.fetchall()

    @classmethod
    def select_title(cls, title):
        _check_sql(cls)
        sql = "SELECT * FROM leetcode WHERE problem_title=%(name_id)s"
        value = {
            'name_id': title
        }
        cur.execute(sql, value)
        return cur.fetchall()



