from django.db import models

# Create your models here.
class Client(models.Model):

    name = models.CharField("Name", max_length=255)
    cpf = models.CharField("CPF", max_length=11)
    birth_date = models.DateField("Birth Date")
    created_at = models.DateTimeField('Created at', auto_now_add=True)
    updated_at = models.DateTimeField('Update at', auto_now_add=True)
    active = models.BooleanField("Active", default=True)

    class Meta:
        db_table = 'tb_client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f"{self.name}"
