import random
import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
def gold():
# Download gold prices data from Yahoo Finance
   gold_prices = yf.download('GC=F', start='2020-01-01', end='2023-04-19')
   print()
# Plot gold prices in a graph
   plt.plot(gold_prices['Close'])
   plt.title('Gold Prices')
   plt.xlabel('Date')
   plt.ylabel('Price (USD)')
   plt.show()

# Define some possible user inputs
greetings = ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon']
thanks = ['thanks', 'thank you', 'appreciate it']
options = ['balance', 'transfer', 'pay', 'statement']
bank=['Accounts','Types of Bank Account']



# Define some responses
greeting_responses = ['Hello!', 'Hi there!', 'Greetings!', 'Nice to meet you.']
thanks_responses = ['You\'re welcome!', 'No problem.', 'Glad to help.']
options_responses = ['You can check your balance, transfer funds, pay bills, or get a statement.']
stocks_response=["Click on Gold Price Button"]
bank_account=["Saving account \n Current Account \n Joint Account ,\n Fixed Deposit Acoount"]


# Define a function to handle user input
def chatbot():
    user_input = entry.get().lower()
    if user_input in greetings:
        response = random.choice(greeting_responses)
    elif user_input in thanks:
        response = random.choice(thanks_responses)
    elif any(option in user_input for option in options):
        response = random.choice(options_responses)
    elif user_input in bank:
        response=random.choice(bank_account)
         
    else:
        response = 'Sorry, I didn\'t understand that.'
    label.config(text=label.cget("text") + "\n" + response)

# Create the GUI
root = tk.Tk()
root.title('Bank Chatbot')

# Add a label for the chatbot responses
label = tk.Label(root, text='How can I help you today?')
label.pack(pady=10)

# Add a scrollable frame for the chatbot responses
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

# canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

chatbot_responses = tk.Frame(canvas)
canvas.create_window((0,0), window=chatbot_responses, anchor='nw')

# Add an entry box for user input
entry = tk.Entry(root)
entry.pack(pady=10)

# Add a button to submit user input
button = tk.Button(root, text='Submit', command=chatbot)
button1=tk.Button(root,text='Gold Price',command=gold).pack(padx=5)
button.pack(pady=10)

root.mainloop()

