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

## Step 1: Check if Python 3 is already available on current computer
1. Open terminal by typing cmd+spacebar and an white window will open, similar to the picture below (mine is black)
<img src="images/terminal.png" width="500">
2. Type 'python3' (without the quote) into the terminal window text similar to the picture will show if you have python 3 installed.  The green square shows that I typed python3 into the terminal, the green underline shows that I have initiated python3, and the green arrow pointing to the three greater than signs (>>>) indicates that I am currently working in the python environment.
<img src="images/terminal_python.png" width="500" >
3. Do not close terminal

## If Python 3 is not on the computer, please download the latest edition of Python:
Python version 3 is available for download here: [python](https://www.python.org/downloads/)

## Step 2: Check if pip/pip3 is installed on the computer:
1. Terminal should still be open and you may still be in python (indicated by these >>>). Please exit out of python by typing 'exit()' without the quotations similar to the image below:
<img src="images/exit_python.png" width="100" >
2. In terminal, type 'pip --version' without quotations and if you receive a message different from what is shown in the image below (in the green underline), that may indicate that pip is not installed.  The picture below shows that I have pip installed.
<img src="images/check_pip.png" width="500" >

- However, if you receive a 'command not found' message, this means pip/pip3 is not installed:

```python
command not found
```

## If pip/pip3 is not installed, please download pip/pip3
1. Right click on this link -> [pip](https://bootstrap.pypa.io/get-pip.py) and select Download Linked File or Save Link As.
<img src="images/download_linked_files.png" width="150" >
2. Click on the Finder icon in your dock, then look for the Downloads tab, and there you will find the 'get-pip.py' file.  Please move/click/drag this file to the desktop.  The pictures should help guide you:
<img src="images/finder_dock.png" width="100" >
<img src="images/download_folder_pip_file.png" width="300" >
3. Let's navigate to the desktop by typing 'cd /users/AccountName/desktop'.  You will be replacing 'AccountName' with your AccountName.  You can find this in the terminal.  I have encased mine in a green box as an example.  The picture should help:
<img src="images/desktop.png" width="400" >
4. Now let's run the get-pip.py file that we just downloaded.  Type 'python3 get-pip.py' into the terminal, just like it is shown in the picture:
<img src="images/run_get_pip.png" width="400" >


## Step 3: Install pydub and xmltodict:
We will use pip to install xmltodict and pydub.  These modules will be used in the silencing and parsing of the audio file and .eaf file
1. In your terminal, type 'pip3 install pydub --user' without the quotations, just like the picture below:
<img src="images/pydub.png" width="400" >
2. Next, after pydub is finishing installing, type 'pip3 install xmltodict --user' without the quotation, just like the picture below:
<img src="images/xmltodict.png" width="400" >

## Step 4: Set/Edit the PATH Environment
Now that the modules pydub and xmltodict have been downloaded, we need to tell Python where to look for them.
1. In terminal, type 'cd /users/AccountName' (w/o quotes), replace AccountName with yours.
<img src="images/user_directory.png" width="300" >
2. Next, we the bash_profile to set our PATH, type 'nano .bash_profile' (w/o quotes).
<img src="images/nano_bash_profile.png" width="300" >
3. You will then be directed to another window that looks similar to the one in the picture below.  There you will type what I have in the red box, then control+x to exit.
<img src="images/add_path.png" width="500" >
4. Then you'll be asked to save. Enter 'y' (w/o quotes).
<img src="images/confirm_path.png" width="400" >
5. Then you'll be asked to write to .bash_profile, hit enter/return on the keyboard.
<img src="images/write_to_bash_profile.png" width="300" >
6. Exit terminal application.
<img src="images/quit_terminal.png" width="200" >
7. Open terminal application again by typing cmd+spacebar, then 'terminal' and hit enter.  We need to check to see if the path that we entered in works, type :
<img src="images/terminal_python.png" width="500" >
8. In the terminal, type 'python3' (w/o quotes), then type 'import xmltodict' (w/o quotes).  See picture below.
<img src="images/module_xmltodict_check.png" width="500" >
9. If you do not get an error, such as the example below, on the next line after typing 'import xmltodict' then you're all set:
``` python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'xmltodict'
```
## Step 5: Download Zip Folder and Extract Contents
Navigate to this link: [main page](https://github.com/truc-c/Comm-Lab-Project)
1. Select the green 'Clone or download' pull down menu.
2. Select 'Download ZIP'.  One of two things may happen, a folder or ZIP named 'Comm-Lab-Project-master' file will be downloaded.
3. On the computer, find the 'Downloads' folder.  Move this folder or ZIP to your desktop.
- If it is a ZIP (the icon will look like a file with a zipper on it) you will need to unzip the file which will then reveal the folder
- If it is a folder icon, you don't need to do anything else.
4. 

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

## Running the code in MacOS terminal:
The sample coded provided is ran in MacOS terminal along with .eaf file name.  The .eaf and .wav files can be dragged into the terminal or typed in.
- for example: 
```python
python3 -W ignore extract_and_silence.py /path/to/file/name/sample.eaf /path/to/audio/file/sample.wav
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
(e.g.,[ELAN_sample.eaf](https://github.com/truc-c/Comm-Lab-Project/blob/master/raw%20data/ELAN_sample.eaf) contains 2 TIER_ID's, cut and bookmark)
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
