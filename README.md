# base-python-django
Este é a base de criação de um ambiente em Django, com algumas boas práticas e facilitações. O projeto está em Postgres mas pode ser trocada facilmente.

## Instalações
- Se você deseja executar o projeto, primeiro certifique-se de ter o python instalado globalmente em seu computador. Se não, você pode obter python [aqui](https://www.python.org/downloads/ "aqui").

## Caso queria usar o repositório como template para o seu projeto.
- Faça o download para uma pasta do seu computador: `git clone https://github.com/eduardo-monita/base-python-django.git`
### Passos a passo para rodar o proejto.
- Atualizar o pip: `pip install --upgrade pip`;
- Instalar a virtualenv: `virtualenv venv -p python3`;
- Criá-la na pasta raiz do projeto: `venv/Scripts/activate`;
- Instalar os pacotes necessários: `pip install -r requirements.txt`;
- Entra na pasta app `cd app`; 
- Criar o banco de dados desejado e subistituir no arquivo app/main/settings.py na variável 'DATABASES';
- Baixar todos os arquivos estáticos do manager do django: `python manage.py collectstatic`;
- Criar um usuário no seu admin: `python manage.py createsuperuser`;
- Criar as tabelas da Django: `python manage.py migrate`;
- Rodar o servidor: `python manage.py runserver`;
- Acessar no browser: `http://localhost:8000/admin`.

## Comandos para criar o projeto do zero.
Observação: todos esses passo estão em uso neste repositório.
- Criar a pasta principal do Djando: `django-admin startproject main`;
- Alterar a pasta raiz com o nome do projeto ou 'app';
- Criando um app da aplicação: `python manage.py startapp example_app`.
### No arquivo settings.py faça as seguintes alterações.
- Adicione o: `import os`;
- Adicione a Variável 'DATA_DIR': `DATA_DIR = os.path.dirname(os.path.dirname(__file__))`;
- Adicione o app recém-criado na variável 'INSTALED APPS': `'example_app.apps.ExampleAppConfig',`;
- Por padrão vem como banco de dados SQLite, caso queria mudar é na variável 'DATABASES';
- Adicione no fim do arquivo as variáveis de diretórios estáticos e medias:
```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
```
