import json
import urllib2
try:
    import settings
    API_HOST_SCHEME=settings.API_HOST_SCHEME
    API_VERSION=settings.API_VERSION
    API_HOST=settings.API_HOST
    API_KEY=settings.API_KEY
except:
    API_HOST_SCHEME='http'
    API_VERSION='1.3'
    API_HOST='api.mailchimp.com/%s/?method=' % (API_VERSION)
    API_KEY = 'Your-MailChimp-API-Key'

class ListManager(object):
    """
        Wrapper for MailChimp list API
    """

    class MEMBER_STATUS(object):
        SUBSCRIBED='subscribed'
        UNSUBSCRIBED='unsubscribed'
        CLEAND='cleaned'

    def __init__(self, apiKey=API_KEY, apiHostScheme=API_HOST_SCHEME, apiHost=API_HOST):
        self._apiUriBase = '%(scheme)s://%(apiHostPrefix)s.%(apiHost)s' % {
            'scheme': apiHostScheme,
            'apiHostPrefix': apiKey[-3:],
            'apiHost': apiHost,
        }
        self._apiKey = apiKey

    def subscribe(self, email):
        url = self._apiUriBase + 'listSubscribe'
        inputJsonObj = {
            'apikey': self._apiKey,
            'id': self.getListId(),
            'email_address': email,
            'double_optin': False,
        }
        request = urllib2.Request(url, urllib2.quote(json.dumps(inputJsonObj)), {'Content-Type': 'application/json'})
        urlObj = urllib2.urlopen(request)
        return urlObj.read()

    def unsubscribe(self, email):
        url = self._apiUriBase + 'listUnsubscribe'
        inputJsonObj = {
            'apikey': self._apiKey,
            'id': self.getListId(),
            'email_address': email,
            'delete_member': False,
            'send_goodbye': False,
            'send_notify': False,
        }
        request = urllib2.Request(url, urllib2.quote(json.dumps(inputJsonObj)), {'Content-Type': 'application/json'})
        urlObj = urllib2.urlopen(request)
        return urlObj.read()

    def getListId(self):
        """
            Currently only support one list
        """
        url = self._apiUriBase + 'lists'
        inputJsonObj = {
            'apikey': self._apiKey,
        }
        request = urllib2.Request(url, urllib2.quote(json.dumps(inputJsonObj)), {'Content-Type': 'application/json'})
        urlObj = urllib2.urlopen(request)
        resp = json.loads(urlObj.read())
        return resp['data'][0]['id']

    def listMembers(self, status=MEMBER_STATUS.SUBSCRIBED):
        url = self._apiUriBase + 'listMembers'
        inputJsonObj = {
            'apikey': self._apiKey,
            'id': self.getListId(),
            'status': status,
        }
        request = urllib2.Request(url, urllib2.quote(json.dumps(inputJsonObj)), {'Content-Type': 'application/json'})
        urlObj = urllib2.urlopen(request)
        resp = json.loads(urlObj.read())
        members = []
        for data in resp['data']:
            members.append(data['email'])
        return members
