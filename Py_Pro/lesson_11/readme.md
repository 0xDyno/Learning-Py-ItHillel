# Lesson 11

- Walked through Django validators, created our own validators as method & class
- Created inner method of model class to fill DB with fake data using Faker library
- Checked urls package and roots, example: if root/\<str:var\> is before root/param, and we receive GET query "https://...root/param/" - will be used first variant root/\<str:var\>

Homework:

> 1. For the Student model, create a validator function that checks the uniqueness of the entered email. (ex.: validate_unique_email)
> 2. For the Group model, create a validator function to check the correctness of entering the start date of the group. When creating a group, it is necessary to prohibit specifying a date from the past. (ex.: validate_start_date)

From lesson_9 Homework is here:
- [Homework 11](https://github.com/0xDyno/django-lms/commit/fa8cb95106807813aff033c1afc0dc581b4ae875)
- [Whole project "django-lms"](https://github.com/0xDyno/django-lms)