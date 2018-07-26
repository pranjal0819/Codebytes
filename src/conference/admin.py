from django.contrib import admin
from .models import paperRecord, authorRecord, reviewPaper

# Register your models here.
admin.site.register(paperRecord)
admin.site.register(authorRecord)
admin.site.register(reviewPaper)