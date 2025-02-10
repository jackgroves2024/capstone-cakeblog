from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Implementation of Summernote Admin application


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)
