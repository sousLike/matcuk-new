from django.db import models

class Client(models.Model):
    """Модель для хранения информации о клиентах."""
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"



    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"


class Membership(models.Model):
    """Модель для хранения информации о абонементах."""
    MEMBERSHIP_TYPES = [
        ('STD', 'Стандартный'),
        ('VIP', 'VIP'),
        ('UNL', 'Безлимитный'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    type = models.CharField(max_length=3, choices=MEMBERSHIP_TYPES, verbose_name="Тип абонемента")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return f"{self.client} - {self.get_type_display()}"

    class Meta:
        verbose_name = "Абонемент"
        verbose_name_plural = "Абонементы"


class Workout(models.Model):
    """Модель для хранения информации о тренировках."""
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, verbose_name="Тренер")
    date = models.DateTimeField(verbose_name="Дата и время тренировки")
    duration = models.DurationField(verbose_name="Продолжительность")
    notes = models.TextField(verbose_name="Заметки", blank=True, null=True)

    def __str__(self):
        return f"{self.client} - {self.date}"

    class Meta:
        verbose_name = "Тренировка"
        verbose_name_plural = "Тренировки"


class Equipment(models.Model):
    """Модель для хранения информации о оборудовании."""
    name = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    purchase_date = models.DateField(verbose_name="Дата покупки")
    last_maintenance_date = models.DateField(verbose_name="Дата последнего обслуживания", blank=True, null=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"