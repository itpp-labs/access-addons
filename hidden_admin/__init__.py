def post_load():
    """Delete tests, that check behavior changed by this module"""
    from openerp.addons.mail.tests.test_mail_message import TestMailMessage
    del TestMailMessage.test_50_mail_flow_access_rights
    del TestMailMessage.test_40_message_vote
