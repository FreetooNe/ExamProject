class StartPageConst:
    """Stores constants related to start page"""

    # Sign in
    SIGN_IN_EMAIL_XPATH = "//*[@id='form_login']/div[1]/input"
    SIGN_IN_PASSWORD_XPATH = "//*[@id='form_login']/div[2]/input"
    SIGN_IN_BUTTON_XPATH = ".//input[@type='submit']"
    SIGN_IN_VERIFY_MASSAGE = ".//h1[@class='card-title']"
    # Sign Up
    REGISTRATION_BUTTON_XPATH = ".//a[@class='nav-item nav-link text-uppercase text-uppercase']"
    INPUT_FIRSTNAME_XPATH = ".//input[@name = 'firstname' and @required]"
    INPUT_LASTNAME_XPATH = ".//input[@name = 'lastname' and @required]"
    INPUT_EMAIL_XPATH = "//*[@id='form_register']/div[2]/div[1]/input"
    INPUT_TELEPHONE_XPATH = ".//input[@name = 'telephone' and @required]"
    INPUT_PASSWORD_XPATH = "//*[@id='form_register']/div[3]/div[1]/input"
    INPUT_PASSWORD_CHECK_XPATH = ".//input[@name = 'confirm' and @required]"
    CONTINUE_BUTTON_XPATH = ".//button[@class='btn btn-primary btn-block']"

    # items
    CHOOSE_BRAND_XPATH = ".//img[@alt='luisa-cerano']"
    CHOOSE_BRAND_XPATH_TEST = ".//a[@href='./uk/brands/luisa-cerano/']"
    ITEM_BUTTON_XPATH = "//*[@id='content']/div/div[3]/div[2]/div"
    CANCEL_MASSAGE_DISCOUNT = ".//div[@class='popmechanic-close']"
    SIZE_BUTTON_XPATH = "//*[@id='product']/div[7]/div/ul/li[5]/label/span"
    ADD_TO_CART_BUTTON_XPATH = ".//button[@id='button-cart']"
    SAVE_ITEM_BUTTON = ".//button[@data-id='9397']"

    # checkout
    VERIFY_ITEM_XPATH = "//*[@id='cart-block']/div[5]/div/span[1]"

    # footer
    INPUT_SUB_XPATH = "//*[@id='tab_subscribe_email']/form/div/input"
    BUTTON_SUB_XPATH = ".//button[@type='submit' and text()='Підписатися']"
    VERIFY_MASSAGE_XPATH = "/html/body/div[7]/div/div[1]"

    # search
    SEARCH_INPUT_XPATH = "//*[@id='search']/form/input"
    ITEM_BAG_XPATH = ".//a[@href='https://bonlook.ua/sumka-stedcon-266719-pl-pink']"
    VERIFY_BAG_XPATH = ".//h1[text()='Сумка Stedcon']"

    # contact information
    VERIFY_CONTACT_XPATH = ".//a[@href='tel:+380675394880' and @class='d-none d-lg-inline-block font-weight-500']"
