from graphics import *

def generateGame():
    pass

def drawHangman(win,wrongAnswers):
    
    if wrongAnswers == 1:
        #Head
        head = Circle(Point(175,250),20)
        head.draw(win)
        
    if wrongAnswers == 2:
        #Body
        body = Line(Point(175,270), Point(175,350))
        body.draw(win)
        
    if wrongAnswers == 3:
        #Leg 1
        leg1 = Line(Point(175,350), Point(160,370))
        leg1.draw(win)
        
    if wrongAnswers == 4:
        #Leg 2
        leg2 = Line(Point(175,350), Point(190,370))
        leg2.draw(win)

    if wrongAnswers == 5:
        #Arm 1
        arm1 = Line(Point(175, 310), Point(150,290))
        arm1.draw(win)
        
    if wrongAnswers == 6:
        #Arm 2
        arm2 = Line(Point(175, 310), Point(200,290))
        arm2.draw(win)
    
def drawHang(win):
    hangBase =  Line(Point(75,400), Point(200,400))
    hangBase.draw(win)
    
    hangStick = Line(hangBase.getCenter(), Point(hangBase.getCenter().getX(),200))
    hangStick.draw(win)
    
    hangSupport = Line(Point(hangBase.getCenter().getX(),200), Point(175,200))
    hangSupport.draw(win)
    
    hangPoint = Line(Point(175,200), Point(175,230))
    hangPoint.draw(win)
    
#wordlines va a necesitar un counter despues para que varie la word_to_guess
def wordLines(words_to_guess, game_rounds, win):
    xi = 300
    x = 340
    for i in range(len(words_to_guess[game_rounds])): 
        letterLine = Line(Point(xi,250), Point(x,250))
        letterLine.draw(win)
        xi = xi + 60
        x = xi + 40

def writeLetterIn(letterIdx, guess, win):
    if letterIdx == 0:
        letter = Text(Point(320,238), guess)
        letter.setSize(25)
        letter.draw(win)
                
    elif letterIdx == 1:
        letter = Text(Point(380,238), guess)
        letter.setSize(25)
        letter.draw(win)
                
    elif letterIdx == 2:
        letter = Text(Point(440,238), guess)
        letter.setSize(25)
        letter.draw(win)
                
    elif letterIdx == 3:
        letter = Text(Point(500,238), guess)
        letter.setSize(25)
        letter.draw(win)
                
    elif letterIdx == 4:
        letter = Text(Point(560,238), guess)
        letter.setSize(25)
        letter.draw(win)
                
    elif letterIdx == 5:
        letter = Text(Point(620,238), guess)
        letter.setSize(25)
        letter.draw(win)
                
    elif letterIdx == 6:
        letter = Text(Point(680,238), guess)
        letter.setSize(25)
        letter.draw(win)

def checkKeyEntered(words_to_guess, game_rounds, guess):
    
    letter_is = False
    idx = 0
    
    for letterIdx in range(len(words_to_guess[game_rounds])):
        if guess == words_to_guess[game_rounds][letterIdx]:
            print(guess)
            print(letterIdx)
            idx = letterIdx
            letter_is = True
            
    return letter_is, idx

def wrongGuess(guess,wrongAnswers,win):
    
    if wrongAnswers == 1:
        message = Text(Point(355,370), "Wrong guess: ")
        message.setSize(16)
        message.setTextColor('black')
        message.draw(win)
        x = 410
    
    wrongLetter = Text(Point(x,370), guess)
    wrongLetter.setSize(16)
    wrongLetter.setTextColor('black')
    wrongLetter.draw(win)
    x += 5
        
def getAnswer(words_to_guess,game_rounds,win): #en un while mientras wrongAnswer != 6
    
    wrongAnswers = 0
    correctAnswers = 0
    
    while wrongAnswers != 6 or correctAnswers != len(words_to_guess[game_rounds]): 
        
        guess = win.getKey()
        print(guess)

        is_letter, idx = checkKeyEntered(words_to_guess, game_rounds, guess)
        
        message = Text(Point(500,300), "Press a letter key!")
        message.setSize(12)
        message.setTextColor('green')
        message.draw(win)

        if is_letter == True:
            correctAnswers += 1
            print('correctAnswers:',correctAnswers)
            message.setText('Congratulations! The letter entered is in the word to guess!')
            message.setTextColor('green')
            #message.draw(win)

            writeLetterIn(idx, guess, win)

        else:
            wrongAnswers += 1
            drawHangman(win,wrongAnswers)
            wrongGuess(guess,wrongAnswers,win)
            message.setText('Sorry! The letter entered is not the word to guess!')
            message.setTextColor('red')
            #message.draw(win)
                

def main():
    
    words_to_guess = ["python","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    game_rounds = 0
    
    keep_playing = True
    
    win = GraphWin('Hangman', 800, 600)    
    
    message = Text(Point(400,60), "HANGMAN!")
    message.setSize(35)
    message.setTextColor('Grey')
    message.setStyle('bold')
    message.draw(win)
    
    message = Text(Point(400,100), "Enter a key on your keyboard of the letter you think that is in the word")
    message.setSize(15)
    message.setTextColor('black')
    message.draw(win)
        
    
    wordLines(words_to_guess, game_rounds, win)

    drawHang(win)
        
    
    while game_rounds != 11 or keep_playing:
          
        getAnswer(words_to_guess,game_rounds,win)
     
        #game_rounds += 1
    
    
main()

if __name__ == "__main__":
    main()