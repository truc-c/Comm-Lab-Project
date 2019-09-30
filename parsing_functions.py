'''
wrapper_time_slot() takes us to the TIME_SLOT elements.  This functions takes an
    argument of an eaf_object and returns a type list of TIME_SLOT elements.
'''
def wrapper_time_slot(eaf_object):
    time_slot_list = eaf_object['ANNOTATION_DOCUMENT']['TIME_ORDER']['TIME_SLOT']

    return time_slot_list


'''
wrapper_tiers() takes us to the TIER elements.  This functions takes an argument
    of an eaf_object and returns a list or dict depending on how many TIERs there
    are.  If there is only one TIER then this function will return a dict, else, 
    the function returns a list.
'''
def wrapper_tiers(eaf_object):
    tier_object = eaf_object['ANNOTATION_DOCUMENT']['TIER']

    return tier_object

'''
wrapper_tier_name() checks for the TIER name provided by the user.  This function
    takes an 2 arguments, an eaf_object and a string value for tier_name.

The functions checks the type of the return value from the function 
    wrapper_tiers(), then checks to see if the TIER name provided by 
    the user is valid or not.

The reason for checking the type of the return value from the function
    wrapper_tiers() is so we can perform the appropriate action whether
    it be working with a list or a dict.
'''
def wrapper_tier_name(eaf_obj,tier_name):
    tier_element = wrapper_tiers(eaf_obj)

    if isinstance(tier_element, dict):
        requested_tier = tier_element['@TIER_ID']
    else:
        for each_tier in tier_element:
            if each_tier['@TIER_ID'] == tier_name:
                requested_tier = each_tier

    return requested_tier


'''
wrapper_annotations() navigates us to the ANNOTATIONS that reside in the 
    TIERs.  There are 2 arguments provided, eaf_object and the tier_name.

The code inside the wrapper_annotations() function handles .eaf files
    with one tier or multiple tiers and adds on the ANNOTATION element
    and then returns a type dict of ANNOTATIONS or a list of ANNOTATIONS
'''
def wrapper_annotations(eaf_obj, tier_name):
    tier_element = wrapper_tiers(eaf_obj)

    if isinstance(tier_element,dict):
        return tier_element['ANNOTATION']
    
    tier_list = wrapper_tier_name(eaf_obj, tier_name)['ANNOTATION']

    return tier_list


'''
extract_annotations() pulls attribute values from the ALIGN_ANNOTATION element.
    This function takes 2 arguments, an eaf object and a tier name provided by
    the user.
    
In the body of the code the if-statement checks to see if whether the TIER element
    is a dict or list.
'''
def extract_annotations(eaf_obj,tier_name):
    annotation_element = wrapper_annotations(eaf_obj,tier_name)
    annotation_product = {}
    annotation_id = ''
    time_slot_ref1 = 0
    time_slot_ref2 = 0
    annotation_value = ''

    if isinstance(annotation_element,dict):
        annotation_id = annotation_element['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']
        time_slot_ref1 = annotation_element['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF1']
        time_slot_ref2 = annotation_element['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF2']
        annotation_value = annotation_element['ALIGNABLE_ANNOTATION']['ANNOTATION_VALUE']
        annotation_product[annotation_id] = {'start_cut_ref': time_slot_ref1, 'start_cut_value': 0,
                                                'end_cut_ref':time_slot_ref2, 'end_cut_value':0,
                                                'annotation_value':annotation_value}
    else:
        for each_align in annotation_element:
            annotation_id = each_align['ALIGNABLE_ANNOTATION']['@ANNOTATION_ID']
            time_slot_ref1 = each_align['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF1']
            time_slot_ref2 = each_align['ALIGNABLE_ANNOTATION']['@TIME_SLOT_REF2']
            annotation_value = each_align['ALIGNABLE_ANNOTATION']['ANNOTATION_VALUE']
            annotation_product[annotation_id] = {'start_cut_ref': time_slot_ref1, 'start_cut_value': 0,
                                                    'end_cut_ref':time_slot_ref2, 'end_cut_value':0,
                                                    'annotation_value':annotation_value}

    return annotation_product


'''
get_tier_names function takes an xml object as its argument.

The function returns a list of all the tier names.
'''
def get_tier_names(eaf_object):
    tier_object = wrapper_tiers(eaf_object)
    tier_names = []

    if isinstance(tier_object,dict):
        return tier_object['@TIER_ID']
    else:
        for tier_name in tier_object:
            tier_names.append(tier_name['@TIER_ID'])

        return tier_names    


'''
simple function that prints all tiers
'''
def print_tiers(eaf_object):
    tier_list = get_tier_names(eaf_object)

    if isinstance(tier_list, str):
        print(tier_list)
    else:
        for each_name in tier_list:
            print(each_name)


'''
extract_timeid_and_value function takes an xml object as its argument.

This function returns a dict of {TIME_SLOT_ID : TIME_VALUE}

In the ANNOTATION section, there are 2 TIME_SLOT_REF's which are used by
    TIME_SLOT_ID to reference the time of the annotation.
'''
def extract_timeid_and_value(eaf_object):
    time_order = wrapper_time_slot(eaf_object)

    time_slot_dict = {}
    for each_time_slot in time_order:
        time_id = each_time_slot['@TIME_SLOT_ID']
        time_value = each_time_slot['@TIME_VALUE']
        time_slot_dict[time_id] = int(time_value)

    return time_slot_dict

'''
fill_time_values function takes 2 arguments.  The first argument is the object
    assigned from the return value of extract_timeid_and_value function.  The second argument
    is another object assigned from the return value of extract_annotations function.

This function fills the empty values belonging to the keys 'start_cut_value' and
    'end_cut_value'.
'''
def fill_time_values(timeid_and_values, annotation_dict):
    cut = timeid_and_values
    for i in annotation_dict.values():
        start_ref = i['start_cut_ref']
        end_ref = i['end_cut_ref']
        i['start_cut_value'] = timeid_and_values.get(start_ref)
        i['end_cut_value'] = timeid_and_values.get(end_ref)


'''
combined_process() function is a combination of functions.

I created this function to shorten the sample_code.py
'''
def combined_process(eaf_obj, user_input):
    time_ids_and_values = extract_timeid_and_value(eaf_obj)
    annotations = extract_annotations(eaf_obj,user_input)
    fill_time_values(time_ids_and_values,annotations)

    return annotations


'''
no_valid_results is a function that prints a string response if a user is
    prompted to enter a tier name and the tier name does not exist

It takes an argument of an object of type list returned from the
    get_tier_names function.
'''
def no_valid_results(list_of_tiers):
    print("\nTier name does not exist. Please enter one of the following tier names or enter 0 to exit:")

    for names in list_of_tiers:
        print(names)


'''
py_version_input function takes 2 arguments.  First argument is the object returned from
    using the module platform (ex: python_version = int(platform.python_version()[0]) ).
    The second argument is a string in the form of a question.

This chooses the correct syntax of getting user input depending on whether this
    code is ran on python 2 or 3.

The return value can be a char or literal string.  Whichever you prefer.
'''
def py_version_input(py_version, question):
    if(py_version == 3):
        tier_name_input = input('\n%s' % question)
    else:
        tier_name_input = raw_input('\n%s' % question)

    return tier_name_input


'''
This is a personal preference function that we use to rename our newly silenced
    audio file.

modify_filename is a function that takes 1 argument, a filename path.

This filename path is split into a list using the forward slash (/) as the
    delimiter.

The return value is a path name along with the .wav file extension.

For example:

    /users/lab/desktop/my_test.wav (this is was the path to the .wav file to be silenced)

    modify_filename returns:

    /users/lab/desktop/my_test_scrubbed.wav
'''
def modify_filename(filename_path):
    scrubbed_string = '_scrubbed'
    split_string = filename_path.split('/')
    reuse_file_path = '/'.join(split_string[:-1]) + '/'
    last_index = split_string[-1]   # name of sound wav
    file_name = last_index[:-4]     # file name without the .wav extension
    dot_wav_ext = last_index[-4:]   # .wav part
    new_name = file_name + scrubbed_string + dot_wav_ext
    reuse_file_path = reuse_file_path + new_name

    return reuse_file_path


'''
silence_segments is a function that takes 2 arguments.

# ============  THIS PART IS A MUST FOR THIS FUNCTION TO WORK =============

First argument, 'annotations', is an xml object with the time values for 'start_cut_value'
    and 'end_cut_value' filled.

# =========================================================================

The second argument is the a wav object (created from AudioSegment()).

This function returns a wav object with the specified times
    (start_cut_value and end_cut_value) silenced out.
'''
def silence_segments(annotations, wav_object):
    holder = 0000
    segment_counter = len(annotations)
    list_of_segments = []

    for key,value in annotations.items():
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

    final_audio = list_of_segments[0]

    for i in list_of_segments[1:]:
        final_audio += i

    return final_audio