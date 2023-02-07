import cv2
from keras.models import load_model
import numpy as np

def get_prediction():
    # returns output of the model created earlier
    # model output = [probablity1, probability2]
    # pick the highest probaility class
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    
    prediction = model.predict(data)

    choices = ["Rock", "Paper", "Scissors", "Nothing"]
    highest_prob = 0
    highest_idx = 0
    for i in range(len(prediciton)): 
        if prediction[i] > highest_prob:
            highest_prob = prediction[i]
            highest_idx = i
    
    predicted_choice = choices[highest_idx]
    return predicted_choice


    
    
    
        
        



    


