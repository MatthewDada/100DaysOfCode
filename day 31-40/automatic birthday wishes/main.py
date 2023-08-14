import pandas as pd
import datetime as dt
import smtplib
import random

letters = []
with open("day 31-40\\automatic birthday wishes\\letter_templates\\letter_1.txt") as file:
    letter1 = file.readlines()
    letters.append(letter1)

with open("day 31-40\\automatic birthday wishes\\letter_templates\\letter_2.txt") as file:
    letter2 = file.readlines()
    letters.append(letter2)

with open("day 31-40\\automatic birthday wishes\\letter_templates\\letter_3.txt") as file:
    letter3 = file.readlines()
    letters.append(letter3)

df = pd.read_csv("day 31-40\\automatic birthday wishes\\birthdays.csv")

# Replace the details in the next two lines
birthdate = dt.datetime(year=0, month=0, day=0)
df.loc[1] = ["name", "email@gmail.com", birthdate.year, birthdate.month, birthdate.day]

now = dt.datetime.now()

if float(now.month) in df["month"].unique():
    if float(now.day) in df[df.month == float(now.month)]["day"].unique():
        name_of_recipient = df[df.month == float(now.month)]["name"].values[0]
        recipient_email = df[df.month == float(now.month)]["email"]

        random_letter = random.choice(letters)
        password = "" # Make use of an app password gotten from google. Check online for guide.
        my_email = ""
        birthday_wish = ""
        random_letter = [i.replace('[NAME]', f'{name_of_recipient}') for i in random_letter]

        for line in random_letter:
            birthday_wish += line

        # print(birthday_wish)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.ehlo()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=recipient_email,
                                msg=f"Subject:It's Your Birthday!.\n\n{birthday_wish}")

