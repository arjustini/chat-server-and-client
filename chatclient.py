





#def main(host, port):
import socket
import select
import sys
import json

def main(user, port, chatip, chatport):
    server_socket = (chatip, int(chatport)) 
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', int(port)))
    sock.connect_ex(server_socket)
    subscribe = '{"operation": "subscribe", "client": "127.0.0.1:' + str(port) + '"}'
    sock.sendall(subscribe.encode())
    seq = 0

    read_list = [sys.stdin,sock]



    while True:
        can_read, _, _ = select.select(read_list, [], [])
        for s in can_read:
            if s == sock:
                data = sock.recv(1024)
                x = json.loads(data)
                if(data != b''):
                    if ("operation" not in x):
                        if(x["user"] != user):
                            print("%s: " % x["user"], end="")
                            print("%s" % x["message"])
                            seq = seq + 1
            else:
                msg = input()
                outgoingJson = '{"seq": ' + str(seq) + ', "user": "' + user + '", "message": "' + msg + '"}'
                if (msg == 'exit'):
                    outgoingJson = '{"operation": "unsubscribe", "client": "127.0.0.1:' + str(port) + '"}'
                    sock.sendall(outgoingJson.encode())
                    for rsock in read_list:
                            rsock.close()
                    sock.close()
                    sys.exit(1)

               # outgoingJson = '{"seq": ' + str(seq) + ', "user": "' + user + '", "message": "' + msg + '"}'
                seq = seq + 1
                sock.sendall(outgoingJson.encode())
        
        
       


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage:%s <user> <port> <chat server>' % sys.argv[0])
        sys.exit(-1)

    h = sys.argv[1]
    p = int(sys.argv[2])
    cs = sys.argv[3].split(":")

    print('user', h)
    print('port', p)
    print('chat server ip', cs[0])
    print('chat server port', cs[1])




    main(h, p, cs[0], cs[1])