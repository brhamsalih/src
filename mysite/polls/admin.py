from django.contrib import admin

# Register your models here.
from .models import Question, Choice

class PollsAdmin(admin.ModelAdmin):
    #list_display = ['question_text','pub_date']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, PollsAdmin)
admin.site.register(Choice)



    