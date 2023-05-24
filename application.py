import re

from flask import Flask, request, render_template

from config import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    req = request.args.get("req")
    if req is not None:
        if re.fullmatch(string=req, pattern="\D+\s\D+\s\D+\s\d\d.\d\d.\d{4}"):
            data = s_users.get_by_fullname_date_birthday(req)
            template = "<div class='info'>"
            for i in data:
                template += "<div class='info'>"
                template += f"<p>Имя: {i[1]}</p>\n<p>Фамилия: {i[2]}</p>\n<p>Отчество: {i[3]}</p>\n<p>Почта: {i[4]}</p>\n<p>Телефон: {i[7]}</p>\n<p>День рождения: {i[5]}</p>\n<p>Адрес: {i[6]}</p>\n"
                template += "</div>"
            template += "</div>"

            data = y_users.get_by_fullname_date_birthday(req)
            template += "<div class='info'>"

            for i in data:
                template += "<div class='info'>"
                template += f"<p>Имя: {i[2]}</p>\n<p>Фамилия: {i[3]}</p>\n<p>Почта: {i[1]}</p>\n<p>Телефон: {i[4]}</p>"
                template += "</div>"
            template += "</div>"

            if len(template) == 72:
                template = "<div class='info'><h1>Ничего не найдено</h1>"
            with open("./templates/index.html", "r", encoding='utf-8') as f:
                page = f.read()
                page = page.split("{{ text }}")
                page[0] += template
            result = "".join(page)
            return result

        elif re.fullmatch("^\\+?[1-9][0-9]{7,14}$", req):
            number = req.replace("+", "")
            if number[0] == "8":
                number = number.replace("8", "7", 1)
            data = s_users.get_by_number_phone(number)
            template = "<div class='info'>"
            for i in data:
                template += "<div class='info'>"
                template += f"<p>Имя: {i[1]}</p>\n<p>Фамилия: {i[2]}</p>\n<p>Отчество: {i[3]}</p>\n<p>Почта: {i[4]}</p>\n<p>Телефон: {i[7]}</p>\n<p>День рождения: {i[5]}</p>\n<p>Адрес: {i[6]}</p>\n"
                template += "</div>"
            template += "</div>"

            number = req
            if number[0] == "7":
                number = number.replace("7", "+7", 1)
            if number[0] == "8":
                number = number.replace("8", "+7", 1)

            data = y_users.get_by_number_phone(number)
            template += "<div class='info'>"
            for i in data:
                template += "<div class='info'>"
                template += f"<p>Имя: {i[2]}</p>\n<p>Фамилия: {i[3]}</p>\n<p>Почта: {i[1]}</p>\n<p>Телефон: {i[4]}</p>"
                template += "</div>"
            template += "</div>"

            number = req.replace("+", "")
            if number[0] == "8":
                number = number.replace("8", "7", 1)
            data = d_users.get_by_number_phone(number)
            template += "<div class='info'>"
            for i in data:
                template += "<div class='info'>"
                template += f"<p>Почта: {i[2]}</p>\n<p>Телефон: {i[1]}</p>\n<p>День рождения: {i[3]}</p>\n"
                template += "</div>"
            template += "</div>"
            if len(template) == 72:
                template = "<div class='info'><h1>Ничего не найдено</h1>"
            with open("./templates/index.html", "r", encoding='utf-8') as f:
                page = f.read()
                page = page.split("{{ text }}")
                page[0] += template
            result = "".join(page)

            return result

        elif re.fullmatch(string=req, pattern="^\S+@\S+\.\S+$"):
            data = s_users.get_by_email(req)
            template = "<div class='info'>"
            for i in data:
                template += "<div class='info'>"
                template += f"<p>Имя: {i[1]}</p>\n<p>Фамилия: {i[2]}</p>\n<p>Отчество: {i[3]}</p>\n<p>Почта: {i[4]}</p>\n<p>Телефон: {i[7]}</p>\n<p>День рождения: {i[5]}</p>\n<p>Адрес: {i[6]}</p>\n"
                template += "</div>"
            template += "</div>"

            data = y_users.get_by_email(req)

            template += "<div class='info'>"
            for i in data:
                template += "<div class='info'>"
                template += f"<p>Имя: {i[2]}</p>\n<p>Фамилия: {i[3]}</p>\n<p>Почта: {i[1]}</p>\n<p>Телефон: {i[4]}</p>"
                template += "</div>"
            template += "</div>"

            data = d_users.get_by_email(req)
            template += "<div class='info'>"
            for i in data:
                template += "<div class='info'>"
                template += f"<p>Почта: {i[2]}</p>\n<p>Телефон: {i[1]}</p>\n<p>День рождения: {i[3]}</p>\n"
                template += "</div>"
            template += "</div>"

            if len(template) == 72:
                template = "<div class='info'><h1>Ничего не найдено</h1>"
            with open("./templates/index.html", "r", encoding='utf-8') as f:
                page = f.read()
                page = page.split("{{ text }}")
                page[0] += template
            result = "".join(page)

            return result

        else:
            data = s_users.get_by_address(req)
            template = "<div class='info'>"
            for i in data:
                template += "<div class='info'>"
                template += f"<p>Имя: {i[2]}</p>\n<p>Фамилия: {i[3]}</p>\n<p>Отчество: {i[4]}</p>\n<p>Почта: {i[5]}</p>\n<p>Телефон: {i[7]}</p>\n<p>День рождения: {i[6]}</p>\n"
                address = ""
                if i[0] is not None and len(i[0]) > 1 and i[0] != "NULL":
                    address += i[0]
                elif i[1] is not None and len(i[1]) > 1 and i[1] != "NULL":
                    address += " " + i[1]
                if address != "":
                    template += f"<p>Адрес: {address}</p>\n"
                template += "</div>"
            template += "</div>"
            if len(template) == 72 or len(data) == 0:
                template = "<div class='info'><h1>Ничего не найдено</h1>"
            with open("./templates/index.html", "r", encoding='utf-8') as f:
                page = f.read()
                page = page.split("{{ text }}")
                page[0] += template
            result = "".join(page)
            return result
    with open("./templates/index.html", "r", encoding='utf-8') as f:
        page = f.read()
        page = page.replace("{{ text }}", "")
    return page


if __name__ == "__main__":
    app.run(debug=False, host='45.12.74.110', port=5000)
