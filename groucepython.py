import os
import re
import hashlib
import subprocess
import urllib
import time

# Set your variables here
directory = ".git/avatar/"
size = 40

if (os.path.exists('.git')):
    if not os.path.exists(directory):
        os.makedirs(directory)

    process = subprocess.Popen('''git log --pretty=format:"%ae,%an"'''.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    if (error == None):
        dictionary = {}
        for l in output.split('\n'):
            email, name = re.findall(r'"(.*?),(.*?)"', l)[0]
            dictionary[email] = name

        for email in dictionary.keys():
            name = dictionary[email]
            gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
            gravatar_url += urllib.urlencode({'d': "http://www.example.com/default.png", 's': str(size)})
            gravatar_name = directory + name + '.png'
            print("Getting image for " + name + " from url " + gravatar_url)
            urllib.urlretrieve(gravatar_url, gravatar_name)

        subprocess.call(["gource","-1024x768","--seconds-per-day 1","--stop-position 1.0", "--highlight-all-users", "--hide-filenames","--output-framerate 60","--output-ppm-stream output.ppm", "--user-image-dir .git/avatar/","--title 'Magic'","--hide dirnames,filenames,usernames"],shell=True)
        subprocess.call(["ffmpeg", "-y", "-r 60", "-f image2pipe", "-vcodec ppm", "-i output.ppm" ,"-vcodec wmv1", "-r 60", "-qscale 0" ,"out.wmv"],shell=True)
