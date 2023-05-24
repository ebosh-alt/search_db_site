from dns import D_users
from sogaz import S_users
from yandex import Y_users

db_file_name = "db.db"

table_name = "y_users"
args = {
    'key': 'integer',
    'yauid': 'integer',
    'username': 'text',
    'email': 'text',
    'first_name': 'text',
    'last_name': 'text',
    'phone_number': 'text',
}

y_users = Y_users(db_file_name=db_file_name, args=args, table_name=table_name)

table_name = "s_users"
args = {
    "key": "integer",
    "TIMESTAMP_X": "text",
    "LOGIN": "text",
    "PASSWORD": "text",
    "CHECKWORD": "text",
    "ACTIVE": "text",
    "NAME": "text",
    "LAST_NAME": "text",
    "EMAIL": "text",
    "LAST_LOGIN": "text",
    "DATE_REGISTER": "text",
    "LID": "text",
    "PERSONAL_PROFESSION": "text",
    "PERSONAL_WWW": "text",
    "PERSONAL_ICQ": "text",
    "PERSONAL_GENDER": "text",
    "PERSONAL_BIRTHDATE": "text",
    "PERSONAL_PHOTO": "text",
    "PERSONAL_PHONE": "text",
    "PERSONAL_FAX": "text",
    "PERSONAL_MOBILE": "text",
    "PERSONAL_PAGER": "text",
    "PERSONAL_STREET": "text",
    "PERSONAL_MAILBOX": "text",
    "PERSONAL_CITY": "text",
    "PERSONAL_STATE": "text",
    "PERSONAL_ZIP": "text",
    "PERSONAL_COUNTRY": "text",
    "PERSONAL_NOTES": "text",
    "WORK_COMPANY": "text",
    "WORK_DEPARTMENT": "text",
    "WORK_POSITION": "text",
    "WORK_WWW": "text",
    "WORK_PHONE": "text",
    "WORK_FAX": "text",
    "WORK_PAGER": "text",
    "WORK_STREET": "text",
    "WORK_MAILBOX": "text",
    "WORK_CITY": "text",
    "WORK_STATE": "text",
    "WORK_ZIP": "text",
    "WORK_COUNTRY": "text",
    "WORK_PROFILE": "text",
    "WORK_LOGO": "text",
    "WORK_NOTES": "text",
    "ADMIN_NOTES": "text",
    "STORED_HASH": "text",
    "XML_ID": "text",
    "PERSONAL_BIRTHDAY": "text",
    "EXTERNAL_AUTH_ID": "text",
    "CHECKWORD_TIME": "text",
    "SECOND_NAME": "text",
    "CONFIRM_CODE": "text",
    "LOGIN_ATTEMPTS": "text",
    "LAST_ACTIVITY_DATE": "text",
    "AUTO_TIME_ZONE": "text",
    "TIME_ZONE": "text",
    "TIME_ZONE_OFFSET": "text",
    "TITLE": "text",
    "BX_USER_ID": "text",
    "LANGUAGE_ID": "text",
    "BLOCKED": "text",
    "PASSWORD_EXPIRED": "text"
}

s_users = S_users(db_file_name=db_file_name, args=args, table_name=table_name)

table_name = "d_users"
args = {
    'key': 'integer',
    'nickname': 'text',
    'phone': 'text',
    'email': 'text',
    'year': 'text',
    'date_registration': 'text',
    'date_last': 'text',
}

d_users = D_users(db_file_name=db_file_name, args=args, table_name=table_name)
