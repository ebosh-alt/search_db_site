from SQLite import Sqlite3_Database
from config import *


class Y_user:
    def __init__(self, key, yauid, username, email, first_name, last_name, phone_number):
        self.key = key
        self.yauid = yauid
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def get_tuple(self) -> tuple:
        return (self.key,
                self.yauid,
                self.username,
                self.email,
                self.first_name,
                self.last_name,
                self.phone_number
                )


class Y_users(Sqlite3_Database):
    def __init__(self, db_file_name, args, table_name):
        Sqlite3_Database.__init__(self, db_file_name, args, table_name)

    def add(self, user):
        self.add_row(user.get_tuple())

    def get(self, id):
        if id in self:
            obj_tuple = self.get_elem_sqllite3(id)
            obj = Y_user(
                key=obj_tuple[0],
                yauid=obj_tuple[1],
                username=obj_tuple[2],
                email=obj_tuple[3],
                first_name=obj_tuple[4],
                last_name=obj_tuple[5],
                phone_number=obj_tuple[6],
            )
            return obj
        return False

    def get_by_number_phone(self, number_phone):
        conn = self.sqlite_connect()
        curs = conn.cursor()
        curs.execute(f"""SELECT key, email, first_name, last_name, phone_number from {self.table_name} where phone_number = '{number_phone}'""")
        grand_tuple = curs.fetchall()
        conn.commit()
        conn.close()
        return grand_tuple

    def get_by_fullname_date_birthday(self, data):
        data = data.split(" ")
        conn = self.sqlite_connect()
        curs = conn.cursor()
        curs.execute(f"""SELECT key, email, first_name, last_name, phone_number from {self.table_name} where first_name = '{data[1]}' and last_name = '{data[0]}'""")
        grand_tuple = curs.fetchall()
        conn.commit()
        conn.close()
        return grand_tuple

    def get_by_email(self, email):
        conn = self.sqlite_connect()
        curs = conn.cursor()
        curs.execute(f"""SELECT key, email, first_name, last_name, phone_number from {self.table_name} where email = '{email}'""")
        grand_tuple = curs.fetchall()
        conn.commit()
        conn.close()
        return grand_tuple

def insert_user():
    with open("/RUYandexPraktikum300k.txt", "r", encoding="utf-8") as f:
        data = f.read().split("\n")

    for obj in data[1::]:
        obj_tuple = obj.split("\t")
        y_users.add(Y_user(
            key=obj_tuple[0],
            yauid=obj_tuple[1],
            username=obj_tuple[2],
            email=obj_tuple[3],
            first_name=obj_tuple[4],
            last_name=obj_tuple[5],
            phone_number=obj_tuple[6],
        ))


if __name__ == "__main__":
    print(y_users.get_by_number_phone("+79003887228"))
    # print(y_users.get(20).phone_number)
