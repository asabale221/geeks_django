from django.db import models
class Currency(models.Model):
    name_currency = models.CharField(
        max_length=50,
        verbose_name="Название валюты"
    )
    def __str__(self) -> str:
        return self.name_currency
    class Meta:
        verbose_name = "Валюта"
        verbose_name_plural = "Валюты"

# Create your models here.
class Products(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название продукта"
    )
    description = models.CharField(
        max_length=300,
        verbose_name= "Описание продукта"
    )
    product_photo = models.ImageField(
        upload_to= 'product_photo/',
        verbose_name="Фотография продукта"
    )
    price = models.PositiveBigIntegerField(
        verbose_name="Цена"
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.CASCADE,
        related_name="product_currency",
        verbose_name="Название валюты"
    )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"