from iot.message import MessageType

class HueLightDevice:
    def connect(self):
        print('Connecting Hue Light.')
        print('Hue Light connected.')

    def disconnect(self):
        print('Disconnect Hue Light.')
        print('Hue Light disconnect.')
    
    def send_message(self, message_type: MessageType, data: str=''):
        print(f'Hue Light handling message of type {message_type.name} with data [{data}].')
        print('Hue Light received message.')


class SmartSpeakerDevice:
    def connect(self):
        print('Connecting to Smart Speaker.')
        print('Smart Speaker connected.')

    def disconnected(self):
        print('Disconnecting Smart Speaker.')
        print('Smart Speaker disconnected.')

    def send_message(self, message_type: MessageType, data: str=''):
        print(f'Smart Speaker handling message of type {message_type.name} with data [{data}]')
        print('Smart Speaker received message.')

class SmartToiletDevice:
    def connect(self):
        print('Connecting to Smart Toilet.')
        print('Smart Toilet connected.')
    
    def disconnect(self):
        print('Disconnecting Smart Toilet.')
        print('Smart Toilet disconnecting')

    def send_message(self, message_type: MessageType, data: str=''):
        print(f'Smart Toilet handling message of type {message_type.name} with data [{data}]')
        print('Smart Toilet received message.')




















