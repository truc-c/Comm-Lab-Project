def extract_timeOrder(*time_order_list):
    time_order_dict = {}
    for time_slot in time_order_list:
        time_id = time_slot['@TIME_SLOT_ID']        # time_id = TIME_SLOT_ID
        time_value = time_slot['@TIME_VALUE']       # time_value = TIME_VALUE
        time_order_dict[time_id] = int(time_value)
    return time_order_dict

def get_TIER(tier_name, *list_of_tiers):
    index_number = 0
    print('get_TIER')
    for i in list_of_tier_objs:
        if i['@TIER_ID'] == tier_name:
            index_number = index_number
            break
        index_number += 1
    return index_number

def get_annotation_values(tier_numer):
    pass
