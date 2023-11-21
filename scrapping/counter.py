import re
from bs4 import BeautifulSoup
import requests

# Список интересующих навыков
skills = {
    'python': re.compile(r'\bpython\b', re.IGNORECASE),
    'django': re.compile(r'\bdjango\b', re.IGNORECASE),
    # Добавьте остальные навыки с соответствующими регулярными выражениями
}

def count_skills(url, skills_count):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text().lower()  # Получаем весь текст страницы

    for skill, pattern in skills.items():
        skills_count[skill] = len(pattern.findall(text))

if __name__ == '__main__':
    skills_count = {}
    count_skills("https://jobs.dou.ua/companies/zone3000/vacancies/245445/", skills_count)
    for skill, count in skills_count.items():
        print(f"{skill}: {count}")
