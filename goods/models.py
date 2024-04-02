from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Products(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    discount = models.IntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def display_id(self) -> str:
        return f'{self.pk:05}'

    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        else:
            return self.price


    def __str__(self):
        return f'{self.name} -> {self.category}'

    class Meta:
        db_table = 'product'
        ordering = ['-id']