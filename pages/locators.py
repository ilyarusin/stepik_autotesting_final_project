from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "a[href='/ru/basket/']")
    PRODUCT_NAME_IN_THE_CART = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_NAME_ON_THE_PAGE = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE_IN_THE_CART = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT_PRICE_ON_THE_PRODUCT_PAGE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
