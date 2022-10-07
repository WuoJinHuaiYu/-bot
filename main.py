from flask import Flask, request
import requests
import reply 

app = Flask(__name__)

class API:
    @staticmethod
    #有规定必须用这个名？
    def send(message):
        data = request.get_json()
        message_type=data['message_type']
        if 'group' == message_type:
            group_id=data['group_id']
            params = {
                "message_type": message_type,
                "group_id": str(group_id),
                #why一定是字符串？
                "message": message
            }
        else:
            user_id=data['user_id']
            params={
                "message_type": message_type,
                "user_id": str(user_id),
                "message": message
            }
        url="http://127.0.0.1:5700/send_msg"

        requests.get(url, params=params)


@app.route('/', methods=["POST"])
def post_data():
    data = request.get_json()
    print(data)
    if data['post_type']=='message':
      message = data ['message']
      print(message)
      reply.reply()
    else:
        print("暂不处理")

    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5701)  