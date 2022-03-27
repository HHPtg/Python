#restart 
def restart():
    resulta = input("wanna try again? y/n")
    if resulta == "y":
        print("ok")
        quiz()
        exit()
    else:
        print("Alright, goodbye")
        exit()
#Ask and answer 
def ask(question, answer):
  result = input(question)
  if result == answer:
      print("Well done")
  else:
    print("wrong")
    print("Sorry You failed to answer all questions correctly :(")
    restart()
#Victory Text
def Victor() :
    print('Congs, You succeeded in answering all questions correctly :)' )
    input("")
#question Input
question1 = input("please enter the first question you would like to ask: ")
answer1 = input('please enter the answer to the first question: ')
question2 = input("please enter the second question you would like to ask: ")
answer2 = input('please enter the answer to the second question: ')
question3 = input("please enter the Third question you would like to ask: ")
answer3 = input('please enter the answer to the third question: ')

#attempt at adding more questions according to the user // to be worked on
'''add = input("would u like to add another question yes/no")
if add == 'yes' :
    question //+1// = input("please enter the question you would like to ask") //add +1 to question and have it added to quiz()
    answer//+1// = input('please enter the answer to the question')// add +1 to answer and have it display after the coma in quiz()
else :
    quiz()'''

#Quiz
def quiz() :
    print("welcome to the quiz")
    ask(question1, answer1)
    ask(question2, answer2)
    ask(question3, answer3)
    Victor()
quiz()