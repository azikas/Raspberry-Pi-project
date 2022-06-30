# Raspberry-Pi-project
This project involves 2 Raspberry Pis (emulated by Virtual Box) connected with each other via Ethernet. It implements the Diffie-Hellmann key exchange protocol in each device. In order to emulate the Ethernet protocol, the 2 virtual machines are connected in an internal network and communicate with each other using their IPs and one socket bounded to a port. The first board operates as server and the second as a client to create a communication via Ethernet.
Then, an image stored in the first device is encrypted and sent to the second device where it is decrypted. 

The first software module implements the Diffie-Hellmann key exchange protocol and works on both board in the same way. First, we choose the two public keys P and G and 
then one private key for each board a and b respectively. Then we compute the generated keys on each board (x = G^a mod P, y = G^b mod P) 
which the boards exchange with each other via the established connection. Now each board has its own and the other's generated keys.

Finally, the secret keys ka and kb can be generated using the received keys x and y (ka = y^a mod P , kb = x^b mod P). It can be proven mathematically that the 2 keys
ka and kb are equal and they are called as the symmetric keys which are used for the encryption and decryption. The key must be 16 bytes long in this case of AES algorithm.


The second software module on the first board uses the symmetric key, that was computed before, and encrypts an image using the AES algorithm on Electronic CodeBook mode. The data are divided into blocks of 16 bytes, thus they must be multiple of 16, and each block is encrypted independently.
For this operation we use the Crypto.Cipher package of Python that provides methods for AES encryption and decryption.
Then the encrypted image is stored and sent to the second board via the established connection.

On the second board, when all the data have been received, they are stored as an encrypted image. Then,
they are decrypted using AES algorithm on ECB mode in the inverse way and stored as a decrypted image.
As it can been seen, the decrypted image is identical to the initial image so the whole process worked perfectly.
