import struct

buffer = struct.pack("ihb", 1, 2, 3)

print(repr(buffer))

print(struct.unpack("ihb", buffer))

data = [1, 2, 3]

buffer = struct.pack("!ihb",  *data)

print(repr(buffer))

print(struct.unpack("!ihb",buffer))