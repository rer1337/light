import threading
from socket import *
from customtkinter import *

class MainWindow(CTk)
    def __init__(self):
        super().__init__()
        self.geometry('400x300')
        self.label = "Talk"
        self.frame = CTkFrame(self, width=200,height=700)
        self.frame.pack_propagate(False)
        self.frame.configurate(width=0)
        self.frame.place(x=0,y=0)
        self.is_show_menu = False
        self.speed_animate_menu = 5 #-5?
        self.frame_width = 0
        
        self.label = CTkLabel(self.frame, text="nickname")
        self.label.pack(pady=30)
        
        self.entry = CTkEntry(self.frame)
        self.entry.pack()
        
        self.label_theme = CTkOptionMenu(self.frame, values=["Темна", "Світла"], command=self.change_theme)
        self.label_theme.place(x=50,y=100)
        self.theme = None
        self.btn = CTkButton(self, text='>', command=self.toggle_show_menu, width=30)
        self.btn.place(x=0,y=0)
        self.menu_show_speed = 20
        
        self.chat_text = CTkTextbox(self, state='disable')
        self.chat_text.place(x=0,y=30)
        
        self.message_input = CTkEntry(self, placeholder_text="msg")
        self.message_input.place(x=0,y=250)
        
        self.send_button = CTkButton(self, text='>', width=30,height=30)
        self.send_button.place(x=0,y=0)
        
        self.username = 'user'
        try:
            self.sock = socket(AF_INET, SOCK_STREAM)
            self.sock.connect(('localhost, 8080'))
            hello = f"TEXT@{self.username}@SYSTEM {self.username} приєднався до сервера: {e}")
            self.sock.send(hello.encode("utf-8"))
            threading.Thread(target=self.recv_message,daemon = True).start()
        except Exception as e:
            self.add_message(f"Не вдалося підключитися до сервера: {e}")
            
        self.adaptive_ui()
        
    def toggle_show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.speed_animate_menu *= -1
            self.btn.configurate(text='>')
            self.show_menu()
        else:
            self.is_show_menu = True
            self.speed_animate_menu *= -1
            self.btn.configurate(text='<')
            self.show_menu()
            
            self.label = CTkLabel(self.frame, text='name')
            self.label.pack(pady=30)
            self.entry = CTkEntry(self.frame)
            self.entry.pack()
            
    def show_menu(self):
        self.frame.configure(width=self.frame.winfo_width + self.speed_animate_menu)
        if not self.frame.winfo_width() >= 200 and self.is_show_menu:
            self.after(10, self.show_menu)
        elif self.frame.winfo_width() >= 40 and not self.is_show_menu:
            if self.label and self.entry:
                
                
                self.label.destroy()
                self.entry.destroy()
                
    def change_theme(self, value):
        if value == 'dark':
            set_apperance_mode('dark')
        else:
            set_apperance_mode('light')