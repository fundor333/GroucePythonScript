import os
import urllib, hashlib
import subprocess
from git import Repo

# Set your variables here
email = "someone@somewhere.com"
default = "http://www.example.com/default.jpg"
size = 40

join = os.path.join
repo = Repo(self.rorepo.working_tree_dir)
assert not repo.bare
commit_list = list(repo.iter_commits('master'))

# construct the url
gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
gravatar_url += urllib.urlencode({'d':default, 's':str(size)})

subprocess.call(["gource","-1024x768","--seconds-per-day 1","--stop-position 1.0", "--highlight-all-users", "--hide-filenames","--output-framerate 60","--output-ppm-stream output.ppm", "--user-image-dir .git/avatar/","--title 'Magic'","--hide dirnames,filenames,usernames"])
subprocess.call(["ffmpeg", "-y", "-r 60", "-f image2pipe", "-vcodec ppm", "-i output.ppm" ,"-vcodec wmv1", "-r 60", "-qscale 0" ,"out.wmv"])
