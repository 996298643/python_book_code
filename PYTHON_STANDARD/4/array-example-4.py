#数据文件所以不能跨平台，主要是由于不同平台的字节顺序不同，这是计算机领域由来已久的问题之一，
# 在各种计算机体系结构中，由于对于字，字节等存储机制有所不同，通信双方交流的信息单元（比特、字节、字、双字等）应该以什么样的顺序进行传送就成了一个问题，如果不达成一致的规则，
# 通信双方将无法进行正确的编/译码从而导致通信失败。
#目前在各种体系的计算机中通常采用的字节存储机制主要有两种：Big-Endian和Little-Endian。
#一些操作系统（包括Windows）在低位内存地址中存放二进制数据的最低有效字节，因此这种系统被称为Little Endian；
# 一些操作系统（包括Solaris）将最高有效字节存储在低位内存地址中，因此这种系统被称为big Endian
#举一个简单的例子，假如1122这样一个数据要存入不同系统，对于Little Endian的系统，存储的顺序就是2211，小头在前；
# 而对于Big Endian的系统来说，存储的顺序就是1122，大头在前，显然Big Endian更符合我们通常的语言习惯。
#那么跨平台的问题就出现了，当一个Little Endian的系统试图从一个Big Endian的系统中读取数据时，就需要通过转换，否则不同的字节顺序将导致数据不能被正确读取'

import array

def litter_endian():
    return ord(array.array("i", [1]).tostring()[0])

if litter_endian():
    print("litter-endian")
else:
    print("big-endian")