# Auto Anki
Open source Anki (language flash card app) automation bot. You are setting words and meanings for Anki in a text file and bot is writing them down in it.

This bot is working with clicking relevant places on screen instead of you. 
What that means is you should set specific pixel locations for every single click to achieve actions.

## For Someone Who Is A Beginner

If you have already Python and VS Code on your computer and you can run apps with Python in VS Code, scroll to the <a href="https://github.com/aktasburaken/auto-anki#everyone"><strong>Everyone</strong></a> topic.

Firstly, <a href="https://code.visualstudio.com">download VS Code</a> on your computer.

Then, <a href="https://www.python.org/downloads/">download Python</a> too.

## Everyone

You should set a specific location for your Anki's adding card page and VS Code on your screen. 

There is config part in the code.

<img width="236" alt="Screen Shot 2023-01-22 at 21 50 46" src="https://user-images.githubusercontent.com/86871383/213934216-508e5563-261c-4fc5-9211-67c4265352ef.png">

Before learning what are these configurations mean, we need to understand <strong>deck configs'</strong> variables with px (All of them ^^). Because you need to reassign these variables one by one according to your monitor and location of the both apps <strong>(If you have 1920x1080px monitor and using the apps as the picture below, you don't need to set the px variables again)</strong>.

<img src="https://user-images.githubusercontent.com/86871383/210191278-52283596-8a43-447b-a39d-2d4793ed0c5b.png" width="800" />

### Finding Position

If you saw, there was a file named "find_position.py" in our code. If you are setting your px configurations first time or again, use it to find declared button's x and y coordinates on your screen. You should open the file in your VS Code and then run the python code (showed below). 

<img width="503" alt="Screen Shot 2023-01-22 at 21 53 02" src="https://user-images.githubusercontent.com/86871383/213934344-d3c3718c-c7c5-4d6d-b638-7664cda76142.png">

You should put your mouse on whatever you want in three seconds to get the certain x and y coordinates of that pixel. You can see the pixels on your terminal (showed below). 

<img width="439" alt="Screen Shot 2023-01-22 at 21 56 10" src="https://user-images.githubusercontent.com/86871383/213934493-1018c3bd-313b-4409-a60d-84e74647b2e0.png">

Let's say these coordinates were the coordinates for front_field_px variable. Then, you should write these coordinates with [x,y] format (showed below). 

<img width="171" alt="Screen Shot 2023-01-22 at 21 59 33" src="https://user-images.githubusercontent.com/86871383/213934619-8fdbbc3c-36d4-4fb2-b866-8c84795deda2.png">

Don't forget that, if you don't want to change all deck config part of your code every single time before using <strong>Auto Anki</strong>, ensure you are preserving location of the both apps VS Code and Anki, also using same monitor.

## What do all configurations mean?

| Config      | Description       |
| ------------- | ------------- |
| isMac  | If you are using mac, set this true.  |
| isGerman  | If your words are German, there are some specifications like coloring der, die, and das artikels.  |
| seperator | Which symbol is going to seperate your words, default " - ". You should set seperator with spaces if you don't want to see unneccessary spaces in your code. |
| card_file_name | This is the word file's name. |
| card_file | This code assign the file to this variable in read mode. |
| word_part_range | If your words are in "english - french" format, that means you should write two as range. For "english - french - turkish" you should write three |
| delay | Delay seconds for mouse clicks. Zero can causes bugs sometime so one is recommended." |

| Anki Click Config | Pixel Description |
| ------------- | ------------- |
| front_field_px | Front card click. |
| back_field_px | Back card click. |
| add_field_px | Add button click. |
| color_ok_button_px | Okay button click. |
| set_color_px (For German) | For german, opens color picker. |
| choose_color_px (For German) | Picker for current color. |
| color_red/green/blue_px (For German) | You should set specific pixels for every single color. |






