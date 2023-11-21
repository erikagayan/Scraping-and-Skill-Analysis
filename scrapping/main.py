import threading
from scraper import get_vacancy_links
from counter import count_skills
from scrapping.writer import write_skills_to_csv


def process_vacancy(url, total_skills_count, lock):
    skills_count = {}
    count_skills(url, skills_count)
    with lock:
        for skill, count in skills_count.items():
            total_skills_count[skill] = total_skills_count.get(skill, 0) + count


def main():
    start_url = "https://jobs.dou.ua/vacancies/?category=Python"
    vacancy_links = get_vacancy_links(start_url)

    total_skills_count = {}
    threads = []
    lock = threading.Lock()

    for url in vacancy_links:
        thread = threading.Thread(target=process_vacancy, args=(url, total_skills_count, lock))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for skill, count in total_skills_count.items():
        print(f"{skill}: {count}")

    csv_filename = 'skills_count.csv'

    write_skills_to_csv(total_skills_count, csv_filename)


if __name__ == "__main__":
    main()
