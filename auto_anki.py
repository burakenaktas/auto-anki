import pyautogui as events
import time
import ftfy as text_corrector
import keyboard

### Config ###
isEnglish = True  # If it is not English that means it is German
seperator = " - "
card_file_name = "english_file.txt" if isEnglish else "german_file.txt"
card_file = open(card_file_name, "r")
word_array = []
word_count = 40
word_part_range = 2  # how many seperator are there? if x, you should write x + 1 here
# At least 1. If computer can't catch bot's speed, try to increase this.
delay = 1

custom_word_file_px = [1061, 123]
inside_of_custom_word_file_px = [1200, 123]
chatGPT_chat_px = [438, 980]
chatGPT_question = "give me the detailed turkish meanings of following words with english - turkish meaning format without listing it:"
chatGPT_right_click_before_examine = [748, 737]
chatGPT_left_click_examine = [750, 720]
chatGPT_examine_p_click = [459, 526]
chatGPT_examine_p_copy_part = [538, 657]

## Deck Config ##
front_field_px = [893, 154]
back_field_px = [867, 226]
add_field_px = [671, 1054]
set_color_px = [285, 87]
choose_color_px = [269, 87]
color_red_px = [242, 638]
color_green_px = [269, 638]
color_blue_px = [301, 638]
color_ok_button_px = [611, 730]

# time.sleep(3)
# print(events.position())
# time.sleep(10)

## Functions ##

# Common Functions #


def findingMeaning():
    events.click(custom_word_file_px[0], custom_word_file_px[1])
    events.click(
        inside_of_custom_word_file_px[0], inside_of_custom_word_file_px[1])
    events.hotkey('ctrl', 'a')
    events.hotkey('ctrl', 'c')
    time.sleep(1)
    events.click(chatGPT_chat_px[0], chatGPT_chat_px[1])
    events.write(chatGPT_question)
    events.hotkey('ctrl', 'v')
    time.sleep(1)
    events.hotkey('enter')
    time.sleep(120)
    events.rightClick(
        chatGPT_right_click_before_examine[0], chatGPT_right_click_before_examine[1])
    time.sleep(5)
    events.click(chatGPT_left_click_examine[0], chatGPT_left_click_examine[1])
    time.sleep(5)
    events.click(chatGPT_examine_p_click[0], chatGPT_examine_p_click[1])
    time.sleep(1)
    events.click(
        chatGPT_examine_p_copy_part[0], chatGPT_examine_p_copy_part[1])
    for number in range(2):
        events.click(650, 1080)
        time.sleep(1)
        events.click(750, 1000)
    events.click(custom_word_file_px[0], custom_word_file_px[1])
    events.click(
        inside_of_custom_word_file_px[0], inside_of_custom_word_file_px[1])
    events.hotkey('ctrl', 'a')
    events.hotkey('ctrl', 'v')


def setFrontWord(word, isGermanNoun):
    events.click(front_field_px[0], front_field_px[1])
    keyboard.write(word)
    if isEnglish == False and isGermanNoun:
        setWordColor()


def writeMeaning(word):
    events.click(back_field_px[0], back_field_px[1])
    keyboard.write('{}, '.format(word))

# German Spesific Functions #


def setWordColor():
    events.hotkey('ctrl', 'a')
    events.click(choose_color_px[0], choose_color_px[1])


def setCurrentColor(type):
    events.click(set_color_px[0], set_color_px[1])
    time.sleep(1)
    if type == 'der ':
        events.click(color_blue_px[0], color_blue_px[1])
    if type == 'das ':
        events.click(color_green_px[0], color_green_px[1])
    if type == 'die ':
        events.click(color_red_px[0], color_red_px[1])
    time.sleep(1)
    events.click(color_ok_button_px[0], color_ok_button_px[1])


### Custom File Preparing ###
findingMeaning()


### Word Array Preparing ###
for card in card_file:
    splitted_array = card.split(seperator)
    if isEnglish:
        last_one_corrected_splitted_array = [
            text_corrector.fix_text(splitted_array[0]), text_corrector.fix_text(splitted_array[1].rsplit("\n")[0])]
    else:
        last_one_corrected_splitted_array = [
            text_corrector.fix_text(splitted_array[0]),
            text_corrector.fix_text(splitted_array[1]),
            text_corrector.fix_text(splitted_array[2].rsplit("\n")[0])]
    word_array.append(last_one_corrected_splitted_array)

# To check word_array
# print(word_array)
# time.sleep(5)

### Deck Writer Bot ###

for word in word_array:
    for index in range(word_part_range):
        current_word = word[index]
        isGermanNoun = isEnglish == False and (
            'der ' == current_word[:4] or 'die ' == current_word[:4] or 'das ' == current_word[:4])
        if index == 0:
            if isGermanNoun:
                setCurrentColor(current_word[:4])
            setFrontWord(current_word, isGermanNoun)
            time.sleep(1)
            continue
        writeMeaning(current_word)
        time.sleep(1)
    events.click(add_field_px[0], add_field_px[1])


# events.click(color_field_px[0], color_field_px[1])
# events.write(deck_name)
# events.click(ok_button_px[0], ok_button_px[1])
