def restart():
    resulta = input("wanna try again? y/n")
    if resulta == "y":
        print("ok")
        quiz()
        exit()
    else:
        print("Alright, goodbye")
        exit()
#def 
def ask(question, answer):
  result = input(question)
  if result == answer:
      print("ok")
  else:
    print("wrong")
    print("Sorry You lose :(")
    restart()

#Quiz
def quiz() :
    print("welcome to the quiz")
    ask("what is 2+2","4" )
    ask("what is 4+4","8" )
    ask("what is 8+8","16" )
    ask("what is 16+16","32" )
quiz()