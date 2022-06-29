# Raspberry-Pi-project
This project involves 2 Raspberry Pis (emulated using Virtual Box) connected with each other via Ethernet. It implements the Diffie-Hellmann key exchange protocol in each device. To emulate the Ethernet protocol the 2 virtual machines are connected in an internal network and communicate with each other using their IPs and one socket
bounded to a port.
Then, an image stored in the first device is encrypted and sent to the second device where it is decrypted. The first board operates as server and the second as client
in order to create a communication via Ethernet.

The first module implements the Diffie-Hellmann key exchange protocol and works on both board in the same way. First, we choose the two public keys P and G and 
then one private key for each board a and b respectively. Then we compute the generated keys on each board (x = G^a mod P, y = G^b mod P) 
which the boards exchange with each other via  the established connection.

Finally, the secret keys ka and kb can be generated using the received keys x and y (ka = y^a mod P , kb = x^b mod P). It can be proven mathematically that the 2 keys
ka and kb are equal and they are called as the symmetric keys which are used for encryption and decryption protocol. The key must be 16 bytes in this case of AES algorithm.


The second module on the first board uses the symmetric key that was computed before and encrypts an image using the AES algorithm on Electronic CodeBook mode.
For this operation we use the Crypto.Cipher package of Python. The data are divided into blocks of 16 bytes, and each block is encrypted independently. 
Then the encrypted image is sent to the second board via the established connectio and when all the data have been received, 
they are decrypted using AES algorithm in the inverse way. 
As it can been seen the decrypted image is identical to the initial image so the whole process worked perfectly.
