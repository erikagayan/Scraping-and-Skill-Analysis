import requests
from bs4 import BeautifulSoup


skills = [
    "python",
    "django",
    "flask",
    "fastapi",
    "sqlalchemy",
    "django orm",
    "aws",
    "docker",
    "kubernetes",
    "pytest",
    "unittest",
    "linux",
    "unix",
    "mysql",
    "postgresql",
    "rabbitmq",
    "git",
    "sql",
    "rest",
    "api",
    "js",
    "asyncio",
    "mongodb",
]


def count_skills(url, skills_count):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        text = soup.get_text().lower()
        for skill in skills:
            if skill in text:
                skills_count[skill] = 1
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    skills_count = {}
    count_skills(
        "https://jobs.dou.ua/companies/sps-ukraine/vacancies/245461/", skills_count
    )
    for skill, count in skills_count.items():
        print(f"{skill}: {count}")
