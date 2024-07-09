
import tkinter as tk
from tkinter import *
import time
from tkinter import ttk
#from tkinter.ttk import Label

def button_click(value):
    global current_input
    current = display.get()

    # Clear the display if the result is shown and a new calculation is started
    # if result_shown:
    #     clear_display()
    #     result_shown = False

    # Update the display based on the button clicked
    if current == '0' and value not in '+-*/':
        current_input = value
        display.set(current_input)
    else:
        current_input += value
        display.set(current_input)

        # Calculate result after the second digit is entered
        if len(current_input) == 2:
            window.after(2000, calculate)  # Schedule evaluation after 2 seconds

# Function to evaluate the expression and update the display
def calculate():
    try:
        result = str(eval(current_input))
        display.set(result)
        #result_shown = True
    except Exception as e:
        display.set("Error")
        #result_shown = True

        # Clear the result after 2 seconds
        window.after(2000, clear_display)

def clear_display():
    display.set("0")

def exit_calculator():
    window.destroy()

def op (x,c,z):

    if x == 'up' and c == 'center':
        c = 'center_up'
    elif x == 'down' and c == 'center':
        c = 'center_down'
    elif x == 'left' and c == 'center':
        c = 'center_left'
    elif x == 'right' and c == 'center':
        c = 'center_right'

    elif x == 'up' and c == 'center_up':
        z = '4'
    elif x == 'down' and c == 'center_up':
        z = '6'
    elif x == 'left' and c == 'center_up':
        z = '5'
    elif x == 'right' and c == 'center_up':
        z = '7'

    elif x == 'up' and c == 'center_down':
        z = '0'
    elif x == 'down' and c == 'center_down':
        z = '2'
    elif x == 'left' and c == 'center_down':
        z = '1'
    elif x == 'right' and c == 'center_down':
        z = '3'

    elif x == 'up' and c == 'center_left':
        z = '8'
    elif x == 'down' and c == 'center_left':
        z = 'E'
    elif x == 'left' and c == 'center_left':
        z = '9'
    elif x == 'right' and c == 'center_left':
        z = 'C'

    elif x == 'up' and c == 'center_right':
        z = '/'
    elif x == 'down' and c == 'center_right':
        z = '+'
    elif x == 'left' and c == 'center_right':
        z = '*'
    elif x == 'right' and c == 'center_right':
        z = '-'

    elif x == 'blinking' and z=='C':
        clear_display()
        c = 'center'
    elif x == 'blinking'and z=='E':
        exit_calculator()

    elif x == 'blinking' and z != 'E' and z != 'C':
        #button_click(z)
        c ='center'

    return c,z




# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.configure(bg='#607FA9')  # Set background color of the window

# StringVar to store and display the current input
display = tk.StringVar()
display.set("0")
current_input = ""
# Entry widget to display the input
entry = tk.Entry(window, textvariable=display, font=('Arial', 20), bd=10, insertwidth=10, width=25, justify='right')
entry.grid(row=0, column=1, columnspan=10)
entry.configure(bg='white')  # Set background color of the entry widget

# Define button labels and their positions
button_labels = [
    ('4', 1, 5), ('5', 2, 4), ('6', 3, 5), ('7', 2, 6),
    ('/', 4, 8), ('*', 5, 7), ('-', 5, 10),('+', 6, 8),
    ('1', 11, 4), ('2', 12, 5), ('3', 11, 6), ('0', 10, 5),
    ('9', 5, 1), ('8', 4, 2), ('C', 5, 3), ('E', 6, 2)
]
lbl1 = Label(window, text="Up", fg='black',
                     bg='white', font=('black', 30, 'bold'))
lbl1.place(x=448, y=135)

lbl2 = Label(window, text="Down", fg='black',
                     bg='white', font=('black', 25, 'bold'))
lbl2.place(x=430, y=570)

lbl3 = Label(window, text="Left", fg='black',
                     bg='white', font=('black', 25, 'bold'))
lbl3.place(x=127, y=356)

lbl4 = Label(window, text="Right", fg='black',
                     bg='white', font=('black', 25, 'bold'))
lbl4.place(x=750, y=356)

lbl5 = Label(window, text="Center", fg='black',
                     bg='white', font=('black', 25, 'bold'))
lbl5.place(x=425, y=356)


# Create buttons with respective commands
for (label, row, column) in button_labels:
    # if label == 'C':
    #     button = tk.Button(window, text=label, font=('Arial', 20), bd=10, width=5)
    # elif label == 'E':
    #     button = tk.Button(window, text=label, font=('Arial', 20), bd=10, width=5)

    button = tk.Button(window, text=label, font=('Arial', 20), bd=10, width=5)
    button.grid(row=row, column=column)

e = "_"
c = 'center'
z = '_'
#arr = {'up','up','blinking','right', 'right','blinking', 'down', 'left','blinking'}#, 'C','up', 'left', 'blinking','right', 'left','blinking', 'down', 'left','blinking'}
#while True:
#print (arr)

#data = ['up', 'up', 'blinking', 'right', 'right', 'blinking', 'down', 'left', 'blinking', 'left', 'right','blinking' ,'up', 'left', 'blinking','right', 'left','blinking', 'down', 'left','blinking', 'left', 'down','blinking']



import pickle
import sklearn
import pandas as pd

with open('C:\\Users\\dell\\Downloads\\rf_classifier_wavelet2.pkl', 'rb') as file:
    loaded_model = pickle.load(file)
X_test_W_data = pd.read_csv("C:\\Users\\dell\\Downloads\\X_test_W_5_rows.csv")
Y_pred = loaded_model.predict(X_test_W_data)
print (Y_pred)

result_list = []
j = " "
# Iterate over the original list
for item in Y_pred:
    if item == 0:
        j='blinking'
    elif item == 1:
        j='up'
    elif item == 2:
        j = 'down'
    elif item == 3:
        j = 'right'
    elif item == 4:
        j = 'left'

        # Append the item to the result list if it meets the condition
    result_list.append(j)
#result_list.append("blinking")
print(result_list)


for i in result_list:
    c, z = op(i, c, z)
    if(z == 'C'):
        clear_display()
        entry.update()
        window.after(1000)
    if (z == 'E'):
        clear_display()
        entry.update()
        window.after(1000)

    if i == 'blinking' and z != 'C'and z != 'E':
        button_click(z)
        entry.update()
        window.after(1000)





# Iterate over the list using a for loop
# blink=0
# up=1
# down=2
# right=3
# left=4

# # Define the original list
# original_list = [1, 2, 1, 1, 3, 2]
#
# # Initialize an empty list to store elements that meet the condition
# result_list = []
# j = " "
# # Iterate over the original list
# for item in original_list:
#     if item == 0:
#         j='blinking'
#     elif item == 1:
#         j='up'
#     elif item == 2:
#         j = 'down'
#     elif item == 3:
#         j = 'right'
#     elif item == 4:
#         j = 'left'
#
#         # Append the item to the result list if it meets the condition
#     result_list.append(j)


#result_list = ['up','down', 'up', 'up', 'right', 'down']










# i1 = 'up'
# c, z = op(i1, c, z)
# i2 = 'up'
# c, z = op(i2, c, z)
# i3 = 'blinking'
# c, z = op(i3, c, z)
# if i3 == 'blinking':
#     button_click(z)
#     entry.update()
#     window.after(1000)
#
# i4 = 'right'
# c, z = op(i4, c, z)
# i5 = 'right'
# c, z = op(i5, c, z)
# i6 = 'blinking'
# c, z = op(i6, c, z)
# if i6 == 'blinking':
#     button_click(z)
#     entry.update()
#     window.after(1000)
#
# i7 = 'down'
# c, z = op(i7, c, z)
# i8 = 'left'
# c, z = op(i8, c, z)
# i9 = 'blinking'
# c, z = op(i9, c, z)
# if i9 == 'blinking':
#     button_click(z)
#     entry.update()
#     window.after(1000)

window.mainloop()
























    # else:
    #     button = tk.Button(window, text=label, font=('Arial', 20), bd=10, width=5, command=lambda value=label: button_click(value))
    # button.grid(row=row, column=column)

#for i in range(1, 6):

# def button_click(value):
#     current = str(display.get())
#     if current == '0':
#         display.set(value)
#     else:
#         display.set(current + value)
#         # Calculate result when the second digit is entered after an operation
#         if current.endswith(('+', '-', '*', '/')):
#             calculate()
#
# # Function to perform calculation and update the display
# def calculate():
#     try:
#         result = str(eval(display.get()))
#         display.set(result)
#     except Exception as e:
#         display.set("Error")







