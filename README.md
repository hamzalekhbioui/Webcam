
Webcam Capture 

Features
Captures live video feed from the webcam.
Displays the live video feed in a window.
Closes the video feed window when the 'Esc' key is pressed.
Technologies Used
Python: Programming language for the application.
OpenCV: Library used for capturing and displaying video.
Installation
Clone the repository:

bash
Copier le code
git clone https://github.com/your-username/your-repository.git
cd your-repository
Install dependencies:

bash
Copier le code
pip install opencv-python
Run the script:

bash
Copier le code
python webcam_capture.py
Usage
Run the script using the command mentioned above.
View the webcam feed in the window that pops up.
Press the 'Esc' key to stop the webcam and close the window.
How It Works
The script uses OpenCV to:

Access the webcam using cv2.VideoCapture().
Continuously read frames from the webcam.
Display each frame in a window using cv2.imshow().
Close the window and release the webcam resources when the 'Esc' key is pressed.
License
This project is licensed under the MIT License. Feel free to use and modify it as per your needs.

Contributing
If you'd like to contribute to this project, feel free to submit a pull request or open an issue with your suggestions.

