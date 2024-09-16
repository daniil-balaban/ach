#!/usr/bin/env python
import ach
import struct
import time

i = 0

channel = ach.Channel('channel152')
time.sleep(1.5)
#channel.flush()

while True:

    buffer = bytearray(4)
    [status, framesize] = channel.get(buffer, wait=True, last=False)

    #if status == ach.ACH_OK:
    x,y = struct.unpack('<hh', buffer)
    print(f"iteration {i} : receiving {x,y} from {buffer}")
    #else:
    #    raise ach.AchException(channel.result_string(int(status)))

    i+= 1

channel.flush()
#channel.unlink()
channel.close()