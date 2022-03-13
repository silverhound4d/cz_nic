import unittest
from webbrowser import BaseBrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Setup method - runs before each test, instantiates webdriver.

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")  # Opens the python.org web page.
        self.assertIn("Python", driver.title)  # Asserts the current web page is of title "Python".
        elem = driver.find_element_by_name("q")  # Selects the search field element.
        elem.send_keys("pycon")  # Enter "pycon" in the search field.
        elem.send_keys(Keys.RETURN)  # Submit the input.
        assert "No results found." not in driver.page_source  # Assert the phrase "No results found." is not anywhere on the page.

    def tearDown(self):
        self.driver.close()  # Teardown method - closes browser after the execution of each test case.

if __name__ == "__main__":
    unittest.main()  # Runs all the tests, given the file was executed directly (and not just imported).
