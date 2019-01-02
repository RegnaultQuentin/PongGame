import tkinter 
from tkinter import *

class Jeu(Frame):
    #Toutes mes variables
    ballX=50
    ballY=50
    player1X = 2
    player1Y = 2
    player2X = 0
    player2Y = 2
    ballDX = 2
    ballDY = -2
    paddleSpeed = 15
    player1Points = 0
    player2Points = 0
    
    def __init__(self, main):
        Frame.__init__(self, main)   
        self.main = main        
        self.initUI()
    #Mouvement raquette
    def key(self, event):
        print ("pressed"), repr(event.char)
        if event.char == 'z':
            if self.canvas.coords(self.player1)[1]>=0:
                self.canvas.move(self.player1,0,-self.paddleSpeed)
        if event.char == 's':
            if self.canvas.coords(self.player1)[3]<=self.winHEIGHT:
                self.canvas.move(self.player1,0,self.paddleSpeed)
        if event.char == 'o':
            if self.canvas.coords(self.player2)[1]>=0:
                self.canvas.move(self.player2,0,-self.paddleSpeed)
        if event.char == 'l':
            if self.canvas.coords(self.player2)[3]<=self.winHEIGHT:
                self.canvas.move(self.player2,0,self.paddleSpeed)
        if event.char == 'q':
            self.main.destroy()


    def callback(self, event):
        self.focus_set()
        print ("clicked at"), event.x, event.y
    '''
    Test avec la sourie
    def motion(self, event):
        coords1 = self.canvas.coords(self.player1)
        height1 = coords1[3]-coords1[1]
        coords1[1] = event.y
        coords1[3] = event.y+height1
        self.canvas.coords(self.player1,coords1[0],coords1[1],coords1[2],coords1[3])
    '''       
    def initUI(self):
        #Initialisation des joueurs et de la balle 
        self.player2X = self.main.winfo_screenwidth() - 15
        self.main.title("Pong")        
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, bg = 'White')
        self.canvas.pack(fill=BOTH, expand=1)
        self.winHEIGHT = self.main.winfo_screenheight()
        self.winWIDTH = self.main.winfo_screenwidth()
        self.ball = self.canvas.create_oval(self.ballX, self.ballY, 20+self.ballX, 20+self.ballY, fill="red", width=1)
        #Taille des raquettes
        self.player1 = self.canvas.create_rectangle(self.player1X, self.player1Y, 10+self.player1X, 100+self.player1Y, fill="Blue")
        self.player2 = self.canvas.create_rectangle(self.player2X, self.player2Y, 10+self.player2X, 100+self.player2Y, fill="Blue")
        self.textLabel = self.canvas.create_text(self.winWIDTH/2,10, text=str(self.player1Points)+" | "+str(self.player2Points))
        self.main.bind("<Key>", self.key)
        self.main.bind("<Button-1>", self.callback)
        self.canvas.pack(fill=BOTH, expand=1)
        self.after(200, self.goal)
        #self.main.bind("<Motion>", self.motion)

    #Collisition
    def collide(self, coords1, coords2):
        height1 = coords1[3]-coords1[1]
        width1 = coords1[2]-coords1[0]
        height2 = coords2[3]-coords2[1]
        width2 = coords2[2]-coords2[0]
        return not (coords1[0] + width1 < coords2[0] or coords1[1] + height1 < coords2[1] or coords1[0] > coords2[0] + width2 or coords1[1] > coords2[1] + height2)
        
    #Detection des raquettes, zone de but et comptages des points
    def goal(self):
        self.canvas.move(self.ball,self.ballDX, self.ballDY)
        if self.canvas.coords(self.ball)[1] <= 0:
            self.ballDY = -self.ballDY
        if self.canvas.coords(self.ball)[3] >= self.winHEIGHT:
            self.ballDY = -self.ballDY
        if self.collide(self.canvas.coords(self.ball),self.canvas.coords(self.player1)) or self.collide(self.canvas.coords(self.ball),self.canvas.coords(self.player2)):
            self.ballDX = -self.ballDX
        if self.canvas.coords(self.ball)[0] <= 0:
            self.ballDX = -self.ballDX
            self.player2Points+=1
            self.canvas.delete(self.textLabel)
            self.textLabel = self.canvas.create_text(self.winWIDTH/2,10, text=str(self.player1Points)+" | "+str(self.player2Points))
            self.canvas.coords(self.ball,self.winWIDTH/2,self.winHEIGHT/2,self.winWIDTH/2+10,self.winHEIGHT/2+10)
        if self.canvas.coords(self.ball)[2] >= self.winWIDTH:
            self.ballDX = -self.ballDX
            self.player1Points+=1
            self.canvas.delete(self.textLabel)
            self.textLabel = self.canvas.create_text(self.winWIDTH/2,10, text=str(self.player1Points)+" | "+str(self.player2Points))
            self.canvas.coords(self.ball,self.winWIDTH/2,self.winHEIGHT/2,self.winWIDTH/2+10,self.winHEIGHT/2+10)
        self.after(10, self.goal)

#Fonction principal
def main():
    canvas = tkinter.Tk()
    Jeu(canvas)
    canvas.overrideredirect(True)
    canvas.geometry("{0}x{1}+0+0".format(canvas.winfo_screenwidth(), canvas.winfo_screenheight()))
    canvas.mainloop()  

if __name__ == '__main__':
    main() 