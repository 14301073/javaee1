#coding=utf-8 
#服务器端
import socket
import threading,getopt,sys,string

opts, args = getopt.getopt(sys.argv[1:], "hp:l:",["help","port=","list="])
#设置默认的最大连接数和端口号，在没有使用命令传入参数的时候将使用默认的值
list=50
port=3333
def usage():
    print """
    -h --help             print the help
    -l --list             Maximum number of connections
    -p --port             To monitor the port number  
    """
for op, value in opts:
    if op in ("-l","--list"):
        list = string.atol(value)
    elif op in ("-p","--port"):
        port = string.atol(value)
    elif op in ("-h"):
        usage()
        sys.exit()

def jonnyS(client, address):
    try:
    #设置超时时间
        client.settimeout(500)
    #接收数据的大小
        buf = client.recv(2048)
    #将接收到的信息原样的返回到客户端中
	    client.send(buf[::-1])
       # client.send(buf)
    #超时后显示退出
    except socket.timeout:
        print 'time out'
    #关闭与客户端的连接
    client.close()

def main():
    #创建socket对象。调用socket构造函数
    #AF_INET为ip地址族，SOCK_STREAM为流套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    #将socket绑定到指定地址，第一个参数为ip地址，第二个参数为端口号
    sock.bind(('localhost', port))  
    #设置最多连接数量
    sock.listen(list) 
    while True:  
    #服务器套接字通过socket的accept方法等待客户请求一个连接
        client,address = sock.accept()  
        thread = threading.Thread(target=jonnyS, args=(client, address))
        thread.start()

if __name__ == '__main__':
    main()
	
	#coding=utf-8
	#客户端
import getopt,socket,sys,string

opts, args = getopt.getopt(sys.argv[1:], "hi:p:",["help","ip=","port="])
#设置默认的ip地址和端口号，在没有使用命令传入参数的时候将使用默认的值
host="localhost"
port=3333
def usage():
    print """
    -h --help             print the help
    -i --ip               Enter the IP address to connect
    -p --port             Enter the port number to connect  
    """
for op, value in opts:
    if op in ("-i","--ip"):
        host = value
    elif op in ("-p","--port"):
        port = string.atol(value)
    elif op in ("-h"):
        usage()
        sys.exit()

def main():   
#创建socket对象。调用socket构造函数
#AF_INET为ip地址族，SOCK_STREAM为流套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#设置要连接的服务器的ip号和端口号
    sock.connect((host, port))
#客户端输入一个字符串给服务器    
    message = raw_input("inupt:")
    #pdb.set_trace()
    sock.send(message)  
    print 'ServerOupt:'+ sock.recv(2048)
#关闭与服务器的连接  
    sock.close()  

if __name__ == '__main__': 
    main()
