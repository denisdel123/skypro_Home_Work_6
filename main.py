"""импортируем функции"""
from functions import get_student, get_job, user_find_job, skills
"""главная функция"""
if __name__ == '__main__':
    """обращаемся к пользователю"""
    print("Введите номер студента")
    number = input()
    """вызываем функции и передаем данные"""
    info_about_user = get_student(number)

    choise_job = get_job(info_about_user)

    skills_job = user_find_job(choise_job)

    result = skills(info_about_user, skills_job)
