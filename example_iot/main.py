from iot.devices import HueLightDevice, SmartSpeakerDevice, SmartToiletDevice
from iot.message import Message, MessageType
from iot.service import IOTService
import asyncio
from typing import Any, Awaitable

async def run_sequence(*functions: Awaitable[Any]):
    for function in functions:
        await function

async def run_parallel(*functions: Awaitable[Any]):
    await asyncio.gather(*functions)



async def main():
    # create a IOT service
    service = IOTService()

    # create and register a few devices
    hue_light = HueLightDevice()
    speaker = SmartSpeakerDevice()
    toilet = SmartToiletDevice()

    # first way to connect
    # hue_light_id = await service.register_device(hue_light)
    # speaker_id = await service.register_device(speaker)
    # toilet_id = await service.register_device(toilet)

    # second way to connect with func gather 
    hue_light_id, speaker_id, toilet_id = await asyncio.gather(
        service.register_device(hue_light),
        service.register_device(speaker),
        service.register_device(toilet)
    )


    # create a few programs
    wake_up_program = [
        Message(hue_light_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.PLAY_SONG, 'miles davis - kind of blue')
    ]

    sleep_program = [
        Message(hue_light_id, MessageType.SWITCH_OFF),
        Message(speaker_id, MessageType.SWITCH_OFF),
        Message(toilet_id, MessageType.FLUSH),
        Message(toilet_id, MessageType.CLEAN)
    ]

    # run the programs
    await service.run_program(wake_up_program)
    # await service.run_program(sleep_program)
    await run_parallel(
        service.send_msg(Message(hue_light_id, MessageType.SWITCH_OFF)),
        service.send_msg(Message(speaker_id, MessageType.SWITCH_OFF)),
        run_sequence(
            service.send_msg(Message(toilet_id, MessageType.FLUSH)),
            service.send_msg(Message(toilet_id, MessageType.CLEAN))
        )
    )


if __name__ == '__main__':
    asyncio.run(main())