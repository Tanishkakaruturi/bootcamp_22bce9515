import random
def Trivia_Quizbot(username):

    while True:
        start_game = input(f"Hello {username}! Do you want to start the quiz? (yes/no): ").lower()

        if start_game == 'yes':
            print("\nAnswer the following questions:\n")
            random.choice(question)

            user_score = 0 

            for question_data in question:
                print(question_data["question"])
                print_options(question_data["options"])

                user_answer = input("Your answer (enter the option number): ")

                if validate_answer(user_answer, question_data["correct_option"]):
                    print("Correct!\n")
                    user_score += 1
                    print(f"your current score is{user_score}")
                else:
                    correct_option = question_data['options'][question_data['correct_option']]
                    print(f"Wrong! The correct answer is {correct_option}\n")

            print(f"Your final score is: {user_score}\n")
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                break
        elif start_game == 'no':
            print("Maybe next time! Goodbye.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no.'")

def print_options(options):
    for i in range(len(options)):
        print(f"{i + 1}. {options[i]}")

def validate_answer(user_answer, correct_option):
    try:
        user_answer = int(user_answer)
        return user_answer == correct_option 
    except ValueError:
        return False

question = [ 
    {   "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_option": 2 },
    {  "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Venus", "Saturn"],
        "correct_option": 0 },
    {   "question": "What is the largest country in the world?",
        "options": ["Russia", "India", "USA", "Pakistan"],
        "correct_option": 0 },
    {   "question": "What is the name of a shape with nine sides?",
        "options": ["pentagon", "Octagon", "Hexagon", "Nonagon"],
        "correct_option": 3 },
    {   "question": "Which Shakespeare play features the character Hamlet?",
        "options": ["Romeo and Juliet", "Macbeth", "Othello", "Hamlet"],
        "correct_option": 3 },
    {   "question": "What is the capital of Australia?",
        "options": ["Canberra", "Sydney", "Melbourne", "Brisbane"],
        "correct_option": 0 },
    {   "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue whale", "Giraffe", "Dolphin"],
        "correct_option": 1 },
    {   "question": "In which year did the Titanic sink?",
        "options": ["1920", "1913", "1912", "1924"],
        "correct_option": 2 },
    {   "question": "What is the currency of Japan?",
        "options": ["Won", "Yon", "Yen", "Yuan"],
        "correct_option": 2 }
]

username = input("enter your name: ")
Trivia_Quizbot(username)
