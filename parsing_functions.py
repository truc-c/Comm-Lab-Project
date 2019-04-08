import pprint

def extract_timeOrder(*time_order_list):
    # using time_order_list in an for-loop, we can extract the values from
    #   TIME_SLOT_ID and TIME_VALUE and store them in our time_order_dict
    # Our time_order_dict-keys will contain the following examples:
    #   "ts1", "ts3", etc.
    #   and the time_order_dict-values will contain the following examples:
    #   10305, 25532, etc.
    # time_order_dict = {}
    time_order_dict = {}
    for time_slot in time_order_list:
        time_id = time_slot['@TIME_SLOT_ID']        # time_id = TIME_SLOT_ID
        time_value = time_slot['@TIME_VALUE']       # time_value = TIME_VALUE
        time_order_dict[time_id] = int(time_value)
    return time_order_dict

def get_TIER(tier_name, *list_of_tiers):
    index_number = 0
    for i in list_of_tiers:
        if i['@TIER_ID'] == tier_name:
            index_number = index_number
            break
        index_number += 1
    return index_number

def get_annotation_values(*annotation_objs):
    final_product = {}
    for each_annotation in annotation_objs:
        annotation_id = each_annotation['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']
        slot_ref1 = each_annotation['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF1']
        slot_ref2 = each_annotation['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF2']
        annotation_text = each_annotation['ALIGNABLE_ANNOTATION']['ANNOTATION_VALUE']
        final_product[annotation_id] = {'start_cut_ref': slot_ref1,'start_cut_value':0,
                                        'end_cut_ref':slot_ref2,'end_cut_value':0,
                                        'annotation_value':annotation_text}
    return final_product
