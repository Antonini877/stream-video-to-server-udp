import socket
import pickle
import cv2
import numpy as np


def main():
    clients = []
    while 1:
        so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        so.bind(("", 555))
        c ,received_package = so.recvfrom(20000) #receive the package from the host
        formatted_package = np.array(pickle.loads(received_package)) #format to matrix
        cv2.imshow("stream", cv2.resize(formatted_package, (960, 540))) #show frame
        cv2.waitKey(2)



if __name__ == '__main__':
    main()