import xmltodict
import pprint
import os
import sys
import platform
from pydub import AudioSegment
from pydub.playback import play
import parsing_functions as pf

eaf_file = sys.argv[1]
python_version = int(platform.python_version()[0])
with open(eaf_file) as file_obj:
    eaf_obj = xmltodict.parse(file_obj.read())

"""
time_order_slots returns an OrderedDict with with two TIME_SLOT_ID's
    as well as, the TIME_VALUE for each TIME_SLOT_ID.

tier_elements returns an OrderedDict with TIER_ID, ANNOTATION_ID, TIME_SLOT_REF1,
    TIME_SLOT_REF2, ANNOTATION_VALUE of each tier (e.g., cut, bookmark)
"""

valid_input = True
time_order_slots = eaf_obj['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']
tier_elements = eaf_obj['ANNOTATION_DOCUMENT']['TIER']
all_TIER_ID_names = pf.get_unique_TIER_ID(tier_elements)

tier_name_prompt = 'Enter a tier name: '
tier_name_input = pf.py_version_input(python_version, tier_name_prompt)



"""
if statement checks the input with of all TIER_ID names
    else, it prints the TIER_ID's available

time_id_and_value holds values of TIME_SLOT_ID and TIME_VALUE

tier_idx_number is the number associated with the TIER name

annotation_objs holds annotations in a tier

final_product is a nested dictionary containing all the annotation values of a tier
"""

while(valid_input):
    if tier_name_input in all_TIER_ID_names:
        print("\nProcess the results for [%s" %tier_name_input + "] tier\n")

        time_id_and_value = pf.extract_TIME_ID_and_VALUE(time_order_slots)
        tier_idx_number = all_TIER_ID_names.index(tier_name_input)
        annotation_objs = tier_elements[tier_idx_number]['ANNOTATION'] # maybe turn into function
        final_product = pf.extract_ANNOTATION_values(annotation_objs, time_id_and_value)

        pprint.pprint(final_product)

        select_diff_tier = 'Would you like to select another tier? (y = yes , n = no): '
        tier_response = pf.py_version_input(python_version, select_diff_tier)

        if(tier_response == 'y'):
            tier_name_input = pf.py_version_input(python_version, tier_name_prompt)
            continue
        else:
            valid_input = False
            break

        # save final_product to disk?

    else:
        pf.no_valid_results(all_TIER_ID_names)
        tier_name_input = pf.py_version_input(python_version, tier_name_prompt)

        if(tier_name_input == '0'):
            sys.exit()

        continue


# silence_segments function works.  Next, you need find a way to use your modify_filename function and export the
#   .wav file

silence_this_wav = input('\nDrag the .wav file here if you\'re ready to silence the audio or enter \'n\' to exit: ')
if(silence_this_wav == 'n'):
    sys.exit()

wav_object = AudioSegment.from_wav(silence_this_wav.strip())
silenced_wav_obj = pf.silence_segments(final_product,wav_object)
new_full_pathname = pf.modify_filename(silence_this_wav.strip())

print('\n==== ! Silencing Process Finished ! ====\n')

# silenced_wav_obj.export(new_full_pathname, format='wav')


# silence_audio_prompt = 'Would you like to silence the audio? (y = yes , n = no): '
# silence_audio_answer = pf.py_version_input(py_version, silence_audio_prompt)
# if(silence_audio_prompt == 'y'):
#     wav_object = AudioSegment.from_wav('/users/curt/desktop/real_sound.wav')
#     final_sound = pf.silence_segments(final_product,wav_object)
#     # play(final_sound)
# else:
#     sys.exit()

# file_obj.close()


'''
This last part we need to export our wave object to a wav file.
'''
# another_list.export('final_sound.wav', format='wav')

# check if user input , then error message, these are the 4 available
#
# check user input with this list
# run code if it passes
# then get_TIER
# just a test change

# Suggestions for improvement ---------------------

'''
# Maybe you can try and limit or make it more convenient for the user
#   by providing a list of tier names depending on the file they provide
# Or you can also provide an option for them to type it in
# for ex:
#   Enter a tier name or choose a number from the following selection:
#   1) cut
#   2) bookmark
#   0) exit


'''













































#
