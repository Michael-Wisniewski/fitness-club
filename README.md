# Fitness Club
**Caution!** This code was created to be a attachment for a job application. It is not suitable for commercial purposes. If you find something interesting in it, please do not hesitate to reuse.

### Instalation
**Notice** The repository contains all the data required to run the application.
Please ensure that you have avalible port:80.
Just copy repository and from the main folder level run listed below commands.

To restore the database:

```
docker-compose up -d db_postgresql

docker-compose exec -T db_postgresql pg_restore -C --clean --no-acl --no-owner -U fitness_club_admin -d fitness_club < ./databases/database.backup

docker-compose stop db_postgresql
```

To run containers:

```
docker-compose up
```

Appplication frontend side.
```
url: http://localhost
```
Appplication backendside.
```
url: http://panel.localhost
login: employee
password: fitness
```


#### Table of Contents

1. Application stack overview
2. Introduction
3. Programming environment and tools
4. Description of functionalities
5. Detailed list of used technologies

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
    <img src="./docs/readme/shields/webpack.svg"><br/>    
    <img src="./docs/readme/shields/docker.svg">
    <img src="./docs/readme/shields/dockercompose.svg">
</p>


### 2. Introduction
**"Fitness Club"** is a web application which allows customers to get to know fitness center's offer and events. It provides many tools both in terms of improving customer service and marketing activities.

<p align="center">
    <img src="./docs/readme/screen.jpg">
</p>
<p align="center">
    <img src="./docs/readme/screen2.jpg">
</p>
<p align="center">
    <img src="./docs/readme/screen3.jpg">
</p>

#### 3. Programming environment and tools

    Docker and Docker Compose are used to perform the virtualization of the runtime environment.

    Http requests for static files are supported directly by Nginx. Site content created dynamically is 
    delivered using uWsgi.

    Support of subdomains traffic is supported by Django Hosts (Django library).

    Application's main data are saved in PostgreSQL database. Data used to search through blog posts are 
    saved in noSql format. Other information which can not be gruped are formatted and pleaced in *.txt files.

    Application's backend is based on Python web framework - Django and oter libraries connected to it. 
    
    All JS and CSS/SCSS files are bundled using the Webpack. Every site contains only one *.js and *.css files.

### 4. Description of functionalities

    Application features grouped by modules.

    Blog
        - reading posts
        - recommending reading posts through email message
        - commenting posts
        - searching posts by tag
        - searching similar posts
        - searching posts by keywords
        - using RSS web feed

    Blog_backend
        - creating, editing and removing posts
        - photo processing
        - assigning tags and SEO friendly urls
        - providing sitemap

    Employees
        - viewing employees pictures
        - reading employees descriptions

    Employees_backend
        - creating and removing employees accounts
        - editing employees data

    Footer_backend
        - editing footer data

    Slider_backend
        - creating and removing main site slides
        - changing slides order

    Account
        - authenticating employees

### 5. Detailed list of used technologies

| Type        | Technologies           |
| ------------- |:-------------:|
| Serwers      | Nginx, Uwsgi |
| Databases      | PostgreSQL, Redis      |
| Search engine | Apache Solr      |
| Python | Pip,  Django, Django REST, Crispy Forms, Taggit, Sitemap, Feed, Haystack, Pillow, Django Hosts, Serializers, sorl-thumbnail, Django-Betterforms      |
| Frontend | Html5, Css3, Sass, Bootstrap, JavaScript, Data Tables, DateTime Picker, CropperJs, jQuery-ui, Waypoints, Parallax, CountUp      |
| Others | Node JS, Npm, Webpack (Css and Js optimizers, svg to woff converter), Docker, Docker-Compose, Mailhog      |
