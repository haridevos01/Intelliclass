from django.contrib import admin

# Register your models here.
from .models import  Student, Faculty, Course, Department, Assignment, Announcement

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Assignment)
admin.site.register(Announcement)

from django.contrib import admin
from .models import Material

@admin.register(Material)
class Archive(admin.ModelAdmin):
    list_display = ('course_code', 'description', 'datetime', 'file')
    search_fields = ('course_code', 'description')
    ordering = ('-datetime',)




