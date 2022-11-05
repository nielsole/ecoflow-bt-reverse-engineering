
import sys
import time

from bluetooth.ble import GATTRequester

def main(address: str):
    ac_on_string = "aa 02 07 00 de 0d 00 00 00 00 00 00 21 05 20 42 01 ff ff ff ff ff ff 6b 11"
    ac_on_string = ac_on_string.replace(" ", "")
    data = bytes.fromhex(ac_on_string)
    print(data)
    requester = GATTRequester(address, False)
    connect(requester)
    request_data(requester)
    print("characeristics:")
    # Sends read by type request instead of read by by group type (UUID 0x2803 vs 0x2800)
    print(requester.discover_characteristics(0x0001, 0xffff))
    print(requester.exchange_mtu(500))
    requester.set_mtu(500)
    time.sleep(1)
    requester.write_cmd(0x002a, data)

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

    service = DiscoveryService("hci0")
    devices = service.discover(2)

    for address, name in devices.items():
        print("name: {}, addr: {}".format(name, address))
        if address.startswith("34:B4"):
            print("^-- This might be an ecoflow device")
    
    if len(sys.argv) < 2:
        print("Usage: {} <addr>".format(sys.argv[0]))
        sys.exit(1)
    main(sys.argv[1])
    time.sleep(5)
