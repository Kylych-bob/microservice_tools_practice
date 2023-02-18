from iot.message import MessageType
import asyncio

# make ansync methods
class HueLightDevice:
    async def connect(self):
        print('Connecting Hue Light.')
        await asyncio.sleep(0.5)
        print('Hue Light connected.')

    async def disconnect(self):
        print('Disconnect Hue Light.')
        await asyncio.sleep(0.5)
        print('Hue Light disconnect.')
    
    async def send_message(self, message_type: MessageType, data: str=''):
        print(f'Hue Light handling message of type {message_type.name} with data [{data}].')
        await asyncio.sleep(0.5)
        print('Hue Light received message.')


class SmartSpeakerDevice:
    async def connect(self):
        print('Connecting to Smart Speaker.')
        await asyncio.sleep(0.5)
        print('Smart Speaker connected.')

    async def disconnected(self):
        print('Disconnecting Smart Speaker.')
        await asyncio.sleep(0.5)
        print('Smart Speaker disconnected.')

    async def send_message(self, message_type: MessageType, data: str=''):
        print(f'Smart Speaker handling message of type {message_type.name} with data [{data}]')
        await asyncio.sleep(0.5)
        print('Smart Speaker received message.')

class SmartToiletDevice:
    async def connect(self):
        print('Connecting to Smart Toilet.')
        await asyncio.sleep(0.5)
        print('Smart Toilet connected.')
    
    async def disconnect(self):
        print('Disconnecting Smart Toilet.')
        await asyncio.sleep(0.5)
        print('Smart Toilet disconnecting')

    async def send_message(self, message_type: MessageType, data: str=''):
        print(f'Smart Toilet handling message of type {message_type.name} with data [{data}]')
        await asyncio.sleep(0.5)
        print('Smart Toilet received message.')




















