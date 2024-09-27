# Create your views here.

from django.shortcuts import render
# Essa função é parte do Django e é utilizada para renderizar templates HTML. 
# Embora não seja utilizada neste código, ela é comum em views baseadas em HTML.

from rest_framework.decorators import api_view
 # Os decorators em Python são uma maneira de modificar ou estender o comportamento de funções ou métodos. 
 # No contexto do Django REST Framework, o decorador @api_view serve para transformar uma função comum em 
 # uma view que pode manipular requisições HTTP.

from .models import Produto
# Importa o modelo Produto definido em models.py. Esse modelo representa 
# uma tabela no banco de dados, permitindo a interação com os registros.

from .serializer import ProdutoSerializer
# Importa o serializador ProdutoSerializer, que é responsável por transformar 
# instâncias do modelo Produto em formatos JSON e vice-versa


from rest_framework.response import Response
# Importa a classe Response do Django REST Framework, que encapsula os dados que serão enviados ao cliente em uma resposta HTTP.

from rest_framework import status

# GET = Pegar dados do banco | POST = Enviar dados para o banco
@api_view(['GET', 'POST']) # Especificar quais os tipos de requisições que o método abaixo pode utilizar
def listar_produtos(request): # Define uma função de view que recebe um objeto request do tipo HttpRequest, contendo todas as informações sobre a requisição recebida, como parâmetros, corpo da requisição e método HTTP.
    if request.method == 'GET': # Verifica se a requisição é do tipo GET. Isso é importante porque, neste contexto, queremos responder a diferentes tipos de requisições de forma específica
        queryset = Produto.objects.all() # Utiliza o método all() do manager padrão (objects) do modelo Produto para obter todos os registros existentes na tabela Produto. O resultado é um QuerySet, que é uma coleção de objetos que pode ser filtrada e manipulada
        seriealizer = ProdutoSerializer(queryset, many=True) # Cria uma instância do ProdutoSerializer, passando o QuerySet obtido. O parâmetro many=True indica que estamos lidando com múltiplos registros, permitindo que o serializador saiba que deve processar uma lista de objetos.
        return Response(seriealizer.data) # Cria e retorna uma instância da classe Response, passando os dados serializados (acessados através da propriedade data do serializador). O Django REST Framework converte automaticamente esses dados em um formato JSON adequado para a resposta HTTP, configurando também o cabeçalho Content-Type como application/json.
    elif request.method == 'POST': # Verifica se a requisição é do tipo POST, que é utilizado para criar novos recursos
        seriealizer = ProdutoSerializer(data = request.data) # Cria uma instância do ProdutoSerializer, passando os dados da requisição
        if seriealizer.is_valid(): # Verifica se os dados fornecidos são válidos de acordo com as regras definidas no serializador
            seriealizer.save() # Se os dados forem válidos, salva a nova instância do modelo Produto no banco de dados
            return Response(seriealizer.data, status=status.HTTP_201_CREATED) # Retorna os dados serializados da nova instância, com um status HTTP 201 (Created)
        else:
            return Response(seriealizer.data, status=status.HTTP_400_BAD_REQUEST) # Se os dados não forem válidos, retorna os erros de validação com um status HTTP 400 (Bad Request)