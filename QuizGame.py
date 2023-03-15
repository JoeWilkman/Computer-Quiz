print("Welcome to my computer quiz!")

name = input("We can start off with some introductions. My name is Test Master; pleasure to meet you. And your name is? ")

print("Well then, " + name + ", it is a pleasure to have you. Now, I have a question you.")

playing = input("Do you want to play my little computer quiz game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("Question 1: What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Question 2: What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Question 3: What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Question 4: What does PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")