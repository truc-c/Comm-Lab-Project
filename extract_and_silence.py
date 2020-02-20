import parsing_functions as pf
import xmltodict
import pprint
import sys
import platform
from pydub import AudioSegment
from pydub.playback import play


eaf_file = sys.argv[1]
selected_audio_file = sys.argv[2]
python_version = int(platform.python_version()[0])
with open(eaf_file) as file_obj:
    eaf_obj = xmltodict.parse(file_obj.read())
is_input_valid = True

tier_name_list = pf.get_tier_names(eaf_obj)
print('List of all tiers: ')
pf.print_tiers(eaf_obj)
tier_name_prompt = 'Enter tier name: '
user_input = pf.py_version_input(python_version,tier_name_prompt)


while is_input_valid:
    if user_input in tier_name_list:
        try:
            print("\nProcess the results for [%s" %user_input + "] tier\n")
            annotation_values = pf.combined_process(eaf_obj,user_input)
            pprint.pprint(annotation_values)
        except:
            print('There are no annotations in the tier: ', user_input)

        diff_tier_prompt = 'Would you like to select another tier? (y = yes , n = no, 0 = exit): '
        user_input = pf.py_version_input(python_version,diff_tier_prompt)

        if user_input == 'y':
            user_input = pf.py_version_input(python_version,tier_name_prompt)
            continue
        elif user_input == '0':
            sys.exit()
        else:
            is_input_valid = False
            break
    else:
        pf.no_valid_results(tier_name_list)
        user_input = pf.py_version_input(python_version, tier_name_prompt)

        if user_input == '0':
            sys.exit()

        continue


audio_silence_question = 'Would you like to silence the audio file? (y = yes, n = no, 0 = exit): '
audio_user_prompt = pf.py_version_input(python_version, audio_silence_question)
if audio_user_prompt == '0':
    sys.exit()

print('\nEnter the tier name that you would like to silence: ')
pf.print_tiers(eaf_obj)
tier_name_prompt = 'Enter tier name: '
user_input = pf.py_version_input(python_version,tier_name_prompt)
annotation_values = pf.combined_process(eaf_obj,user_input)
audio_object = AudioSegment.from_wav(selected_audio_file)
silenced_product = pf.silence_segments(annotation_values, audio_object)

rename_wav = pf.modify_filename(sys.argv[2])
silenced_product.export(rename_wav, format="wav")
