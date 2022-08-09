import pytz
from django.db import models
from django.core.validators import RegexValidator


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    id = models.BigAutoField(primary_key=True)
    format_phone = RegexValidator(regex=r'^7\d{10}$', message="Номер телефона клиента в формате 7XXXXXXXXXX")
    phone_number = models.CharField(verbose_name='Phone number', validators=[format_phone], unique=True, max_length=11)
    mobile_operator_code = models.CharField(verbose_name='Mobile operator code', max_length=3, editable=False)
    tag = models.CharField(verbose_name='Search tags', max_length=100, blank=True)
    timezone = models.CharField(verbose_name='Time zone', max_length=32, choices=TIMEZONES, default='UTC')

    def save(self, *args, **kwargs):
        self.mobile_operator_code = str(self.phone_number)[1:4]
        return super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return f'Клиент №{self.id} с номером телефона: {self.phone_number}'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
