import socket
import time
import cv2
import pickle
from PIL import Image

stream_time = 30 #time which the video will be transmitted to the server, 30 seconds
cap = cv2.VideoCapture(0)
start_time = time.time()
ip = "127.0.0.1" #local address
port = 555
while 1:
    if time.time()-start_time>=stream_time: break
    frame = cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY) #capture the frame
    frame = Image.fromarray(frame)

    resized_frame = frame.resize((32,32), resample=Image.BILINEAR) #resize the frame to fit in the package

    pickled_frame = pickle.dumps(resized_frame) #transform the image matrix in binary
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #ipv4 and udp protocol respectively
    address = (ip, port)
    client.sendto(pickled_frame, address) #send the frame matrix to the specified address
