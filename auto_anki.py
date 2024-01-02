import pyautogui as events
import time
import ftfy as text_corrector
import keyboard

word_array = []

### Config ###
isMac = True
isGerman = True
seperator = " - "
card_file_name = "word_file.txt"
card_file = open(card_file_name, "r")
word_part_range = 4
delay = 0.5

## Deck Config ##
front_field_px = [207, 208]
back_field_px = [721, 283]
add_field_px = [132, 542]
color_ok_button_px = [654, 516]
set_color_px = [366, 136]
choose_color_px = [351, 135]
color_red_px = [115, 406]
color_green_px = [147, 406]
color_blue_px = [90, 406]

## Functions ##


def setFrontWord(word, isGermanNoun):
    events.click(front_field_px[0], front_field_px[1])
    keyboard.write(word)
    if isGerman and isGermanNoun:
        setWordColor()


def writeMeaning(word):
    events.click(back_field_px[0], back_field_px[1])
    keyboard.write('{}, '.format(word))

# German Spesific Functions #


def setWordColor():

    key = 'ctrl'

    if isMac:
        key = 'command'

    time.sleep(delay)
    events.hotkey(key, 'a')
    events.click(choose_color_px[0], choose_color_px[1])


def setCurrentColor(type):
    events.click(set_color_px[0], set_color_px[1])
    time.sleep(delay)
    if type == 'der ':
        events.click(color_blue_px[0], color_blue_px[1])
    if type == 'das ':
        events.click(color_green_px[0], color_green_px[1])
    if type == 'die ':
        events.click(color_red_px[0], color_red_px[1])
    time.sleep(delay)
    events.click(color_ok_button_px[0], color_ok_button_px[1])


### Word Array Preparing ###
for card in card_file:
    splitted_array = card.split(seperator)
    last_one_corrected_splitted_array = []

    if word_part_range == 2:
        last_one_corrected_splitted_array = [
            text_corrector.fix_text(splitted_array[0]),
            text_corrector.fix_text(splitted_array[1].rsplit("\n")[0])]

    if word_part_range == 3:
        last_one_corrected_splitted_array = [
            text_corrector.fix_text(splitted_array[0]),
            text_corrector.fix_text(splitted_array[1]),
            text_corrector.fix_text(splitted_array[2].rsplit("\n")[0])]
        
    if word_part_range == 4:
        last_one_corrected_splitted_array = [
            text_corrector.fix_text(splitted_array[0]),
            text_corrector.fix_text(splitted_array[1]),
            text_corrector.fix_text(splitted_array[2]),
            text_corrector.fix_text(splitted_array[3].rsplit("\n")[0])]


    word_array.append(last_one_corrected_splitted_array)

# To check the word_array
# print(word_array)
# time.sleep(5)

### Deck Writer Bot ###
for word in word_array:
    for index in range(word_part_range):
        current_word = word[index]
        isGermanNoun = isGerman and (
            'der ' == current_word[:4] or 'die ' == current_word[:4] or 'das ' == current_word[:4])
        if index == 0:
            if isGermanNoun:
                setCurrentColor(current_word[:4])
            setFrontWord(current_word, isGermanNoun)
            time.sleep(delay)
            continue
        writeMeaning(current_word)
        time.sleep(delay)
    events.click(add_field_px[0], add_field_px[1])
    time.sleep(delay)
