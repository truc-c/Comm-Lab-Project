import xmltodict
import pprint
import parsing_functions
import time
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
import pyautogui
# 1. you can also look for and open for the .wav file
#   for ex: open -a Audacity /Users/curt/desktop/my_test.wav
# Here we are send a command to terminal to open our file
#   with Audacity
# -a allows us to open Audacity without having to navigate to
#   the apps location


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
# pyautogui.press('enter')

# pyautogui.press('enter')
# pyautogui.PAUSE = 7.0

# This is an idea
my_tuple_list = ()
for i in final_product:
    start_end_value_pairs = (final_product[i]['start_cut_value'],final_product[i]['end_cut_value'])
    my_tuple_list = my_tuple_list + (start_end_value_pairs,)
#
# count = 0
#
while count < len(my_tuple_list):
    pass

    count += 1

# full_time = time.strftime('%H:%M:%S',time.gmtime(str_result))

print(my_tuple_list[0])
start_time = str(my_tuple_list[0][0])
end_time = str(my_tuple_list[0][1])
print('start:'+ start_time)
print('end:'+ end_time)

# We need to hold on to the mili seconds until later when we add it on to
#   part of our list that we will use in the press() function
start_time_mili = start_time[-3:]
end_time_mili = end_time[-3:]
print('start mili:'+start_time_mili)
print('end mili:'+end_time_mili)

# We will use these seconds for the time converting function
# We also need to convert it back to an int in order for it to work with
#   the converting function
start_convert = int(start_time[:-3])
end_convert = int(end_time[:-3])

# Now we have convert seconds to hours, minutes, seconds
start_result = time.strftime('%H:%M:%S',time.gmtime(start_convert))
end_result = time.strftime('%H:%M:%S',time.gmtime(end_convert))
print('start (hh:mm:ss) - ' + start_result)
print('end (hh:mm:ss) - ' + end_result)

# Lets remove the colons (:) from our results
start_result = start_result.replace(':','')
end_result = end_result.replace(':','')
print('start (removed colons) - ' + start_result)
print('end (removed colons) - '+ end_result)

# Let's create our list that we are going to use with the press() function
start_press_list = []
for i in start_result:
    start_press_list.append(i)

end_press_list = []
for i in end_result:
    end_press_list.append(i)

print('start (press list) - ' ,start_press_list)
print('end (press list) - ' ,end_press_list)

# Now let's add our mili-seconds to the end of our list
for i in start_time_mili:
    start_press_list.append(i)

for i in end_time_mili:
    end_press_list.append(i)

print('start final product = ', start_press_list)
print('end final product = ', end_press_list)





# pyautogui.press(['[','right'])
































#
