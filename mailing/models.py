from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    """
    Client Model - модель клиентов
    email: почта
    first_name: имя
    last_name: фамилия
    comment: Комментарий
    """
    email = models.EmailField(verbose_name='email')
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    comment = models.CharField(max_length=255, verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент рассылки'
        verbose_name_plural = 'клиенты рассылки'
        ordering = ('email',)


class MailingMessage(models.Model):
    """
    MailingMessage Model - модель сообщения
    subject: тема
    message: текст рассылки
    """
    subject = models.CharField(max_length=255, verbose_name='тема')
    body = models.TextField(verbose_name='текст рассылки')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('subject',)


class MailingList(models.Model):
    """
    MailingList Model - модель рассылки
    mail_start: дата начала рассылки
    mail_end: дата окончания рассылки
    mail_period: периодичность рассылки
    mail_status: статус рассылки
    """
    class FREQUENCY(models.TextChoices):
        DAILY = 'Ежедневно'
        WEEKLY = 'Еженедельно'
        MONTHLY = 'Ежемесячно'

    class STATUS(models.TextChoices):
        DRAFT = 'Черновик'
        CREATED = 'Создана'
        RUNNING = 'Запущена'
        COMPLETED = 'Завершена'

    message = models.ForeignKey(MailingMessage, on_delete=models.CASCADE, verbose_name='рассылка')
    mail_start = models.DateField(verbose_name='начало рассылки', **NULLABLE)
    mail_end = models.DateField(verbose_name='конец рассылки', **NULLABLE)
    mail_period = models.CharField(max_length=15, choices=FREQUENCY.choices, verbose_name='периодичность', **NULLABLE)
    mail_status = models.CharField(max_length=15, choices=STATUS.choices, verbose_name='статус рассылки', **NULLABLE)

    recipient = models.ManyToManyField(Client, related_name='clients', verbose_name='клиенты')

    def __str__(self):
        return f'{self.mail_start} - {self.mail_end}'

    class Meta:
        verbose_name = 'настройка рассылки'
        verbose_name_plural = 'настройки рассылки'


class MailingLog(models.Model):
    """
    MailingLog Model: модель логов рассылок
    last_attempt_time: время последней попытки
    attempt_status: статус попытки
    server_response: ответ сервера
    """

    class STATUS(models.TextChoices):
        SUCCESS = 'Успешно'
        FAILED = 'Неуспешно'

    last_attempt_time = models.DateTimeField(verbose_name='время последней попытки', **NULLABLE)
    attempt_status = models.CharField(max_length=15, choices=STATUS.choices, verbose_name='статус попытки', **NULLABLE)
    server_response = models.TextField(max_length=255, verbose_name='ответ сервера', **NULLABLE)
    mailing = models.ForeignKey(MailingMessage, on_delete=models.SET_NULL, verbose_name='рассылка', **NULLABLE)

    def __str__(self):
        return f'{self.last_attempt_time} - {self.attempt_status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('attempt_status',)
