# Python Quiz Game
def quiz_game():
    questions = [
        {
            "question": "Which type of language is Python?",
            "options": ["Compiled", "Interpreted", "Machine", "Assembly"],
            "answer": 2
        },
        {
            "question": "Which brackets are used to create a list in Python?",
            "options": ["{}", "()", "[]", "<>"],
            "answer": 3
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "define", "def", "function"],
            "answer": 3
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["//", "/* */", "#", "<!-- -->"],
            "answer": 3
        },
        {
            "question": "Which function is used to open a file in Python?",
            "options": ["file()", "open()", "read()", "write()"],
            "answer": 2
        }
    ]

    score = 0
    print("================================")
    print("       Welcome to Quiz Game")
    print("================================")

    for i in range(len(questions)):
        q = questions[i]
        print(f"\nQ{i+1}. {q['question']}")
        for j in range(len(q["options"])):
            print(f"{j+1}. {q['options'][j]}")

        try:
            user_ans = int(input("Enter your answer (1-4): "))
            if user_ans == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Wrong!")
                print("Correct answer:", q["options"][q["answer"] - 1])
        except:
            print("Invalid input!")

    print("\n==============================")
    print(f"Your Final Score: {score}/{len(questions)}")
    print("==============================")

    if score == len(questions):
        print("Excellent!")
    elif score >= 3:
        print("Good Job!")
    else:
        print("Keep Practicing!")


# Run the game
quiz_game()
       
    
