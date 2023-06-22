from django.db import models

# Create your models here.
class Order(models.Model):
    order_dt = models.DateField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name="Ім'я")
    order_prone = models.CharField(max_length=200, verbose_name="Телефон")

    # тут пееропределно название для каждого обьекта Order в спсике ордеров админке
    def __str__(self):
        return self.order_name
    
    # переопределяются названия слова Order в админке добавлением подкласса Мета
    class Meta:
        verbose_name = "Замовленя" # в единственнном числе
        verbose_name_plural = "Замовлення" # во множкственнном числе
