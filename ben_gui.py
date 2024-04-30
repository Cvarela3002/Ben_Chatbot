#ben_gui.py
import tkinter as tk
from tkinter import scrolledtext
from ben import get_events_on_date, extract_date
from train_chatbot import response

# Create main window
root = tk.Tk()
root.title("MyBen")
root.configure(bg='#B7DFFA')  # Set background color to baby blue

# Create chat display
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25, bg='#FFFFFF', fg='#000000', padx=10, pady=10)
chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Function to handle sending messages
def send_message(event=None):
    user_input = entry.get().strip()  # Get user input from entry field and remove leading/trailing whitespaces
    if not user_input:
        chat_display.insert(tk.END, "Ben: How can I help you today?\n")
    else:
        chat_display.insert(tk.END, "You: " + user_input + "\n")
        date = extract_date(user_input)
        if date:
            events = get_events_on_date(date)
            if events:
                chat_display.insert(tk.END, "Ben: Here are the events happening on " + date + ":\n")
                for event in events:
                    chat_display.insert(tk.END, "- " + event + "\n")
            else:
                chat_display.insert(tk.END, "Ben: There are no events happening on " + date + "\n")
        elif "graduation" in user_input.lower():
            chat_display.insert(tk.END, "Ben: Graduation is on May 18, 2024.\n")
        elif "class" in user_input.lower() and ("end" in user_input.lower() or "finish" in user_input.lower()):
            chat_display.insert(tk.END, "Ben: Classes end on May 08, 2024.\n")
        elif "registration" in user_input.lower() and ("summer" in user_input.lower() or "fall" in user_input.lower()):
            chat_display.insert(tk.END, "Ben: Summer and fall registration begins on April 1, 2024.\n")
        elif "withdrawal" in user_input.lower() and ("deadline" in user_input.lower()):
            chat_display.insert(tk.END, "Ben: The withdrawal deadline for 7-week courses is April 19, 2024, and for 14-week courses is April 2, 2024.\n")
        else:
            # If no rule-based response is found, use the trained model
            chat_response = response(user_input)
            chat_display.insert(tk.END, "Ben: " + chat_response + "\n")
    entry.delete(0, tk.END)
    chat_display.see(tk.END)
# Create entry field for user input
entry = tk.Entry(root, width=40)
entry.grid(row=1, column=0, padx=10, pady=10)
entry.bind("<Return>", send_message)  # Bind Enter key to send_message function

# Create send button
send_button = tk.Button(root, text="Send", command=send_message, bg='#5BC0EB', fg='#5C5858', padx=10, pady=5)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Greet the user
send_message()

# Run the main event loop
root.mainloop()
