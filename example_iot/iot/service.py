import random 
import string 
from typing import Protocol

from iot.message import Message, MessageType

def generate_id(length: int=8):
    return ''.join(random.choices(string.ascii_uppercase, k=length))

class Device(Protocol):
    def connect(self):
        ...
    def disconnect(self):
        ...
    def send_message(self, message_type: MessageType, data: str):
        ...
    
class IOTService:
    def __init__(self):
        self.devices: dict[str, Device] = {}

    def register_device(self, device: Device):
        device.connect()
        device_id = generate_id()
        self.devices[device_id] = device
        return device_id

    def unregister_device(self, device_id:str):
        return self.devices[device_id]
    
    def run_program(self, program: list[Message]):
        print('==========RUNNING PROGRAM==========')
        for msg in program:
            self.send_msg(msg)
        print('==========END OF PROGRAM==========')

    def send_msg(self, msg: Message):
        self.devices[msg.device_id].send_message(msg.msg_type, msg.data)