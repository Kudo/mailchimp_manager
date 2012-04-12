MailChimp Manager
====================

1. Introduction
---------------------
MailChimp Manager is a wrapper for MailChimp.com's version 1.3 API focus on management usage

2. Installation
---------------------
- Download mailchimp_manager to somewhere and use locally
- Download whole package and use 'python setup.py install' to install globally 


3. Usage
---------------------
```python
from mailchimp_manager import MailChimpManager

listMgr = MailChimpManager.ListManager('Your-API-Key')
listMgr.subscribe('foo@bar.com')    # Add foo@bar.com to subscribed list
listMgr.unsubscribe('foo@bar.com')  # Move foo@bar.com to unsubscribed list
listMgr.listMembers()    # List subscribed list
listMgr.listMembers(MailChimpManager.ListManager.MEMBER_STATUS.SUBSCRIBED)    # List subscribed list, again
listMgr.listMembers(MailChimpManager.ListManager.MEMBER_STATUS.UNSUBSCRIBED)  # List unsubscribed list   
```

You can also put a settings.py in the program folder as global settings.

```python
API_HOST_SCHEME='http'
API_VERSION='1.3'
API_HOST='api.mailchimp.com/%s/?method=' % (API_VERSION)
API_KEY = 'Your-API-Key'
```

Then you don't need you can simply use ListManager() without specifying API key every time.

4. Limiations
---------------------
- Currently only support list management
- Currently support only one list
