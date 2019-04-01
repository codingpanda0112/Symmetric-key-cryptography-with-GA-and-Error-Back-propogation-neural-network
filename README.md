# Symmetric-key-cryptography-with-GA-and-Error-Back-propogation-neural-network
Encrypting the text using Genetic Algorithm (crossover and mutation) and decrypting using neural network error back propagation.

Encryption:
1. Get input data from the sender in ie plaintext.
2. Convert plain text in ASCII format.
3. Convert the ASCII value in to binary value (use asTarget value for the Error back propagation neural network).
4. Take the binary string and divide in to equal size and crossover both string.
5. Now use mutation over the string get from crossover section. This string use as cipher text and send this to the receiver over the network.
Decryption:-
1. Receiver receives the cipher text sending by the sender.
2. Send that cipher text as input in to error back propagation neural network and set the target value.
3. When the output data of the error back propagation neural network is same as target value then take the  output.
4. Convert that output (binary string) in to ASCII
5. And last convert ASCII to corresponding to plain text.

# how to run:
On System 1
1.Run encryption.py on one system 
2.On the same system run client.py

On System 2
1.Open Wireshark to capture the packets (filtered by ip_addr==ip of system1 and tcp)
2. Run server.py
3. save the captured packets as pcap file.
4. Run decryption.py


