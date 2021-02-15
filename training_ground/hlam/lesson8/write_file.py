from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = ord('a') + i

try:
    bf = open(r'training_ground/lesson8/file.bin', 'ab')
    bytes = bf.write(data)
    bf.close()
    print(f'Successfully written {bytes} bytes')
except IOError as e:
    print('I/O error occured:', strerror(e.errno))