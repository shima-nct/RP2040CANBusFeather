#!/usr/bin/env python

# pytyon-can
# https://python-can.readthedocs.io/en/stable/

# 2-CH CAN HAT
# https://www.waveshare.com/wiki/2-CH_CAN_HAT

import os
import can

# CANバスの取得
bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')

def send_motor_control_amount(left=0.0, right=0.0, duration=1.0):

    # メッセージの組み立て
    msg_txt = f"{left:.1f},{right:.1f},{duration:2.1f}"
    # https://python-can.readthedocs.io/en/stable/message.html
    msg_bytes = bytes(msg_txt, 'utf-8')
    msg = can.Message(data=msg_bytes, is_extended_id = False)

    try:
        bus.send(msg)
        print(f"Message sent on {bus.channel_info}")
    except can.CanError:
        print("Message NOT sent")

def main():
    while True:
        send_motor_control_amount(left=0.4, right=0.0, duration=1)
        send_motor_control_amount(left=0.0, right=-0.4, duration=1)

if __name__ == "__main__":
    main()