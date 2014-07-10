#! /usr/bin/env python
# -*- coding:utf8 -*-
from django.contrib import admin

from haumevents.models import Hacker

class HackerAdmin(admin.ModelAdmin):

    list_display = ('pseudo', 'mail', 'batches_count', 'haum')
    ordering = ['pseudo']

admin.site.register(Hacker, HackerAdmin)

