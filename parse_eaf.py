import xmltodict

def sp():
    print ''
# read in elan file (xml)
# convert to dict using xmltodict
with open('0204_000609_uclacurt_vetting.eaf') as fd:
    doc = xmltodict.parse(fd.read())

# -----------------------------------------------------------------------
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
# This part of the code takes us to the ANNOTATION tags
# Since there are many annotations we need to be able to loop through each
#   ANNOTATION tag and extract the following:
#       ANNOTATION_ID (e.g. "a2", "a10", etc.)
#       TIME_SLOT_REF1 (e.g. "ts1", "ts3", "ts5", etc.)
#       TIME_SLOT_REF2 (e.g. "ts2", "ts4", "ts6", etc.)
#       ANNOTATION_VALUE (e.g. "annotation notes")

# list_of_tier_objs holds the different TIER tags
list_of_tier_objs = doc['ANNOTATION_DOCUMENT']['TIER']

# annotation_objs are the many ANNOTATION tags in each TIER
# tier_number indicates which TIER we want, in this case we are indexing
#   the TIER_ID="cut"
tier_number = 0
annotation_objs = list_of_tier_objs[tier_number]['ANNOTATION']

# list_of_tuples is a list that will hold tuples that contain values from
#   ANNOTATION_ID, TIME_SLOT_REF1, TIME_SLOT_REF2 and ANNOTATION_VALUE
list_of_tuples = []

# This annotation_index variable will help us move from one annotation
#   to the next
annotation_index = 0

# final_product is a dictionary that will later contain another dictionary
final_product = {}

# This for-loop is to iterate through the ANNOTATIONS while extracting values
#   from:   @ANNOTATION_ID      (e.g. 'a1','a7','a22', etc.)
#           @TIME_SLOT_REF1     (e.g. 'ts1','ts3','ts7', etc.)
#           @TIME_SLOT_REF2     (e.g. 'ts2','ts4','ts8', etc.)
#           ANNOTATION_VALUE    (e.g. 'some text')

# annotation_id, slot_ref1, slot_ref2, and annotation_v are the variables
#   that we are using to store the values

# for-loop will iterate through each ANNOTATION tag and extract values
# tuple_of_values variable will hold the values; we use tuple to avoid
#   any accidential changes
# We call the append() to add the tuple_of_values to our list_of_tuples
# Lastly, we increment annotation_index to move to the next index
for each_annotation in annotation_objs:
    # print(i['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID'])
    # print(i['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF1'])
    annotation_id = each_annotation['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']
    slot_ref1 = each_annotation['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF1']
    slot_ref2 = each_annotation['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF2']
    annotation_text = each_annotation['ALIGNABLE_ANNOTATION']['ANNOTATION_VALUE']
    final_product[annotation_id] = {'start_cut_ref': slot_ref1,'start_cut_value':0,
                            'end_cut_ref':slot_ref2,'end_cut_value':0,
                            'annotation_value':annotation_text}
        # annotation_id = annotation_objs[annotation_index]['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']
        # slot_ref1 = annotation_objs[annotation_index]['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF1']
        # slot_ref2 = annotation_objs[annotation_index]['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF2']
        # annotation_v = annotation_objs[annotation_index]['ALIGNABLE_ANNOTATION']['ANNOTATION_VALUE']
        # tuple_of_values = (annotation_id, slot_ref1, slot_ref2, annotation_v)
        # list_of_tuples.append(tuple_of_values)
        # annotation_index += 1
        # print(annotation_id, slot_ref1, slot_ref2, annotation_v)

# -------------------------------------------------------------------

# THIS IS FINISHED!!!! DO NOT TOUCH!!!!

# This part of the code will extract all values from list_of_tuples which
#   contains the values of: ANNOTATION_ID, TIME_SLOT_REF1, TIME_SLOT_REF2,
#   and ANNOTATION_VALUE, and place it into our final_product dict



# This for-loop will loop through our list_of_tuples to extract and store
#   values for our final_product
# Maybe instead of using indexes you can use the same variables from above,
#   this way we avoid the assumption that index[0] is the ANNOTATION_ID
#   or that id_index[1] is TIME_SLOT_REF1

# for id_index in list_of_tuples:
#     cut_id = id_index[0]                # cut_id = ANNOTATION_ID ('a1','a3', etc.)
#     time_ref1 = id_index[1]             # time_ref1 = TIME_SLOT_REF1 ('ts1','ts3', etc.)
#     time_ref2 = id_index[2]             # time_ref2 = TIME_SLOT_REF2 ('ts2','ts4', etc.)
#     annotation_text = id_index[3]       # annotation_text = ANNOTATION_VALUE ('some text')
#     final_product[cut_id] = {'start_cut_ref': time_ref1,'start_cut_value':0,
#                             'end_cut_ref':time_ref2,'end_cut_value':0,
#                             'annotation_value':annotation_text}

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

print(len(final_product))
print(final_product)
sp()


# -------------------------------------------------------------------

# final_product[annotation_id] = {'start_cut_ref': slot_ref1,'start_cut_value':0,
#                         'end_cut_ref':slot_ref2,'end_cut_value':0,
#                         'annotation_value':annotation_text}























#
