import cv2
import os
import string
import subprocess


img = cv2.imread("Source_Image.jpeg")  


msg = input("Enter secret message: ")
password = input("Enter a passcode: ")


d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}


m, n, z = 0, 0, 0


for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n += 1
    m += 1
    z = (z + 1) % 3


cv2.imwrite("encryptedImage.jpg", img)


subprocess.run(["xdg-open", "encryptedImage.jpg"])


message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT authorized")

