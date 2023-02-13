import random
from selenium.webdriver.common.keys import Keys
from constants.header import HeaderConsts
from constants.start_page import StartPageConst
from constants.user_profile import ProfileConsts
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_wrapper, random_str


class StartPage(BasePage):
    """Stores methods describes start page actions"""

    @log_wrapper
    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.consts_header = HeaderConsts
        self.const_profile = ProfileConsts

    @wait_until_ok()
    @log_wrapper
    def sign_up(self):
        """sign up using provided values"""
        username = f"D{random_str(length=7).lower()}"
        lastname = f"{username}"
        email = f"{username}@gmail.com"
        password = "G21312ffpw2!"
        phone = f"0506188{random.randint(100, 999)}"

        # fill fields
        self.click(xpath=self.consts_header.SIGN_IN_BUTTON_XPATH)
        self.click(xpath=self.const.REGISTRATION_BUTTON_XPATH)
        self.fill_field(xpath=self.const.INPUT_FIRSTNAME_XPATH, value=username)
        self.fill_field(xpath=self.const.INPUT_LASTNAME_XPATH, value=lastname)
        self.fill_field(xpath=self.const.INPUT_EMAIL_XPATH, value=email)
        self.click(xpath=self.const.INPUT_TELEPHONE_XPATH)
        self.fill_field(xpath=self.const.INPUT_TELEPHONE_XPATH, value=phone)
        self.fill_field(xpath=self.const.INPUT_PASSWORD_XPATH, value=password)
        self.fill_field(xpath=self.const.INPUT_PASSWORD_CHECK_XPATH, value=password)
        self.click(xpath=self.const.CONTINUE_BUTTON_XPATH)

        from pages.hello_page import HelloPage
        return HelloPage(self.driver)

    @wait_until_ok()
    @log_wrapper
    def sign_in(self):
        """sign in using provided values"""
        self.click(self.consts_header.SIGN_IN_BUTTON_XPATH)
        self.fill_field(self.const.SIGN_IN_EMAIL_XPATH, value="test_321@gmail.com")
        self.fill_field(self.const.SIGN_IN_PASSWORD_XPATH, value="test123")
        self.click(self.const.SIGN_IN_BUTTON_XPATH)
        assert self.is_element_visible(xpath=self.consts_header.EXIT_BUTTON_XPATH)

    @wait_until_ok()
    @log_wrapper
    def add_item_to_cart(self):
        """add item to cart and verify"""
        self.click(xpath=self.const.CHOOSE_BRAND_XPATH)
        self.click(xpath=self.const.ITEM_BUTTON_XPATH)
        self.click(xpath=self.const.CANCEL_MASSAGE_DISCOUNT)
        self.click(xpath=self.const.SIZE_BUTTON_XPATH)
        self.click(xpath=self.const.ADD_TO_CART_BUTTON_XPATH)
        self.click(xpath=self.consts_header.CART_BUTTON_XPATH)
        assert self.const.VERIFY_ITEM_XPATH

    @wait_until_ok()
    @log_wrapper
    def sub_discount(self):
        """Create and verify email subscription"""
        self.fill_field(self.const.INPUT_SUB_XPATH, value=f"D{random_str(length=7)}@gmail.com")
        self.click(self.const.BUTTON_SUB_XPATH)
        assert self.const.VERIFY_MASSAGE_XPATH

    @wait_until_ok()
    @log_wrapper
    def search_item(self):
        """ Search item via function 'Search' and verify"""
        self.click(self.const.SEARCH_INPUT_XPATH)
        self.fill_field(self.const.SEARCH_INPUT_XPATH, value='сумка' + Keys.ENTER)
        assert self.is_element_exists(self.const.ITEM_BAG_XPATH)

    @wait_until_ok()
    @log_wrapper
    def add_item_to_favorites(self):
        """Add item to favorites page and verify"""
        self.click(self.const.CHOOSE_BRAND_XPATH)
        self.click(self.const.SAVE_ITEM_BUTTON)
        self.fill_field(self.const.SIGN_IN_EMAIL_XPATH, value="test_321@gmail.com")
        self.fill_field(self.const.SIGN_IN_PASSWORD_XPATH, value="test123")
        self.click(self.const.SIGN_IN_BUTTON_XPATH)
        self.click(self.consts_header.FAVORITES_BUTTON_XPATH)
        assert self.consts_header.FAVORITES_VERIFY_XPATH

    @wait_until_ok()
    @log_wrapper
    def contact_information(self):
        """Open contact information Pop-Up and verify"""
        assert self.is_element_visible(self.const.VERIFY_CONTACT_XPATH)

    @wait_until_ok()
    @log_wrapper
    def navigate_to_hello_page(self):
        """Navigate to hello page"""
        from pages.hello_page import HelloPage
        return HelloPage(self.driver)
