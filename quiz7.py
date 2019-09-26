from quiz6 import connection

def report_name():
    db = connection()
    sql = "SELECT name, count(car) FROM CARS GROUP BY name;"
    cursor = db.execute(sql)
    for row in cursor:
        print("{name}, {num}".format(name=row[0], num=row[1]))

if __name__ == '__main__':
    report_name()