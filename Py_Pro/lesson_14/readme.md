# Lesson 14

- First part is about templates. I know basics, but it was interesting to know about details:
  - How named blocks work, {% block NAME %} and add it to base template to indicate custom title on the page
  - Get info from form using form.FIELD_NAME.value
- Second Talked about CRUD and Routes. Interesting - func "django.urls.reverse" that gives link from name. Also using kwargs we can pass vars. reverse("person", kwargs={"id": id})
- In routing if we have urls with the same naming - we can add "app_name = 'ourname'", and then we can use ourname:delete as name.. who knows they know..

Homework:

1. Implement all CRUD browsing features in your applications. 
2. Add the required templates. 
3. Move the general part of the HTML code into the base template. All templates are executed from the base. 
4. Split the main router. 
5. Replace all HARD code mixtures with mortar. 
6. Apply, where appropriate, the get_object_or_404 function.

CRUD, templates, base template, router, links and get_object_or_404 I realised while I was doing previous HW. So now I just a little improve it. \
Also try to use TabninePro from now on.. let's check what it can. Even tho nothing to write this time, lol..

PS: for refactoring TabninePro is useless

From lesson_9 Homework is here:
- [homework 14](https://github.com/0xDyno/django-lms/pull/5/commits/e6b49e490debfeae7c7a65a359fe8c940d65c733)
- [Whole project "django-lms"](https://github.com/0xDyno/django-lms)