import smtplib
import datetime as dt
import random

myemail = "aakashdhariwal26@gmail.com"
password = "gqysjzstsidkttyd"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt") as quotes:
        all_quote = quotes.readlines()
        quote = random.choice(all_quote)

    print(quote)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(myemail, password )
        connection.sendmail(from_addr=myemail, to_addrs=myemail, msg =f"subject:Monday motivation\n\n {quote}")
