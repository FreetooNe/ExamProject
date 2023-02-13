import pytest
from constants.base import BaseConstants


# @pytest.mark.parametrize("browser", [BaseConstants.FIREFOX, BaseConstants.CHROME])
@pytest.mark.parametrize("browser", [BaseConstants.CHROME])
class TestUserProfile:
    """Tests for user-profile page"""

    def test_change_contact_information(self, start_page):
        """
         -Description: Positive test to change contact information into profile page
              - Pre-condition:
                 -Open start page
            - Steps:
                  Login via valid user
                  Open Change Contact information page
                  Fill Name, lastname, email, phone
                  Save changes
                  Verify excepted result
        """
        hell = start_page.navigate_to_hello_page()
        hell.change_contact_information()

    def test_history_orders(self, start_page):
        """
         -Description: Positive test to change contact information into profile page
              - Pre-condition:
                 -Open start page
            - Steps:
                  Login via valid user
                  Open History Page
                  Verify excepted result
        """
        hell = start_page.navigate_to_hello_page()
        hell.history_orders()
