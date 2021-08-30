import unittest

import tgcf.const


class TestConst(unittest.TestCase):

    def test_BotMessages_start_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.start) > 3)

    def test_BotMessages_bot_help_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.bot_help) > 3)

    def test_BotMessages_user_not_admin_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.user_not_admin) > 3)

    def test_BotMessages_forward_applied_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.forward_applied) > 3)

    def test_BotMessages_display_forwards_empty_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.display_forwards_empty) > 3)

    def test_BotMessages_forward_str_title_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.forward_str_title) > 3)

    def test_BotMessages_forward_str_source_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.forward_str_source) > 3)

    def test_BotMessages_forward_str_destination_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.forward_str_destination) > 3)

    def test_BotMessages_remove_source_not_exists_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.remove_source_not_exists) > 3)

    def test_BotMessages_remove_applied_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.remove_applied) > 3)

    def test_BotMessages_style_applied_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.style_applied) > 3)

    def test_BotMessages_style_unexpected_len(self):
        self.assertTrue(len(tgcf.const.BotMessages.style_unexpected) > 3)

    def test_BotMessages_forward_usage(self):
        self.assertTrue(len(tgcf.const.BotMessages.forward_usage) > 3)
        self.assertNotIn("    ", tgcf.const.BotMessages.forward_usage)

    def test_BotMessages_style_usage(self):
        self.assertTrue(len(tgcf.const.BotMessages.style_usage) > 3)
        self.assertNotIn("    ", tgcf.const.BotMessages.style_usage)

    def test_BotMessages_remove_usage(self):
        self.assertTrue(len(tgcf.const.BotMessages.remove_usage) > 3)
        self.assertNotIn("    ", tgcf.const.BotMessages.remove_usage)
