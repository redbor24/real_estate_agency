from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)

    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    new_building = models.BooleanField('Новостройка', null=True, db_index=True)
    likes = models.ManyToManyField(User, verbose_name='Кто поставил лайк', related_name='liked_flats', null=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Compliant(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Кто пожаловался',
        on_delete=models.DO_NOTHING,
        related_name='compliants'
    )
    flat = models.ForeignKey(
        Flat,
        verbose_name='Объявление',
        on_delete=models.DO_NOTHING,
        related_name='compliants'
    )
    text = models.TextField(verbose_name='Текст жалобы', blank=False)

    def __str__(self):
        return f'{self.user}, {self.flat}'

    class Meta:
        verbose_name = 'Жалоба на объявление'
        verbose_name_plural = 'Жалобы на объявления'


class Owner(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200, db_index=True)
    phone = models.CharField('Телефон владельца', max_length=20, db_index=True)
    pure_phone = PhoneNumberField(verbose_name='Нормализованный телефон владельца', blank=True, db_index=True)
    flats = models.ManyToManyField(Flat, verbose_name='Квартиры', related_name='owners', db_index=True)

    def __str__(self):
        return f'{self.owner}, {self.pure_phone if self.pure_phone else self.phone}'

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
