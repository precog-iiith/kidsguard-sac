#!/bin/bash
# Extract frames from video files
	
if [[ "$1" ]]; then
 echo "Extracting frames..."
 for entry in ~/Hercules/kidstube-data/videos/*
 do
  filename=${entry##*/}
  filename="${filename%.*}"
  echo $filename
  fps="frames_${1}fps"
  echo $fps
  mkdir -p ~/Hercules/kidstube-data/video_splits/${filename}/${fps}/
  ffmpeg -i ${entry} -r $1 -s 224x224 -f image2 ~/Hercules/kidstube-data/video_splits/${filename}/${fps}/frames_%03d.jpg
 done
else
 echo "No argument given"
fi
