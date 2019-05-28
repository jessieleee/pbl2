import datetime
import os
import sqlite3

from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

filename = './chat.db'
try:
    os.remove(filename)
except OSError:
    pass


def execute(query, parameters=(), result_mapper=None):
    result = None

    conn = sqlite3.connect(filename)
    c = conn.cursor()
    c.execute(query, parameters)
    conn.commit()

    if result_mapper:
        result = result_mapper(c)

    conn.close()

    return result


execute('CREATE TABLE message(id integer primary key autoincrement, nickname text, msg text, ts integer)')


class ChatMessage(Resource):
    def get(self):
        def message_result_mapper(c):
            messages = []
            for row in c:
                messages.append({
                    'id': row[0],
                    'nickname': row[1],
                    'message': row[2],
                    'timestamp': row[3],
                })
            return messages

        parser = reqparse.RequestParser()
        parser.add_argument('last_timestamp', type=int)
        args = parser.parse_args()

        last_timestamp = args['last_timestamp']

        if not last_timestamp:
            last_timestamp = 0

        messages = execute(
            'SELECT * FROM message WHERE ts > ? ORDER BY ts desc',
            parameters=(last_timestamp,),
            result_mapper=message_result_mapper,
        )

        return {'messages': messages}

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('nickname', type=str)
            parser.add_argument('message', type=str)
            args = parser.parse_args()

            execute(
                'INSERT INTO message(nickname, msg, ts) VALUES (?, ?, ?)',
                parameters=(args['nickname'], args['message'], int(datetime.datetime.now().timestamp())),
            )

            return {'nickname': args['nickname'], 'message': args['message']}
        except Exception as e:
            return {'error': str(e)}


api.add_resource(ChatMessage, '/chat')

if __name__ == '__main__':
    app.run(debug=True)
