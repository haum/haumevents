#! /usr/bin/env python
# -*- coding:utf8 -*-

from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory

from haumevents.models import Hacker

class HackerForm(forms.ModelForm):

    class Meta:
        model = Hacker

    def save(self):

        return Hacker.objects.get_or_create(
            pseudo=self.cleaned_data['pseudo'],
            mail=self.cleaned_data['mail'],
            haum=self.cleaned_data.get('haum') # can be blank
        )[0] # indice comme pour le TalkProposalForm
