from rest_framework import serializers
from .models import Produto, Carrinho, Itens, User
from django.contrib.auth import get_user_model

# User = get_user_model()

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class ItensSerializer(serializers.ModelSerializer):
    nome = serializers.CharField(source='produto.nome', read_only=True)
    valor = serializers.DecimalField(source='produto.valor', max_digits=10, decimal_places=2, read_only=True)
    quantidade = serializers.IntegerField(source='produto.quantidade', read_only=True)
    total = serializers.FloatField(source='produto.total', read_only=True)
    class Meta:
        model = Itens
        # fields = ['nome', 'valor', 'quantidade', 'total']
        fields = '__all__'

class CarrinhoSerializer(serializers.ModelSerializer):
    user = ItensSerializer(read_only=True)
    itens = ItensSerializer(many=True, read_only=True)

    class Meta:
        model = Carrinho
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
