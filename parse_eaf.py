import xmltodict

def sp():
    print ''
# read in elan file (xml)
# convert to dict using xmltodict
with open('0204_000609_uclacurt_vetting.eaf') as fd:
    doc = xmltodict.parse(fd.read())

# -----------------------------------------------------------------------

# DO NOT TOUCH THIS !!!! FINISHED WITH COMPLETED COMMENTS !!!!!
# Let's start with the TIME_ORDER tag and extract the
#   TIME_SLOT_ID values (e.g. "ts1", "ts3", etc.) and
#   TIME_VALUE values (e.g. 10305, 25532, etc.)

# time_order_obj will store TIME_SLOT_ID and TIME_VALUE as an OrderedDict
time_order_obj = doc['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']

# using time_order_obj in an for-loop, we can extract the values from
#   TIME_SLOT_ID and TIME_VALUE and store them in our time_order_dict
# Our time_order_dict keys will contain the following examples:
#   "ts1", "ts3", etc.
#   and the time_order_dict values will contain the following examples:
#   10305, 25532, etc.
time_order_dict = {}
for time_slot in time_order_obj:
    time_id = time_slot['@TIME_SLOT_ID']        # time_id = TIME_SLOT_ID
    time_value = time_slot['@TIME_VALUE']       # time_value = TIME_VALUE
    time_order_dict[time_id] = int(time_value)



# --------------------------------------------------------------------

# DO NOT TOUCH THIS!!!!! FINISHED!!!!

# This part of the code takes us to the ANNOTATION tags
# Since there are many annotations we need to be able to loop through each
#   ANNOTATION tag and extract the following:
#       ANNOTATION_ID (e.g. "a2", "a10", etc.)
#       TIME_SLOT_REF1 (e.g. "ts1", "ts3", "ts5", etc.)
#       TIME_SLOT_REF2 (e.g. "ts2", "ts4", "ts6", etc.)
#       ANNOTATION_VALUE (e.g. "annotation notes")


list_of_annotation_objs = doc['ANNOTATION_DOCUMENT']['TIER']

path_to_annotation_info = list_of_annotation_objs[0]['ANNOTATION']
# print(path_to_annotation_info)

# You want to do something with this, but you don't know what yet
# Maybe you should write it out first
# for i in path_to_annotation_info:
#     print i['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']

count = 0
list_of_id = []
num_of_annotations = len(list_of_annotation_objs[0]['ANNOTATION'])
while count < num_of_annotations:
    nested_list = ()
    annotation_id = path_to_annotation_info[count]['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']
    slot_ref1 = path_to_annotation_info[count]['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF1']
    slot_ref2 = path_to_annotation_info[count]['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF2']
    annotation_v = path_to_annotation_info[count]['ALIGNABLE_ANNOTATION']['ANNOTATION_VALUE']
    nested_list = nested_list + (annotation_id,)
    nested_list = nested_list + (slot_ref1,)
    nested_list = nested_list + (slot_ref2,)
    nested_list = nested_list + (annotation_v,)
    list_of_id.append(nested_list)
    del nested_list
    count += 1

sp()
# -------------------------------------------------------------------

# THIS IS FINISHED!!!! DO NOT TOUCH!!!!

# This part of the code will extract all values from the list of tuples
#   (list_of_id) which contains: ANNOTATION_ID, TIME_SLOT_REF1, TIME_SLOT_REF2,
#   and ANNOTATION_VALUE, and place it into our final_product dict
final_product = {}

for id_index in list_of_id:
    cut_id = id_index[0]                # cut_id = ANNOTATION_ID
    time_ref1 = id_index[1]             # time_ref1 = TIME_SLOT_REF1
    time_ref2 = id_index[2]             # time_ref2 = TIME_SLOT_REF2
    annotation_text = id_index[3]       # annotation_text = ANNOTATION_VALUE
    final_product[cut_id] = {'start_cut_ref': time_ref1,'start_cut_value':0,
                            'end_cut_ref':time_ref2,'end_cut_value':0,
                            'annotation_value':annotation_text}

# Now that we have filled our final_product dict with keys and
#   default values we want to use our time_order_dict as a reference to
#   fill the values in our final_product dict
# Let's create a separate loop that will populate the values in
#   final_product

for cut_refs in final_product.values():
    # Let's loop through the final_product keys and grab the values for
    #   'start_cut_ref' and 'end_cut_ref' and place it variables that we
    #   can use when looking for time values in our time_order_dict
    start_ref = cut_refs['start_cut_ref']
    end_ref = cut_refs['end_cut_ref']

    # After extracting values (e.g. 'ts1','ts2',etc.) from 'start_cut_ref' and
    #   'end_cut_ref' we can now look in time_order_dict and grab the values
    #   (10049,38505, etc.) that correspond, and at the same time we can store
    #   it in variables 'start_value' and 'end_value'
    if start_ref in time_order_dict:
        start_value = int(time_order_dict[start_ref])
        #print('key:',start_ref,' ','value:',start_value)
    if end_ref in time_order_dict:
        end_value = int(time_order_dict[end_ref])

    # Now let's store the values into 'start_cut_value' and 'end_cut_value' in
    #   our final_product dict
    cut_refs['start_cut_value'] = start_value
    cut_refs['end_cut_value'] = end_value

#print final_product

sp()


# -------------------------------------------------------------------

# final_product = {cut_id: {'start_cut_ref': start_cut_ref, 'start_cut_value': 0,
#                 'end_cut_ref': end_cut_ref, 'end_cut_value': 0,
#                 'annotation_value':annotation_value}
#






















#
