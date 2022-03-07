from django.db import models
from django.db.models import functions


# Lowercase CharField
class LowerCaseCharField(models.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_prep_value(self, value):
        val = super().get_prep_value(value)
        if isinstance(val, str):
            return val.lower()
        return val

    def to_python(self, value):
        val = super().to_python(value)
        if isinstance(val, str):
            return val.lower()
        return val


# ------------------------------------------
#                   Models
# ------------------------------------------

class College(models.Model):
    name = LowerCaseCharField(max_length=30, db_index=True)

    class Meta:
        ordering = ('name', 'id')
        constraints = [models.UniqueConstraint(
            functions.Lower('name'),
            name='%(class)s_name_should_be_unique'),
        ]

    def __str__(self):
        return self.name


class Student(models.Model):
    name = LowerCaseCharField(max_length=20, db_index=True)
    gpa = models.DecimalField(max_digits=4, decimal_places=2)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', 'id')
        constraints = [models.CheckConstraint(
            check=models.Q(gpa__gte=0) & models.Q(gpa__lte=10),
            name='%(class)s_gpa_should_be_between_0_and_10'
        )]

    def __str__(self):
        return self.name

