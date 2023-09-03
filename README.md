## (DESAFIO) Cart

1. Create (Criar):
    
    O projeto foi construído na intenção de se criar novos objetos utilizando o django. No caso a criação de produtos para determinado serviço e carrinhos vinculados a cada usuário criados/existentes. Você pode criar um novo usuário pelo path /carrinho/register/ e para criar produtos pode ser acessado direto pela path /carrinho/produtos
            teoricamente era par poder inserir produtos em cada usuário específico, através da path /carrinho/carrinhos/{user-id}/adicionar-item/ porém F.
        

2. Read (Ler):

    A leitura dos registros do banco de dados é feita por meio de consultas ao banco de dados.
    Você pode listar todos os produtos existentes e carrinhos por meio da paths /carrinho/produtos
    Para ler produtos específicos criados você acessa /carrinho/produtos/1, por exemplo, sendo 1 o id do produto.

3. Update (Atualizar):

    Você pode atualizar seus produtos criados acessando produtos específicos como foi apresentado anteriormente: /carrinho/produtos/1.
    E fazer a alteração do nome do produto e do preço.

4. Delete (Excluir):

A exclusão de registros envolve a remoção de objetos Django do banco de dados.
Para excluir um usuário ou usuário você deve acessar diretamente pela path específica do mesmo como apresentado no tópico anterior: /carrinho/produtos/1

# Passos para executar o projeto:

1. Clone o repositório:
```bash
git clone https://github.com/allanrgc/desafio_workshop_backend_2023_2
```

2. dentro da pasta clonada insira os códigos a seguir para ativar:
> 1º
```bash
python -m venv venv
```
>2º
```bash
.\venv\Scripts\activate.ps1
```

3. baixar dependências:
```bash
pip install -r requirements.txt
```

4. atualizar banco de dados:
```bash
python manage.py makemigrations
python manage.py migrate
```


5. rodar o servidor:
```bash
python manage.py runserver
```
