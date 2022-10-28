import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200)

print(ser.name)

ser.write(b'ATE1\r') # disable echo


# while True:

# cmd = b'AT+CSQ'
# ser.write(cmd+b'\r')
# ser.write(b'AT+CSQ\r')
# print('================')
# print(ser.readline())
# # print(ser.readline())
# print('----------------')
# time.sleep(0.1)
response = bytearray()
while True:
    b = ser.read_until(b'\r\n')
    if b == b'\r\n':
        continue
    # if b[0] == 13:
    #     if response == cmd:
    #         print('cmd')
    #     # break
    # response.extend(b)
    print(b)
print(response)
print('-------------')
time.sleep(3)
pass
