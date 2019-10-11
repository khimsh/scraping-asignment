from flask import Flask, request, jsonify
from scraper import get_user

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    try:
        user_email = request.args.get('email')
        user_password = request.args.get('password')
        return jsonify(get_user(user_email, user_password))
    except:
        return 'Enter url in following format: ?email=test@testmail.com&password=pass123'


if __name__ == '__main__':
    app.run()
