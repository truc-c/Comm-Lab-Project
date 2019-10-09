# Silence .eaf Audio Segments

**University of California, Los Angeles**\
Communications Department\
Lab of Professor Anne Warlaumont

**Mentors:**\
Anne Warlaumont\
UCLA Professor\
https://www.annewarlaumont.org

Kyle MacDonald\
UCLA Postdoc Researcher\
https://kemacdonald.com

**Contributors:**\
Anne Warlaumont

Kyle MacDonald

Vicky Chen\
Double Major: Business Economics and Communication\
UCLA Anderson School of Management: Masters of Science in Business Analytics

Curt Chang\
Major: Commuications w/ Computing Specialization


Greetings,

Thank you for taking the time to take a look at our project!

Our most important task as Research Assistants is to ensure the privacy of particpants as we vet audio recordings.  ELAN is
a software tool that we utilize to annotate time selections of the sensitive information during the vetting process.  ELAN
creates a A file extension of type (.eaf) that containing annotations and their associated time segments.  

Opening the file (.eaf) with a text editor displays the ELAN information (annotation and time selections) in XML format.  We
utilize Python and the module [xmltodict](https://pypi.org/project/xmltodict/) to extract this information, such as annotated text, selected tiers, time slots, etc.  

After we have extracted the time segments (from the .eaf file) that contain the sensitive information of the
participants, we use the module [pydub](https://pypi.org/project/pydub/) to silence out those time segments.

P.S.

Special thank you to James Robert (http://jiaaro.com) for his guidance on using the pydub module.

## Download and install Python 3:
- Python version 3 is available for download here: [python](https://www.python.org/downloads/release/python-374/)

## Install pip:
- [pip](https://pip.pypa.io/en/stable/installing/)

## pip install pydub and xmltodict:
- We used pip to install xmltodict and pydub.  In terminal (MacOS) or command prompt (Windows OS) you can perform a pip install.

pip install xmltodict --user\
pip install pydub --user


## Modules:
- [xmltodict](https://pypi.org/project/xmltodict/)
- [pydub](https://pypi.org/project/pydub/)
- os
- sys
- platform
- pprint

Modules os, sys, platform and pprint are built-in modules.  


## Sample audio, Sample .eaf file, and Sample code:
- [sample audio](https://github.com/truc-c/Comm-Lab-Project/tree/master/raw%20data)
- [sample .eaf](https://github.com/truc-c/Comm-Lab-Project/tree/master/raw%20data)
- [extract_and_silence](https://github.com/truc-c/Comm-Lab-Project/blob/master/extract_and_silence.py)

The sample_audio.wav is a 30 second audio of Curt Chang counting from 1 to 30.\
The ELAN_sample.eaf are annotations that Curt Chang has made using ELAN.\
The software is available for download here: [ELAN](https://tla.mpi.nl/tools/tla-tools/elan/)

## Running the code in MacOS terminal and Windows:
The sample coded provided is ran in MacOS terminal along with .eaf file name.  The .eaf and .wav files can be dragged into the terminal or typed in.
- for example: 
```python
python -W ignore extract_and_silence.py /path/to/file/name/sample.eaf /path/to/audio/file/sample.wav
```

We use '-W ignore' to ignore this warning:
-  RuntimeWarning: Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work
  warn("Couldn't find ffmpeg or avconv - defaulting to ffmpeg, but may not work", RuntimeWarning)



## Documentation:
Here are some examples of how to use the functions and their output.

### imports:
```python
import parsing_functions as pf
import xmltodict
import pprint
import sys
import platform
```

- myproject is a folder where we stored our parsing_functions.py
- `xmltodict` module is used to create a xml object from our .eaf file
- `pprint` module helps with the format of the output
- `sys` module is used to provide an additional argument (path to eaf file) when running our python code in terminal
- `platform` is used to check our python version

### code example of functions and their output:
get_tier_names(eaf_obj) 
- returns a list of all the TIER_ID's in the .eaf file\
(e.g.,[ELAN_sample.eaf](https://github.com/truc-c/Comm-Lab-Project/blob/master/ELAN_sample.eaf) contains 2 TIER_ID's, cut and bookmark)
```python
with open(eaf_file) as file_obj:
    eaf_obj = xmltodict.parse(file_obj.read())
tier_name_list = pf.get_tier_names(eaf_obj)

print(tier_name_list)             # output: [cut,bookmark]
```

py_version_input(python_version,tier_name_prompt) 
- selects the input format depending on the python version and returns a string
```python
python_version = int(platform.python_version()[0])
tier_name_prompt = 'Enter tier name: '
user_input = pf.py_version_input(python_version,tier_name_prompt)
```

extract_timeid_and_value(eaf_obj)
- retrieves the values for TIME_SLOT_ID and TIME_VALUE in the TIME_ORDER tag from the .eaf file and returns a dict
```python
with open(eaf_file) as file_obj:
    eaf_obj = xmltodict.parse(file_obj.read())
time_ids_and_values = pf.extract_timeid_and_value(eaf_obj)

print(time_ids_and_values)        # output: {'ts1': 4670, 'ts2': 7310, ...,'ts11': 25605, 'ts12': 28445}
```

extract_annotations(eaf_obj,user_input)
- creates a nested dict that contains the ANNOTATION_ID, TIME_SLOT_REF1, TIME_SLOT_REF2, and ANNOTATION_VALUE
- this function requires 2 arguments, the eaf object and user input of the requested tier name returned from the py_version_input() function
- in addition, we use pprint() to better format the output
- NOTICE: the keys start_cut_value and end_cut_value are empty (0).  These values will be filled with the next function fill_time_values() 
```python
with open(eaf_file) as file_obj:
    eaf_obj = xmltodict.parse(file_obj.read())
user_input = pf.py_version_input(python_version,tier_name_prompt)

annotation_values = pf.extract_annotations(eaf_obj,user_input)

pprint.pprint(annotation_values)

# output: {'a1': {'annotation_value': 'cc: five six seven',
#        'end_cut_ref': 'ts2',
#        'end_cut_value': 0,
#        'start_cut_ref': 'ts1',
#        'start_cut_value': 0},
#        ...
```

fill_time_values(time_ids_and_values,annotation_values)
- ! IMPORTANT ! before using, this function REQUIRES the dict returned from the function extract_timeid_and_value(eaf_obj)
- this function does not return anything, but only fills the values inside our annotation_values object from the extract_annotations(eaf_obj,user_input) function
```python
with open(eaf_file) as file_obj:
    eaf_obj = xmltodict.parse(file_obj.read())
time_ids_and_values = pf.extract_timeid_and_value(eaf_obj)
annotation_values = pf.extract_annotations(eaf_obj,user_input)

pf.fill_time_values(time_ids_and_values,annotation_values)

# output: {'a1': {'annotation_value': 'cc: five six seven',
#        'end_cut_ref': 'ts2',
#        'end_cut_value': 7310,
#        'start_cut_ref': 'ts1',
#        'start_cut_value': 4670},
#        ...
```

silence_segments(annotation_values,audio_object)
- ! IMPORTANT ! before using, this function REQUIRES the annotation dict returned from the extract_annotations() function
- ! IMPORTANT ! before using, the function fill_time_values() must be called on the returned dict from extract_annotations()
please see code above
- this function takes 2 arguments, first argument is the returned dict and the second argument is audio wave object created from AudioSegment
- this function returns the an audio object with the time segments, provided by start_cut_value and end_cut_value, silenced
- (Optional play function)
- the module simpleaudio is need to use the play() function
```python
pip install simpleaudio
```
- pydub has a play() function to listen to the silenced audio
```python
from pydub.playback import play
... #skipped some code
annotation_values = pf.extract_annotations(eaf_obj,user_input)
pf.fill_time_values(time_ids_and_values,annotation_values)

audio_object = AudioSegment.from_wav(selected_audio_file.strip())
silenced_audio_object = pf.silence_segments(annotation_values,audio_object)
play(silenced_audio_object)
```
