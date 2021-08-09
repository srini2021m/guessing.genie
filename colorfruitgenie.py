import time
name=input("Hi!Welcome!" + "\n" + "What is your name?")
print("\n")
time.sleep(1)
print("Hello %s!!I am Jen and am going to be your guessing genie today."%(name))
time.sleep(1)
print("Lets play a guessing game. Take some time to think of a fruit and tell me its color.I will try to guess what it is.")
print("\n")
time.sleep(2)
color=input("Time's up! Now what is the color of the fruit you were thinking of?")
print("\n")
print("I was thinking about a %s colored fruit."%(color))
print("\n")
time.sleep(2)
print("oh the color of the fruit is %s? Let me guess what it could be!"%(color))
print("\n")
time.sleep(4)
if color=="red":
    print("The fruit your thinking of is either apple or strawberry.")
elif color=="green":
    print("The fruit your thinking of is either pear or guava.")
elif color=="yellow":
    print("The fruit your thinking of is either banana, mango or papaya.")
elif color=="orange":
    print("The fruit your thinking of is orange.")
elif color=="blue":
    print("The fruit your thinking of is blueberry.")
else:
    print("Unknown color, could not guess fruit, try again with a different color!")
print("\n")
time.sleep(2)
print("Thank you for playing this game, %s :)"%(name))


