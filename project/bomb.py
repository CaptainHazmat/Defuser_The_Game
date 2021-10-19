from tkinter import *
from tkinter import messagebox
import pygame

wndw = Tk()
wndw.title('Bomb')
wndw.resizable(width = False, height = False)
pygame.mixer.init()

def btn_d(number):
    current = inputer.get()
    inputer.delete(0, END)
    inputer.insert(0,str(current) + str(number))
    print('number button was clicked')

def btn_entr():
    inputer.get()
    password = inputer.get()
    inputer.delete(0, END)
    if password == '7355608':
        pygame.mixer.music.load("df.mp3")
        pygame.mixer.music.play(loops=0)
        messagebox.showinfo('END', 'YOU WON') 
        wndw.quit()
    else:
        messagebox.showinfo('ERROR', 'WRONG PASSWORD') 
    print('enter button was clicked')

    
def started(): 
    pygame.mixer.music.load("pl.mp3")
    pygame.mixer.music.play() 
    messagebox.showinfo('The Sapper', 'Welcome to "Sapper the Game", your job is defusing the bomb, you have only 30 seconds before it explodes') 
    
def timer():
    pygame.mixer.music.load("ex.mp3")
    pygame.mixer.music.play()
    messagebox.showinfo('GAME OVER','BOMB EXPLODED')
    wndw.quit()

t = 30

def countdown():
    global t, wndw
    wndw.title(str(t))
    if t == 8:
        pygame.mixer.music.load("gt.mp3")
        pygame.mixer.music.play()
    if t==0: wndw.destroy()
    t-=1
    wndw.after(1000, countdown)
    

inputer = Entry(wndw, width = 25, borderwidth = 5, bg = 'DarkGreen')
inputer.grid(column=0, row=0, columnspan = 3, padx = 10, pady = 10)

lbl = Label(text = 'PASSWORD:')
lbl2 = Label(text = '7355608')
lbl.grid(column=4, row=2)
lbl2.grid(column=4, row=3)
lbl.after(31000, timer)

butt = Button(wndw, text = '1', bg = 'grey', padx = 30, pady = 10, command = lambda: btn_d(1))
butt2 = Button(wndw, text = '2', bg = 'grey', padx = 30, pady = 10, command = lambda: btn_d(2))
butt3 = Button(wndw, text = '3', bg = 'grey', padx = 30, pady = 10, command = lambda: btn_d(3))

butt4 = Button(wndw, text = '4', bg = 'grey', padx = 30, pady = 10, command = lambda: btn_d(4))
butt5 = Button(wndw, text = '5', bg = 'grey', padx = 30, pady = 10, command = lambda: btn_d(5))
butt6 = Button(wndw, text = '6', bg = 'grey', padx = 30, pady = 10, command = lambda: btn_d(6))

butt7 = Button(wndw, text = '7', bg = 'grey', padx = 30, pady = 10, command = lambda: btn_d(7))
butt8 = Button(wndw, text = '8', bg = 'grey', padx = 30, pady = 10, command = lambda: btn_d(8))
butt9 = Button(wndw, text = '9', bg = 'grey', padx = 30, pady = 10, command = lambda: btn_d(9))

butt0 = Button(wndw, text = '0', bg = 'grey', padx = 30, pady = 10, command = lambda: btn_d(0))
butt_entr = Button(wndw, text = 'ENT', bg = 'grey', padx = 22, pady = 10, command = btn_entr)

butt.grid(column=0, row=1)
butt2.grid(column=1, row=1)
butt3.grid(column=2, row=1)
butt4.grid(column=0, row=2)
butt5.grid(column=1, row=2)
butt6.grid(column=2, row=2)
butt7.grid(column=0, row=3)
butt8.grid(column=1, row=3)
butt9.grid(column=2, row=3)
butt0.grid(column=1, row=4)
butt_entr.grid(column=2, row=4)

started()
countdown()
wndw.mainloop()
