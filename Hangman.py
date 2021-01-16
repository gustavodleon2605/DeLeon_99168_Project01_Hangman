from graphics import *

def generateGame():
    pass

def drawHangman(win):
    #Head
    head = Circle(Point(175,250),20)
    head.draw(win)
    
    #Body
    body = Line(Point(175,270), Point(175,350))
    body.draw(win)
    
    #Legs
    leg1 = Line(Point(175,350), Point(160,370))
    leg1.draw(win)
    
    leg2 = Line(Point(175,350), Point(190,370))
    leg2.draw(win)
    
    #Arms
    arm1 = Line(body.getCenter(), Point(150,290))
    arm1.draw(win)
    
    arm2 = Line(body.getCenter(), Point(200,290))
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
        
def main():
    
    words_to_guess = ["python","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    game_rounds = 0
    keep_playing = True
    
    letters = ["J","k"]
    win = GraphWin('Hangman', 800, 600)    
    
    
    #for i in range(11):
     #   word = words_to_guess[i]
      #  print(len(word))
    
    while game_rounds != 11 or keep_playing:
        
        message = Text(Point(400,100), "Enter a key on your keyboard of the letter you think that is in the word")
        message.setSize(15)
        message.setTextColor('black')
        message.draw(win)
        
        guess = win.getKey()
        print(guess)

        #hacer el check en una funcnion y que entonces devuelva true or false para entonces
        #si es falso que pueda añadir al count de las falsas y sino pues que haga lo de true
        
        for letterIdx in range(len(words_to_guess[game_rounds])):
            if guess == words_to_guess[game_rounds][letterIdx]:
                message = Text(Point(500,300), "Congratulations! The letter entered is in the word to guess!")
                message.setSize(12)
                message.setTextColor('green')
                message.draw(win)
                print(guess)
                print(letterIdx)
                idx = letterIdx
                
        
        
        writeLetterIn(idx, guess, win)
            #else:
             #   message = Text(Point(500,300), "Sorry! The letter entered is not the word to guess!")
              #  message.setSize(12)
               # message.setTextColor('red')
                #message.draw(win)

        message = Text(Point(400,50), "HANGMAN!")
        message.setSize(35)
        message.setTextColor('Grey')
        message.setStyle('bold')
        message.draw(win)


        wordLines(words_to_guess, game_rounds, win)

        drawHang(win)

        drawHangman(win)
        
        #game_rounds += 1
    
    
main()

if __name__ == "__main__":
    main()