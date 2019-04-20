University of California, Los Angeles
Communications Department
Lab of Professor Anne Warlaumont
https://www.annewarlaumont.org

Mentor:
Kyle MacDonald
UCLA Postdoc Researcher
https://kemacdonald.com

Contributors:
Kyle MacDonald

Vicky Chen
Double Major: Business Economics and Communication

Curt Chang
Major: Commuications w/ Computing Specialization



Hello Everybody,

Thank you for taking the time to take a look at our project!

Our most important task as Research Assistants is to ensure the privacy of particpants as we vet audio recordings.  ELAN is a software that we use to help us annotate time selections of the sensitive information during the vetting process.  A file extension of type (.eaf) is created, which contains annotations of text and time selections associated with it.  Opening the file (.eaf) with a text editor displays the ELAN information (annotation and time selections) in XML format.  We utilize Python and the module/package xmltodict to extract this information, such as annotated text, selected tiers, time slots, etc.

Currently in progress:

After extracting the information, we will use the time selection to silence portions of the audio where it contains sensitive information about the participants.
