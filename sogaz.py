from SQLite import Sqlite3_Database
from config import *


class S_user:
    def __init__(self, key, yauid, username, email, first_name, last_name, phone_number):
        self.key = key
        self.yauid = yauid
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def get_tuple(self) :
        return (self.key,
                self.yauid,
                self.username,
                self.email,
                self.first_name,
                self.last_name,
                self.phone_number
                )


class S_users(Sqlite3_Database):
    def __init__(self, db_file_name, args, table_name):
        Sqlite3_Database.__init__(self, db_file_name, args, table_name)

    def add(self, user):
        if user is S_user:
            self.add_row(user.get_tuple())
        else:
            self.add_row(user)

    def get(self, id):
        if id in self:
            obj_tuple = self.get_elem_sqllite3(id)
            obj = S_user(
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
        curs.execute(
            f"""SELECT key, NAME, LAST_NAME, SECOND_NAME, EMAIL, PERSONAL_BIRTHDATE, PERSONAL_STREET, PERSONAL_PHONE FROM {self.table_name} where WORK_PHONE = '{number_phone}' or PERSONAL_PHONE = '{number_phone}'""")
        grand_tuple = curs.fetchall()
        conn.commit()
        conn.close()
        return grand_tuple

    def get_by_fullname_date_birthday(self, res):
        new_data: list = res.split(" ")
        conn = self.sqlite_connect()
        curs = conn.cursor()
        curs.execute(f"""SELECT key, NAME, LAST_NAME, SECOND_NAME, EMAIL, PERSONAL_BIRTHDATE, PERSONAL_STREET, PERSONAL_PHONE from {self.table_name} where NAME = '{new_data[1]}' and LAST_NAME = '{new_data[0]}' 
                                                and SECOND_NAME = '{new_data[2]}'""")
        grand_tuple = curs.fetchall()
        conn.commit()
        conn.close()
        return grand_tuple

    def get_by_email(self, email):
        conn = self.sqlite_connect()
        curs = conn.cursor()

        curs.execute(f"""SELECT key, NAME, LAST_NAME, SECOND_NAME, EMAIL, PERSONAL_BIRTHDATE, PERSONAL_STREET, PERSONAL_PHONE
                                                                    from {self.table_name} where EMAIL = '{email}'""")
        grand_tuple = curs.fetchall()
        conn.commit()
        conn.close()
        return grand_tuple

    def get_by_address(self, address):
        conn = self.sqlite_connect()
        curs = conn.cursor()
        curs.execute(f"""SELECT PERSONAL_STREET, PERSONAL_CITY, NAME, LAST_NAME, SECOND_NAME, EMAIL, PERSONAL_BIRTHDATE, 
            PERSONAL_PHONE  from {self.table_name} where PERSONAL_STREET is not null or PERSONAL_CITY is not null """)
        grand_tuple = curs.fetchall()
        result = []
        conn.commit()
        conn.close()
        for tup in grand_tuple:
            if address in tup[0] or address in tup[1]:
                result.append(tup)
        return result

def insert_user():
    with open("Sogaz_LIFE.sql", "r", encoding="utf-8") as f:
        data = f.read().replace("'", "").replace(",", "").replace("(", "").replace(")", "").replace(";", "").split("\n")

    for obj in data[1::]:
        if "INTO" not in obj:
            obj_tuple = obj.split("\t")
            s_users.add(obj_tuple)


if __name__ == "__main__":
    data = s_users.get_by_address("Прохоров")
    print(data)
    # a = "89987388284"
    # print(a.replace("8", "7", 1))