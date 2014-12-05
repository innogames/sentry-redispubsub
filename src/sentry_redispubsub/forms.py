# coding: utf-8
"""
sentry_redispubsub.forms
"""
from django import forms


class RedisPubSubOptionsForm(forms.Form):
    host = forms.CharField(
        max_length=255,
        help_text='Redis host (for example: "localhost")'
    )
    port = forms.IntegerField(
        max_value=65535,
        help_text='Redis port (for example: "6379")'
    )
    db = forms.IntegerField(
    	max_value=65535,
    	help_text='Redis db (for example: "0")'
    )
    channel_name = forms.CharField(
        max_length=255,
        help_text='Channel name for Sentry metrics to push to (for example: "sentry")'
    )
