import xmltodict
import pprint
import parsing_functions
import os
with open('0204_000609_uclacurt_vetting.eaf') as fd:
    doc = xmltodict.parse(fd.read())

# List of all TIERs, each one can be accessed by indexing followed by
#   keys() and values() function
list_of_TIER_objs = doc['ANNOTATION_DOCUMENT']['TIER']

# List of all TIME_SLOTs, each can be accessed by indexing followed
#   by keys() and values() function
list_of_TIME_SLOT_objs = doc['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']

# Ask user for for name of TIER (e.g. cut, bookmark)
user_input_tier_name = raw_input('Enter a tier name: ')

# get_unique_TIER_ID function returns a list of all TIER_ID names using
#   the list_of_TIER_objs that we passed in as an argument
# This list is helpful for checking the users input
all_TIER_ID_names = parsing_functions.get_unique_TIER_ID(list_of_TIER_objs)

# This if-else statement checks the users input
# If the input is valid then the program will run
#   else, an error message will appear providing a list of names
#   of available TIERs
if user_input_tier_name in all_TIER_ID_names:
    print("Processing the [%s" %user_input_tier_name + "] tier")
    time_id_and_value_dict = parsing_functions.extract_TIME_ID_and_VALUE(list_of_TIME_SLOT_objs)
    tier_idx = parsing_functions.get_TIER_idx(user_input_tier_name, list_of_TIER_objs)

    annotation_objs = list_of_TIER_objs[tier_idx]['ANNOTATION'] # maybe turn into function
    my_product = parsing_functions.get_annotation_values(annotation_objs)
    my_product = parsing_functions.fill_time_values(my_product, time_id_and_value_dict)
    pprint.pprint(my_product)
    # save my_product to disk

else:
    print("Please enter one of the following TIER_IDs:")
    for names in all_TIER_ID_names:
        print(names)

# check if user input , then error message, these are the 4 available


# write if statement to check user input, else don't run rest of code

# check user input with this list
# run code if it passes
# then get_TIER
















#
