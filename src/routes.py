# API router example in Flask

from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Facebook verification
        verify_token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if verify_token == 'YOUR_VERIFY_TOKEN':
            return challenge, 200
        else:
            return 'Invalid verification token', 403
    elif request.method == 'POST':
        # Handle incoming messages
        data = request.get_json()
        # Process the data and send appropriate responses
        # ...
        return 'OK', 200

if __name__ == '__main__':
    app.run()