from django.db import models
from django.utils import timezone


class Mailing(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_start = models.DateTimeField(verbose_name='Launching mailing')
    date_end = models.DateTimeField(verbose_name='Ending mailing')
    time_start = models.TimeField(verbose_name='Sending time')
    time_end = models.TimeField(verbose_name='The end time of sending')
    text = models.TextField(max_length=255, verbose_name='Message text')
    tag = models.CharField(max_length=100, verbose_name='Tag', blank=True)
    mobile_operator_code = models.CharField(verbose_name='Mobile operator code', max_length=3, blank=True)

    @property
    def to_send(self):
        now = timezone.now()
        if self.date_start <= now <= self.date_end:
            return True
        else:
            return False

    def __str__(self):
        return f'Рассылка №{self.id} от даты: {self.date_start}'

    class Meta:
        verbose_name = 'Mailing'
        verbose_name_plural = 'Mailings'