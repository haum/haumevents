#! /usr/bin/env python
# -*- coding:utf8 -*-
from django.db import models
from django.contrib.auth.models import User

from talksplanning.models import HackerBatch


class Hacker(models.Model):
    """
    Hacker (vaillant rien d'impossible)
    """

    pseudo = models.CharField(max_length=50)
    mail = models.EmailField()
    haum = models.BooleanField(default=False, blank=True)

    # names for forms
    pseudo.verbose_name = "nom/pseudonyme"
    mail.verbose_name = "adresse e-mail"
    haum.verbose_name = "membre du HAUM"

    def __unicode__(self):
        return self.pseudo

    def batches_count(self):
        return HackerBatch.objects.filter(hacker=self).count()



