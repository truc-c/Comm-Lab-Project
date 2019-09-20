# sample branch

import parsing_functions as pf
import xmltodict
import pprint
import sys
import platform
from pydub import AudioSegment

eaf_file = sys.argv[1]
python_version = int(platform.python_version()[0])
with open(eaf_file) as file_obj:
    eaf_obj = xmltodict.parse(file_obj.read())

is_input_valid = True
tier_name_list = pf.get_tier_names(eaf_obj)
tier_name_prompt = 'Enter tier name: '
user_input = pf.py_version_input(python_version,tier_name_prompt)

'''
you may want to consider a function that checks the user input,
    because what if the user wants 'all' tiers and not just a
    specific one.
'''
while(is_input_valid):
    if(user_input in tier_name_list):
        try:
            print("\nProcess the results for [%s" %user_input + "] tier\n")
            time_ids_and_values = pf.extract_timeid_and_value(eaf_obj)
            annotation_values = pf.extract_annotations(eaf_obj,user_input)
            pf.fill_time_values(time_ids_and_values,annotation_values)
            pprint.pprint(annotation_values)
        except:
            print('There are no annotations in the tier: ', user_input)

        diff_tier_prompt = 'Would you like to select another tier? (y = yes , n = no): '
        user_input = pf.py_version_input(python_version,diff_tier_prompt)

        if(user_input == 'y'):
            user_input = pf.py_version_input(python_version,tier_name_prompt)
            continue
        else:
            is_input_valid = False
            break

    else:
        pf.no_valid_results(tier_name_list)
        user_input = pf.py_version_input(python_version, tier_name_prompt)

        if(user_input == '0'):
            sys.exit()

        continue

'''
This portion of the code REQUIRES the functions extract_annotations() and
    fill_time_values() to be called already on our eaf object.

The silence_segments() function uses the time values from start_cut_ref and
    end_cut_ref.

We will start off with a prompt requesting the audio file that is to be silenced.

Once again, we drag the audio file to the terminal upon given the prompt.
'''

audio_file_prompt = '\nDrag the .wav file here if you\'re ready to silence the audio or enter \'n\' to exit: '
selected_audio_file = pf.py_version_input(python_version,audio_file_prompt)
if(selected_audio_file == 'n'):
    sys.exit()

audio_object = AudioSegment.from_wav(selected_audio_file.strip())
silenced_audio_object = pf.silence_segments(annotation_values,audio_object)
print('\nSilenced Complete!')

file_obj.close()

