from django.contrib import admin

# Register your models here.
from .models import student_detail, candidate, election_posts

admin.site.register(student_detail)
admin.site.register(candidate)
admin.site.register(election_posts)