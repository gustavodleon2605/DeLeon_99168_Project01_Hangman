from graphics import *
from button import Button

class Hangman:

    """ Methods for running the 
    Hangman game."""

    def __init__(self,win,game_rounds,words_to_guess):
        self.win = win
        self.game_rounds = game_rounds
        self.words_to_guess = words_to_guess
    
    def generateGame(self,win,game_rounds,words_to_guess):
        message = Text(Point(400,60), "HANGMAN")
        message.setSize(35)
        message.setTextColor('black')
        message.setStyle('bold')
        message.draw(win)

        message = Text(Point(405,100), "Enter a key on your keyboard of the letter you think that is in the word")
        message.setSize(15)
        message.setTextColor('black')
        message.draw(win)

        message = Text(Point(405,120), "You'll have until the hangman is completely drawn (6 chances)")
        message.setSize(15)
        message.setTextColor('black')
        message.draw(win)
            
        message = Text(Point(405,160), 'Round: ')
        message.setSize(20)
        message.setStyle('bold')
        message.setTextColor('black')
        message.draw(win)
            
        message = Text(Point(450,160), str(game_rounds+1))
        message.setSize(20)
        message.setStyle('bold')
        message.setTextColor('black')
        message.draw(win)

        message = Text(Point(410,320), "Click anywhere on the screen to start round!")
        message.setSize(20)
        message.setStyle('bold')
        message.setTextColor('black')
        message.draw(win)

        nextRoundButton = Button(win, Point(400,500), 70,40,"Next Round")

        quitButton = Button(win, Point(550,500), 70,40,"Quit")
        quitButton.activate()
        
        pt = win.getMouse()

        message.undraw()

        if (not quitButton.clicked(pt)):
            self.wordLines(words_to_guess, game_rounds, win)
            self.drawHang(win)
            self.getAnswer(words_to_guess,game_rounds,win)

        else:
            win.close()
            
        nextRoundButton.activate()

    def clear(self, win):
        for item in win.items[:]:
            item.undraw()
        win.update()
    
    def drawHangman(self,win,wrongAnswers):
        
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
            
            #Xeyes
            xeyel1 = Line(Point(165,243), Point(172,250))
            xeyel1.draw(win)
            
            xeyel2 = Line(Point(165,250), Point(172,243))
            xeyel2.draw(win)
            
            xeyel3 = Line(Point(180, 243), Point(187,250))
            xeyel3.draw(win)
            
            xeyel4 = Line(Point(180, 250), Point(187,243))
            xeyel4.draw(win)

    def drawHang(self, win):
        hangBase =  Line(Point(75,400), Point(200,400))
        hangBase.draw(win)
        
        hangStick = Line(hangBase.getCenter(), Point(hangBase.getCenter().getX(),200))
        hangStick.draw(win)
        
        hangSupport = Line(Point(hangBase.getCenter().getX(),200), Point(175,200))
        hangSupport.draw(win)
        
        hangPoint = Line(Point(175,200), Point(175,230))
        hangPoint.draw(win)
        
    def wordLines(self, words_to_guess, game_rounds, win):
        xi = 300
        x = 340

        for i in range(len(words_to_guess[game_rounds])): 
            letterLine = Line(Point(xi,250), Point(x,250))
            letterLine.draw(win)
            xi = xi + 60
            x = xi + 40

    def writeLetterIn(self, letterIdx, guess, win):
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

    def checkKeyEntered(self, words_to_guess, game_rounds, guess):
        letter_is = False
        idx = 0

        for letterIdx in range(len(words_to_guess[game_rounds])):
            if guess == words_to_guess[game_rounds][letterIdx]:
                idx = letterIdx
                letter_is = True
                
        return letter_is, idx

    def wrongGuess(self, guess,wrongAnswers,win):
        x = 400
        i = 0
        
        if wrongAnswers == 1:
            message = Text(Point(355,300), "Wrong guess: ")
            message.setSize(16)
            message.setTextColor('black')
            message.draw(win)
        
        while i < wrongAnswers:
            x += 15
            i += 1
        
        wrongLetter = Text(Point(x,300), guess)
        wrongLetter.setSize(16)
        wrongLetter.setTextColor('black')
        wrongLetter.draw(win)
        coma = Text(Point(x+7,300), ",")
        coma.draw(win)
            
    def getAnswer(self, words_to_guess,game_rounds,win):
        wrongAnswers = 0
        correctAnswers = 0
            
        while wrongAnswers != 6 and correctAnswers != len(words_to_guess[game_rounds]): 

            guess = win.getKey()
            
            is_letter, idx = self.checkKeyEntered(words_to_guess, game_rounds, guess)
                
            if is_letter == True:
                correctAnswers += 1
                self.writeLetterIn(idx, guess, win)

            else:
                wrongAnswers += 1
                self.drawHangman(win,wrongAnswers)
                self.wrongGuess(guess,wrongAnswers,win)
                    
        if correctAnswers ==  len(words_to_guess[game_rounds]):
            winmsg = Text(Point(465,385),'Congratulations! You guessed the word!')
            winmsg.setTextColor('green')
            winmsg.setSize(20)
            winmsg.draw(win)
        
        elif wrongAnswers == 6:
            losemsg = Text(Point(465,385),"Sorry!, you didn't guessed the word!")
            losemsg.setTextColor('red')
            losemsg.setSize(20)
            losemsg.draw(win)


def main():
    
    words_to_guess = ["python","image","film","promise","kids","lungs","rhyme","plants"]
    game_rounds = 0
    keep_playing = True
    
    win = GraphWin('Hangman Game', 800, 600)

    nextRoundButton = Button(win, Point(400,500), 70,40,"Next Round")

    while game_rounds != 8 and keep_playing:

        inputHangman = Hangman(win,game_rounds,words_to_guess)
        inputHangman.generateGame(win,game_rounds,words_to_guess)

        nextRoundButton.activate()
        pt = win.getMouse()

        if (nextRoundButton.clicked(pt)):
            game_rounds += 1
            inputHangman.clear(win)
        else:
            keep_playing = False
            win.close()
            
    win.close()


if __name__ == "__main__":
    main()