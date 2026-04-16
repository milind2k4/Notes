Links: 
___
# Computer Networks 

Port number is a 16 bit unique identification number assigned to processes. 

They are integer between 0 to 65535

## Transport Layer Protocols 

### UDP (User Datagram)
It is unreliable connection less protocol. 

It doesnt provide flow control or ordered delivery. 

It is used to send small messages. 

It has fixed size header of 8 bytes made up of 4 fields. 

UDP header 

Total length of udp packet (datagram) = header length + data length

#### Services 
Connection less service: There is no connection establishment and no connection termination. 

Process to Process Communication 

Error control- No

Congestion control- No 

Flow Control- No

Encapsulation and Decapsulation 

Multiplexing and Demultiplexing. 

### TCP (Transmission Control)
It is connection oriented, reliable and byte stream protocol. 

It guarantees in order delivery of stream of bytes. 

It is a full duplex protocol. 

A packet in TCP is called segment. 

#### Services 
Stream Delivery Service: It delivers data as a stream of bytes. 

Process to process communication 

Full duplex 

Multiplexing Demultiplexing

Reliable Flow Control 

Congestion Control 

Error Control 

Encapsulation Decapsulation

#### TCP Packet Format 

The segment consist of header of 20-60 bytes. 

The header is of 20 bytes if there are no options and upto 60 bytes if it contains options. 

TCP header 

#### Connection Establishment 
Three way handshake 

Diagram 

#### Connection Termination 

### SCTP (Stream Control Transmission)