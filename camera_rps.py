import cv2
from keras.models import load_model
import numpy as np
import time

def get_prediction():
    # returns output of the model created earlier
    # model output = [probablity1, probability2]
    # pick the highest probaility class
    model = load_model('keras_model.h5')
    time.time()
    TIMER = 3
    cap = cv2.VideoCapture(0)
    # we can specify the countdown timer 
    ## First, we will be setting the initial value of Countdown timer in second. 
    # SET THE COUNTDOWN TIMER
    # for simplicity we set it to 3
    # We can also take this as input
    TIMER = 3
    ## Open the camera and create a video Capture object using cv2.VideoCapture().
    # Open the camera
    cap = cv2.VideoCapture(0)

    ## While camera is open
    while True:
    ### We will read each frame and display it using cv2.imshow().      
        # Read and display each frame
        ret, img = cap.read()
        cv2.imshow('a', img)

    # whenever the particular key will be pressed (let’s say q) 
    ### Now we will set a key (we use q ) for the countdown to begin.
    ### As soon as this key will be pressed, we will start the Countdown.
        # check for the key pressed
        k = cv2.waitKey(125)

        # set the key for the countdown
        # to begin. Here we set q
        # if key pressed is q
        if k == ord('q'):
            ### We will be keeping track of countdown with the help of time.time() function 
            prev = time.time()

            while TIMER >= 0:
                ret, img = cap.read()

    # the countdown timer will be started and we will be displaying the countdown on our camera with the help of cv2.putText() 
    ### and display the countdown on the video using cv2.putText()  function.
                # Display countdown on each frame
                # specify the font and draw the
                # countdown using puttext
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, str(TIMER), 
                            (200, 250), font,
                            7, (0, 255, 255),
                            4, cv2.LINE_AA)
                cv2.imshow('a', img)
                cv2.waitKey(125)
                # current time
                cur = time.time()

                # Update and keep track of Countdown
                # if time elapsed is one second 
                # then decrease the counter
                if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER-1

            else:
    # when it reaches zero we will capture the image, 
                ret, img = cap.read()
                cv2.imshow('a', img)
                # display the captured image for fixed number of seconds (according to our need )  
                # Display the clicked frame for 2 sec. You can increase time in waitKey also
                # time for which image displayed
                cv2.waitKey(2000)

    ### we will copy the current frame and write the current frame at desired location on disk 
    ### by using cv2.imwrite() function.  
    # write/save the image on disk. 
                # Save the frame
                cv2.imwrite('camera.jpg', img)

                # HERE we can reset the Countdown timer
                # if we want more Capture without closing
                # the camera
    ### On pressing ‘Esc’ we will close the camera.  
        # Press Esc to exit
        elif k == 27:
            break

    # close the camera
    cap.release()

    # close all the opened windows
    cv2.destroyAllWindows()

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)      
    resized_frame = cv2.resize(img, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    # ind = np.unravel_index(np.argmax(prediction, axis=None), prediction.shape)
    # print(ind)
    highest_idx = np.argmax(prediction) 
    print(highest_idx)
    # print(prediction[ind])
    choices = ["Rock", "Paper", "Scissors", "Nothing"]
    predicted_choice = choices[highest_idx]
    return predicted_choice

print(get_prediction())
