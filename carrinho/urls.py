from rest_framework import routers
from .views import ProdutoViewSet, CarrinhoViewSet, UserCreateView

# router = routers.DefaultRouter()
# router.register(r'produto', ProdutoViewSet)
# router.register(r'carrinho', CarrinhoViewSet)
# urlpatterns = router.urls


from django.urls import path, include
from .import views

router = routers.DefaultRouter()
router.register(r'produtos', views.ProdutoViewSet)
router.register(r'carrinhos', views.CarrinhoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('carrinhos/<int:pk>/adicionar-item/', views.CarrinhoViewSet.as_view({'post': 'adicionar_item'}), name='carrinho-adicionar-item'),
    path('carrinhos/<int:pk>/remover-item/', views.CarrinhoViewSet.as_view({'post': 'remover_item'}), name='carrinho-remover-item'),
    path('register/', UserCreateView.as_view(), name='register')
]