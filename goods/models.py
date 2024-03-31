from django.db import models



class Categories(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'


class Products_kitchen(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    discount = models.IntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'kitchen'


class Products_bedroom(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    discount = models.IntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bedroom'


class Products_livingroom(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    discount = models.IntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'living_room'


class Products_office(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    discount = models.IntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'office'


class Products_accessories(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    discount = models.IntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'accessories'



class Products_decor(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2)
    discount = models.IntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'decor'