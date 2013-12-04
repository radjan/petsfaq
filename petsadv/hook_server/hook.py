import logging
log=logging.getLogger()

from bottle import route, run, template, request
import os
from subprocess import Popen, PIPE

hook_key = '5e4ac67053292fe7f96c63f423e7'
hook_secret = '97c1a1c0bc10a4c90154803227066'


os.chdir('/home/petsquare/petsfaq/')
cmd1   = [ "git", "log"]
pipe   = Popen(cmd1, stdout=PIPE) 
text   = pipe.communicate()[0].splitlines()
text1  = text[2]
text2  = text[4]
gitlog = {'date':text1, 'msg':text2}



@route('/api/gitlog', method='GET')
def show_gitlog():
    global gitlog
    return gitlog

@route('/api/reload', method='POST')
def github_hook():
    global gitlog
    key = request.query.get('key',None)
    secret = request.query.get('secret',None)
    print key
    print secret

    if any ([ key    == None,
              secret == None,
              key    == '',
              secret == '',
              key    != hook_key,
              secret != hook_secret,
            ]):
        return 'fail'
    else:
        #update git
        os.chdir('/home/petsquare/petsfaq/')
        os.system('git pull') 

        cmd1 = [ "git", "log"]
        pipe = Popen(cmd1, stdout=PIPE) 
        text = pipe.communicate()[0].splitlines()
        text1 = text[2]
        text2 = text[4]
        gitlog = {'date':text1, 'msg':text2}


        #update frontend-code
        os.chdir('/home/petsquare/petsfaq/petsadv/web-frontend')
        os.system('rm -rf dist')
        os.system('./compile.sh --force')
        return gitlog


run(host='0.0.0.0', port=35423)

