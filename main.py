##################### Hard Starting Project ######################

import datetime as dt
import smtplib
import random
import pandas
EMAIL = "khazratkulovshokhzod@gmail.com"
PASSWORD = "wpirdldodbbhhljv"

today = dt.datetime.now()
today_tuple = (today.month, today.day) # kerakli bo'lgan kunni tuple ko'rinishida saqalab olish
data = pandas.read_csv("birthdays.csv")  #pandas orqali csv fileni o'qib olish
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()} #o'qib olingan
# csv fileni dictionary ga saqlash bunda row orqali ishlanadi.
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]  #kimning tugilgan kun sanasi to'g'ri kelsa ana o'shani shaxs sifatida
# barcha ma'lumotlarni saqlaydi ismini emailini hammasini
    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt" #letterlardan birini tanlab olish usuli
    with open(letter_path) as letters: #letterni ochib olamiz va uni o'qitamiz
        contents = letters.read()
        contents = contents.replace("[NAME]", birthdays_person["name"]) #ismni o'zgartirish usuli

    with smtplib.SMTP("smtp.gmail.com") as connection: #har doim smtplib ni start() bilan boshlab keyin close() bilan
        connection.starttls()              #tugatish kerak bo'ladi agar with open() bn ochsak uni o'zi automatic yopiladi
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=birthdays_person.email,
                            msg=f"subject: Happy birthday\n\n{contents}")





