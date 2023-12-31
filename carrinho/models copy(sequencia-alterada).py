from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models import FloatField

    
class Produto(models.Model):
    nome = models.CharField(max_length=40)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

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
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    # nome = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total = self.produto.valor * self.quantidade
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantidade}x {self.nome} - Total: R$ {self.total}"
    
class Carrinho(models.Model):
    # carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE, related_name='itens_carrinho')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Itens, through='Itens')
    # quantidade = models.PositiveIntegerField(Produto, through='Itens', related_name='quantidade_itens')
    # total = models.ForeignKey(Itens, on_delete=models.CASCADE)
    # Produto.objects.aggregate(price_diff="price", output_field=FloatField())

    def __str__(self):
        return f'Carrinho de {self.usuario.username}'

