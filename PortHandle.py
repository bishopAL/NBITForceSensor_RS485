import serial
import time
import binascii

class PortHandle(object):
    def __init__(self, port, baudrate):
        self.s = serial.Serial(port, baudrate, timeout=0.05)
        self.getForceCmd = b'\x01\x03\x02\x00\x12\x38\x49'
        self.clearZeroCmd = b'\x01\x19\x00\x00\x01\xdf\x5c'
        self.setZeroCmd = b'\x01\x12\x00\x00\x01\xdd\x78'
        self.force = [0, 0, 0, 0, 0, 0]

    def clearZero(self):
        self.s.write(self.clearZeroCmd)
    def setZero(self):
        self.s.write(self.setZeroCmd)
    def getForce(self):
        self.s.write(self.getForceCmd)
        temp_back = self.s.readlines()  # get the force data
        hex_bytes=binascii.hexlify(temp_back[0])
        hex_str=hex_bytes.decode("ascii")
        listIndex = 0
        if(len(hex_str)==46):
            index=6  # 数据起始位置
            while(index<42):  # 每6位为一个数据，第一位为符号位，转换为十进制输出，共36位数据（6*6）
                num=(hex_str[index+1:index+6])
                if(hex_str[index]=='8'):
                    self.force[listIndex] = -int(num,16)
                else:
                    self.force[listIndex] = int(num,16)
                index += 6
                listIndex += 1
        