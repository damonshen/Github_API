#!/usr/bin/python
import subprocess
import json

response = subprocess.check_output('curl -s https://api.github.com/repositories', shell=True)
repos = json.loads(response)
print repos
for repo in repos:
    print repo['full_name'], "\n", repo['url'], "\n"
    lang = subprocess.check_output('curl -s '+repo['languages_url'], shell=True)
    lang_dict = json.loads(lang)
    if len(lang_dict) is 1:
        print lang_dict, '\n-----------------\n'
    #subprocess.check_output('git clone '+repo['clone_url'], shell=True)
