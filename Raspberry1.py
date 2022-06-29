# Write your code here :-)
import socket
from Crypto.Cipher import AES

#public and private keys
P=23
G=9
a=4

def generate_key(base, power, modulo):
    key = int(pow(base, power, modulo))
    return key

def module1():

    #compute key
    x = generate_key(G, a, P)

    #send private key
    clientconnected.send(str(x).encode())
    print("Sending key...\n")

    #receive private key
    y = clientconnected.recv(16)
    print("Receiving key...\n")

    #symmetric key->16 bytes
    ka = generate_key(int(y), a, P)
    ka = str(ka).encode()
    ka = ka.zfill(16)

    return ka

def module2(key):

    #read image
    plain_img = open("/home/pi/mu_code/images/raspberry-pi-logo.jpg",'rb')
    plain_data = plain_img.read()
    plain_data = plain_data[: - (len(plain_data)%16) ]
    plain_img.close()

    #encrypt data
    cipher = AES.new( key , AES.MODE_ECB)
    enc_data = cipher.encrypt(plain_data)
    print("Encrypting data...\n")

    #create encrypted image
    enc_img = open("enc_img.jpg","wb")
    enc_img.write(enc_data)
    enc_img.close()

    #send encrypted image
    clientconnected.sendall(enc_data)
    print("Sending encrypted image...\n")
    clientconnected.close()


#Main program

#open socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("169.254.193.224", 9090))
serversocket.listen()

#connect with client
(clientconnected, clientaddress) = serversocket.accept()
print("Accepted a connection request \n")

symmetric_key = module1()

module2(symmetric_key)

serversocket.close()




