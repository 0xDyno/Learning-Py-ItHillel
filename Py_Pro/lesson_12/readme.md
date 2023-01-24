# Lesson 12
 
- Library **webargs**, is being used to get params ?key=value&k2=v2&etc=etc. Important:
  -  `from webargs.djangoparser import use_args` and `from webargs.fields import Str`
  - _use_args_ is being used as decorator that takes dict with params `"key": Str(requred etc..)` and from where catch the info `location="query"`
  - using this param we specified info we want to get adding `.filter(param=args["param"])` to `Model.object.all() `
- Q queries to filter 2+ field in DB with OR 
  - in general when we use filter with 2 params - in DB it shows as 2 required conditions: P1 AND P2, but with Q we can search as P1 OR P2
  - also we specify query by adding to Model attribute __, example, PersonModel with attribute name, `filter(Q(name__in=args.get("...") / name_contains / name__exact))` etc ...
- Using GET query in form we pass params as ?k=v&k2=v2 in a URL, using POST query we pass params as.. in body of http query
- Started using django forms - ModelForm

Homework:

> 1. Add a new field phone to the Student model. Add it to the form. Create a method that will check the entered phone number and strip it of all characters except numbers, dashes, pluses, and parentheses.
> 2. As an additional optional task, you can think about and implement the formatting of a telephone number in accordance with the international standard.
> 3. (Optional) Think about the implementation / try to implement the student editing mechanism: form + controller.

From lesson_9 Homework is here:
- [homework 12](https://github.com/0xDyno/django-lms/pull/new/homework_12)
- [Whole project "django-lms"](https://github.com/0xDyno/django-lms)