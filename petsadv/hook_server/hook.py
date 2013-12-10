#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
log=logging.getLogger()

from bottle import route, run, template, request
import os
input_d = dict(os.environ.copy())   # Make a copy of the current environment
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
        return update_server()

def update_server():
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
    input_d['PATH'] = input_d['PATH'] + ':/home/petsquare/.rvm/bin'
    #os.system('source "/home/petsquare/.rvm/scripts/rvm" && ./compile.sh --force')
    Popen(['./compile.sh', '--force'], shell=False, env=input_d)
    return gitlog

print 'update?', update_server()
run(host='0.0.0.0', port=35423)
