#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    test_list_manager.py - Integration test for list management of mailchimp_manager
"""
try:
    from mailchimp_manager import MailChimpManager
except:
    # Local module testing - assuming mailchimp_manager folder put in grandparent folder
    import sys, os.path
    # Hack for import module in grandparent folder
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
    from mailchimp_manager import MailChimpManager
import unittest

TEST_EMAIL = u'john.doe@gmail.com'

class TestMailChimpListManager(unittest.TestCase):
    def test_Subscribe_TestEmailInSubscribedList_True(self):
        listMgr = MailChimpManager.ListManager()
        listMgr.subscribe(TEST_EMAIL)
        emails = listMgr.listMembers()
        self.assertIn(TEST_EMAIL, emails)

    def test_Unsubscribe_TestEmailInSubscribeList_False(self):
        listMgr = MailChimpManager.ListManager()
        listMgr.unsubscribe(TEST_EMAIL)
        emails = listMgr.listMembers()
        self.assertNotIn(TEST_EMAIL, emails)

    def test_Unsubscribe_TestEmailInUnsubscribeList_True(self):
        listMgr = MailChimpManager.ListManager()
        listMgr.unsubscribe(TEST_EMAIL)
        emails = listMgr.listMembers(MailChimpManager.ListManager.MEMBER_STATUS.UNSUBSCRIBED)
        self.assertIn(TEST_EMAIL, emails)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMailChimpListManager)
    unittest.TextTestRunner(verbosity=2).run(suite)
