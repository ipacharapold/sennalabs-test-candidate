import sqlite3
import os

def connection():
    file = 'test.db'
    my_dir = os.path.dirname(__file__)
    file_path = os.path.join(my_dir, file)
    conn = sqlite3.connect(file_path)
    return conn

def create_table():
    db = connection()
    db.execute("""CREATE TABLE CARS
    (ID INTEGER PRIMARY KEY,
    NAME CHAR(50) NOT NULL,
    CAR CHAR(50) NOT NULL);""")
    db.close()
    print("Table created successfully")

def insert():
    db = connection()
    data = {
        'Rick': ['Corvette Z06', 'Lotus Exige S', 'BMW M3'],
        'John': ['BMW 320d', 'Mercedes SLK AMG'],
        'Zing': ['Toyota Alphard', 'Mercedes Sprinter'],
        'Nan': ['Toyota Camry', 'BMW M5', 'Porsche 911', 'Jaguar', 'TukTuk', 'Mini Cooper', 'Honda Jazz']
    }
    for name in data.keys():
        for item in data[name]:
            db.execute("INSERT INTO CARS (NAME, CAR) VALUES ('{name}', '{car}');".format(name=name, car=item))
    db.commit()
    db.close()
    print("Insert data successfully")

def show():
    db = connection()
    sql = "SELECT * FROM CARS;"
    cursor = db.execute(sql)
    for row in cursor:
        print("{id} {name} {car}".format(id=row[0], name=row[1], car=row[2]))

if __name__ == '__main__':
    create_table()
    insert()
    show()
