from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'url', 'user', 'date')
    list_filter = ('date', 'user')
    search_fields = ('question', 'answers')
    prepopulated_fields = {'url': ('question',)}
admin.site.register(Year)
admin.site.register(Subject)
admin.site.register(Tag)
admin.site.register(Answer)