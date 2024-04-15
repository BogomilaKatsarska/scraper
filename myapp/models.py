from django.db import models


class Link(models.Model):
    ADDRESS_MAX_LEN = 1000
    NAME_MAX_LEN = 1000
    address = models.CharField(
        max_length=ADDRESS_MAX_LEN,
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=NAME_MAX_LEN,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    #TODO: migrate, create superuser