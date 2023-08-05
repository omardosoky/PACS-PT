from tkinter import *
from tkinter import filedialog
import socket
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import io

PORT = 7510
client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((socket.gethostname(), PORT))
BufferSize= 1024*500000


BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="Welcome", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        # bottom label
        bottom_label1 = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label1.place(relwidth=1, rely=0.825)
        # message entry box
        self.msg_entry = Entry(bottom_label1, bg="#2C3E50", fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        # send button
        send_button = Button(bottom_label1, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.001, relheight=0.03, relwidth=0.22)
        # upload button
        upload_button = Button(bottom_label1, text="upload", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self.upload())
        upload_button.place(relx=0.77, rely=0.03, relheight=0.03, relwidth=0.22)
        self.connected = True

    
    # sending an image to server
    def upload(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("jpeg files", ".jpg"), ("all files", ".*")))
        with open(filename, 'rb') as file:
            file_data = file.read(BufferSize)
            while file_data:
                client.send(file_data)
                file_data = file.read(BufferSize)
        client.send(b"%finish%")

        while self.connected:
            file_stream = io.BytesIO()
            recv_data = client.recv(BufferSize)
            while recv_data:
                recv_data = recv_data.decode('UTF-8')
                self._insert_message(recv_data, "")


        
    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "")

        # id which is sent to server 
        client.send(msg.encode('UTF-8'))
        # receiving and displaying the requested image and saving the image in clientimage folder
        with open('./clientimage/mri (4).png','wb')as file:
            recv_data=client.recv(BufferSize)
            while recv_data:
                file.write(recv_data)
                recv_data=client.recv(BufferSize)
                if recv_data == b"%finish%":
                   break
                img = mpimg.imread('./clientimage/mri (4).png')
                imgplot = plt.imshow(img)
                plt.show()




    def _insert_message(self, msg, sender):
        if not msg:
            return
        self.msg_entry.delete(0, END)
        msg1 = f"{sender} {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.configure(state=NORMAL)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.see(END)


             
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()