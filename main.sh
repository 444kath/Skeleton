#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS="Skeleton-7f23947fef20.json"
source /opt/intel/computer_vision_sdk/bin/setupvars.sh 

age=15
gender="male"
emotion="happy"
sampleString="30 year old male. He looks happy."

#python face_parse.py > $sampleString
python face_parse.py 






curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"   -H "Content-Type: application/json; charset=utf-8"   --data "{
    'input':{
      'text':'Activity alert: There is a $sampleString '
    },
    'voice':{
      'languageCode':'en-gb',
      'name':'en-GB-Standard-A',
      'ssmlGender':'FEMALE'
    },
    'audioConfig':{
      'audioEncoding':'MP3'
    }
  }" "https://texttospeech.googleapis.com/v1/text:synthesize" > synthesize-text.txt


cat synthesize-text.txt | jq -r '.audioContent' > synthesize-output-base64.txt

#cat synthesize-output-base64.txt

#jsonVar=$( cat synthesize-text.txt )

#echo $jsonVar

base64 synthesize-output-base64.txt --decode > synthesized-audio.mp3

rhythmbox-client synthesized-audio.mp3 --play
