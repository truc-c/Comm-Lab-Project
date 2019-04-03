import xmltodict

def sp():
    print ''
# read in elan file (xml)
# convert to dict using xmltodict
with open('0204_000609_uclacurt_vetting.eaf') as fd:
    doc = xmltodict.parse(fd.read())

# -----------------------------------------------------------------------

# Let's start with the time order tags and separate the time_slot_id (e.g. ts1)
#   from the time_value (e.g. 32343)
# We can either create 2 list, one storing the time_slot_id and the other for
#   the time_value or we can directly put it into a dict
time_order_obj = doc['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']
keys_list = []
values_list = []
sp()

for i in time_order_obj:
    keys_list.append(i.values()[0])
    values_list.append(i.values()[1])

time_order_dict = dict(zip(keys_list,values_list))

# -----------------------------------------------------------------------

# Extract relevant annotation values to build dictionary
# Let's move to the annotation tag and grab the annotation_id (e.g. a1),
#   time_slot_ref1 (e.g. ts1), and time_slot_ref2 (e.g. ts2)

# The reason we might need ref1 and ref2 is so that we can use these to
#   reference our time_order object (which contains the time selection)

# list_of_annotation_objs allows us to access the tiers (e.g. cut or bookmark)
# annotation_obj contains the first tier (in this case 'cut' tier)..
#   this was possible by indexing ([0]) with list_of_annotation_objs
list_of_annotation_objs = doc['ANNOTATION_DOCUMENT']['TIER'] # iterate over this eventually
annotation_obj = list_of_annotation_objs[0]# <--IMPORTANT

#print list_of_annotation_objs
#print annotation_obj

sp()

# cut_dict gives us our first of many annotations.  We need to use the
#   index ([0]) to reference the first annotation.  Our next tag
#   ALIGNABLE_ANNOTATION brings us to our final step where we can start
#   extracting values
cut_dict = annotation_obj['ANNOTATION'][0]['ALIGNABLE_ANNOTATION']
# print cut_dict

# cut_id will be the very first key in our dict.  The value for cut_id
#   is another dict consisting of references to start and end objects and
#   its values.  These start and end objects are time_slot_id's that we
#   will use to reference back to our time_order_dict

# --------------------------------------------------------------------

# DO NOT TOUCH THIS!!!!! FINISHED!!!!
# Let's try finding how many annotations there are first so that we
#   can use it in a loop
# print('How many annotations are there? ',len(list_of_annotation_objs[0]['ANNOTATION']))
# sp()
num_of_annotations = len(list_of_annotation_objs[0]['ANNOTATION'])
# print(type(num_of_annotations))
# print num_of_annotations

# Now that we have found how many there are we can probably use it
#   in a while-loop, but first we need to get to the annotations
# Let's use the list_of annotation_obj from earlier to
# FINISHED !!!!!!!!!! DO NOT CHANGE THIS CODE!!!
# Be sure to move this part of the code up top because we have extracted
#   the cut_id or can be used for the cut_id
# print(len(list_of_annotation_objs[0]['ANNOTATION']))

# 4/2
# Since you're grabbing the ANNOTATION_ID, you may as well grab the
#   TIME_SLOT_REF's and ANNOTATION_VALUE
# I'm debating whether I should continuously create and delete my tuple
path_to_annotation_info = list_of_annotation_objs[0]['ANNOTATION']
sp()
count = 0
list_of_id = []
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

# for i in list_of_id:
#     print(i)
sp()
# -------------------------------------------------------------------

# Here we are going to use list_of_id (contains ANNOTATION_ID: a1, a2, a3)
#   for our cut_id
# Let's use a for-loop with our list_of_id and create and empty dict as
#   the value and the key will be the list_of_id
# THIS IS FINISHED!!!! DO NOT TOUCH!!!!

# 4/3
# Since you are creating you're final dict, should you also input the other
#   information while you're at it?
final_product = {}


for id_index in list_of_id:
    cut_id = id_index[0]
    time_ref1 = id_index[1]
    time_ref2 = id_index[2]
    annotation_text = id_index[3]
    #print(cut_id)
    final_product[cut_id] = {'start_cut_ref': time_ref1,'start_cut_value':0,
                            'end_cut_ref':time_ref2,'end_cut_value':0,
                            'annotation_value':annotation_text}

# Now that we have filled our final_product dict with the keys and
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

print final_product

sp()


# -------------------------------------------------------------------

# final_product = {cut_id: {'start_cut_ref': start_cut_ref, 'start_cut_value': 0,
#                 'end_cut_ref': end_cut_ref, 'end_cut_value': 0,
#                 'annotation_value':annotation_value}
#






















#
