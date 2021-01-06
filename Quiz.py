def start ():
    print("Welcome to the quiz")
    print("Best of Luck :) PS: you only have one life :)")

#def sorry
def sorry() :
    print("Sorry You lose :(")
    restart()
#def restart
def restart():
    resulta = input("wanna try again? y/n" )
    if resulta == "y":
        print("ok")
    else:
        print("Alright, goodbye")

#def 
def ask(question, answer):
  result = input("")
  if result == answer:
      print("ok")
  else:
    print("wrong")
    sorry()

#Quiz
def quiz() :
start()
print('what is 2+2?' )
ask("what is 2+2","4" )
print('what is 4+4?' )
ask("what is 4+4","8" )


