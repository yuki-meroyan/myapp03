from django.db import models
from django.contrib.auth import get_user_model

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    menu_number = models.IntegerField(blank=False, null=False)
    menu_name   = models.CharField(max_length=50, blank=False, null=False)
    create_user = models.CharField(max_length=150)
    update_user = models.CharField(max_length=150)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    def __str__(self):
        return str(self.menu_number) + ":" + self.menu_name

class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    name        = models.CharField(max_length=50, blank=False, null=False)
    amount      = models.IntegerField(blank=False, null=False)
    unit        = models.CharField(max_length=10, blank=False, null=False)
    limit_date  = models.DateTimeField()
    create_user = models.CharField(max_length=150)
    update_user = models.CharField(max_length=150)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    def __str__(self):
        return str(self.user.id) + "-" + str(self.id) + ":" + self.name + " " + str(self.amount) + "(" + self.unit + ")"

class Material(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
    )
    name        = models.CharField(max_length=50, blank=False, null=False)
    amount      = models.IntegerField(blank=False, null=False)
    unit        = models.CharField(max_length=10, blank=False, null=False)
    create_user = models.CharField(max_length=150)
    update_user = models.CharField(max_length=150)
    create_date = models.DateTimeField()
    update_date = models.DateTimeField()

    def __str__(self):
        return str(self.user.id) + "-" + str(self.menu.id) + "-" + str(self.stock.id) + ":" + self.name + " " + str(self.amount) + "(" + self.unit + ")"

