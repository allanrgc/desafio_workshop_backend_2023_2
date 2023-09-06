from django.db import models
from django.contrib.auth.models import User, AbstractUser

    
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    valor = models.FloatField()

    def __str__(self):
        return self.nome

class User(AbstractUser):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_set",
        related_query_name="customuser",
    )

    def __str__(self):
        return self.username
    
class Itens(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, max_length=12)
    quantidade = models.IntegerField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantidade}x {self.produto}"

class Carrinho(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Itens)
    total = models.FloatField(default=0, editable=False)

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)