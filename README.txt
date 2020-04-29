Device Detector - Server & Client Setup

Description:
The client (client.py) takes in an image path, reads the image and is base64 encoded to a string. This is then POSTed to the backend (app.py) where the object detection model is run. Bounding boxes are drawn onto the image and the image is once again encoded and sent as a json as the response from the API call. The client then decodes this image, and displays it using matplotlib. The may then choose to save the result.


*The commands mentioned below are for Windows.

Preparation:
1) Ensure that you have pip and python (3.7) on your computer

2) Install virtualenv (pip install virtualenv) if you wish to create an venv for this

3) Open cmd prompt and navigate to this directory. Type python -m venv env (which creates a virtual environment for this directory)

4) Activate the venv (.\env\Scripts\activate)


Instructions:
1) Install the required packages in requirements.txt (pip install -r requirements.txt)

2) Open app.py (the server)

3) Check if the url variable in client.py matches what is shown in the app.py cmd window. (Change it if it isn't)

4) Run client.py. This should open a cmd window which prompts you to 'enter image path' once the packages are loaded.

5) Enter the image path and press enter. In the client.py window, you should see the message 'interpreting image'. (You can test this by entering test.jpg and test2.jpg as the image path)

6) Once interpretation is complete, a window should pop up showing the image with bounding boxes (if any devices were detected). The interpretation time is also shown in the client window.
*Note that bounding boxes will only appear if devices are detected.

7) Close the image window. The client will give you the option of saving the result. If yes, enter the name you wish to save the image as. 

8) If no, the client will ask if you want to enter another image path, and it will proceed to repeat the process if you do.

9) Otherwise, the client will exit.