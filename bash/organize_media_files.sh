# Organize media files
#
# Many types of files buried at different levels of folders and it it becoming hard to track them.
# Create a script to make folders for "images", "music", "and "videos",
# and move the appropriate files to them. There are also old log files scattered in the folders.
# Delete the old log files since they are not needed anymore.

# Setup the problem:
#
# Make a folder called temp, cd into it, and put this script in it.
# Create a subdirectory called temp2.
# Run this script to build the test files in temp2.
# Write a script to solve the problem.


echo "Current directory is:"
pwd
echo "Implement script? (y/n)"
read response
if [ $response = "y" ]
then
  echo "* Backup temp2 to temp2old *"
  rm -r temp2old
  mv temp2 temp2old
  mkdir temp2
  cd temp2

  echo "* Files to test move.sh *"
  :> picture1.jpg
  :> picture2.png
  :> music1.mp3
  :> music2.flac
  :> video1.mov
  :> video2.avi
  mkdir other_files
  :> other_files/picture3.jpg
  :> other_files/data.log
  mkdir other_files/more_files
  :> other_files/more_files/music3.mp3
  :> other_files/more_files/data2.log
  find . -exec echo {} \;
else
  echo "Exiting without implementing script."
fi
