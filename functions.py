import json


def get_student(number):
    student_info = []

    """обращаемся к файлу JSON"""
    with open('data/students.json') as file:
        info = json.load(file)

        """обработчик исключений"""
        try:
            number = int(number)
        except ValueError:
            number = int(len(info) + 1)

            """проверяем студента"""
        for i in info:
            if int(number) == i["pk"]:
                student_info = i

                """возвращаем результат если есть студент в базе
                если нет то выводим на консоль информацию"""
        if student_info:
            return student_info
        else:
            print("У нас нет такого студента")


""" проверяем на None. выводим информацию на консоль
и возвращаем результат"""


def get_job(students):
    if students is not None:
        full_name = students["full_name"]
        skills = ", ".join(students["skills"])
        print(f"Студент {full_name}\nЗнает {skills}")
        print(f"Выберите специальность для оценки студента {full_name}")
        job = input()
        return job
    else:
        return


"""проверяем на None и возвращаем результат"""


def user_find_job(job):
    if job is not None:

        professions = []
        with open('data/professions.json') as file:
            jons = json.load(file)

            for i in jons:
                if job == i["title"]:
                    professions = i["skills"]

        if professions:
            return professions
        else:
            print("У нас нет такой специальности")


"""проверяем на None, переводим словари во множители, сравниваем, считаем проценты,
выводим на консоль информацию"""


def skills(user_skill, job_skills):
    if user_skill is not None and job_skills is not None:
        user_skills = set(user_skill["skills"])
        job_skills = set(job_skills)
        know_not_things = job_skills.difference(user_skills)
        know_things = job_skills.intersection(user_skills)
        name = user_skill["full_name"]
        percent = int(len(know_things)) / int(len(job_skills)) * 100
        print(f"Пригодность {round(percent)}%\n{name} знает {', '.join(know_things)}\n{name} \
не знает {', '.join(know_not_things)}")
    else:
        print("None")
