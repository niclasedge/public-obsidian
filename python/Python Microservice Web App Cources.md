parent: [[Django]]
tags:
aliases: 
Reference: [[Microservice]]

---
# Python Microservice Web App Cources

Fortschritt: 100
Related to Projects (Property): ../../Reporting%20Data%20Warehouse%20b3d8444aefd241f7b0d1b0d04764c671.md
Status: Fertig
Tags: Django, Referenz, Video
bearbeitet: May 25, 2021 8:55 AM

[https://www.youtube.com/watch?v=0iB5IPoTDts&list=PLoB1sTYyPYTFjzAz_32rC3202uvCdC1QZ&index=19&t=168s](https://www.youtube.com/watch?v=0iB5IPoTDts&list=PLoB1sTYyPYTFjzAz_32rC3202uvCdC1QZ&index=19&t=168s)

Setup:

- VSCode
- extension mysql

## Docker

- 1 Project Introduction
- 2 Django Setup

    Create the Django project

    ```bash
    # Create the project directory
    mkdir tutorial
    cd tutorial

    # Create a virtual environment to isolate our package dependencies locally
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`

    # Install Django and Django REST framework into the virtual environment
    pip install django
    pip install djangorestframework

    # Set up a new project with a single application
    django-admin startproject tutorial .  # Note the trailing '.' character
    cd tutorial
    django-admin startapp quickstart
    cd ..
    ```

    Then go into the folder and start the server:

    ```bash
    python3 manage.py runserver
    ```

- 3 Adding Docker Files

    ### Create a Dockerfile:

    ```bash
    FROM python:3.9
    ENV PYTHONUNBUFFERED 1
    WORKDIR /app
    COPY requirements.txt /app/requirements.txt
    RUN pip install -r requirements.txt
    COPY . /app
    ```

    ### Create requirements.txt

    ```bash
    Django==3.1.3
    djangorestframework==3.12.2
    mysqlclient==2.0.1
    django-mysql==3.9
    django-cors-headers==3.5.0
    pika==1.1.0
    ```

    Docker-compose.yml file

    - includes all the services in the docker file with ports etc
    - example

        ```bash
        version: '3.9'
        services:
          backend:
            build:
              context: .
              dockerfile: Dockerfile
            command: 'python manage.py runserver 0.0.0.0:8000'
            ports:
              - 8000:8000
            volumes:
              - .:/app
            depends_on:
              - db

          queue:
            build:
              context: .
              dockerfile: Dockerfile
            command: 'python -u consumer.py'
            depends_on:
              - db

          db:
            image: mysql:5.7.22
            restart: always
            environment:
              MYSQL_DATABASE: admin
              MYSQL_USER: root
              MYSQL_PASSWORD: root
              MYSQL_ROOT_PASSWORD: root
            volumes:
              - .dbdata:/var/lib/mysql
            ports:
              - 33066:3306
        ```

    ### Recompile Docker File from the docker-compose file

    ```bash
    docker-compose up
    ```

    → recompiles the docker file, if something in the docker-compose-file has changed

    requirements.txt

    - includes all the python packages
- 4 Connect Django with MySQL with Docker
- 5 Models & Serializers

    ### Migrate Table sctructure

    in the Folder Products/models.py

    - create the table structure
    - example

        from django.db import models

        # Create your models here.

        class Product(models.Model):

        title = models.CharField(max_length=200)

        image = models.CharField(max_length=200)

        likes = models.PositiveIntegerField(default=0)

        class User(models.Model):

        pass

    Then run the Docker container

    - docker-compose up

    Open new terminal

    - docker-compose exec backend sh
    - **python [manage.py](http://manage.py) makemigrations**
        - creates a migration structure for mysql to import
    - p**ython [manage.py](http://manage.py) migrate**
        - this migrates the structure to the mysql db
    - Then the admin db should have new tables

        ![Python%20Microservice%20Web%20App%20Cources%201085d38a112f48748ee88b7e2dbb7a0c/Bildschirmfoto_2021-03-10_um_11.37.44.png](Bildschirmfoto_2021-03-10_um_11.37.44.png)

- 6 Rest APIs with ViewSets

    Download Postman App, to check API Endpoints

    Define the Endpoints 

- 7 User Endpoint with APIView

    Define the URLs

- 8 Flask Setup with Docker
- 9 Connect Flask with Mysql
    - connect o the docker mysql db
    - create Table
        - ready to recieve information from the Admin App

    ```bash
    #main.py
    from flask import Flask
    from flask_cors import CORS
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy import UniqueConstraint

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/main' ## connect to the created docker mysql database
    CORS(app)

    db = SQLAlchemy(app)

    class Product(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=False)
        title = db.Column(db.String(200))
        image = db.Column(db.String(200))

    class ProductUser(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id = db.Column(db.Integer)
        product_id = db.Column(db.Integer)

        UniqueConstraint('user_id','product_id', name='user_product_unique')

    @app.route('/')
    def index():
        return 'Hello'

    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
    ```

    - Migrate the Tables from the python script to the mysql db in docker

    ```bash
    # manager.py
    from main import app, db
    from flask_migrate import Migrate, MigrateCommand
    from flask_script import Manager

    migrate = Migrate(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)

    if __name__ == '__main__':
        manager.run()
    ```

    - execute the migration in the terminal

    ```bash
    docker-compose exec backend sh

    python3 manager.py db init

    python3 manager.py db migrate

    python manager.py db upgrade
    ```

- 10 Models
- 11 Flask Migrations
- 12 RabbitMQ
- 13 Django Producer and Consumer

    Publish() in views hinzufügen

    ```bash
    def list(self, request):
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            publish()
            return Response(serializer.data)
    ```

    Producer.py erstellen

    ```bash
    import pika

    params = pika.URLParameters('amqps://exzxsquu:M_lJuqkhZCjE0olcY-tkuyewHrV_YE0O@cow.rmq2.cloudamqp.com/exzxsquu')

    connection = pika.BlockingConnection(params)

    channel = connection.channel()

    def publish():
        channel.basic_publish(exchange='', routing_key='main', body='hello main')
    ```

    consumer.py erstellen und diesen ausführen

    ```bash
    import pika

    params = pika.URLParameters('amqps://exzxsquu:M_lJuqkhZCjE0olcY-tkuyewHrV_YE0O@cow.rmq2.cloudamqp.com/exzxsquu')

    connection = pika.BlockingConnection(params)

    channel = connection.channel()

    channel.queue_declare(queue='admin')

    def callback(ch, method, properties, body):
        print('Received in admin')
        print(body)

    channel.basic_consume(queue='admin', on_message_callback=callback)

    print('Started Consuming')

    channel.start_consuming()

    channel.close()
    ```

- 14 Flask Producer and Consumer
- 15 Queue Service
- 16 Data Consistency

    To create data consistenci eg. same data in both apps:

    1. you need to connect the 2 apps with rabitMQ
    2. greate an api to create/delete/update data in the first apps DB - views.py

    ```bash
    class ProductViewSet(viewsets.ViewSet):
        def list(self, request):
            products = Product.objects.all()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

        def create(self, request):
            serializer = ProductSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            publish('product_created', serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        def retrieve(self, request, pk=None):
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)

        def update(self, request, pk=None):
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(instance=product, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            publish('product_updated', serializer.data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        def destroy(self, request, pk=None):
            product = Product.objects.get(id=pk)
            product.delete()
            publish('product_deleted', pk)
            return Response(status=status.HTTP_204_NO_CONTENT)
    ```

    1. connect the 2 apps together with rabbit mq and callback in [consumer.py](http://consumer.py) file
    2. set the callback up, to recieve the API call to create the same Data as in the first app - consumer.py

    ```bash
    connection = pika.BlockingConnection(params)

    channel = connection.channel()

    channel.queue_declare(queue='main')

    def callback(ch, method, properties, body):
        print('Received in main')
        data = json.loads(body)
        print(data)

        if properties.content_type == 'product_created':
            product = Product(id=data['id'], title=data['title'], image=data['image'])
            db.session.add(product)
            db.session.commit()
            print('Product Created')

        elif properties.content_type == 'product_updated':
            product = Product.query.get(data['id'])
            product.title = data['title']
            product.image = data['image']
            db.session.commit()
            print('Product Updated')

        elif properties.content_type == 'product_deleted':
            product = Product.query.get(data)
            db.session.delete(product)
            db.session.commit()
            print('Product Deleted')

    channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

    print('Started Consuming')

    channel.start_consuming()

    channel.close()
    ```

- 17 Internal Http Requests
- 18 Finishing the python apps

time: 1:26 

- 19 React Setup

    initialize the react app:

    ```bash
    npx create-react-app new-app-name —template typescript
    ```

    Then go to folder and start the app:

    ```bash
    npm start
    ```

- 20 Products CRUD
- 21 Completing the Main App