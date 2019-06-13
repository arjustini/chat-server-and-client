import socket
import select
import sys
import json

def main(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print('listening on', (host, port))

    read_list = [server_socket]
    write_list = []
    seq = 0

    while True:
        can_read, _, _ = select.select(read_list, [], [])
        for s in can_read:
            if s == server_socket:
                    # a connection is incoming
                    conn, addr = s.accept()
                    read_list.append(conn)
                    print("accepted connection from", addr)
                    write_list.append(conn)
            else:
                data = s.recv(1024)
               
                if data:
                    x = json.loads(data)
                    print(x)
                    for s in write_list:
                            s.sendall(data)
                else:
                    if (len(write_list) != 1):
                        write_list.remove(s)
                        s.close()
                    else:
                        server_socket.close()
                        sys.exit(1)


           



if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage:%s <IP> <port>' % sys.argv[0])
        sys.exit(-1)

    h = sys.argv[1]
    p = int(sys.argv[2])

    print('host', h)
    print('port', p)

    main(h, p)