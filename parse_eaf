import xmltodict

def sp():
    print ''
# read in elan file (xml)
# convert to dict using xmltodict
with open('0196_000902_uclacurt_vetting.eaf') as fd:
    doc = xmltodict.parse(fd.read())

# Grab just the tags we care about
time_order_obj = doc['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']
annotation_obj = doc['ANNOTATION_DOCUMENT']['TIER'][1]['ANNOTATION']
# print annotation_obj # (This works, it grabbed the info you wanted)
sp()

# # This part is a bit confusing to me, the type says it is a list, however,
# #   I am able to use the keys() and values() function as if it was a dict
# # This also gives us each annotation tier, for this instancd we are using bookmarks tier
# print type(annotation_obj)
print annotation_obj[0]
# print annotation_obj[1]
# print annotation_obj[2]
# print annotation_obj[3]

sp()

# ALIGNABLE_ANNOTATION is the key and everything else is the value
print annotation_obj[0]['ALIGNABLE_ANNOTATION']

sp()

# Now that we have designated which key we want, we can select which values
#   we want to extract that particular key
# Below this, you created some keys to use for your dict, you can probably
#   directly assign each of the values that you are extracting and assign
#   it to the variable
print annotation_obj[0]['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']
print annotation_obj[0]['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF1']
print annotation_obj[0]['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF2']
print annotation_obj[0]['ALIGNABLE_ANNOTATION']['ANNOTATION_VALUE']

# Here we create objects to use in our dict (cut_list)
# When we create a for-loop later we can generate custom annotationIDs
#   as well as, filling in the start and end times, and the annotations,
#   however, you might not need the annotation because you'll be combining
#   annotations later
# count = 1
# annotationID = 'a' + str(count)
# start_time = 0
# end_time = 0
# annotation = 'empty'
# cut_list = {annotationID:{'start_time':start_time,'end_time':end_time,
#                             'annotation':annotation}}



sp()
