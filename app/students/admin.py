from django.contrib import admin

from .models import College, Student


# Register your models here.
@admin.display(description='title_name')
def title_name(obj):
    if isinstance(obj.name, str):
        return obj.name.title()
    return obj.name


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('id', title_name)
    search_fields = ('name',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', title_name, 'title_college', 'gpa')
    search_fields = ('name',)
    list_filter = ('college__name',)

    @admin.display()
    def title_college(self, obj):
        if isinstance(obj.college, College):
            return title_name(obj.college)
        return obj.college
