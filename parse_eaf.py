import xmltodict

def sp():
    print ''
# read in elan file (xml)
# convert to dict using xmltodict
with open('0196_000902_uclacurt_vetting.eaf') as fd:
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

# print time_order_dict

# -----------------------------------------------------------------------

# Extract relevant annotation values to build dictionary
# Let's move to the annotation tag and grab the annotation_id (e.g. a1),
#   time_slot_ref1 (e.g. ts1), and time_slot_ref2 (e.g. ts2)

# The reason we might need ref1 and ref2 is so that we can use these to
#   reference our time_order object (which contains the time selection)

# list_of_annotation_objs allows us to access the tiers (e.g. cut or bookmark)
# annotation_obj contains the first tier (in this case 'cut' tier)..
#   this was possible by indexing ([0]) with list_of_annotation_objs, however
#   this doesn't apply for this situation

# annotation_obj is the annotations inside the tier tag
list_of_annotation_objs = doc['ANNOTATION_DOCUMENT']['TIER'][0] # iterate over this eventually
annotation_obj = list_of_annotation_objs#[0] <--IMPORTANT

# IMPORTANT ----- IMPORTANT
# You may or may not need to change the index above depending on how many
#   tiers you have.  If you only have one tier, then you don't need to
#   index, however if you have more than one tier, you will need to index.
#   This way annotation_obj knows which tier to reference to.

<<<<<<< HEAD
#print annotation_obj
sp()

=======
>>>>>>> d003bc84e49146ac4a5c381891472bcbb6682425
# cut_dict gives us our first of many annotations.  We need to use the
#   index ([0]) to reference the first annotation.  Our next tag
#   alignable_annotation brings us to our final step where we can start
#   extracting values
cut_dict = annotation_obj['ANNOTATION']['ALIGNABLE_ANNOTATION']

# cut_id will be the very first key in our dict.  The value for cut_id
#   is another dict consisting of references to start and end objects and
#   its values.  These start and end objects are time_slot_id's that we
#   will use to reference back to our time_order_dict
# start_cut_ref gives us 'ts1','ts2', etc.
cut_id = cut_dict['@ANNOTATION_ID']
start_cut_ref = cut_dict['@TIME_SLOT_REF1']
end_cut_ref = cut_dict['@TIME_SLOT_REF2']
annotation_value = cut_dict['ANNOTATION_VALUE']
<<<<<<< HEAD

# -------------------------------------------------------------------
=======
>>>>>>> d003bc84e49146ac4a5c381891472bcbb6682425

sp()
# d is our final product consisting of:
# cut_id (e.g. 'a1','a2', etc.)
# start_cut_ref (e.g. 'ts1','ts3', etc.)
# end_cut_ref (e.g. 'ts2', 'ts4', etc.)
# start_cut_value (e.g. 1000)
# end_cut_value (e.g. 1010)
# we might want to think about adding annotation and its value
d = {cut_id: {'start_cut_ref': start_cut_ref, 'start_cut_value': 0,
                'end_cut_ref': end_cut_ref, 'end_cut_value': 0,
                'annotation_value':annotation_value}
}

start_cut_value = time_order_dict[d['a1']['start_cut_ref']]
end_cut_value = time_order_dict[d['a1']['end_cut_ref']]
d['a1']['start_cut_value'] = start_cut_value
d['a1']['end_cut_value'] = end_cut_value

<<<<<<< HEAD
# print d
#
# #print d['a1']['start_cut_ref']

# --------------------------------------------------------------------

# Let's try finding how many annotations there are first so that we
#   can use it in a loop

print len(list_of_annotation_objs['ANNOTATION'])
sp()
num_of_annotations = len(list_of_annotation_objs['ANNOTATION'])
print num_of_annotations

# Now that we have found how many there are we can probably use it
#   in a while-loop, but first we need to get to the annotations
# Let's use the list_of annotation_obj from earlier to
sp()
print list_of_annotation_objs['ANNOTATION'][4]
sp()
print list_of_annotation_objs['ANNOTATION'][4]['ALIGNABLE_ANNOTATION']
sp()
print list_of_annotation_objs['ANNOTATION'][4]['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']
sp()
count = 0
list_of_id = []
while count != num_of_annotations:
    id = list_of_annotation_objs['ANNOTATION'][count]['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']
    print id
    list_of_id.append(id)
    count += 1

print list_of_id

sp()

list_of_annotation_objs['ANNOTATION']

num = 0

while num != list_of_annotation_objs['ANNOTATION']:
    print list_of_annotation_objs['ANNOTATION'][num]
    num += 1















=======
print d

#print d['a1']['start_cut_ref']
>>>>>>> d003bc84e49146ac4a5c381891472bcbb6682425

sp()
# print annotation_obj
# stuff = annotation_obj['ANNOTATION']
#
# sp()
