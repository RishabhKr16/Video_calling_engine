from vidstream import *
import tkinter as tk
import socket
import threading
import requests

local_ip_adress = socket.gethostbyname(socket.gethostname())
server = StreamingServer(local_ip_adress, 9999)
reciever = AudioReceiver(local_ip_adress, 8888)

def start_listening():
    t1 = threading.Thread(target=server.start_server)
    t2 = threading.Thread(target=reciever.start_server)
    t1.start()
    t2.start()

def start_Camerastream():
    camera_client = CameraClient(text_target_ip.get("1.0", 'end-1c'), 7777)
    t3 = threading.Thread(target=camera_client.start_stream)
    t3.start()

def start_ss():
    ss_client = SSClient(text_target_ip.get("1.0", 'end-1c'), 7777)
    t4 = threading.Thread(target=ss_client.start_stream)
    t4.start()

def start_audio():
    audio_client = AudioClient(text_target_ip.get("1.0", 'end-1c'), 7777)
    t5 = threading.Thread(target=audio_client.start_stream)
    t5.start()       

# GUI
window = tk.Tk()
window.title("vidletter v1 alpha")
window.geometry('300x200')
 
local_target_ip = tk.Label(window, text="target ip:")
local_target_ip.pack()

text_target_ip = tk.Text(window, height=2)
text_target_ip.pack()

button_listen = tk.Button(window, text="Start listening", width=50, command=start_listening)
button_listen.pack(side=tk.TOP, expand=True)

button_camera = tk.Button(window, text="Start camera", width=50, command=start_Camerastream)
button_camera.pack(side=tk.TOP, expand=True)

button_audio = tk.Button(window, text="Start Audio", width=50, command=start_audio)
button_audio.pack(side=tk.TOP, expand=True)

button_ss = tk.Button(window, text="Start ss", width=50, command=start_ss)
button_ss.pack(side=tk.TOP, expand=True)

window.mainloop()

