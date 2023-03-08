questions = [
    # Format => [Question, Option 1, Option 2, Option 3, Option 4, Answer index]
    # Q.1
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", 4
    ],
    # Q.2
    [
        "Who invented calculus?", "Issac Newton", "Albert Einstien", "Aristotle",
        "Leonardo Da Vinci", 1
    ],
    # Q.3
    [
        "Who is regarded as father of Evolution?", "James Norway", "Issac Newton", "Charles Darwin",
        "Aristotle", 3
    ],
    # Q.4
    [
        "Which of the following is a python framework?", ".Net", "Flask", "React",
        "Nodejs", "None", 2
    ],
    # Q.5
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    # Q.6
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    # Q.7
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    # Q.8
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    # Q.9
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
    # Q.10
    [
        "Which language was used to create fb?", "Python", "French", "JavaScript",
        "Php", "None", 4
    ],
]

levels = [1000, 5000, 10000, 30000, 80000,
          160000, 320000, 650000, 980000, 15000000]
money = 0
for i in range(0, len(questions)):

    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print("=>", question[0])
    print(f"1. {question[1]}          2. {question[2]} ")
    print(f"3. {question[3]}          4. {question[4]} ")
    reply = int(input("Enter your answer (1-4) or  0 to quit:\n"))
    if (reply == 0):
        money = levels[i-1]
        break
    if (reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 320000
        elif (i == 14):
            money = 10000000
    else:
        print("Wrong answer!")
        break

reward_money = "{:,.2f}".format(money)
print(f"Your take home money is {reward_money}")
