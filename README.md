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

Every action on the Delta 2 sends a UDP packet.
I started labelling sample packets in commands. I have gotten some of them wrong, focussing on the data points I care about most rn.

## Contributing

If you want to reverse engineer the connection from your Android phone to your bluetooth device, use the following process:

Prerequisites:
* An android phone with the app installed
* A way to record your screen
* A computer ideally with linux with wireshark and adb installed

* Connect phone via USB with Debugging turned on
* Enable HCI snooping
* (re-)enable Bluetooth
* Film your actions e.g. with a second phone or screen recording
* Open the app and do the thing you want to investigate
* Optionally: turn off blueooth and HCI snooping
* Retrieve the Blueooth snoop log
    * Either it is on the sd_card (wasn't for me), then do `adb pull ...` from the device
    * retrieve it via `adb bugreport`
* open the file in wireshark
* Try to establish a match between the video and the wireshark data. Tip: Jot down the times and their offsets on a piece of paper together with the performed action.

In rare cases the app is stuck for up to 3 seconds after pressing a button before sending the packet, introducing an offset.
