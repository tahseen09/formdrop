from django.db import models


class Form(models.Model):
    # TODO: Add User FK
    name = models.CharField(max_length=30, default="Default")
    success_redirect = models.URLField(null=True, blank=True)
    failure_redirect = models.URLField(null=True, blank=True)


class Content(models.Model):
    # TODO: Handle Files
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    body = models.JSONField(null=True, blank=True)
