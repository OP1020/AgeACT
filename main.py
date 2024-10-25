age = int(input("What is your age?:"))
if age < 5:
    print("You should play with toys.")
elif age >= 5 and age <= 12:
    print("You can play outdoor games.")
# TODO: handle the 13 to 17 condition
elif age >= 13 and age <= 17:
    print("You can play video games.")
# TODO: handle the 18 or older condition.
else:
    print("You can try hiking or traveling")