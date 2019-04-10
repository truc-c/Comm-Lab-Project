import pprint

# helps to identify the responsibilities of each part of code
# think about the purpose of the variable, name should sugges purpose
# single responsibility rule

def user_input_valid(input, TIER_ID_names):
    pass

# get_unique_TIER_ID function takes in a list of all TIERs
#   and extracts the TIER_ID name
# The names are added to a list and returns the list
def get_unique_TIER_ID(list_of_tiers):
    tier_name_list = []
    for tier_name in list_of_tiers:
        tier_name_list.append(tier_name['@TIER_ID'])
    return tier_name_list #return list of TIER_ID names

# extract_TIME_ID_and_VALUE function creates a dictionary of
#   TIME_SLOT_ID value as the key, and TIME_VALUE as the
#   its value
def extract_TIME_ID_and_VALUE(time_slot_list):
    time_slot_dict = {}
    for each_time_slot in time_slot_list:
        time_id = each_time_slot['@TIME_SLOT_ID']        # time_id = TIME_SLOT_ID
        time_value = each_time_slot['@TIME_VALUE']       # time_value = TIME_VALUE
        time_slot_dict[time_id] = int(time_value)
    return time_slot_dict

# get_TIER_index associates user input and tier number index and
#   returns the index number 
def get_TIER_idx(tier_name, list_of_tiers):
    index_number = list_of_tiers.index(tier_name)
    return index_number

def extract_ANNOTATION_values(annotation_objs, time_slot_dict):
    result = {}
    for each_annotation in annotation_objs:
        annotation_id = each_annotation['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']
        slot_ref1 = each_annotation['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF1']
        slot_ref2 = each_annotation['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF2']
        annotation_text = each_annotation['ALIGNABLE_ANNOTATION']['ANNOTATION_VALUE']
        result[annotation_id] = {'start_cut_ref': slot_ref1,'start_cut_value':0,
                                        'end_cut_ref':slot_ref2,'end_cut_value':0,
                                        'annotation_value':annotation_text}

    for cut_refs in result.values():
        start_ref = cut_refs['start_cut_ref']
        end_ref = cut_refs['end_cut_ref']
        if start_ref in time_slot_dict:
            start_value = int(time_slot_dict[start_ref])
        if end_ref in time_slot_dict:
            end_value = int(time_slot_dict[end_ref])
        cut_refs['start_cut_value'] = start_value
        cut_refs['end_cut_value'] = end_value

    return result
