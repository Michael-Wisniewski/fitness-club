# Fitness Club
**Caution!** This code was created to be a attachment for a job application. It is not suitable for commercial purposes. If you find something interesting in it, please do not hesitate to reuse.


#### Table of Contents

1. Application stack overview
2. Introduction
3. Simplified use cases diagram
4. Application’s architecture and programming environment  
    4.1 Virtual enviroment  
    4.2 Servers  
    4.3 App Backend  
    4.4 App Frontend  
    4.5 Tools  
5. Description of functionalities and programming notes
6. Detailed list of used technologies

### 1. Application stack overview

      
<p align="center">
    <img src="./docs/readme/shields/nginx.svg">
    <img src="./docs/readme/shields/uwsgi.svg"><br/>    
    <img src="./docs/readme/shields/postgresql.svg">
    <img src="./docs/readme/shields/redis.svg"><br/>   
    <img src="./docs/readme/shields/solr.svg"><br/>    
    <img src="./docs/readme/shields/python.svg">
    <img src="./docs/readme/shields/django.svg"><br/>    
    <img src="./docs/readme/shields/sass.svg">
    <img src="./docs/readme/shields/bootstrap.svg"><br/>     
    <img src="./docs/readme/shields/javascript.svg">
    <img src="./docs/readme/shields/vue.svg">
    <img src="./docs/readme/shields/vuex.svg"><br/>     
    <img src="./docs/readme/shields/webpack.svg"><br/>    
    <img src="./docs/readme/shields/docker.svg">
    <img src="./docs/readme/shields/dockercompose.svg">
    dodac rest
</p>


### 2. Introduction
**"Fitness Club"** is a web application which  in a complex way supports running a modern fitness center. It provides many tools both in terms of improving customer service and marketing activities.


### 3. Simplified use cases diagram
<img src="./docs/readme/diagrams/use_cases.svg">


### 4. Application’s architecture and programming environment
<img src="./docs/readme/diagrams/system_architecture.svg">
#### 4.1 Virtual enviroment

#### 4.2 Servers

#### 4.3 App Backend

#### 4.4 App Frontend

#### 4.5 Tools

### 5. Description of functionalities and programming notes

    Landing Page
    css/js only two bootstrap okrojony

    Blog
    klient - 
        -czytać posty 
        -zachecać znajomych do przeczytania posta za pomocą wiadomości     email
        -komentować posty
        - wyszukiwać po tagu
        - wyszukać podobne posty
    Pracownik
        -

    Added RWD and scrolling to CropperJS plugin
    All views are class based
    Custom crispy fields are used during forms generation
    Mailhog is used for email testing (localhost:8025)
    Django Sitemap framework is used to generate sitemaps
    Feed framework is used to provide Rich Site Summary


### 6. Detailed list of used technologies

    fitness.pl 

    panel.fitness.pl

    admin.fitness.pl (dodac tylko dla admina)


Nginx, Uwsgi
PostgreSQL, Redis
Apache Solr
Python, Pip,  Django, Django REST, Crispy Forms, Taggit, Sitemap, Feed, Haystack, Pillow, Django Hosts, Serializers, sorl-thumbnail, Django-Betterforms
Html5, Css3, Sass, Bootstrap
JavaScript, Vue, Vuex, Data Tables, DateTime Picker, CropperJs, jQuery-ui, Waypoints, Parallax, CountUp
Node js, Npm, Webpack (Css and Js optimizers, svg to woff converter)
Docker, Docker-Compose
Mailhog
