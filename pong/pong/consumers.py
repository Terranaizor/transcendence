from channels.generic.websocket import WebsocketConsumer
import json

class MyConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # message_type = text_data_json['type']
        # if message_type == 'inputs_data':
        #     player1_dy = text_data_json['player1_dy']
        #     player2_dy = text_data_json['player2_dy']
        #     game_state['paddles']['player1_y'] += player1_dy
        #     game_state['paddles']['player2_y'] += player2_dy
        num += 1
        if num % 10 == 0:
            self.send(text_data=json.dumps({
                'message': 'plus'
            }))

num = 0
# game_state = {
#     'game_started': False,
#     'score': {'player1': 0, 'player2': 0}
#     'ball': {'x': 240, 'y': 240, 'dx': -1, 'dy': -1},
#     'paddles': {
#         'player1_y': 0,
#         'player2_y': 0,
#     },
# }