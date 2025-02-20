import unittest
from selenium import webdriver

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
        
        # invited to finish the to-do item right away
        self.fail("finish test")
        
        
if __name__ == "__main__":
    unittest.main()