import pytest
from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.FIREFOX])
class TestStartPage:
    """Tests for start page """

    def test_register_user(self, start_page):
        """
         -Description: Positive test to register new user
              - Pre-condition:
                 -Open start page
             - Steps:
                  Open register-form
                  Fill FirstName, LastName, EMAIl, Phone and Password fields
                  Click on register button
                  Verify excepted result
        """
        # register new user
        register_user = start_page.sign_up()
        # verify sign_out button
        register_user.verify_sign_out_button()

    def test_add_item_to_cart(self, start_page):
        """
         -Description: Positive test to add item to cart
              - Pre-condition:
                 -Open start page
            - Steps:
                  Click on Brand
                  Add item to cart
                  Verify excepted result
        """
        start_page.add_item_to_cart()

    def test_sub_discount(self, start_page):
        """
         -Description: Positive test make a subscription
              - Pre-condition:
                 -Open start page
            - Steps:
                  Fill Email
                  Click on button subscribe
                  Verify excepted result
        """

        start_page.sub_discount()

    def test_sign_in(self, start_page):
        """
         -Description: Positive test to register new user
              - Pre-condition:
                 -Open start page
            - Steps:
                  Click on Brand
                  Add item to cart
                  Verify excepted result
        """
        start_page.sign_in()

    def test_search_item(self, start_page):
        """
         -Description: Positive test function search items
              - Pre-condition:
                 -Open start page
            - Steps:
                  Find item via function "Search"
                  Verify excepted result
        """
        start_page.search_item()

    # def test_add_item_to_favorites(self, start_page):
    #     """
    #      -Description: Positive test to add items for favorites
    #           - Pre-condition:
    #              -Open start page
    #         - Steps:
    #               Click on Heart near item
    #               Fill Email and Password
    #               Click on Favorites button
    #               Verify excepted result
    #     """
    #     start_page.add_item_to_favorites()

    def test_contact_information(self, start_page):
        """
         -Description: Positive test to check contact information
              - Pre-condition:
                 -Open start page
            - Steps:
                  Click on contact-Information button
                  Verify excepted result
        """
        start_page.contact_information()
