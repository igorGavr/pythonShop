from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField("Назва", max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    order_number = models.PositiveSmallIntegerField(blank=True, null=True)
    icon = models.ImageField(upload_to="category/imgs/")

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
        ordering = ["-order_number"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Назва", max_length=200)
    description = models.TextField("Опис")
    image = models.ImageField("Фото", upload_to="products/imgs/")
    price = models.DecimalField("Ціна", max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"
        ordering = ["category", "is_available"]

    def __str__(self):
        return self.name
