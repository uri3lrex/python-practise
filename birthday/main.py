import datetime, bday_messages
today= datetime.date.today()
next_birthday= datetime.date(2024,11,16)
diff= next_birthday-today

if (today==next_birthday):
    print(bday_messages.wish)
else:
    print("My next birthday is " + str(diff.days) +" days away!")
