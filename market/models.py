from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models, transaction

from users.models import CustomUser


class ProductCategory(models.Model):

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Категории товаров'
        verbose_name = 'Категория товара'

    def __str__(self):
        return self.name



# Create your models here.
class Product(models.Model):

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)

    price = models.PositiveIntegerField(help_text='в сомах', verbose_name='цена без скидки')
    sales_percent = models.PositiveSmallIntegerField(
        verbose_name='скидка процентах',
        null=True,
        validators=[MaxValueValidator(100)]
                                                     )

    descriptions = models.TextField()
    preview_image = models.ImageField()

    new_expiry_date = models.DateField()



    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def get_price_with_sales(self):
        if self.sales_percent == 0:
            return self.price
        else:
            return int((self.price/100))*(100-self.sales_percent)

    def __str__(self):
        return self.name

class ProductGallery(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='products')
    image = models.ImageField(upload_to='product_gallery')

    class Meta:
        verbose_name_plural = 'Галерея товаров'
        verbose_name = 'Галерея товара'

class ProductUserRating(models.Model):

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(15), MinValueValidator(1)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        unique_together = ('user', 'product')


