from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    owner = models.CharField('ФИО владельца', max_length=200)
    # owner_id = models.ForeignKey('Owner', on_delete=models.CASCADE, related_name='flat_owners')
    owners_phonenumber = models.CharField('Номер владельца', max_length=20)
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
    like = models.ManyToManyField(User, verbose_name='Кто лайкнул')
    owner_pure_phone = PhoneNumberField(verbose_name='Нормализованнцый номер владельца', blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Compliant(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.DO_NOTHING,
        related_name='user_compliants'
    )
    flat = models.ForeignKey(
        Flat,
        verbose_name='Объявление',
        on_delete=models.DO_NOTHING,
        related_name='flat_compliants'
    )
    compliant_text = models.TextField(verbose_name='Текст жалобы', blank=False)

    def __str__(self):
        return f'{self.user}, {self.flat}'

    class Meta:
        verbose_name = 'Жалоба на объявление'
        verbose_name_plural = 'Жалобы на объявления'


class Owner(models.Model):
    user = models.CharField('ФИО владельца', max_length=200)
    phone = models.CharField('Телефон владельца', max_length=20, blank=True)
    pure_phone = PhoneNumberField(verbose_name='Нормализованный телефон владельца', blank=True)
    flat = models.ManyToManyField(Flat, verbose_name='Квартира', related_name='owner_flats')

    def __str__(self):
        return f'{self.user}, {self.pure_phone if self.pure_phone else self.phone}'

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'
