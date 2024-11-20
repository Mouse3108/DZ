from django.db import models


class Master(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    contact_info = models.TextField(blank=True, verbose_name='Контактная информация')
    photo = models.ImageField(upload_to='masters/photos/', blank=True, null=True, verbose_name='')
    services = models.ManyToManyField('Service', related_name='masters', verbose_name='Услуги')

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.contact_info}'

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Visit(models.Model):
    STATUS_CHOICES = [
        (0, 'В обработке'),
        (1, 'Подтверждена'),
        (2, 'Отменена'),
        (3, 'Выполнена'),
    ]

    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='Статус')
    master = models.ForeignKey('Master', on_delete=models.CASCADE, verbose_name='Мастер')
    services = models.ManyToManyField('Service', verbose_name='Услуги')

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
