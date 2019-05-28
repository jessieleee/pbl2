import datetime
import sqlite3

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

conn = sqlite3.connect('chat.db')

c = conn.cursor()
c.execute('CREATE TABLE message(nickname text, message text, timestamp real)')
c.commit()


class ChatMessage(Resource):
    def get(self):
        return {
            'messages': [
                {'nickname': 'tester1', 'message': 'test1', 'timestamp': int(datetime.datetime.now().timestamp())},
                {'nickname': 'tester2', 'message': 'test2', 'timestamp': int(datetime.datetime.now().timestamp())},
                {'nickname': 'tester1', 'message': 'test3', 'timestamp': int(datetime.datetime.now().timestamp())},
                {'nickname': 'tester2', 'message': 'test4', 'timestamp': int(datetime.datetime.now().timestamp())},
                {'nickname': 'tester1', 'message': 'test5', 'timestamp': int(datetime.datetime.now().timestamp())},
            ]
        }

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('nickname', type=str)
            parser.add_argument('message', type=str)
            args = parser.parse_args()

            c = conn.cursor()

            c.execute('INSERT INTO ')

            return {'nickname': args['nickname'], 'message': args['message']}
        except Exception as e:
            return {'error': str(e)}


api.add_resource(ChatMessage, '/chat')

if __name__ == '__main__':
    app.run(debug=True)
    conn.close()
