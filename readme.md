# Projeto e-diaristas

### Instalando o projeto

#### Clonar o projeto
`git clone https://github.com/nicolascoliveira/e-diaristas.git`

#### Instalar dependencias
`pip install -r requirements.txt`

#### Alterar configurações do BD do arquivo settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_bd',
        'HOST': 'host_do_bd',
        'PORT': 'porta_do_bd',
        'USER': 'usuario_do_bd',
        'PASSWORD': 'senha_do_bd'
    }
}
```

#### Migrar banco de dados
`python manage.py migrate`

#### Executar o servidor
`python manage.py runserver`