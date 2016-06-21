import apiKey
import json
import urllib2
import os

# URL for random image from Unsplash API
url = 'https://api.unsplash.com/photos/random/?client_id=' + apiKey.Unsplash_Application_ID

# Get the random pic info JSON and load it into 'data' variable
data = urllib2.urlopen(url).read()

# Load the JSON
output = json.loads(data)

# Capture image URLs and other pic info in variables for other use
raw_URL = output['urls']['raw']
small_URL = output['urls']['small']
full_URL = output['urls']['full']
regular_URL = output['urls']['regular']
thumb_URL = output['urls']['thumb']
link_URL = output['links']['html']
userName = output['user']['username']
pic_id = output['id']

'''   NOT WORKING YET
# Figure out how to Like the picture.
headers = unsplashAuth.something
likeURL = 'https://api.unsplash.com/photos/' + pic_id + '/like'
liked = urllib2.urlopen(likeURL).read()
print (liked)
'''

# ok we have the user, the pic, and the ID let's populate a source URL

sourceURL = 'https://source.unsplash.com/user/' + userName + '/' + pic_id
sourceData = urllib2.urlopen(sourceURL).read()

print("downloading:" + sourceURL + "...")

# rename the picture, with username and image id
fileName = os.getcwd().replace("\\", "/") + "/" + userName + "_"+ pic_id + ".jpg"

print(fileName)

# write pic to file
if not os.path.exists(fileName):
    output = open(fileName, 'wb+')
    output.write(sourceData)
    output.close()
    print("Finished download " + fileName)
else:
    print("path not exists")