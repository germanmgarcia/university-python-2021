# Django

### Iniciar un nuevo projecto, crear la aplicación admin y ejecutar django
'''
docker-compose run --rm web python manage.py startapp webapp
docker-compose run --rm web django-admin startproject sap ./
docker-compose up -d
'''

### Enumerar las migraciones de un proyecto y su estado
'''
docker exec -it django python manage.py showmigrations
'''

### Aplicar y desaplicar migraciones
'''
docker exec -it django python manage.py migrate
'''

### Se encarga de crear nuevas migraciones en función de los cambios que haya realizado
'''
docker exec -it django python manage.py makemigrations
'''

### Mostar el sql que se va a ejecutar
'''
docker exec -it django python manage.py sqlmigrate personas 0001
'''