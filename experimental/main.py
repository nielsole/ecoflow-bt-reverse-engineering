
import sys

from bluetooth.ble import GATTRequester

class Requester(GATTRequester):
    def on_notification(self, handle: int, data: str):
        pass


def main(address: str):
    requester = Requester(address, False)
    connect(requester)
    request_data(requester)
    print("characeristics:")
    # Sends read by type request instead of read by by group type (UUID 0x2803 vs 0x2800)
    print(requester.discover_characteristics(0x0001, 0xffff))
    print(requester.exchange_mtu(500))
    requester.set_mtu(500)
    actions = {
        "ac_on":    "aa 02 07 00 de 0d 00 00 00 00 00 00 21 05 20 42 01 ff ff ff ff ff ff 6b 11",
        "ac_off":   "aa 02 07 00 de 0d 00 00 00 00 00 00 21 05 20 42 00 ff ff ff ff ff ff 7b d1",
        "12v_on":   "aa 02 01 00 a0 0d 00 00 00 00 00 00 21 05 20 51 01 32 c2",
        "12v_off":  "aa 02 01 00 a0 0d 00 00 00 00 00 00 21 05 20 51 00 f3 02",
        "usb_on":   "aa 02 01 00 a0 0d 00 00 00 00 00 00 21 02 20 22 01 16 86",
        "usb_off":  "aa 02 01 00 a0 0d 00 00 00 00 00 00 21 02 20 22 00 d7 46",
    }
    while True:
        print("Available actions:")
        for action in actions.keys():
            print("{}".format(action))
        selected_action = input("Which action to send? Leave empty and press return to exit. ")
        if len(selected_action) == 0:
            break
        try:
            trimmed_hex_string = actions[selected_action].replace(" ", "")
            data = bytes.fromhex(trimmed_hex_string)
            requester.write_cmd(0x002a, data)
        except KeyError as e:
            break

def connect(requester):
    print("Connecting...", end=" ")
    sys.stdout.flush()

    requester.connect(True)
    print("OK.")

def request_data(requester):
    data = requester.read_by_uuid(
        "00002a00-0000-1000-8000-00805f9b34fb")[0]
    try:
        print("Device name:", data.decode("utf-8"))
    except AttributeError:
        print("Device name:", data)


if __name__ == "__main__":
    from gattlib import DiscoveryService

    if len(sys.argv) < 2:
        print("Usage: {} <addr>".format(sys.argv[0]))
        service = DiscoveryService("hci0")
        devices = service.discover(2)

        for address, name in devices.items():
            if address.startswith("34:B4"):
                print("name: {}, addr: {}".format(name, address))
                print("^-- This might be an ecoflow device")
        sys.exit(1)
    main(sys.argv[1])
