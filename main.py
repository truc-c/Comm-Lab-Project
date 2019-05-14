import xmltodict
import pprint
import parsing_functions
import os
with open('0204_000609_uclacurt_vetting.eaf') as fd:
    doc = xmltodict.parse(fd.read())

'''
List of all TIERs, each one can be accessed by indexing followed by
keys() and values() function
'''
list_of_TIER_objs = doc['ANNOTATION_DOCUMENT']['TIER']

'''
List of all TIME_SLOTs, each can be accessed by indexing followed
by keys() and values() function
'''
list_of_TIME_SLOT_objs = doc['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']

'''
Ask user for for name of TIER (e.g. cut, bookmark)
'''
user_input_tier_name = raw_input('Enter a tier name: ')

'''
all_TIER_ID_names contains a list of TIER_ID names
'''
all_TIER_ID_names = parsing_functions.get_unique_TIER_ID(list_of_TIER_objs)

# Maybe you can try and limit or make it more convenient for the user
#   by providing a list of tier names depending on the file they provide
# Or you can also provide an option for them to type it in
# for ex:
#   Enter a tier name or choose a number from the following selection:
#   1) cut
#   2) bookmark
#   0) exit

'''
This if-else statement checks the users input with list of all
  TIER_ID names

If the input is valid then the program will run
  else, an error message will appear providing a list of names
  of available TIERs
'''
if user_input_tier_name in all_TIER_ID_names:
    print("Process the results for [%s" %user_input_tier_name + "] tier")

    '''
    time_id_and_value_dict is a dictionary that contains
        the values of TIME_SLOT_ID and TIME_VALUE
    '''
    time_id_and_value_dict = parsing_functions.extract_TIME_ID_and_VALUE(list_of_TIME_SLOT_objs)

    '''
    tier_idx_number is the number associated with the TIER name
        prompted by the user
    '''
    tier_idx_number = all_TIER_ID_names.index(user_input_tier_name)

    '''
    list_of_ANNOTATIION_objs contains all ANNOTATIONS to a
        specific TIER
    '''
    list_of_ANNOTATIION_objs = list_of_TIER_objs[tier_idx_number]['ANNOTATION'] # maybe turn into function

    '''
    final_product is a nested dictionary containing all the ANNOTATION
        values
    '''
    final_product = parsing_functions.extract_ANNOTATION_values(list_of_ANNOTATIION_objs, time_id_and_value_dict)
    # pprint.pprint(final_product)

    # save final_product to disk

else:
    parsing_functions.no_valid_results(all_TIER_ID_names)
#
# print('annotation_id =',final_product['a11'])
# print('start time =',final_product['a11']['start_cut_value'])
# print('end time =',final_product['a11']['end_cut_value'])

# check if user input , then error message, these are the 4 available
#
# check user input with this list
# run code if it passes
# then get_TIER
# just a test change

import subprocess
import time
import pyautogui
# 1. you can also look for and open for the .wav file
#   for ex: open -a Audacity /Users/curt/desktop/my_test.wav
# Here we are send a command to terminal to open our file
#   with Audacity
# -a allows us to open Audacity without having to navigate to
#   the apps location

# subprocess.call(['open','-a','Audacity'])

# or

# wav_location = '/Users/curtchang/desktop/eaf_files/0204_000609/0204_000609.wav'
# # my_wav = '/Users/curt/desktop/my_test.wav'
# subprocess.call(['open','-a','Audacity',my_wav])
# pyautogui.PAUSE = 3.0
# # 2. wait for a bit while Audacity opens and loads
# # time.sleep(5)
# # pyautogui.PAUSE = 5.0
# x,y = pyautogui.position()
# print(x,y)
# pyautogui.PAUSE = 3.0
# pyautogui.moveTo(1221,701)
# pyautogui.PAUSE = 3.0
# pyautogui.click()
# pyautogui.PAUSE = 3.0
#
# # 3. then select ok
# #
# pyautogui.press('enter')

# 4. Use bracket keys to select left and right selection boundaries
#   for silencing
# enter left bracket key and push left arrow once, enter the time,
#   then hit ok

# enter right bracket key and push left arrow once, enter the time,
#   then hit ok

# enter cmd+l to silence the selection

# repeat until you've silenced all parts of the audio
#
# pyautogui.press('enter')
# pyautogui.PAUSE = 7.0
# # 4. Use bracket keys to select left and right selection boundaries
# #   for silencing
# # enter left bracket key and push right arrow once, enter the time,
# #   then hit ok
# # Enter right bracket key and push right arrow once, enter the time,
# #   then hit ok
#
# pyautogui.press(['[','right'])
# print(final_product['a11']['start_cut_value'],final_product['a11']['end_cut_value'])
time = final_product['a11']['start_cut_value']
seconds_format = str(time)
seconds_to_convert = seconds_format[:-3]
convert_this = int(seconds_to_convert)
import time
result = time.strftime('%H:%M:%S',time.gmtime(convert_this))
print(result)       # result is a string
hours = result[:2]
minutes = result[3:5]
seconds = result[6:]
print(hours, minutes, seconds)
# print(seconds_format[:-3])



# import datetime
# print(datetime.timedelta(seconds=))

# hours =
# minutes =
# seconds =


# enter right bracket key and push left arrow once, enter the time,
#   then hit ok

# enter cmd+l to silence the selection

# repeat until you've silenced all parts of the audio
#pyautogui.press('enter')





























#
