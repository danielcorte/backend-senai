"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Importa o módulo de administração do Django, que fornece uma interface administrativa para gerenciar modelos e dados do banco de dados.
from django.urls import path, include # Importa as funções path e include para definir rotas de URL e incluir URLs de outros módulos ou aplicativos.

urlpatterns = [ # Define uma lista que contém as rotas de URL para o projeto. O Django utiliza essa lista para determinar qual view deve ser chamada para cada requisição.
    path('admin/', admin.site.urls), # Essa linha define uma rota que mapeia a URL /admin/ para a interface administrativa do Django. Quando um usuário acessa essa URL, o Django apresenta a interface para gerenciar os modelos registrados. O admin.site.urls é um roteador que fornece todas as URLs necessárias para a administração.
    path('api/', include('api.urls')) # Essa linha inclui as URLs definidas no arquivo urls.py do aplicativo api sob o prefixo /api/. Isso significa que qualquer URL definida no api.urls será acessível a partir de /api/.... A função include permite modularizar as URLs, facilitando a organização e manutenção do código. Por exemplo, se o api.urls tiver uma rota definida como listar_produtos/, ela será acessível em /api/listar_produtos/.
]
