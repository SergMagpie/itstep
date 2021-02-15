from os import strerror
data = bytearray(20)
try:
    bf = open(r'training_ground/lesson8/file.bin', 'rb')
    bf.readinto(data)
    bf.close()
    for b in data:
        print(chr(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))