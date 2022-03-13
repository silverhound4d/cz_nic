from mojeid_registration.page_objects.reg_page import RegistrationPage
from mojeid_registration.config import config as c


class Test_003_Registration:
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

    def test_captcha(self, setup):
        reg = RegistrationPage(setup)
        reg.driver.get("https://mojeid.regtest.nic.cz/registration/")
        reg.set_username(c.username)
        reg.set_first_name(c.firstname)
        reg.set_last_name(c.lastname)
        reg.set_email(c.email)
        reg.set_country_code(c.countrycode)
        reg.set_phone_number(c.phonenumber)
        reg.set_street(c.addres_street)
        reg.set_city(c.city)
        reg.set_zip(c.zipcode)
        reg.set_country(c.country)
        reg.set_captcha(c.captcha)
        reg.check_confirmation()
        reg.submit_form()
        assert "Kontrolní kód nesouhlasí, zkuste to znovu." in reg.driver.page_source
        
