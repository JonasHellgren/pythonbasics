import math

class BucketMemory:
    def __init__(self):
        self.memory = {}

    def get_hc(self, x):
        # Maps x to memory cell hc using floor(x) + 10
        return math.floor(x) + 10

    def writeAtHash(self, hc, value):
        self.memory[hc] = value

    def write(self, x, value):
        hc = self.get_hc(x)
        self.writeAtHash(hc,value)
        print(f"✅ Stored {value} at hc = {hc}")

    def readAtHash(self, hc):
        value = self.memory.get(hc, 0)
        return value

    def read(self, x):
        hc = self.get_hc(x)
        value=self.readAtHash(hc)
        print(f"📥 Read from hc = {hc}: {value}")
        return value

    def dump(self):
        print("📦 Current Memory:")
        for hc in sorted(self.memory):
            print(f"  hc = {hc} → {self.memory[hc]}")