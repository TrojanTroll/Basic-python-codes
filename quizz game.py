#----------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    
    for key in questions:
        print ("-----------------------------------------")
        print(key)
        for i in answers[question_num-1]:
            print (i)
        guess = input("Enter (A,B,C,D): ")
        guess = guess.upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
        
    display_score(correct_guesses, guesses)
    
        
#----------------------
def check_answer(answer,guess):
    
    if answer == guess:
        print ("Correct!")
        return 1
    else:
        print("WRONG!")
        return 0
#----------------------
def display_score(correct_guesses, guesses):
    print ("-----------------------------------------")
    print ("RESULTS")
    print ("-----------------------------------------")
    print ("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print ()
    
    print ("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print ()
    
    score = (correct_guesses/len(questions)*100)
    print ("Your score is: " + str(score)+"%")
    
#----------------------
def play_again():
    
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()
    
    if response == "YES":
        return True
    else:
        return False
        
#----------------------

questions = {
    "Who created Python?: " : "C",
    "What year was Python created?: ": "D",
    "Python is tributed to what comedy group?: ": "A",
    "Is Earth round?: ": "B"
}

answers = [["A. Elon Musk", "B. Armando", "C. Guido van Rossum", "D. Marky ZuckDeezNutz"],
           ["A. 2077", "B. 2000", "C. 2014", "D. 1991"],
           ["A. Monty Python", "B. Smosh", "C. CoolPals", "D. Kuya Jobert and friends"],
           ["A. False","B. True", "C. Sometimes", "D. Someday"]]

new_game()

while play_again():
    new_game()
    
print ("Thanks for playing!")
