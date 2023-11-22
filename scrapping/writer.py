import csv


def write_skills_to_csv(skills_count, filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Skill", "Count"])

        for skill, count in skills_count.items():
            writer.writerow([skill, count])
