import xmltodict
import pprint
import os
from pydub import AudioSegment
from pydub.playback import play
import parsing_functions as pf
with open('/users/curt/desktop/elan_test.eaf') as fd:
    doc = xmltodict.parse(fd.read())

'''
time_order_elements returns an OrderedDict with with two TIME_SLOT_ID's
    as well as, the TIME_VALUE for each TIME_SLOT_ID.

Example:

    print(time_order_elements)

    [OrderedDict([('@TIME_SLOT_ID', 'ts1'), ('@TIME_VALUE', '4670')]),
        OrderedDict([('@TIME_SLOT_ID', 'ts2'), ('@TIME_VALUE', '7310')])
    ... # additional output excluded

Example:
    print(time_order_elements[1])

    output:

    OrderedDict([('@TIME_SLOT_ID', 'ts2'), ('@TIME_VALUE', '7310')])

Example:
    print(time_order_elements[1]['@TIME_SLOT_ID'])

    output:

    ts2

tier_elements returns an OrderedDict with TIER_ID, ANNOTATION_ID, TIME_SLOT_REF1,
    TIME_SLOT_REF2, ANNOTATION_VALUE of each tier (e.g., cut, bookmark)
'''

time_order_elements = doc['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']
tier_elements = doc['ANNOTATION_DOCUMENT']['TIER']
tier_name_input = input('Enter a tier name: ')

all_TIER_ID_names = pf.get_unique_TIER_ID(tier_elements)

# if-else statement checks the users input with list of all TIER_ID names
if tier_name_input in all_TIER_ID_names:
    print("Process the results for [%s" %tier_name_input + "] tier")

    # time_id_and_value_dict holds values of TIME_SLOT_ID and TIME_VALUE
    time_id_and_value_dict = pf.extract_TIME_ID_and_VALUE(time_order_elements)

    # tier_idx_number is the number associated with the TIER name
    tier_idx_number = all_TIER_ID_names.index(tier_name_input)

    # list_of_ANNOTATIION_objs contains all ANNOTATIONS to a specific TIER
    list_of_ANNOTATIION_objs = tier_elements[tier_idx_number]['ANNOTATION'] # maybe turn into function

    # final_product is a nested dictionary containing all the annotation values of a tier
    final_product = pf.extract_ANNOTATION_values(list_of_ANNOTATIION_objs, time_id_and_value_dict)

    pprint.pprint(final_product)
    # save final_product to disk

else:
    pf.no_valid_results(all_TIER_ID_names)

wav_object = AudioSegment.from_wav('/users/curt/desktop/real_sound.wav')
final_sound = pf.silence_segments(final_product,wav_object)
# play(final_sound)

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
