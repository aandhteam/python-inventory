from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Suppliers"


class Inventory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    note = models.TextField()
    stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Inventories"
