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

def get_TIER_idx(tier_name, *list_of_tiers): # get_tier_index
    index_number = 0
    for i in list_of_tiers:
        if i['@TIER_ID'] == tier_name:
            index_number = index_number
            break
        index_number += 1
    return index_number #return list of TIER_ID
    #
def get_unique_TIER_ID(list_of_tiers):
    my_list = []
    for i in list_of_tiers:
        my_list.append(i['@TIER_ID'])
    return my_list #return list of TIER_ID

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

def fill_time_values(my_product,time_order_dict):
    for cut_refs in my_product.values():
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
    return my_product
