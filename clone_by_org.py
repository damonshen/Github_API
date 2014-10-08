import subprocess
import os
import json

repos = json.loads(open('./eclipse_projects.txt', 'r').read())

def clone(repos):
    """@todo: Docstring for clone.

    :repos: @todo
    :returns: @todo

    """
    for i, repo in enumerate(repos):
        name = repo['full_name'].split('/')
        #divide the owner and project name
        owner = name[0]
        projectName = name[1]
        url = repo['clone_url']
        name = repo['full_name']

        #create the owner for avoiding the confict of projects with same name
        if not os.path.exists(name):
            os.makedirs(name)

        clone_shell = 'git clone ' + url + ' ' + name
        subprocess.check_output(clone_shell, shell=True)
        if i is len(repos)-1:
            print repo['id']

clone(repos)
