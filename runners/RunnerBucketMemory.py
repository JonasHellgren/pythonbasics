from src.rlexplained_ch2.BucketMemory import BucketMemory

mem = BucketMemory()

mem.write(-9.5, 3.14)    # hc = 0
mem.write(-8.1, 2.71)    # hc = 1
mem.write(-7.5, 1.41)    # hc = 2
mem.write(5.2, 99.9)     # hc = 15

mem.read(-9.9)           # Should return 3.14
mem.read(-8.2)           # Should return 2.71
mem.read(5.3)            # Should return 99.9

mem.dump()               # Show everything