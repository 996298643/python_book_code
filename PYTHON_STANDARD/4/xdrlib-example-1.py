###xdrlib模块定义了两个类，一个用于将变量打包到XDR表示中，另一个用于从XDR表示中解压缩。还有两个异常类。
#class xdrlib.Packer
#Packer是将数据打包到XDR表示中的类。将Packer类实例化不带任何参数。
#class xdrlib.Unpacker(data)
#Unpacker是从字符串缓冲区中解压XDR数据值的补充类。输入缓冲区是作为数据给出的。
import xdrlib

p = xdrlib.Packer()

p.pack_uint(1)

#p.pack_string("spam")

data = p.get_buffer()

print("packed"+repr(data))

u = xdrlib.Unpacker(data)

print("unpacked"+u.unpack_string())

u.done()
