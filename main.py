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

Example:

    print(time_order_slots)

    [OrderedDict([('@TIME_SLOT_ID', 'ts1'), ('@TIME_VALUE', '4670')]),
        OrderedDict([('@TIME_SLOT_ID', 'ts2'), ('@TIME_VALUE', '7310')])
    ... # additional output excluded

Example:
    print(time_order_slots[1])

    output:

    OrderedDict([('@TIME_SLOT_ID', 'ts2'), ('@TIME_VALUE', '7310')])

Example:
    print(time_order_slots[1]['@TIME_SLOT_ID'])

    output:

    ts2

tier_elements returns an OrderedDict with TIER_ID, ANNOTATION_ID, TIME_SLOT_REF1,
    TIME_SLOT_REF2, ANNOTATION_VALUE of each tier (e.g., cut, bookmark)
"""

time_order_slots = eaf_obj['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']
tier_elements = eaf_obj['ANNOTATION_DOCUMENT']['TIER']

if(python_version == 3):
    tier_name_input = input('Enter a tier name: ')
else:
    tier_name_input = raw_input('Enter a tier name: ')

all_TIER_ID_names = pf.get_unique_TIER_ID(tier_elements)


"""
if statement checks the input with of all TIER_ID names
    else, it prints the TIER_ID's available

time_id_and_value holds values of TIME_SLOT_ID and TIME_VALUE

tier_idx_number is the number associated with the TIER name

annotation_objs holds annotations in a tier

final_product is a nested dictionary containing all the annotation values of a tier
"""

if tier_name_input in all_TIER_ID_names:
    print("Process the results for [%s" %tier_name_input + "] tier")

    time_id_and_value = pf.extract_TIME_ID_and_VALUE(time_order_slots)
    tier_idx_number = all_TIER_ID_names.index(tier_name_input)
    annotation_objs = tier_elements[tier_idx_number]['ANNOTATION'] # maybe turn into function
    final_product = pf.extract_ANNOTATION_values(annotation_objs, time_id_and_value)

    pprint.pprint(final_product)
    # save final_product to disk?

else:
    pf.no_valid_results(all_TIER_ID_names)

wav_object = AudioSegment.from_wav('/users/curt/desktop/real_sound.wav')
final_sound = pf.silence_segments(final_product,wav_object)
# play(final_sound)

file_obj.close()


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
