import xmltodict
import pprint
import parsing_functions

with open('0204_000609_uclacurt_vetting.eaf') as fd:
    doc = xmltodict.parse(fd.read())

# -----------------------------------------------------------------------
# Let's start with the TIME_ORDER tag and extract the
#   TIME_SLOT_ID values (e.g. "ts1", "ts3", etc.) and
#   TIME_VALUE values (e.g. 10305, 25532, etc.)

# time_order_obj will store TIME_SLOT_ID and TIME_VALUE as an OrderedDict


# using time_order_obj in an for-loop, we can extract the values from
#   TIME_SLOT_ID and TIME_VALUE and store them in our time_order_dict
# Our time_order_dict keys will contain the following examples:
#   "ts1", "ts3", etc.
#   and the time_order_dict values will contain the following examples:
#   10305, 25532, etc.
# time_order_dict = {}
# for time_slot in time_order_obj:
#     time_id = time_slot['@TIME_SLOT_ID']        # time_id = TIME_SLOT_ID
#     time_value = time_slot['@TIME_VALUE']       # time_value = TIME_VALUE
#     time_order_dict[time_id] = int(time_value)



# --------------------------------------------------------------------
# This part of the code takes us to the ANNOTATION tags
# Since there are many annotations we need to be able to loop through each
#   ANNOTATION tag and extract the following:
#       ANNOTATION_ID (e.g. "a2", "a10", etc.)
#       TIME_SLOT_REF1 (e.g. "ts1", "ts3", "ts5", etc.)
#       TIME_SLOT_REF2 (e.g. "ts2", "ts4", "ts6", etc.)
#       ANNOTATION_VALUE (e.g. "annotation notes")

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
    time_order_dict = parsing_functions.extract_timeOrder(*time_order_obj)

    tier_idx = parsing_functions.get_TIER_idx(tier_name_user_input, *list_of_tier_objs)

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
