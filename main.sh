#!/bin/bash
export GOOGLE_APPLICATION_CREDENTIALS="/home/intel/Documents/Skeleton-7f23947fef20.json"

curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)"   -H "Content-Type: application/json; charset=utf-8"   --data "{
    'input':{
      'text':'We are Skeleton Team. We are here at the AT&T hackathon. White male age 30 is sitting on a chair hold a mouse.'
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


cat synthesize-text.txt | jq '.audioContent'


base64 synthesize-output-base64.txt --decode > synthesized-audio.mp3
