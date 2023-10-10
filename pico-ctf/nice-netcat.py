import socket

HOST = "mercury.picoctf.net"
PORT = 21135

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))

data = s.recv(1024)
data = str(data)
print(data)



def sort_int(data):
    symbol = ""
    sorted = ""
    for i in range(len(data)):
        if data[i].isdigit():
            symbol += data[i]
        else:
            if symbol != "":
                sorted += chr(int(symbol))
                symbol = ""
                
    return sorted

print(sort_int(data))

"""
def sort_symbol_int(data):
    sorted = ""

    for i in range(len(data)):
        symbol = ""
        if data[i] == "'" or data[i] == 'n':
            while data[i] != " " and i < len(data) - 1 or data[i] != "'":
                i+= 1
                if data[i].isdigit():
                    symbol += data[i]
            
            symbol = symbol[:-1]
            i += 1
            sorted += chr(int(symbol))
            
    return sorted

print(sort_symbol_int(data))
"""  
s.close()