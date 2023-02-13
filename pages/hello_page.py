import random
from constants.header import HeaderConsts
from constants.start_page import StartPageConst
from constants.user_profile import ProfileConsts
from pages.base_page import BasePage
from pages.utils import log_wrapper, wait_until_ok


class HelloPage(BasePage):
    """Stores methods describes hello page action"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.consts_header = HeaderConsts
        self.const_profile = ProfileConsts

    @wait_until_ok()
    @log_wrapper
    def verify_sign_out_button(self):
        """Verify sign out button"""
        assert self.is_element_visible(xpath=self.consts_header.EXIT_BUTTON_XPATH)

    @wait_until_ok()
    @log_wrapper
    def change_contact_information(self):
        """Change contact information and verify it"""
        self.click(self.consts_header.SIGN_IN_BUTTON_XPATH)
        self.fill_field(self.const.SIGN_IN_EMAIL_XPATH, value="test_321@gmail.com")
        self.fill_field(self.const.SIGN_IN_PASSWORD_XPATH, value="test123")
        self.click(self.const.SIGN_IN_BUTTON_XPATH)
        self.click(self.consts_header.PROFILE_XPATH)
        self.click(self.consts_header.USER_PROFILE_XPATH)
        self.click(self.const_profile.CHANGE_INFORMATION_XPATH)
        self.fill_field(self.const_profile.NAME_INPUT_XPATH, value="test123")
        self.fill_field(self.const_profile.LASTNAME_INPUT_XPATH, value="test333")
        self.fill_field(self.const_profile.EMAIL_INPUT_XPATH, value="test_321@gmail.com")
        self.fill_field(self.const_profile.TELEPHONE_INPUT_XPATH, value=f"0506188{random.randint(100, 999)}")
        self.click(self.const_profile.CONTINUE_BUTTON_XPATH)

        assert self.is_element_visible(xpath=self.const_profile.CHANGE_INFORMATION_XPATH)

    @wait_until_ok()
    @log_wrapper
    def history_orders(self):
        """Open history page"""
        self.click(self.consts_header.SIGN_IN_BUTTON_XPATH)
        self.fill_field(self.const.SIGN_IN_EMAIL_XPATH, value="test_321@gmail.com")
        self.fill_field(self.const.SIGN_IN_PASSWORD_XPATH, value="test123")
        self.click(self.const.SIGN_IN_BUTTON_XPATH)
        self.click(self.consts_header.PROFILE_XPATH)
        self.click(self.consts_header.USER_PROFILE_XPATH)
        self.click(self.const_profile.HISTORY_ORDERS_XPATH)
        assert self.is_element_visible(self.const_profile.HISTORY_ORDERS_VERIFY)


