import socket
import io
import DataBase as DB
from PIL import Image
import random

IP = socket.gethostbyname(socket.gethostname())
PORT = 7510
ADDR = (socket.gethostname(), PORT)
SIZE = 1024*500000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[STARTING] Server is starting...")
server.bind(ADDR)
server.listen()


def main():
    while True:
        conn, addr = server.accept()
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True
        while connected:
            file_stream = io.BytesIO()
            recv_data = conn.recv(SIZE)
            # data is image
            if (len(recv_data) > 50):
                # receiving  the image from client and store it in the database
                while recv_data:
                    file_stream.write(recv_data)
                    recv_data = conn.recv(SIZE)
                    if recv_data == b"%finish%":
                        break

                # save an image in a path specified by `getPath` function
                image = Image.open(file_stream)
                image.save(DB.getPath())
                confirmation_msg = 'store processs is done!'
                conn.send(confirmation_msg.encode('UTF-8'))



            else:
                # sending the demanded image to the client
                recv_data = recv_data.decode('UTF-8')
            # data is image id
                #data = {'retrieve', recv_data}
                # print("-----------------------")
                # print(f"Image ID: {recv_data}")
                # print("-----------------------")
                img_name = DB.send_img_data(recv_data) # Image ID
                with open( img_name , 'rb') as file:
                # with open('./images/x-ray ('+recv_data+').png', 'rb') as file:

                    file_data = file.read(SIZE)
                    while file_data:
                        conn.send(file_data)
                        file_data = file.read(SIZE)
                conn.send(b"%IMA%")


            connected = False
            conn.close()

if __name__ == "__main__":
    main()
