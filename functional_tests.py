import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    """generate test case for onboarding a new user

    Args:
        unittest (I don't know): whatever man just learning
    """
    
    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_todo_list(self):
        # Here is the story as it goes from user perspective
        # Topendra goes to check out a new todo app
        self.browser.get("http://localhost:8000")
        
        # He notices the title and header contain to-do
        self.assertIn("To-do", self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME,"h1").text
        self.assertIn("To-Do", header_text)
                
        # invited to finish the to-do item right away
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(inputbox.get_attribute("placeholder"), 
                         "Enter a todo item")
        
        #He types "Buy peacock feathers" into a text box
        inputbox.send_keys("Buy peacock feathers")
        #when Topendra hits enter the page updates and now the page lists
        # "1: Buy peacock feathers" as an item in todo list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertTrue(any(row.text == "1: Buy peacock feathers"
                            for row in rows))
        
        # He also enters "Use peacock feathers to make a fly" in text box
        self.fail("finish test")
        
        # the page updates again and shows both items on his list
        
        
if __name__ == "__main__":
    unittest.main()