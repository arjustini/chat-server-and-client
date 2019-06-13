- Chat app that allows multiple users to register with the chat server -- all the users that are registered will receive the messages sent to the chat server.




- Instructions: To start the server, the chatserver.py file needs to be run with an IPv4 address as well as a port number that the server will be hosted on. An example is provided below:



    Chat server input: '\<IP>' '<port>'
    example arguments: 192.168.1.101 5000
 
 
 
- After running the server, multiple instances of the chatclient.py file may be ran to register more users to the chat server. These clients require a username, a port number to connect to on the server, and the IPv4 and port number of the server. An example is provided below:
  
  
  
  
    Chat client input: <user> <port> <chat server>
    example arguments: user1 5001 192.168.1.101:5000
