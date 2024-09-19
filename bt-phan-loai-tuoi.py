# age = int(input("ls enter your age:"))
# if age >= 0 and age <=12:
#     print ("Child")
# elif age >=13 and age <=17:
#     print ("Teenager")
# elif age >=18 and age <=59:
#     print ("Adult")
# elif age >= 60:
#     print ("Old person")
# else:
#     print ("Invalid age.")

age = int(input("Pls enter your age:"))
if age >= 0 and age <=12:
    age_category = "Child"
elif age >=13 and age <=17:
    age_category = "Teenager"
elif age >=18 and age <=59:
    age_category = "Adult"
elif age >= 60:
    age_category = "Old person"
else:
    print ("Invalid age.")

print(f"Age category is {age_category}")
