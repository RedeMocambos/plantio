# Instale o Pip e o Python 3

    # apt install pip python3
	
# Instale as dependências do pip

    $ pip3 install virtualenv
    $ virtualenv env
    $ source env/bin/activate
    $ pip3 install -r requirements.txt

# Instale o postgreSQL

    # apt install docker
    $ docker pull postgres
    $ docker run -it --rm --link some-postgres:postgres postgres psql -h postgres -U postgres
    
    $ docker exec -it [postgres] bash
    $ su postgres
    $ createdb plantio

# Rode o servidor

    $ python3 manage.py makemigrations familia especie
    $ python3 manage.py migrate
    $ python3 manage.py createsuperuser
    $ python manage.py runserver
