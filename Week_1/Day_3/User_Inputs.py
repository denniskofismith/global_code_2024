name = input("What is your name? ")

age = (input("What is your Age? "))

y = "years" if int(age) > 1 else "year"

print ("Hello " + name + "! You are " + age + " " + y + " old.")

if 0 < int(age)  < 24:
    print( "hello" + name + "you are " + age + "years" + "keep playing")
elif 13 >= int(age) < 24:
    print("hello" + name + "you are " + age + "years" + "start looking for job")
else:
    print("hello" + name + "you are " + age + "years" + "stop playing and start thinking")