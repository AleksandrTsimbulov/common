"""
2018.01.31 by Alexander Tsimbulov
the simplest speech-to-text script converts all .wav audio files from 'recordings' folder into text. The result is
written to translated.txt file by adding it to the end.

text output:
    audiofilename\n
    converted_text\n
    ....
    other files
    ...
    The following files have been proceeded: list_of_files \n

known issues:
- The IMB Watson doesn't proceed some files for unknown reason. The final result doesn't include final:True flag, which
leads to raising a ConnectionClosed Error from websockets.exceptions.ConnectionClosed. Current implementation prints
the error message to the file, skips it and proceed with other files

- Only .wav audio formats are proceeded at the moment. To work with other formats audio_content_type variable should
be specified

- Username and password used in the script are for development purpose only and subject to change in release.

"""


import os
from ws_speech_to_text_v1 import WSSpeechToTextV1

recordings = [f"./recordings/{x}"
              for x
              in os.listdir('./recordings')]


username = '0c6d792b-cbad-4a86-b60b-d157254f07c7'
password = 'FtiOgb1F4OZO'
audio_content_type = 'audio/wav'

ws = WSSpeechToTextV1(username=username, password=password)

for record in recordings:
    with open(record, 'rb') as audiofile:
        try:
            results = ws.recognize(file_object=audiofile,
                                   content_type=f"{audio_content_type}",
                                   )
            with open('translated.txt', 'a') as file:
                file.write(record + ' :\n')
                file.write(results['results'][0]['alternatives'][0]['transcript'] + '\n')
            print('done' + ' ' + record)
        except Exception as e:
            # print(e)
            with open('translated.txt', 'a') as file:
                file.write(f'{record} was not proceeded successfully and the following exception have been raised:'
                           f' {e}\n')
            continue
with open('translated.txt', 'a') as file:
    file.write(f'The following files have been proceeded: {recordings} \n')
print('done all')
