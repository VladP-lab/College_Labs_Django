from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    short_description = models.TextField(verbose_name="Короткий анонс")
    content = models.TextField(verbose_name="Повний матеріал теми")
    image = models.ImageField(upload_to='topics/', blank=True, null=True, verbose_name="Логотип/Фото")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Вартість курсу")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Теми"

class PythonLibrary(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва бібліотеки")
    description = models.TextField(verbose_name="Опис")
    link = models.URLField(verbose_name="Посилання на документацію", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Бібліотека"
        verbose_name_plural = "Бібліотеки"


# Додаємо в кінець models.py

class Newsletter(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email для розсилки")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Підписник"
        verbose_name_plural = "Підписники"

class Rating(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name="Оцінка (1-5)")

    def __str__(self):
        return f"{self.topic.title} - {self.score} зірок"

class CartItem(models.Model):
    session_key = models.CharField(max_length=255, verbose_name="Ключ сесії")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.topic.title} (у кошику)"