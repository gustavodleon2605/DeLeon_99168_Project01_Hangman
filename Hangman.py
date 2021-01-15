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
def wordLines(words_to_guess, win):
    xi = 300
    x = 340
    for i in range(len(words_to_guess[4])): 
        letterLine = Line(Point(xi,250), Point(x,250))
        letterLine.draw(win)
        xi = xi + 60
        x = xi + 40
        
def main():
    
    words_to_guess = ["python","border","image","film","promise","kids","lungs","doll","rhyme","damage","plants"]
    letters = ["J","k"]
    win = GraphWin('Hangman', 800, 600)    
    
    
    #for i in range(11):
     #   word = words_to_guess[i]
      #  print(len(word))
    
    key = win.getKey()
    print(key)
    
    for i in range(len(words_to_guess[0])):
        if key == words_to_guess[0][i]:
                   print(key)
    
    
    message = Text(Point(400,100), "HANGMAN!")
    message.setSize(35)
    message.setTextColor('Grey')
    message.setStyle('bold')
    message.draw(win)
    
    letter1 = Text(Point(320,238), letters[0])
    letter1.setSize(25)
    letter1.draw(win)
    
    letter2 = Text(Point(380,238), "Y")
    letter2.setSize(25)
    letter2.draw(win)

    
    
    wordLines(words_to_guess, win)
    
    drawHang(win)
    
    drawHangman(win)
    
    
main()

if __name__ == "__main__":
    pass