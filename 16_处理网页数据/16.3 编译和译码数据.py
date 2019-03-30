import xdrlib

#编码数据
def packer(name, sex, age):
    
    #创建Packer类的实例变量
    p = xdrlib.Packer()

    #将一个变动长度的字符串做XDR编码
    p.pack_string(name)
    p.pack_string(sex)

    #将一个32位的无正负号整数做XDR编码
    p.pack_uint(age)

    #将目前的编码缓冲区内容以字符串类型返回
    data = p.get_buffer()
    return data

#译码数据
def unpacker(packer):

    #创建Unpacker类的实例变量
    p = xdrlib.Unpacker(packer)
    return p

#打印未编码前的数据
print ("没有编码前的数据: '张芳', '女', 24")

#编码数据
packedData = packer("张芳".encode('utf-8'), "女".encode('utf-8'), 24)

#打印编码后的数据
print ("编码后的数据为： ", repr(packedData))

#打印译码后的数据
unpackedData = unpacker(packedData)
print ("编译后的数据为: ")
print ((repr(unpackedData.unpack_string()), ", ", \
      repr(unpackedData.unpack_string()), ", ", \
      unpackedData.unpack_uint()))

#译码完毕
unpackedData.done()
