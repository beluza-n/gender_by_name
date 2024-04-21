from django.db import models
from django.core.validators import RegexValidator

class Woman(models.Model):
    name_regex = RegexValidator(regex=r"^[a-zA-Z]+$")
    name = models.CharField(
        validators=[name_regex],
        max_length=50,
        verbose_name='name')

    def __str__(self):
        return self.name


class Man(models.Model):
    name_regex = RegexValidator(regex=r"^[a-zA-Z]+$")
    name = models.CharField(
        validators=[name_regex],
        max_length=50,
        verbose_name='name')

    def __str__(self):
        return self.name