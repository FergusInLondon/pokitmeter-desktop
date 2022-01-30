import asyncio
from sys import platform

from bleak import BleakScanner

_KNOWN_SERVICE_UUID = "57d3a771-267c-4394-8872-78223e92aec4"

class Scanner:
    def __init__(self):
        self.devices = {} # Dict[str, BLEDevice]
        self.selected_device = None #Optional[BLEDevice]
    
    def scan(self):
        async def _scan(self):
            if platform == "darwin":
                devices = await BleakScanner.discover(service_uuids=[_KNOWN_SERVICE_UUID])
            else:
                devices = await BleakScanner.discover()

            return devices
        
        loop = asyncio.new_event_loop()
        devices = loop.run_until_complete(_scan(self))
        loop.close()

        self.devices = {
            d.name : d for d in devices
        }
    
    def select_device(self, device_key):
        self.selected_device = self.devices.get(device_key)
        if not self.selected_device:
            raise Exception("unrecognised device selected!", device_key)
