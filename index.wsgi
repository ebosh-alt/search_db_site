import os
import sys
BASE_DIR = 'host1854955/xmee.info/htdocs/www/flask/' # путь до сайта

# Добавляем путь в переменные среды/переменное окружение
sys.path.append(BASE_DIR)

# делаем этот путь активным каталогом (т.е переходим в него)
os.chdir(BASE_DIR)

# Подключение виртуальной среды python (опционально)
# Указываем путь до активации виртуальной среды (замена source activate)
# activate_this = '/home/hostXXXXXXX/flask-dev.com/htdocs/www/virtualenv/bin/activate_this.py'

# Выполняем активацию
# exec(open(activate_this).read())

# Добавляем путь в переменные среды пакеты python
# sys.path.append('/home/hostXXXXXXX/flask-dev.com/htdocs/www/virtualenv/lib/python3.6/site-packages/')

from bottle import default_app

sys.path.insert(0, 'host1854955/xmee.info/htdocs/www/flask')
from app import app as application