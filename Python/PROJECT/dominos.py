from tkinter import *
import tkinter.messagebox as tm

import random

def readfile():
        fob=open('manual.txt','r')
        print(fob.read())
        fob.close()
class tile:
    def __init__(self):
        self.lno=0
        self.rno=0
        self.vorh="h"
    def insertval(self,x,y):
        self.lno=x
        self.rno=y
        
    def disp(self):
        print("%d%d   " %(self.lno,self.rno))
    def chkdouble(self):
        if self.lno==self.rno:
            return 1
        #return right
    def retrt(self,x):
        if x==1:
            return self.rno
        else:
            return self.lno
def dominos():
        pl1=input("Player 1...Enter your name...")
        pl2=input("Player 2...Enter your name...")
        mark=[]
        for i in range(0,28):
            mark.append(0)
        tiles=[]
        for i in range(0,7):
            for j in range(i,7):
                temp=tile()
                temp.insertval(i,j)
                #list of objects
                tiles.append(temp)
#print(tiles)

        #coin flipping
        print(pl1,"or",pl2,"toss")
        print("Heads or Tails",pl1,"?")
        calltoss=input()
        randnum=random.randint(0,1)
        if randnum==0:
            if calltoss=='heads' or calltoss=='h':
                print(pl1,"plays first")
                calltoss=1
            else:
                print(pl2,"plays first")
                calltoss=2
        else:
            if calltoss=='tails' or calltoss=='t':
                print(pl1,"plays first")
                calltoss=1
            else:
                print(pl2,"plays first")
                calltoss=2

        #shuffling
        i=0
        P1tiles=[]
        P2tiles=[]
        i=0
        while i<7:
            first=random.randint(0,27)
            if tiles[first]!=0: 
                P1tiles.append(tiles[first])
        
                tiles[first]=0
                i+=1
        print(pl1,"tiles:")        
        for i in range(7):
            P1tiles[i].disp()
        #index start from 1
        i=0
        while i<7:
            first=random.randint(0,27)
            if tiles[first]!=0: 
                P2tiles.append(tiles[first])
        
                tiles[first]=0
                i+=1
        print(pl2,"tiles:")       
        for i in range(7):
            P2tiles[i].disp()

        #game starts    
        game=[]
        head=None
        tail=None
        double=0
        tileno=0
        if calltoss==1:
            for i in range(7):
                double=P1tiles[i].chkdouble()
                if double==1:
                    break
            i=0
            while(1):
                tileno=input("Enter the tile no.(starts from 0):")
                tileno=ord(tileno)-48
        
                chkdouin=P1tiles[tileno].chkdouble()
                if double==1 and chkdouin!=1:
                    print("Double exists-Reenter")
                else:
                    P1tiles[tileno].vorh='v'
                    game.append(P1tiles[tileno])
                    P1tiles[tileno]=0
                    break
        else:
            for i in range(7):
                double=P2tiles[i].chkdouble()
                if double==1:
                    break
            while(1):
                tileno=input("Enter the tile no.(starts from 0)")
                tileno=ord(tileno)-48
                chkdouin=P2tiles[tileno].chkdouble()
                if double==1 and chkdouin!=1:
                    print("Double exists-Reenter")
                else:
                    P2tiles[tileno].vorh='v'
                    game.append(P2tiles[tileno])
                    P2tiles[tileno]=0
                    break
        head=game[0]
        tail=game[0]
        turn=0
        ans=0
        lorr=0
        right=0
        left=0
        if calltoss==1:
            turn=2
        else:
            turn=1
        flag=0
        passcount=0
        passflag=0
        validpass=0
        finishflag=-1
        while(1):
            for i in game:
                i.disp()
            flag=0
            validpass=1
            finishflag=0
            if(turn==1):
                while(1):
                    print(pl1,"turn")
                    ans=input("1.Place a tile 2.Pass")
                    ans=ord(ans)-48
                    if ans==1:
                        for i in range(7):
                            if P1tiles[i]!=0:
                                print(i,end=" ")
                                print("--->",end=" ")
                                P1tiles[i].disp()
                        while(1):
                            ans=input("Enter the num of tile:")
                            ans=ord(ans)-48
                            if P1tiles[ans]!=0:
                                break
                            else:
                                print("Wrong tile number")

                        lorr=input("Enter the side to place the tile on the board -L or R")
                        temporary=0
                        if lorr=='R' or lorr=='r':
                            left=P1tiles[ans].retrt(0)
                            right=P1tiles[ans].retrt(1)
                            if(left==tail.retrt(1)):
                                game.append(P1tiles[ans])
                                tail=game[-1]
                                P1tiles[ans]=0
                                flag=1
                            
                            elif(right==tail.retrt(1)):
                                temporary=P1tiles[ans].lno
                                P1tiles[ans].lno=P1tiles[ans].rno
                                P1tiles[ans].rno=temporary
                                game.append(P1tiles[ans])
                                tail=game[-1]
                                P1tiles[ans]=0
                                flag=1
                            else:
                                  #print("Not possibe")
                                tm.showinfo("Message", "Not possible")
                                
                        else:
                            right=P1tiles[ans].retrt(1)
                            left=P1tiles[ans].retrt(0)
                            if(right==head.retrt(0)):
                                game.insert(0,P1tiles[ans])
                                head=game[0]
                                P1tiles[ans]=0
                                flag=1
                    
                            elif(left==head.retrt(0)):
                                temporary=P1tiles[ans].rno
                                P1tiles[ans].rno=P1tiles[ans].lno
                                P1tiles[ans].lno=temporary
                                game.insert(0,P1tiles[ans])
                                head=game[0]
                                P1tiles[ans]=0
                                flag=1
                            else:
                                #print("Not possible")
                                tm.showinfo("Message", "Not possible")
                                
                        if(flag==1):
                            passcount=0
                            for i in range(7):
                                if P1tiles[i]!=0:
                                    finishflag=1
                            turn=2
                            if(finishflag==0):
                                print(pl1,"Wins")
                            break
                        #passing
                    else:
                
                        for i in P1tiles:
                            if(i!=0):
                                if(head.retrt(0)==i.retrt(0) or head.retrt(0)==i.retrt(1)):
                                    validpass=0
                                    break
                                if(tail.retrt(1)==i.retrt(0) or tail.retrt(1)==i.retrt(1)):
                                    validpass=0
                                    break
                        if(validpass==1):
                            turn=2
                            
                            for i in range(7):
                                if P1tiles[i]!=0:
                                    finishflag=1
                            passcount+=1
                            if(passcount==2):
                                passflag=1
                            break
                        else:
                            print("Invalid Pass")
                            validpass=1
                
            
                if(passflag==1 or finishflag==0):
                    break
            else:
                finishflag=0
                while(1):
                    flag=0
                    print(pl2,"turn")
                    ans=input("1.Place a tile 2.Pass")
                    ans=ord(ans)-48
                    if ans==1:
                        for i in range(7):
                            if P2tiles[i]!=0:
                                print(i,end=" ")
                                print("--->",end=" ")
                                P2tiles[i].disp()
                        while(1):
                            ans=input("Enter the num of tile:")
                            ans=ord(ans)-48
                            if P2tiles[ans]!=0:
                                break
                            else:
                                print("Wrong tile number")
        
                        lorr=input("Enter the place to place the disk in the board -L or R")
                        if lorr=='R' or lorr=='r':
                            left=P2tiles[ans].retrt(0)
                            right=P2tiles[ans].retrt(1)
                            if(left==tail.retrt(1)):
                                game.append(P2tiles[ans])
                                tail=game[-1]
                                P2tiles[ans]=0
                                flag=1
                    
                            elif(right==tail.retrt(1)):
                                temporary=P2tiles[ans].lno
                                P2tiles[ans].lno=P2tiles[ans].rno
                                P2tiles[ans].rno=temporary
                                game.append(P2tiles[ans])
                                tail=game[-1]
                                P2tiles[ans]=0
                                flag=1
                            else:
                                #print("Not possibe")
                                tm.showinfo("Message", "Not possible")

                    
                        else:
                            right=P2tiles[ans].retrt(1)
                            left=P2tiles[ans].retrt(0)
                                
                            if(right==head.retrt(0)):
                                game.insert(0,P2tiles[ans])
                                head=game[0]
                                P2tiles[ans]=0
                                flag=1
                    
                            elif(left==head.retrt(0)):
                                temporary=P2tiles[ans].rno
                                P2tiles[ans].rno=P2tiles[ans].lno
                                P2tiles[ans].lno=temporary
                                game.insert(0,P2tiles[ans])
                                head=game[0]
                                P2tiles[ans]=0
                                flag=1
                            else:       
                                #print("Not possible")
                                tm.showinfo("Message", "Not possible")

                                print(left,right)
                        if(flag==1):
                            passcount=0
                            for i in range(7):
                                if P2tiles[i]!=0:
                                    finishflag=1
                    
                            turn=1
                            if(finishflag==0):
                                print(pl2,"wins")
                            break
                
                    else:
                        for i in P2tiles:
                            if(i!=0):
                                if(head.retrt(0)==i.retrt(0) or head.retrt(0)==i.retrt(1)):
                                    validpass=0
                                    break
                                if(tail.retrt(1)==i.retrt(0) or tail.retrt(1)==i.retrt(1)):
                                    validpass=0
                                    break
                        if(validpass==1):
                            turn=1
                            
                            for i in range(7):
                                if P2tiles[i]!=0:
                                    finishflag=1
                            passcount+=1
                            if(passcount==2):
                                passflag=1
                            break
                        else:
                            print("Invalid Pass")
                            validpass=1
            
                if(passflag==1 or finishflag==-1):
                    break
        if(passflag==1):
            sum2=0
            sum1=0
            fob=open('hof.txt','a')
            a=None
            for i in range(7):
                if P1tiles[i]!=0:
                    sum1+=P1tiles[i].lno+P1tiles[i].rno
            for i in range(7):
                if P2tiles[i]!=0:
                    sum2+=P2tiles[i].lno+P2tiles[i].rno
            dummy=0
            if(sum2>sum1):
                print(pl1,"wins")
                dummy=sum2-sum1
                a=pl1+" "+str(dummy)+"\n"
                fob.write(a)
            elif sum1>sum2:
                print(pl2,"wins")
                dummy=sum2-sum1
                a=pl2+" "+str(dummy)+"\n"
                fob.write(a)

            else:
                print('tie')
                small1=36
                small2=36.
                for i in range(7):
                        if P1tiles[i]!=0:
                                sumt1=P1tiles[i].lno+P1tiles[i].rno
                                if sumt1<small1:
                                        small1=sumt1
                for i in range(7):
                        if P2tiles[i]!=0:
                                sumt2=P2tiles[i].lno+P2tiles[i].rno
                                if sumt2<small2:
                                        small2=sumt2
                if(small1<small2):
                        print(p1,"wins")
                        dummy=small2-small1
                        a=pl1+" "+str(dummy)+"\n"
                        fob.write(a)
                else:
                        print(p2,"wins")
                        dummy=small2-small1
                        a=pl1+" "+str(dummy)+"\n"
                        fob.write(a)
            fob.close()    
            file1=open('hof.txt','r')
            data=file1.read()
            print(data)
            file1.close()
            sys.exit()


class SplashScreen(Frame):
    def __init__(self, master=None, width=1.0, height=1.0, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws*width) or width
        h = (useFactor and ws*height) or height
        # calculate position x, y
        x = (ws/2) - (w/2) 
        y = (hs/2) - (h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        self.master.overrideredirect(True)
        self.lift()

if __name__ == '__main__':
    root = Tk()

    sp = SplashScreen(root)
    sp.config(bg="#3366ff")

    m = Label(sp, text="DOMINOS GAME")
    
    
    m.pack(side=TOP, expand=YES)
    m.config(bg="#3366ff", justify=CENTER, font=("calibri", 29))

    root.after(5000, root.destroy)
    root.mainloop()
    
class MyApp:
	def __init__(self, parent):
		
		#------ constants for controlling layout ------
		button_width = 10    
		
		button_padx = "2m"
		button_pady = "1m"

		buttons_frame_padx =  "3m"   
		buttons_frame_pady =  "2m"   		
		buttons_frame_ipadx = "3m"   
		buttons_frame_ipady = "1m"   
		# -------------- end constants ----------------
		
		self.myParent = parent   
		self.buttons_frame = Frame(parent)
		
		self.buttons_frame.pack(   
			ipadx=buttons_frame_ipadx,  
			ipady=buttons_frame_ipady,  
			padx=buttons_frame_padx,    
			pady=buttons_frame_pady,    
			)    
		
	
		self.button1 = Button(self.buttons_frame, command=dominos)
		self.button1.configure(text="New Game", background= "cyan")
		self.button1.focus_force()       
		self.button1.configure( 
			width=button_width,  
			padx=button_padx,     
			pady=button_pady     
			)

		self.button1.pack(side=LEFT)	
		self.button1.bind("<Return>", self.button1Click_a)  
		
		self.button2 = Button(self.buttons_frame, command=readfile)
		self.button2.configure(text="Manual", background="red")  
		self.button2.configure( 
			width=button_width,  
			padx=button_padx,     
			pady=button_pady     
			)
	
		self.button2.pack(side=RIGHT)
		self.button2.bind("<Return>", self.button2Click_a)
 
		
	def button1Click(self):      
		if self.button1["background"] == "green":  
			self.button1["background"] = "yellow"
		else:
			self.button1["background"] = "green"
	
	def button2Click(self):
		self.myParent.destroy()     
		
	def button1Click_a(self, event):  
		self.button1Click()
				
	def button2Click_a(self, event): 
		self.button2Click()
  
	pass


root = Tk()
myapp = MyApp(root)
root.mainloop()

