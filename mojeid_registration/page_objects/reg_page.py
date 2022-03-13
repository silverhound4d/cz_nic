from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from mojeid_registration.page_objects.base_class import BaseClass


class RegistrationPage(BaseClass):
    text_username_id = "id_username"
    text_firstname_id = "id_first_name"
    text_lastname_id = "id_last_name"
    text_email_id = "id_email-default-email"
    text_countrycode_id = "id_phone-default-number_0"
    text_phonenumber_id = "id_phone-default-number_1"
    text_addres_street_id = "id_address-default-street1"
    text_city_id = "id_address-default-city"
    text_zipcode_id = "id_address-default-postal_code"
    select_country_id = "id_address-default-country"
    text_captcha_id = "id_captcha_1"
    checkbox_confirmation_id = "id_confirmation"

    def set_username(self, username):
        username_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.text_username_id)))
        username_field.clear()
        username_field.send_keys(username)
    
    def set_first_name(self, first_name):
        first_name_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.text_firstname_id)))
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def set_last_name(self, last_name):
        last_name_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.text_lastname_id)))
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def set_email(self, email):
        email_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.text_email_id)))
        email_field.clear()
        email_field.send_keys(email)

    def set_country_code(self, countrycode):
        countrycode_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.text_countrycode_id)))
        countrycode_field.clear()
        countrycode_field.send_keys(countrycode)
    
    def set_phone_number(self, phone_num):
        phone_num_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.text_phonenumber_id)))
        phone_num_field.clear()
        phone_num_field.send_keys(phone_num)
    
    def set_street(self, street):
        street_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.text_addres_street_id)))
        street_field.clear()
        street_field.send_keys(street)
    
    def set_zip(self, zipcode):
        zip_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.text_zipcode_id)))
        zip_field.clear()
        zip_field.send_keys(zipcode)

    def set_city(self, city):
        city_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.text_city_id)))
        city_field.clear()
        city_field.send_keys(city)
    
    def set_country(self, country):
        country_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.select_country_id)))
        select = Select(country_field)
        select.select_by_visible_text(country)
    
    def set_captcha(self, code):
        captcha_field = self.wait.until(EC.element_to_be_clickable((By.ID, self.text_captcha_id)))
        captcha_field.clear()
        captcha_field.send_keys(code)
    
    def check_confirmation(self):
        checkbox = self.wait.until(EC.element_to_be_clickable((By.ID, self.checkbox_confirmation_id)))
        checkbox = self.driver.find_element(By.ID, self.checkbox_confirmation_id)
        checkbox.click()
    
    def submit_form(self):
        self.driver.find_element(By.ID, self.checkbox_confirmation_id).submit()


    

    







    
