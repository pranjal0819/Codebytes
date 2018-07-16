from django.contrib import admin
from .models import paperRecord, commentOnPaper

# Register your models here.
admin.site.register(paperRecord)
admin.site.register(commentOnPaper)