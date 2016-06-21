import apiKey
import getRandomPic
import postToTwitter
import subprocess

# gather image
image = getRandomPic.fileName

# change the desktop background via osascript
# probably wont work on your Mac, or will eventually stop working because Apple.

SCRIPT = """/usr/bin/osascript<<END
tell application "Finder"
set desktop picture to POSIX file "%s"
end tell
END"""

def set_desktop_background(filename):
    subprocess.Popen(SCRIPT%filename, shell=True)

set_desktop_background(image)
