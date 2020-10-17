from simple_rpc import Interface
import time

iface = Interface(f"/dev/ttyACM0")

while True:
    print(iface.call_method('button_state'))
    time.sleep(1)
