from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Produto, Carrinho, Itens, User
from .serializers import ProdutoSerializer, CarrinhoSerializer, UserSerializer, ItensSerializer

# User = get_user_model()

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ItensViewSet(viewsets.ModelViewSet):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
