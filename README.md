# Auto Anki
Open source Anki (language flash card app) automation bot. You are setting words and meanings for Anki in a text file and bot is writing them down in it.

This bot is working with clicking relevant places on screen instead of you. 
What that means is you should set specific pixel locations for every single click to achieve actions.

## For Someone Who Are A Beginner

If you have already Python and VS Code on your computer and you can run apps with Python in VS Code, scroll to the <strong>Everyone</strong> topic.

Firstly, <a href="https://code.visualstudio.com">download VS Code</a> on your computer.

Then, <a href="https://www.python.org/downloads/">download Python</a> too.

## Everyone

You should set a specific location for your Anki's adding card page and VS Code on your screen. 

There is config part in the code.

<img src="https://user-images.githubusercontent.com/86871383/210197768-905c4c0c-7c08-4dd3-8554-d5fbf247447b.png" width="800" />

Before learning what are these configurations mean, we need to understand <strong>deck configs'</strong> variables with px (All of them ^^). Because you need to reassign these variables one by one according to your monitor and location of the both apps <strong>(If you have 1920x1080px monitor and using the apps as the picture below, you don't need to set the px variables again)</strong>.

<img src="https://user-images.githubusercontent.com/86871383/210191278-52283596-8a43-447b-a39d-2d4793ed0c5b.png" width="800" />

### Finding Position

If you saw, there was a file named "find_position.py" in our code. If you are setting your px configurations first time or again, use it to find declared button's x and y coordinates on your screen. You should open the file in your VS Code and then run the python code (showed below). 

<img src="https://user-images.githubusercontent.com/86871383/210199003-8e93d5a1-23c3-4be0-aeb5-d9f0fbac7c03.png" width="400" />

You should put your mouse on whatever you want in three seconds to get the certain x and y coordinates of that pixel. You can see the pixels on your terminal (showed below). 

<img src="https://user-images.githubusercontent.com/86871383/210199277-cdac661a-c74b-4362-ae71-89852b1cfc21.png" width="400" />

Let's say these coordinates were the coordinates for front_field_px variable. Then, you should write these coordinates with [x,y] format (showed below). 

<img src="https://user-images.githubusercontent.com/86871383/210199622-c3a4493a-fdfa-4219-9274-37d4ac084334.png">

Don't forget that, if you don't want to change all deck config part of your code every single time before using <strong>Auto Anki</strong>, ensure you are preserving location of the both apps VS Code and Anki, also using same monitor.

### What do all configurations mean?
