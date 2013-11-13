import logging
log=logging.getLogger()

from bottle import route, run, template, request
import os
from subprocess import Popen, PIPE

hook_key = '5e4ac67053292fe7f96c63f423e7'
hook_secret = '97c1a1c0bc10a4c90154803227066'


@route('/api/reload', method='POST')
def github_hook():
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
        os.chdir('/home/petsquare/petsfaq/')
        os.system('git pull') 

        cmd1 = [ "git", "log"]

        pipe = Popen(cmd1, stdout=PIPE) 
        text = pipe.communicate()[0].splitlines()
        text1 = text[2]
        text2 = text[4]
        return text1+text2

run(host='0.0.0.0', port=35423)

