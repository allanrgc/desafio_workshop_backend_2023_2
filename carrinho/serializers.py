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
    class Meta:
        model = Itens
        fields = '__all__'

class CarrinhoSerializer(serializers.ModelSerializer):
    itens = ItensSerializer(many=True, write_only=True)
    class Meta:
        model = Carrinho
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        itens_queryset = Itens.objects.filter(carrinho = instance)
        representation['itens'] = ItensSerializer(itens_queryset, many=True).data
        return representation
    
    def create(self, validated_data):
        itens = validated_data.pop('itens', [])
        print("items => ",itens)
        print("validated data =>", validated_data)
        carrinho = Carrinho.objects.create(**validated_data)

        total=0
        for i in itens:
            item, created = Itens.objects.get_or_create(**i)
            carrinho.itens.add(item)
            produto = Produto.objects.get(id=item.produto_id)
            total += produto.valor * item.quantidade

        carrinho.total = total
        carrinho.save()
        return carrinho

        


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
