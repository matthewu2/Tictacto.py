from tkinker import * 
from tkinker import messagebox

# Creating a function button for tic tac toe game
def ButtonClick(button):
    global x_o, flag
    button["bg"] = "#2ec4b6"
    if button["text"] == "" and x_o == True:
        button["text"] = "x"
        x_o = False
        CheckForWin()
        flag = flag+1
    elif button["text"] == "" and x_o == False:
        button["text"] = "o"
        x_o = True
        CheckForWin()
        flag = flag+1
    else:
        messagebox.showinfo("Matthew Tic Tac Toe", "player has already entered!")

"""
1 2 3
4 5 6
7 8 9
1 5 9
3 5 7
1 4 7
2 5 8
3 6 9
"""

# creating function to check for wins 
def CheckForWin():
    global button1,button2,button3,button4,button5,button6,button7,button8,button9
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        messagebox.showinfo("Jude Tic Tac Toe", "Player X has Won!!")
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        messagebox.showinfo("Jude Tic Tac Toe", "Player O has Won!!")
    elif flag ==8:
        messagebox.showinfo("Jude Tic Tac Toe","Game Tied!")

main = TK()
main.title("Matthew Tic Tac Toe")

# creating a global variable using to play my tic tac toe game
X_O = True
flag = 0

# creating buttons for tic tac toe game
button1 = Button(main,text="", font=("roboto",50,"bold"),bg="#9ab973",fg="white",width=3, command=lambda: ButtonClick(button1))
button1.grid(row=0,column=0)

button2 = Button(main,text="", font=("roboto",50,"bold"),bg="#9ab973",fg="white",width=3, command=lambda: ButtonClick(button2))
button2.grid(row=0,column=1)

button3 = Button(main,text="", font=("roboto",50,"bold"),bg="#9ab973",fg="white",width=3, command=lambda: ButtonClick(button3))
button3.grid(row=0,column=2)

button4 = Button(main,text="", font=("roboto",50,"bold"),bg="#9ab973",fg="white",width=3, command=lambda: ButtonClick(button4))
button4.grid(row=1,column=0)

button5 = Button(main,text="", font=("roboto",50,"bold"),bg="#9ab973",fg="white",width=3, command=lambda: ButtonClick(button5))
button5.grid(row=1,column=1)


button6 = Button(main,text="", font=("roboto",50,"bold"),bg="#9ab973",fg="white",width=3, command=lambda: ButtonClick(button6))
button6.grid(row=1,column=2)


button7 = Button(main,text="", font=("roboto",50,"bold"),bg="#9ab973",fg="white",width=3, command=lambda: ButtonClick(button7))
button7.grid(row=2,column=0)


button8 = Button(main,text="", font=("roboto",50,"bold"),bg="#9ab973",fg="white",width=3, command=lambda: ButtonClick(button8))
button8.grid(row=2,column=1)

button9 = Button(main,text="", font=("roboto",50,"bold"),bg="#9ab973",fg="white",width=3, command=lambda: ButtonClick(button9))
button9.grid(row=2,column=2)


main.mainloop()
