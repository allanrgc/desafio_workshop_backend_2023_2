from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Produto, Carrinho, Itens, User
from .serializers import ProdutoSerializer, CarrinhoSerializer, UserSerializer

# User = get_user_model()

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer

    @action(detail=True, methods=['post'])
    def adicionar_item(self, request, pk=None):
        carrinho = self.get_object()
        produto_id = request.data.get('produto')
        quantidade = request.data.get('quantidade')

        if not produto_id or not quantidade:
            return Response({'message': 'Escolha um produto e uma quantidade.'}, status=status.HTTP_400_BAD_REQUEST)

        produto = get_object_or_404(Produto, pk=produto_id)

        item_carrinho, created = Itens.objects.get_or_create(
            carrinho=carrinho,
            produto=produto,
            defaults={'nome': produto.nome, 'quantidade': quantidade}
        )

        if not created:
            item_carrinho.quantidade += quantidade
            item_carrinho.save()

        carrinho_serializer = CarrinhoSerializer(carrinho)
        return Response(carrinho_serializer.data)

    @action(detail=True, methods=['post'])
    def remover_item(self, request, pk=None):
        carrinho = self.get_object()
        produto_id = request.data.get('produto')

        if not produto_id:
            return Response({'message': 'Escolha um produto para remover.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            item_carrinho = carrinho.itens.get(produto=produto_id)
            item_carrinho.delete()
        except Itens.DoesNotExist:
            return Response({'message': 'Item não encontrado no carrinho.'}, status=status.HTTP_400_BAD_REQUEST)

        carrinho_serializer = CarrinhoSerializer(carrinho)
        return Response(carrinho_serializer.data)
    
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
