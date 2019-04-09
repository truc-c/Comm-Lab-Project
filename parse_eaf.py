import xmltodict
import pprint
import parsing_functions
import os
print(os.getcwd())
with open('0204_000609_uclacurt_vetting.eaf') as fd:
    doc = xmltodict.parse(fd.read())


# list_of_tier_objs holds the different TIER tags

# print(list_of_tier_objs['@TIER_ID'])
# pprint.pprint(list_of_tier_objs)
# annotation_objs are the many ANNOTATION tags in each TIER
# tier_number indicates which TIER we want, in this case we are indexing
#   the TIER_ID="cut"
tier_name_user_input = input('Enter tier name: ')
list_of_tier_objs = doc['ANNOTATION_DOCUMENT']['TIER']
list_of_TIER_IDs = parsing_functions.get_unique_TIER_ID(list_of_tier_objs)

if tier_name_user_input in list_of_TIER_IDs:
    print("Processing the [%s" %tier_name_user_input + "] tier")
    time_order_obj = doc['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']
    time_order_dict = parsing_functions.extract_timeOrder(time_order_obj)

    tier_idx = parsing_functions.get_TIER_idx(tier_name_user_input, list_of_tier_objs)

    annotation_objs = list_of_tier_objs[tier_idx]['ANNOTATION'] # maybe turn into function
    my_product = parsing_functions.get_annotation_values(annotation_objs)
    my_product = parsing_functions.fill_time_values(my_product, time_order_dict)
    pprint.pprint(my_product)
    # save my_product to disk

else:
    print("Please enter one of the following TIER_IDs", list_of_TIER_IDs)

# check if user input , then error message, these are the 4 available


# write if statement to check user input, else don't run rest of code

# check user input with this list
# run code if it passes
# then get_TIER
















#
