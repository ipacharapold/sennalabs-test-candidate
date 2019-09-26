from quiz6 import connection

def report_more():
    db = connection()
    sql = "SELECT name, count(car) as 'total' FROM CARS GROUP BY name HAVING total > 2 ORDER BY total ASC;"
    cursor = db.execute(sql)
    for row in cursor:
        print("{name}, {num}".format(name=row[0], num=row[1]))

if __name__ == '__main__':
    report_more()