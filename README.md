# Silence .eaf Audio Segments

**University of California, Los Angeles**\
Communications Department\
Lab of Professor Anne Warlaumont\
https://www.annewarlaumont.org

**Mentors:**\
Anne Warlaumont

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

Special thank you to James Robert (http://jiaaro.com) for his guidance on using the pydub module/package.


## Modules used:
- [xmltodict](https://pypi.org/project/xmltodict/)
- [pydub](https://pypi.org/project/pydub/)
- os
- sys
- platform
- pprint

## Sample audio:
- [sample](https://github.com/truc-c/Comm-Lab-Project/blob/master/sample_audio.wav)

The sample_audio.wav provided is a simple of Curt Chang counting from 1 to 30.
