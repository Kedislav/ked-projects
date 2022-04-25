import random

name = str(input("What is your name? "))
question = str(input("What question do you want to ask the magic 8-ball? "))
random_number = random.randint(1, 9)
answers = ["Yes - definitely.", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful."]

print(name + " asks: " + question + "\n")
print("Magic 8-Ball’s answer: " + answers[random_number])
