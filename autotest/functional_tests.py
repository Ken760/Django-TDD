from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    """тест нового посетителя"""

    def setUp(self):
        """установка"""
        self.browser = webdriver.Chrome(executable_path="driver/chromedriver")

    def tearDown(self):
        """демонтаж"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест: можно начать список и получить его позже"""

        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Закончить тест!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')