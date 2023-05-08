from django.db import models

from core.models import BaseModel
from shift.enums import SHIFT_PERIOD


class Shift(BaseModel):
    worker = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='shift', null=True)
    shift_period = models.CharField(choices=SHIFT_PERIOD, max_length=10)
    date = models.DateField(null=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.worker.username
