from django.contrib import admin


from oj.models import User, Problem, Contest

admin.site.register(User)
admin.site.register(Contest)
admin.site.register(Problem)
