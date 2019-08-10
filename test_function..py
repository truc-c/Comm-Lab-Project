# ================= test individual functions in here =====================
# cut_ids_and_values = pf.extract_TIME_ID_and_VALUE(eaf_obj)    dict of slot_id and value
# all_TIER_ID_names = pf.get_tier_names(eaf_obj)                   gets tier names









# =======================================================================

# ============== Need to work on this ==========
# create a function get specifices an ANNOTATION_ID.   All they need to do is pass in the ID because each ID is different
def get_annotation_id(eaf_object):
    tier_object = pf.get_TIERs(eaf_object)
    print(tier_object[0]['ANNOTATION'][0]['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID'])

    # for i in tier_object:
    #     if(i['@TIER_ID'] == tier_id_name):
    #         print('it worked')

get_annotation_id(eaf_obj)

# ========================================== 
