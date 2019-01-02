import hashlib
m=hashlib.md5()
#r='64:6c:bf:d4:a8:f8:a9:33:27:ed:32:80:b5:bd:dd:63'

r='80:b3:7b:ee:af:47:54:c2:8f:f8:91:01:e2:b7:62:0b'
#r='aa:e7:76:4a:bd:2c:51:a1:6d:b9:4a:b3:ff:7b:15:bc'
r='80:b3:7b:ee:af:47:54:c2:8f:f8:91:01:e2:b7:62:0b'
p='sjyhvpdn4g'.encode('ascii')
br=bytearray()
id1=chr(0x01).encode('ascii')

#for i in range(0,len(r)):
#    if i%2==0:br.append(eval('0x'+r[i]+r[i+1]))
             
for i in r.split(':'):
    br.append(eval('0x'+i))

def print_br(br):
    for i in br:
        print('%x'%i)
m.update(id1)
#m.update(p)
m.update(br)
#print(m.hexdigest())
print('expect='+m.hexdigest())

