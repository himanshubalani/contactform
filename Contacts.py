#imports
import time
import datetime
from csv import writer
from contactcode import codes
import re


# predefined variables
now = datetime.datetime.now()
islongenough = False
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


# functions
def wait():  # ADD WAITING TIME TO FEEL REALISTIC
    print('....')
    time.sleep(0.75)


def lil():  # ADD LITTLE WAITING TIME TO FEEL REALISTIC
    time.sleep(0.35)

# for name and address


def input_validation(prompt):
    # keep looping until they enter a proper name
    while True:
        # get the answer as a string
        answer = input(prompt)
        try:
            score = str(answer)
            if answer == "tick":
                import easter as easter
                easter.ACTIVE
            elif answer == "exit":
                exit()
            # if in range, we're done!
            elif 1 < len(score) < 50:
                return score
            # otherwise out of range, print an error message and keep looping
            else:
                print('Input cannot be less than 2 characters or more than 50!')
        # if the answer wasn't a number, print an error message and keep looping
        except ValueError:
            print('That is not a name.')

# for date


def date_validation(prompt):
    while True:
        answer = input(prompt)
        try:
            score = int(answer)
            if score <= 31:
                return score
            else:
                print('date cannot be greater than 31')
        except ValueError:
            print('That is not a date')

# month


def month_validation(prompt):
    while True:
        answer = input(prompt)
        try:
            score = int(answer)
            if score <= 12:
                return score
            else:
                print('month cannot be greater than 12')
        except ValueError:
            print('That is not a date')

# year


def year_validation(prompt):
    while True:
        answer = input(prompt)
        try:
            score = int(answer)
            if score <= now.year:
                if score >= (now.year - 120):
                    return score
                else:
                    print("You sure aren't older than 120,RETRY!")
            else:
                print(
                    "Year cannot be greater than current year,make sure you're born! :)")
        except ValueError:
            print('That is not a year')

# PhoneNumber


def contact_validaton(prompt):
    while True:
        answer = input(prompt)
        try:
            if len(answer) == 10:
                return answer
            else:
                print(
                    "Contact Number cannot be greater than or less than 10 digits, make sure you've entered it properly! :)")
        except ValueError:
            print('That is not a contact Number')

# email address


def email_verfication(prompt):
    while True:
        answer = input(prompt)
        try:
            if(re.search(regex, answer)):
                return answer
            else:
                print("Invalid E-mail, make sure you've entered it properly! :)")
        except ValueError:
            print('That is not a E-mail address')

#Saving data
def csvsave(ans):
    if ans == "Y":
        with open(filename, 'a') as csvfile:
            csvwriter = writer(csvfile)
            csvwriter.writerows(data)
            csvfile.close()
    elif ans == "N":
        print('\t OK BYE')
        exit()



# Flow
print("Hello! Let's create your record")  # welcome
fname = input_validation('Enter your first name:    ').title()
print(fname, 'is a good name!')
lil()
print('Now tell me your middle and last names')
lil()
mname = input_validation('Enter your middle name:    ').title()
lil()
sname = input_validation('Enter your last name:    ').title()
wait()
print('Ok so,', fname, mname, sname)
lil()
email = email_verfication('Enter email address: ')
wait()
print("Let's see how old are you")
lil()
dat = date_validation('Enter your Birth-date(DD):   ')
mon = month_validation('Enter your Birth-month(MM):   ')
monab = int(mon)
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
if 1 <= monab <= 12:
    print('ok so', months[monab - 1], ' Great!')
print('i was born in Feb 2021,well talking about years;')
yea = year_validation("What's your year?'(YYYY)   ")
wait()
print('ok you were born on', dat, mon, yea, "\nAnd that makes you around")
lil()
age = now.year - int(yea)
if (now.month == mon and now.day < dat) or now.month < mon:
    age -= 1
print(age, 'years old')
lil()
contact = contact_validaton("Enter your Phone Number:   ")
print("Your number is ", contact)
wait()
print("SO, where do you live?\nLet's do it in three lines")
housen = input_validation('Enter your address(1):   ').title()
streetn = input_validation('(2):    ').title()
land = input_validation('(3):   ').title()
lil()
print('Now.....')
wait()
city = input_validation('Your city:   ').title()
state = input_validation('Your state:   ').title()
country = input("Your Country:  ").title()
pincode = int(input('Your Pincode:   '))
lil()
print('Noted.', housen, streetn, land, city, state, country, '-', pincode)

name = '{} {} {}'.format(fname, mname, sname)
bd = '"{}-{}-{}"'.format(dat, mon, yea)
bm = months[monab - 1]
con = '{} {} {} {}'.format(
    "+" + str(codes[country]), contact[0:3], contact[3:6], contact[6:10])
adr = '{}, {}, {}'.format(housen, streetn, land)
#header = ['Name', 'Birthmonth', 'BirthDate', 'Age', 'Email','Contact No.', 'Address', 'City', 'State', 'Country', 'Pincode']
data = [[name, bm, bd, str(age), email, con, adr,
         city, state, country, str(pincode)]]

# name of csv file
filename = "data.csv"
wait()
# Summary
print('Let me gather your info and present it to you in a second')
time.sleep(2.0)
print(f'Name         | {name}')
lil()
print(f'Birthmonth   | {bm}')
lil()
print(f'Birthdate    | {bd}')
lil()
print(f'Age          | {age}')
lil()
print(f'E-mail       | {email}')
lil()
print(f'Contact No.  | {con}')
lil()
print('Address      | {}\n''             | {}\n''             | {}'.format(
    housen, streetn, land))
lil()
print('City         | {}\n''State        | {}\n''Country      | {}\n''Pincode      | {}'.format(
    city, state, country, pincode))
lil()

sav = input("Do you wish to save this data? (Y/N)").title()
csvsave(sav)
print('Here you go!', "\n Saving your data...")
print("Good Bye 👋")