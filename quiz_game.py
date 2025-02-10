
questions = [
    {
        "question" : "What is the Capetal of France? ",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "Answer" : "A"
    },
    {
        "question" : "Which language is primarily spoken in Brazil?",
        "options" : ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "Answer" : "B"
    },
    {
        "question" : "What is the smallest prime number?",
        "options" : ["A. 1", "B. 2", "C. 3", "D. 5"],
        "Answer" : "B"
    },
    {
        "question" : "Who wrote 'To Kill a Mockingbird'?",
        "options" : ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "Answer" : "A"
    }
]


def quiz():
    score = 0
    for item in questions:  
        print(item["question"])

        for option in item["options"]:
            print(option)
        
        user_answer = input("Enter your answer (A, B, C, D): ").upper().strip()

        if user_answer == item["Answer"]:
            score += 1
            print("Correct!","\n")
        else:
            print(f"Wrong! The correct answer was {item["Answer"]}","\n")
        
    print(f"You got {score} out of {len(questions)}")
quiz()
        
