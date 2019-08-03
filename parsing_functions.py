import pprint
from pydub import AudioSegment
from pydub.playback import play

'''
helps to identify the responsibilities of each part of code
think about the purpose of the variable, name should sugges purpose
single responsibility rule
'''

'''
get_unique_TIER_ID function takes in a list of all TIERs
  and extracts the TIER_ID name
The names are added to a list and returns the list
'''
def get_unique_TIER_ID(list_of_tiers):
    tier_name_list = []
    for tier_name in list_of_tiers:
        tier_name_list.append(tier_name['@TIER_ID'])
    return tier_name_list #return list of TIER_ID names

'''
extract_TIME_ID_and_VALUE function creates a dictionary of
  TIME_SLOT_ID value as the key, and TIME_VALUE as the
  its value
'''
def extract_TIME_ID_and_VALUE(time_slot_list):
    time_slot_dict = {}
    for each_time_slot in time_slot_list:
        time_id = each_time_slot['@TIME_SLOT_ID']        # time_id = TIME_SLOT_ID
        time_value = each_time_slot['@TIME_VALUE']       # time_value = TIME_VALUE
        time_slot_dict[time_id] = int(time_value)
    return time_slot_dict

'''
extract_ANNOTATION_values returns a nested dictionary that containing
    the ANNOTATION_ID, TIME_SLOT_REF's, and ANNOTATION_VALUE
'''
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

def no_valid_results(list_of_tiers):
    print("Tier name does not exist. Please enter one of the following tier names:")
    for names in list_of_tiers:
        print(names)

def silence_segments(final_product, wav_object):
    holder = 0000
    segment_counter = len(final_product)
    list_of_segments = []

    for key,value in final_product.items():
        begin = wav_object[holder:value['start_cut_value']]
        sensitive_info = wav_object[value['start_cut_value']:value['end_cut_value']]
        sensitive_info = wav_object.silent(duration=len(sensitive_info))
        list_of_segments.append(begin)
        list_of_segments.append(sensitive_info)
        holder = value['end_cut_value']
        segment_counter -= 1
        if(segment_counter == 0):
            end_segment = wav_object[value['end_cut_value']:]
            list_of_segments.append(end_segment)

    final_list = list_of_segments[0]

    for i in list_of_segments[1:]:
        final_list += i

    return final_list
