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
def Victor() :
    print('Congs, You win :)' )
    input("")
#Quiz
def quiz() :
    print("welcome to the quiz")
    ask("what is 2+2","4" )
    ask("what is 4+4","8" )
    ask("what is 8+8","16" )
    ask("what is 16+16","32" )
    ask("waht is 32+32",'64')
    ask('what is 64+64', '128')
    ask('what is 128+128','256')
    Victor()
quiz()