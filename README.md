# E-Commerce-Django-rest-framework

##### About Project
- E-commerce is all about buying and selling of products.

- In this project we have three Database tables 
  - Category
  - Product
  - Cart
  - User (Default django model)
  
- Frontend
  - HTML
  - CSS
  - JS 

- API'S 
  ```
  - 0.0.0.0:8000/api/category_list/                     To fetch all categories
  - 0.0.0.0:8000/api/category-list/<str:pk>/            To fetch all products present in particular category
  - 0.0.0.0:8000/api/product-list/                      To fetch all the products present in products table
  - 0.0.0.0:8000/api/selected-product/<str:pk>/         To fetch specific product from product table
  - 0.0.0.0:8000/api/cart_item/                         To fetch all the items in the cart 
  ```
  
- Docker Container is used to run this project

- Framework
  - Django and Django rest-framework 

- **Login, cart pages are yet to be developed**

- Django provides it's default admin panel where superuser can create, update or delete data

##### Steps to Run the Project(only for win/linux):

- Install docker and docker-compose *if not installed*
  - [docker-installation](https://docs.docker.com/compose/install/)

- Pull git repo to local machine 
```
  - git clone git@github.com:harshith-byte/E-Commerce-Django-rest-framework.git
```

- open terminal and Change directory to main
```
  - cd main/
```

- run docker-compose 
```
  - docker-compose up
```

- Open any browser and type :
```
  - 0.0.0.0:8000/
```

- To stop docker type in terminal
```
  - ctrl+c
```

- To create a superuser in django
```
  - docker-compose web run python manage.py createsuperuser
```

- To Turn down docker
```
  - docker-compose down
```
