# Instale o Pip e o Python 3

    # apt install pip python3
	
# Instale as dependências do pip

    $ pip install virtualenv
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

# Instale o postgreSQL

    # apt install docker
    $ docker pull postgres
    $ docker start [imagem]
    $ docker exec -it [imagem] bash
    $ su postgres
    $ createdb plantio

# Rode o servidor

    $ python manage.py makemigrations familia especie
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver
	
