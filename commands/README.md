Analyzing commands and decompiled source code there was some success in understanding command structure.

Lets take a look at provided command dumps:

```
                     Data    <     Flags (incl. encr, chk, ack)   Cmd Func                       <<     Similar MQTT   
Filename   Hdr  Ver  length  CRC8  |  Seq number  Prod    Src Dst |  C.Id  Data                  CRC16  command name
12v-off    aa   02   01 00   a0    0d 00 00 00 00 00 00   21  05  20  51   00                    f3 02  mpptCar
12v-on     aa   02   01 00   a0    0d 00 00 00 00 00 00   21  05  20  51   01                    32 c2  mpptCar
400w-chl   aa   02   03 00   8a    0d 00 00 00 00 00 00   21  05  20  45   90 01 ff              8a 43  acChgCfg
800w-chl   aa   02   03 00   8a    0d 00 00 00 00 00 00   21  05  20  45   20 03 ff              8a c4  acChgCfg
1000w-chl  aa   02   03 00   8a    0d 00 00 00 00 00 00   21  05  20  45   e8 03 ff              0b 3a  acChgCfg
ac-off     aa   02   01 00   a0    0d 00 00 00 00 00 00   21  05  20  51   01                    32 c2  <-- is a 12v command!
ac-off2    aa   02   07 00   de    0d 00 00 00 00 00 00   21  05  20  42   00 ff ff ff ff ff ff  7b d1  acOutCfg
ac-off3    aa   02   07 00   de    0d 00 00 00 00 00 00   21  05  20  42   00 ff ff ff ff ff ff  7b d1  acOutCfg
ac-off4    aa   02   07 00   de    0d 00 00 00 00 00 00   21  05  20  42   00 ff ff ff ff ff ff  7b d1  acOutCfg
ac-on      aa   02   07 00   de    0d 00 00 00 00 00 00   21  05  20  42   00 ff ff ff ff ff ff  7b d1  acOutCfg
ac-on2     aa   02   07 00   de    0d 00 00 00 00 00 00   21  05  20  42   01 ff ff ff ff ff ff  6b 11  acOutCfg
ac-on3     aa   02   07 00   de    0d 00 00 00 00 00 00   21  05  20  42   01 ff ff ff ff ff ff  6b 11  acOutCfg
ac-on4     aa   02   07 00   de    0d 00 00 00 00 00 00   21  05  20  42   01 ff ff ff ff ff ff  6b 11  acOutCfg
usb-off    aa   02   01 00   a0    0d 00 00 00 00 00 00   21  02  20  22   00                    d7 46  dcOutCfg
usb-on     aa   02   01 00   a0    0d 00 00 00 00 00 00   21  02  20  22   01                    16 86  dcOutCfg          
```

There was an extra part `02 40 00 1a 00 16 00 04 00 52 2a 00` in `usb-on` command not related to it.

I have also tried to point out corresponding MQTT commands and outlined them after the binary part.
