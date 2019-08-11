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

# time_order returns an OrderedDict with with two TIME_SLOT_ID's
#     as well as, the TIME_VALUE for each TIME_SLOT_ID.

# tier_elements returns an OrderedDict with TIER_ID, ANNOTATION_ID, TIME_SLOT_REF1,
#   TIME_SLOT_REF2, ANNOTATION_VALUE of each tier (e.g., cut, bookmark)

valid_input = True
tier_elements = pf.get_TIERs(eaf_obj)
all_TIER_ID_names = pf.get_tier_names(eaf_obj)
tier_name_prompt = 'Enter a tier name: '
tier_name_input = pf.py_version_input(python_version, tier_name_prompt)


# if statement checks the input with of all TIER_ID names
#     else, it prints the TIER_ID's available

# time_ids_and_values is a dictionary that holds values of TIME_SLOT_ID and TIME_VALUE

# tier_idx_number is the number associated with the TIER name

# annotation_objs holds annotations in a tier

# final_product is a nested dictionary containing all the annotation values of a tier


while(valid_input):
    if tier_name_input in all_TIER_ID_names:
        print("\nProcess the results for [%s" %tier_name_input + "] tier\n")

        time_ids_and_values = pf.extract_TIME_ID_and_VALUE(eaf_obj)     # you need this
        tier_idx_number = all_TIER_ID_names.index(tier_name_input)

        try:
            annotation_objs = tier_elements[tier_idx_number]['ANNOTATION'] # maybe turn into function
        except:
            print('There are no annotations in the tier: ' + tier_name_input)

            select_diff_tier = 'Would you like to select another tier? (y = yes , n = no): '
            tier_response = pf.py_version_input(python_version, select_diff_tier)
            if(tier_response == 'y'):
                tier_name_input = pf.py_version_input(python_version, tier_name_prompt)
                continue
            else:
                break

        final_product = pf.extract_ANNOTATION_values(annotation_objs, time_ids_and_values)

        pprint.pprint(final_product)

        select_diff_tier = 'Would you like to select another tier? (y = yes , n = no): '
        tier_response = pf.py_version_input(python_version, select_diff_tier)

        if(tier_response == 'y'):
            tier_name_input = pf.py_version_input(python_version, tier_name_prompt)
            continue
        else:
            valid_input = False
            break
    else:
        pf.no_valid_results(all_TIER_ID_names)
        tier_name_input = pf.py_version_input(python_version, tier_name_prompt)

        if(tier_name_input == '0'):
            sys.exit()

        continue

# -- Silencing Portion --

silence_instruction = '\nDrag the .wav file here if you\'re ready to silence the audio or enter \'n\' to exit: '
silence_this_wav = pf.py_version_input(python_version, silence_instruction)
if(silence_this_wav == 'n'):
    sys.exit()

wav_object = AudioSegment.from_wav(silence_this_wav.strip())
silenced_wav_obj = pf.silence_segments(final_product,wav_object)
new_full_pathname = pf.modify_filename(silence_this_wav.strip())

print('\n==== ! Silencing Process Finished ! ====\n')

# silenced_wav_obj.export(new_full_pathname, format='wav')












































#
