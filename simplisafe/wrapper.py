import requests
from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session
import uuid

import constants

class SimpliSafeApi(object):

    def __init__(self, username, password, sid, device_id=''):
        self.username = username
        self.password = password
        self.sid = sid
        self.device_id = device_id
        self.uuid = str(uuid.uuid1())


    def fetch_access_token(self):
        oauth = OAuth2Session(client=LegacyApplicationClient(client_id=constants.CLIENT_ID))
        return oauth.fetch_token(token_url=constants.ACCESS_TOKEN_URL,username=self.username,password=self.password,device_id=self.device_id,uuid=self.uuid,client_id=constants.CLIENT_ID, client_secret='')

    def get_state(self, access_token):
        url = constants.RESOURCE_URL + self.sid + '/state/'
        headers = {'Authorization': 'Bearer ' + access_token}
        request = requests.get(url, headers=headers)
        return request.json()

    def set_state(self, access_token, state):
        url = constants.RESOURCE_URL + self.sid + '/state/' + state
        headers = {'Authorization': 'Bearer ' + access_token}
        request = requests.post(url, headers=headers)
        return request.json()


