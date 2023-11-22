import unittest

from scrapping.scraper import get_vacancy_links


class TestWebScraping(unittest.TestCase):
    def test_return_type(self):
        result = get_vacancy_links("https://jobs.dou.ua/vacancies/?category=Python")
        self.assertTrue(isinstance(result, list), "The result should be a list")

    def test_non_empty_result(self):
        result = get_vacancy_links("https://jobs.dou.ua/vacancies/?category=Python")
        self.assertTrue(len(result) > 0, "The list should not be empty")

    def test_links_format(self):
        result = get_vacancy_links("https://jobs.dou.ua/vacancies/?category=Python")
        for url in result:
            self.assertTrue(
                url.startswith("http://") or url.startswith("https://"),
                f"Invalid URL: {url}",
            )


if __name__ == "__main__":
    unittest.main()
