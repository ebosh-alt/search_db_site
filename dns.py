from SQLite import Sqlite3_Database
from config import *


class D_user:
    def __init__(self, key, nickname, phone, email, year, date_registration, date_last):
        self.key = key
        self.nickname = nickname
        self.phone = phone
        self.email = email
        self.year = year
        self.date_registration = date_registration
        self.date_last = date_last

    def get_tuple(self):
        return (self.key,
                self.nickname,
                self.phone,
                self.email,
                self.year,
                self.date_registration,
                self.date_last
                )


class D_users(Sqlite3_Database):
    def __init__(self, db_file_name, args, table_name) :
        Sqlite3_Database.__init__(self, db_file_name, args, table_name)

    def add(self, user):
        if user is D_user:
            self.add_row(user.get_tuple())
        else:
            self.add_row(user)

    def get(self, id):
        if id in self:
            obj_tuple = self.get_elem_sqllite3(id)
            obj = D_user(
                key=obj_tuple[0],
                nickname=obj_tuple[1],
                phone=obj_tuple[2],
                email=obj_tuple[3],
                year=obj_tuple[4],
                date_registration=obj_tuple[5],
                date_last=obj_tuple[6],
            )
            return obj
        return False

    def get_by_number_phone(self, number_phone):
        conn = self.sqlite_connect()
        curs = conn.cursor()
        curs.execute(f"""SELECT key, phone, email, year FROM {self.table_name} where phone = '{number_phone}'""")
        grand_tuple = curs.fetchall()
        conn.commit()
        conn.close()
        return grand_tuple

    def get_by_fullname_date_birthday(self, data):
        data = data.split(" ")
        conn = self.sqlite_connect()
        curs = conn.cursor()
        curs.execute(f"""SELECT key from {self.table_name} where year = '{data[3].replace(".", "-")}'""")
        grand_tuple = curs.fetchall()
        conn.commit()
        conn.close()
        return grand_tuple

    def get_by_email(self, email):
        conn = self.sqlite_connect()
        curs = conn.cursor()
        curs.execute(f"""SELECT key from {self.table_name} where email = '{email}'""")
        grand_tuple = curs.fetchall()
        conn.commit()
        conn.close()
        return grand_tuple




def insert_user():
    with open("/dns-shop.sql", "r", encoding="utf-8") as file1:
        while True:
            line = file1.readline()
            if not line:
                break
            line = line.strip().replace("'", "").replace("(", "").replace("),", "")
            if "--" in line or "SET" in line or "INSERT" in line or len(line) < 2:
                continue
            else:
                try:
                    line = line.split(", ")
                    line[0] = int(line[0])
                    d_users.add(line)
                except Exception as ex:
                    logging.error(f"{line} - {ex}")


if __name__ == "__main__":
    insert_user()
