import xmltodict
import pprint
import os
from pydub import AudioSegment
from pydub.playback import play
import parsing_functions

with open('/users/curt/desktop/elan_test.eaf') as fd:
    doc = xmltodict.parse(fd.read())

# with open('0204_000609_uclacurt_vetting.eaf') as fd:
#     doc = xmltodict.parse(fd.read())

'''
time_order_elements returns an OrderedDict with with two TIME_SLOT_ID's
    as well as, the TIME_VALUE for each TIME_SLOT_ID.

Here is a sample:

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
'''
time_order_elements = doc['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']
print(time_order_elements[1]['@TIME_SLOT_ID'])
tier_elements = doc['ANNOTATION_DOCUMENT']['TIER']

user_input_tier_name = input('Enter a tier name: ')

all_TIER_ID_names = parsing_functions.get_unique_TIER_ID(tier_elements)


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
    time_id_and_value_dict = parsing_functions.extract_TIME_ID_and_VALUE(time_order_elements)

    '''
    tier_idx_number is the number associated with the TIER name
        prompted by the user
    '''
    tier_idx_number = all_TIER_ID_names.index(user_input_tier_name)

    '''
    list_of_ANNOTATIION_objs contains all ANNOTATIONS to a
        specific TIER
    '''
    list_of_ANNOTATIION_objs = tier_elements[tier_idx_number]['ANNOTATION'] # maybe turn into function

    '''
    final_product is a nested dictionary containing all the ANNOTATION
        values
    '''
    final_product = parsing_functions.extract_ANNOTATION_values(list_of_ANNOTATIION_objs, time_id_and_value_dict)
    # pprint.pprint(final_product)
    # save final_product to disk

else:
    parsing_functions.no_valid_results(all_TIER_ID_names)

wav_object = AudioSegment.from_wav('/users/curt/desktop/real_sound.wav')
final_sound = parsing_functions.silence_segments(final_product,wav_object)
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












































#
