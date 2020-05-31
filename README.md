# Graduation-Project
## Env: Python3.6 + OpenCV3.4.7 + PyQt5
### a man-machine interactive system based on gesture recognition.

This project refers to the works of many authors on the Internet, and I would like to express my gratitude.

Run the main.py, then you can use the system. Before use it, You can read the manual by clicking the 'Help' option in the menu bar. 
The detect_hand.py is about skin color detection, gesture_svm.py is the SVM training model and save the best model as gestureLib/svm_train_model.m. The model can recognition the gesture 1 to 10.
The main window load the model by the sklearn.joblib.

Notes on gesture:
1.'one': Stick out your index finger.

2.'two': Stick out your index and middle fingers.

3.'three': Stick out your little finger, ring finger and middle finger.

4.'four': Stick out all fingers other than thumb.

5.'five': Stick out all fingers.

6.'six': Stick out your thumb and little finger.

7.'seven': Stick out your thumb, index finger and little finger.

8.'eight': Stick out your thumb and index finger.

9.'nine': Stick out your index finger and little finger.

10.'ten': Clenched fist.
