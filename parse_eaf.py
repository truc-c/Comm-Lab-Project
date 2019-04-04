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

# annotation_id, slot_ref1, slot_ref2, and annotation_text are the variables
#   that we are using to store the values in

# for-loop will iterate through each ANNOTATION tag and extract values
#   and place them into the variables mentioned above
# We can then start using the variables in our final_product dictionary
# Our final_product dictionary will contain another dictionary that will
#   contain values associated with the annotation_id (e.g. 'a1','a2','a3', etc.)
# For the moment we will leave the values to the keys, 'start_cut_value' and
#   'end_cut_value', as a default value (0)
for each_annotation in annotation_objs:
    annotation_id = each_annotation['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']
    slot_ref1 = each_annotation['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF1']
    slot_ref2 = each_annotation['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF2']
    annotation_text = each_annotation['ALIGNABLE_ANNOTATION']['ANNOTATION_VALUE']
    final_product[annotation_id] = {'start_cut_ref': slot_ref1,'start_cut_value':0,
                                    'end_cut_ref':slot_ref2,'end_cut_value':0,
                                    'annotation_value':annotation_text}

# -------------------------------------------------------------------


# Now that we have filled our final_product dictionary with keys and
#   default values we want to use our time_order_dict as a reference to
#   fill the start and end cut values in our final_product dictionary

for cut_refs in final_product.values():
    # Let's loop through the final_product keys and grab the values for
    #   'start_cut_ref' and 'end_cut_ref' and place it into variables that we
    #   can use when looking for time values in our time_order_dict
    start_ref = cut_refs['start_cut_ref']
    end_ref = cut_refs['end_cut_ref']

    # After extracting the start and end references (e.g. 'ts1','ts2',etc.)
    #   we can now look for the associated time in our time_order_dict
    if start_ref in time_order_dict:
        start_value = int(time_order_dict[start_ref])
    if end_ref in time_order_dict:
        end_value = int(time_order_dict[end_ref])

    # Now that we have the time, we can replace the default values (0) with
    #   the times that are associated with the reference
    cut_refs['start_cut_value'] = start_value
    cut_refs['end_cut_value'] = end_value

sp()

# -------------------------------------------------------------------

# final_product[annotation_id] = {'start_cut_ref': slot_ref1,'start_cut_value':0,
#                         'end_cut_ref':slot_ref2,'end_cut_value':0,
#                         'annotation_value':annotation_text}























#
