#loop- a loop is a construct (special function)that repeats itself
# in programing . a loop allows to repeat code instructions 

# there are two types of loops for loop and while loop 

 
# while - loop - a  type of loop where so long condtion is equal 
# to true it will keep running forever 
  
# the keyword is while do while  
 
# syntax
num = 4 
while 2+2 == num: # condtion---> opertian - must be true 
    print("the program is running...")
    num=input() 
# while loop will ALWAYS run unless you change the condtinal! 
# we can do this by writing instructions to manually changer it. 
 
  
def guessinggame():
    correctanswer=12
    attempts=0 
    print ("GUESSING GAME HAS STARTED")
    userguess=int(input("please guess a number between 1 and 50") )

    while userguess != correctanswer:
        print (" incorecct. please try agian")
        attempts+=1
        print("guess attempts: "+ str(attempts))
        userguess = int(input(" please guess a number between 1 and 50")) 

        print (" congrats! you guess the right number!") 
         
guessinggame()
           
            
             

def Password():
    CorrectPassword = '1200'
    attemps = 4
    print('type your password...')
    userPassword = str(input('password...'))

    while userPassword != CorrectPassword
    print('wrong password..please try again')
    attemps -=1
    print('wrong attemps:' +str(attemps))
    userPassword = str(input('password...'))