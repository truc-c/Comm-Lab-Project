import xmltodict

# read in elan file (xml)
# convert to dict using xmltodict
with open('0196_000902_uclacurt_vetting.eaf') as fd:
    doc = xmltodict.parse(fd.read())

# grab just the tags we care about
time_order_obj = doc['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']
print time_order_obj
