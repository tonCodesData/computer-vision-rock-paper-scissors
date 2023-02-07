# Computer Vision RPS
# MIlestone 2: 
Created a computer vision system, or model using Teachable-Machine website. On the website I created 4 classes: 'none' class with just my pictures. Then I trained 3 classes, rock, paper, and scissors, with images of yourself showing each option to the camera. The "None" class represents the lack of option in the image. 

Downloaded the model from the "Tensorflow" tab in Teachable-Machine. 

The files contain the structure and the parameters of a deep learning model. They are not files that can be run, and they do not contain anything readable if you look inside. Pushed the model and labels to my GitHub repository after committing.

# MILESTONE 4: 
Plays the game without the camera.
Randomly chooses an option (rock, paper, or scissors) and then asks the user for an input.
Use the random module to pick a random option between rock, paper, and scissors and the input function to get the user's choice.

First created two functions: get_computer_choice and get_user_choice.

In the get_computer_choice function, a randomly picked option between "Rock", "Paper", and "Scissors" is returned as the choice.
The get_user_choice function asks the user for an input and returns it.
Using if-elif-else statements, the script chooses a winner based on the classic rules of Rock-Paper-Scissors.

Then wraped in a function called get_winner to print the winner. This function takes two arguments: computer_choice and user_choice.

If the computer wins, the function should print "You lost", if the user wins, the function should print "You won!", and if it's a tie, the function should print "It is a tie!".

All of the code programmed so far relates to one thing: running the game - so wraped it all in one function.

Created and called a new function called play.
Inside the function, it calls all the other three functions created so far (get_computer_choice, get_user_choice, and get_winner)
