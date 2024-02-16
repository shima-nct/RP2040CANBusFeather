#!/usr/bin/env python

# pytyon-can
# https://python-can.readthedocs.io/en/stable/

# 2-CH CAN HAT
# https://www.waveshare.com/wiki/2-CH_CAN_HAT

import struct
import os
import can

# CANバスの取得
bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')

def send_motor_control_amount(left=0.0, right=0.0, duration=1.0):

    msg_left = can.Message(arbitration_id = 0x123, data=struct.pack('f', left), is_extended_id = False)
    msg_right = can.Message(arbitration_id = 0x124, data=struct.pack('f', right), is_extended_id = False)
    msg_dulation = can.Message(arbitration_id = 0x125, data=struct.pack('f', msg_dulation), is_extended_id = False)

    try:
        for msg in (msg_left, msg_right, msg_dulation):
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