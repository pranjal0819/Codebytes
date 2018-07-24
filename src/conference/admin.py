from django.contrib import admin
from .models import paperRecord, reviewPaper

# Register your models here.
admin.site.register(paperRecord)
admin.site.register(reviewPaper)