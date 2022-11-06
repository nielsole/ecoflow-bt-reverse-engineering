# Delta 2 Bluetooth

Reverse engineering of Delta 2 Bluetooth interface.
No affiliation with Ecoflow.

What currently works:
* Turn on/off USB, AC and 12VDC output

## Demo

The `experimental/main.py` script connects to the Delta 2 and let's you toggle the outputs.
Follow the installation instructions for pybluez.
The script must run as root.
This is experimental.
This might brick your device.
I use linux, no other OS is tested, but it might just work for you.

## Overview

The Delta 2 uses an Espressif bluetooth MAC Address (mine starts with 34:b4).

The Delta 2 offers up 3 attributes:

```
Bluetooth Attribute Protocol
    Opcode: Read By Group Type Response (0x11)
    Length: 6
    Attribute Data, Handle: 0x0001, Group End Handle: 0x0005, UUID: Generic Attribute Profile
    Attribute Data, Handle: 0x0014, Group End Handle: 0x001c, UUID: Generic Access Profile
    Attribute Data, Handle: 0x0028, Group End Handle: 0xffff, UUID: SDP
    [UUID: GATT Primary Service Declaration (0x2800)]
    [Request in Frame: 726]
```

In my traces the following handles were used:
* 0x002d SDP: RFCOMM Delta2->Phone
* 0x002a SDP: UDP Phone -> Delta2


### RFCOMM status

The Delta 2 sends out a beacon every 500ms that likely contains all current information, such as charge, discharge, port states etc.
I tried decoding this beacon in `states` and `states2` but haven't had much success yet.

### UDP Commands

Every action on the Delta 2 sends a UDP packet. In rare cases there is up to 3 seconds delay from pressing a button to sending the packet.
I started labelling sample packets in commands. I have gotten some of them wrong, focussing on the data points I care about most rn.

## Contributing

