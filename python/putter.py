#!/usr/bin/env python
import ach
import struct
import time

i = 0
x,y = 320,240
channel = ach.Channel('channel152')
channel.flush()

time.sleep(1)


while i < 10:
    data = struct.pack('<hh', x+(i*10), y+(i*10))
    print(f"iteration {i} : sending {x+(i*10),y+(i*10)} as {data}")
    channel.put(data)
    i += 1

#channel.unlink()
channel.close()