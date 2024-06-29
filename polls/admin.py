from django.contrib import admin

# Register your models here.

from .models import Choice, Question


class MyAdminSite(admin.AdminSite):
    site_header = "Administration"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date",
        "was_published_recently"]
    list_filter = ["pub_date"]
    question_fields = ["question_text"]


admin_site = MyAdminSite()
admin_site.register(Question, QuestionAdmin)
