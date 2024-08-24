from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "В корзине есть товары"
    
    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Корзина не пуста"
    
    def should_be_items_in_the_basket(self):
        assert self.is_element_present(*BasketPageLocators.ITEMS_IN_BASKET), "В корзине нету товаров"

    def should_not_be_empty_basket_text(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), "Корзина не пуста"