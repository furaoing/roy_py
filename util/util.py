import time
from mysql_driver import MySQLdriver


def get_formated_time():
    struct_time = time.localtime()
    year = struct_time.tm_year
    month = struct_time.tm_mon
    day = struct_time.tm_mday
    hour = struct_time.tm_hour
    min = struct_time.tm_min
    sec = struct_time.tm_sec
    formated_time = str(year) + "-" + str(month) + "-" + str(day) + "T" + str(hour) + ":" + str(min) + ":" + str(sec) + "+08:00"
    return formated_time


def es_to_mysql(json_obj, table):
    sql_part1 = "insert into " + table
    keys = json_obj.keys()

    sql_part2 = "("
    for key in keys:
        sql_part2 += key
        sql_part2 += ","
    sql_part2 = sql_part2.rstrip(",")
    sql_part2 += ")"

    sql_part3 = "("
    for key in keys:
        sql_part3 += "'" + str(json_obj[key]) + "'"
        sql_part3 += ","
    sql_part3 = sql_part3.rstrip(",")
    sql_part3 += ")"

    sql = sql_part1 + " " + sql_part2 + " values " + sql_part3
    return sql


if __name__ == "__main__":
    mysql = MySQLdriver("localhost", "root", "", "stock_market")
    json_obj = {"id": "23er454f"}
    table = "financial_summary"
    sql = es_to_mysql(json_obj, table)
    print(sql)
    mysql.insert(sql)
    mysql.clean_up()
