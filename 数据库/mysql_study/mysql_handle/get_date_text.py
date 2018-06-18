import mysql_handle

def read_file(file_path):
    with open(file_path, 'r', encoding='UTF-8') as  f:
        r = f.readlines()

    return r

def data_split(list):
    list_ret = []
    for line in list:
        l = line.strip().split('，')
        list_ret.append(l)
    return list_ret




if __name__ == '__main__':
    mysql = mysql_handle.MySQL()
    data = read_file('data_test.txt')
    l = data_split(data)
    #print(l)
    sql = 'insert into expense (person_sn, name, dname, money, expense_date)VALUES (%s,%s,%s,%s,%s)'
    for line in l:
        #print(line)
        mysql.insert_one(sql,line)
    mysql.dispose()
    #print(mysql.insert_many(sql,l))
    #mysql = mysql_handle.MySQL()