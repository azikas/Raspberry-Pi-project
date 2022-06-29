# Write your code here :-)
import socket
from Crypto.Cipher import AES

#public and private keys
P=23
G=9
b=3

def generate_key(base, power, modulo):
    key = int(pow(base, power, modulo))
    return key;

def module1():

    #compute key
    y = generate_key(G, b, P);

    #receive private key
    x = clientsocket.recv(16)
    print("Receiving key...\n")

    #send private key
    clientsocket.send(str(y).encode())
    print("Sending key...\n")

    #symmetric key
    kb = generate_key(int(x), b, P)
    kb = str(kb).encode()
    kb = kb.zfill(16)

    return kb


def module2(key):

    #receive encrypted data
    rcv_img = open("rcv_img.jpg", "wb")
    print("Receiving encrypted data...\n")
    r = clientsocket.recv(1024)

    #wait all data
    while(r):
        rcv_img.write(r)
        r = clientsocket.recv(1024)
    rcv_img.close()

    #read encrypted data
    rcv_img = open("rcv_img.jpg", "rb")
    enc_data = rcv_img.read()
    rcv_img.close()

    #decrypt data
    decipher = AES.new( key, AES.MODE_ECB)
    dec_data = decipher.decrypt(enc_data)
    print("Decrypting data..\n")

    #store decrypted image
    dec_img = open("dec_img.jpg", "wb")
    dec_img.write(dec_data)
    dec_img.close()


#Main program

#connect with server
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("169.254.193.224", 9090))
print("Requesting a connection...\n")

symmetric_key = module1()

module2(symmetric_key)

