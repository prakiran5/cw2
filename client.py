import tkinter as tk
import socket
import threading

def send_message():
    message = user_input.get()
    chat_output.insert(tk.END, f"You: {message}\n")
    user_input.delete(0, tk.END)
    client_socket.send(message.encode())

def receive_message():
    while True:
        data = client_socket.recv(1024).decode()
        chat_output.insert(tk.END, f"Friend: {data}\n")

# Set up the GUI window
window = tk.Tk()
window.title("Python Chat App")

chat_output = tk.Text(window)
chat_output.pack()

user_input = tk.Entry(window)
user_input.pack()

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Connect to the server
server_address = ('localhost', 12345)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

# Start receiving messages in a separate thread
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

window.mainloop()

