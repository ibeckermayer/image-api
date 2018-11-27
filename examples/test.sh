#!/bin/bash

if [ "$1" == "" ]; then
   echo "You must specify an operation to run. See examples/json for possible test operations"
   exit 1
fi

OPERATION_FILE="./json/$1.json"

if [ ! -f $OPERATION_FILE ]; then
   echo "You must specify an operation to run. See examples/json for possible test operations"
   exit 1
fi

if [ "$2" == "" ]; then
    OUT="out.jpg"
else
    OUT=$2
fi

curl -X POST "http://localhost:5000/image/image-process" -H  "accept: application/json" -H  "Content-Type: multipart/form-data" -F "Image=@./pics/kek.jpg;type=image/jpeg" -F "Processes=@$OPERATION_FILE;type=application/json" --output $OUT