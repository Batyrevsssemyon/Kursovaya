from django.db import models

class Product(models.Model):
    title = models.CharField('Название товара', max_length=50)
    image = models.ImageField('Изображение товара', upload_to='static/main/img')
    amount = models.DecimalField('Стоимость товара', max_digits=10, decimal_places=2)
    quantity = models.IntegerField('Количество товара')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Order(models.Model):
    address = models.CharField('Адресс доставки', max_length=50)
    latitude = models.CharField('Широта', max_length=50)
    longitude = models.CharField('Долгота', max_length=50)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class ProductOrder(models.Model):
    productId = models.IntegerField('Id товара')
    orderId = models.IntegerField('Id заказа')
    quantity = models.IntegerField('Количество товара')

    class Meta:
        verbose_name = 'Содержание заказа'
        verbose_name_plural = 'Содержания заказа'