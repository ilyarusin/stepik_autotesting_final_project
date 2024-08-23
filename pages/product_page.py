from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def product_name_check(self):
        product_name_on_the_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_THE_PAGE).text
        product_name_in_the_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_THE_CART).text
        assert product_name_in_the_cart == product_name_on_the_page, f"Название должно быть {product_name_on_the_page}"
        print("Товар добавлен в корзину")
    
    def cart_summ_check(self):
        product_price_in_the_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_THE_CART).text
        product_price_on_the_product_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_THE_PRODUCT_PAGE).text
        assert product_price_in_the_cart == product_price_on_the_product_page, "Стоимость корзины не совпадает с ценой товара"
        print("Сумма в корзине соответствует цене товара")

    def should_not_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
