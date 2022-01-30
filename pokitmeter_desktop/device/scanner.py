from sys import platform

from bleak import BleakScanner

# Workaround for macOS Monterey; should be resolved in 12.3; but
# scanning for devices without providing a service UUID will fail.
# Frustratingly this is the only service UUID contained in the
# advertising data.
_KNOWN_SERVICE_UUID = "57d3a771-267c-4394-8872-78223e92aec4"

class Scanner:
    def __init__(self, loop):
        # The event loop is required as the macOS driver caches the "central manager
        # delegate" upon device discovery, so subsequent attempts at pairing will fail
        # should the interaction come from another loop.
        self.loop = loop
        self.devices = {} # Dict[str, BLEDevice]
        self.selected_device = None #Optional[BLEDevice]

    def scan(self):
        async def _scan():
            if platform == "darwin":
                devices = await BleakScanner.discover(service_uuids=[_KNOWN_SERVICE_UUID])
            else:
                devices = await BleakScanner.discover()

            return devices

        devices = self.loop.run_until_complete(_scan())

        self.devices = {
            d.name : d for d in devices
        }
    
    def select_device(self, device_key):
        self.selected_device = self.devices.get(device_key)
        if not self.selected_device:
            raise Exception("unrecognised device selected!", device_key)

        print("selected device:")
        print(self.selected_device)
