# For sending requests as json
import requests
import json

# for encoding/decoding images
import cv2
import base64

# utility
import sys
import os
import io

# for displaying the returned image from server
import matplotlib.pyplot as plt

#for saving Image
from PIL import Image


def display_image(image):
    fig = plt.figure(figsize=(20, 15))
    plt.grid(False)
    plt.imshow(image)
    plt.show()

# takes in image path, sends encoded image as json to backend then decodes and displays the resultant image


def main():
    if len(sys.argv) != 1:
        print('Usage: python tool.py')
        return
    user_exit = False
    while not user_exit:
        #Obtain image path from user, load and encode the image using base64. 
        path = input('Enter image path:')
        image_path = os.path.abspath(path)
        img = cv2.imread(image_path)
        string = base64.b64encode(cv2.imencode('.jpg', img)[1]).decode()
        data = {'image': string}
        #Make a POST request to the client, with the encoded image as a json object
        url = 'http://127.0.0.1:5000/' #change URL here to match what is shown in app.py window
        r = requests.post(url, json=data)
        if r.json()['time']:
            print('Inference time: ', r.json()['time'])
        if r.json()['image']:
            result = r.json()['image']
            result = base64.b64decode(str(result))
            display_image(Image.open(io.BytesIO(result)))
        
        #check if user wants to save image
        resp = input('Would you like to save the image? [y/n]')
        valid_resp = resp in ['y', 'n']
        while not valid_resp:
            resp = input('Would you like to save the image? [y/n]')
            valid_resp = resp in ['y', 'n']
        #image saving functionality
        if resp == 'y':
            name = input('Enter your desired image name (without file extension):')
            with open(name + '.jpg', 'wb') as f:
                f.write(result)
        #check if user wants to enter another image
        resp = input('Enter another image? [y/n]')
        valid_resp = resp in ['y', 'n']
        while not valid_resp:
            resp = input('Enter another image? [y/n]')
            valid_resp = resp in ['y', 'n']
        if resp == 'n':
            user_exit = True
            print('Bye!')


if __name__ == '__main__':
    main()
