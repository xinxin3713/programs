import pymysql.cursors

from mysql_study.config import db_config


class MySQL(object):
    '''

    MySQL类需要要connect和cursors属性，封装了对数据库的增，删，改，查的功能
    是没有实现连接池的，大家在项目的实际应用中。
    需要使用连接池，使用pymysqlpool或者自己实现一个连接池
    '''

    def __init__(self):
        self._conn = self.__create_conn()
        self._cursor = self._conn.cursor()

    def __create_conn(self):
        '''
        创建mysql数据库的连接
        :return:
        '''
        # 通过配置文件的方式来初始化连接信息
        config = db_config.config
        # 添加一些必要有不常修改的初始化信息
        config['cursorclass'] = pymysql.cursors.DictCursor
        connect = pymysql.connect(**config)
        return connect

    def _execute(self, sql, param):
        '''
        提取增删改查都要执行的语句（sql的执行语句）cursor.execut()
        :param sql:sql的执行语句
        :param param:SQL语句的参数
        :return:返回sql执行成功的数量
        '''
        if param is None:
            count = self._cursor.execute(sql)
        else:
            count = self._cursor.execute(sql,param)
        return count

    def get_select_all(self, sql, param=None):
        '''
        执行查询，并取得所有的匹配的结果集
        :param sql:
        :param param:
        :return: list(字典对象)
        '''
        count = self._execute(sql, param)
        if count > 0:
            result = self._cursor.fetchall()
        else:
            result = []
        return result

    def get_select_one(self, sql, param=None):
        '''
        执行查询，并取出第一条
        :param sql:
        :param param:
        :return:
        '''
        count = self._execute(sql, param)
        if count > 0:
            result = self._cursor.fetchone()
        else:
            result = []
        return result

    def get_select_many(self, sql, param=None, num=0):
        '''

        :param sql: sql查询语句
        :param param: 条件参数
        :param num: 取得的结果条数
        :return:
        '''
        count = self._execute(sql, param)
        if count > 0:
            result = self._cursor.fetchmany(num)
        else:
            result = []
        return result

    def __get_insert_id(self):
        '''
        通过execute('SELECT @@IDENTITY AS id')获取插入后的信息
        :return:
        '''
        self._cursor.execute('SELECT @@IDENTITY AS id')
        result = self._cursor.fetchall()
        return result[0]['id']

    def insert_one(self, sql, param):
        '''
        插入一条数据
        :param sql:
        :param param:
        :return:
        '''
        self._execute(sql, param)
        return self.__get_insert_id()

    def insert_many(self, sql, param):
        '''
        插入多条数据
        :param sql:
        :param param:
        :return:
        '''
        count = self._cursor.executemany(sql, param)
        return count

    def update(self,sql,param=None):
        return self._execute(sql,param)

    def delete(self,sql,param = None):
        return self._execute(sql,param)

    def dispose(self):
        self._conn.commit()
        self._cursor.close()
        self._conn.close()


