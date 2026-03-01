bold = "\033[1m"
italic = "\033[3m"
reset = "\033[0m"
from colorama import init, Fore
init (autoreset=True)

# RESUME TITLE
print (( bold + "RESUME" + reset ).center(65))
print (" ")


# Objective
print ( italic + "OBJECTIVES" + reset )
objectives = input (("What are your objectives? :").center(30))
print (bold + "You want" " " + Fore.GREEN + objectives)
print ("")

# Personal Information
print ( italic + "PERSONAL INFORMATION" + reset )
name = input (("What is your name? :").center(30))
birthdate = input (("When is your birthday? :").center(30))
age = input (("How old are you? :").center(30))
gender = input (("What is your gender? : ").center(30))
nationality = input (("What is your nationality? :").center(30))
religion = input (("What is your religion? :").center(30))
language = input (("What are the your languages you know? :").center(30))
print (" ")
print ( bold + "Your name is" " " + Fore.GREEN + name)
print (bold + "Your birthdate is" " " + Fore.GREEN + birthdate)
print (bold + "You are" " " + Fore.GREEN + age +" " "years old")
print (bold + "You are a" " " + Fore.GREEN + gender)
print (bold + "You are a" " " + Fore.GREEN + nationality)
print (bold + "Your religion is" " " + Fore.GREEN + religion)
print (bold + "You speak" " " + Fore.GREEN + language)
print ("")

# Educational Background
print ( italic + "EDUCATIONAL BACKGROUND" + reset )
print ("Please input corresponding answers")
shs = input (("Senior High School : ").center(30))
year = input (("Year :").center(30))
jhs = input (("Junior High School : ").center(30))
year = input (("Year :").center(30))
elem = input (("Elementary : ").center(30))
year = input (("Year :").center(30))
print ("")

# Skills
print ( italic + "SKILLS" + reset )
skills = input (("What are your skills? : ").center(30))
print (bold + "You can" " " + Fore.GREEN + skills)
print ("")

# Characteristics
print ( italic + "CHARACTERISTICS" + reset)
first_characteristic = input ((" First characteristic :").center(30))
print (bold + "a." " " + Fore.GREEN + a)
second_characteristic = input ((" Second characteristic :").center(30))
print (bold + "b." " " + Fore.GREEN + b)
third_characteristic = input ((" Third characteristic :").center(30))
print (bold + "c." " " + Fore.GREEN + c)
print("")

# Achievements
print ( italic + "ACHIEVEMENTS" + reset)
achievement_one = input ((" Achievement 1 :").center(30))
print (bold + "a." " " + Fore.GREEN + a)
achievement_two = input ((" Achievement 2 :").center(30))
print (bold + "b." " " + Fore.GREEN + b)
achievement_three = input ((" Achievement 3 :").center(30))
print (bold + "c." " " + Fore.GREEN + c)
achievement_four = input ((" Achievement 4 :").center(30))
print (bold + "d." " " + Fore.GREEN + d)
achievement_five = input ((" Achievement 5 :").center(30))
print (bold + "e." " " + Fore.GREEN + e)
achievement_six = input ((" Achievement 6 :").center(30))
print (bold + "f." " " + Fore.GREEN + f)
print ("")

# Contact Details
print ("Please feel free to contact me through :")
input_email = input (("E-mail : ").center(30))
input_number = input (("Number :").center(30))






