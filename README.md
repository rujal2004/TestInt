#  Flask CRUD API with MongoDB and Docker

This project is a simple and scalable RESTful API built using **Flask** and **MongoDB**, containerized using **Docker**, and tested via **Postman**.

The API provides full CRUD (Create, Read, Update, Delete) functionality for a `User` resource.

## Tech Used
Python (Flask)
MongoDB (NoSQL)
Docker & Docker Compose
Postman (for API testing)

####  Features

REST API for managing users
MongoDB as a backend database
Dockerized setup for both backend and database
Clean and scalable project structure
API tested with Postman collections

## Project Structure
projecttutorial/

├── app.py # Main Flask app

├── requirements.txt # Python dependencies

├── Dockerfile # Flask app Docker config

├── README.md # You're reading this!


## Installing dependicies

###  Step 1: Clone the Repository

git clone https://github.com/rujal2004/flask-mongo-crud.git

cd flask-mongo-crud

## Start MongoDB in Docker
docker network create flasknet

docker run -d --name mongo-container --network flasknet -p 27017:27017 mongo

##  Build and Run Flask App

docker build -t flask-mongo-crud .

docker run -p 5000:5000 --network flasknet flask-mongo-crud


## Screenshots

  ## Docker Containers Running

  ![Docker Containers]![image](https://github.com/user-attachments/assets/e1dea9be-baab-4c3e-ab6c-658dade289ad)

  ## Postman - Create User (POST)

  ![Postman POST] ![image](https://github.com/user-attachments/assets/a3236770-9eb9-4122-9665-9532b17f4ace)

  ## Postman - All User (GET)

  ![Postman GET] ![image](https://github.com/user-attachments/assets/0ef21dd4-0626-4ba9-ab32-8370249d9ccf)

  ## Postman - Upadate User(Put)

  ![Postman PUT]![image](https://github.com/user-attachments/assets/01514f0d-ade6-4959-8060-937957ed769b)

  ## Postman - Delete User(Delete)

  ![Postman DELETE]![image](https://github.com/user-attachments/assets/d8dbcb69-3674-430c-acde-27dd4b577dbd)




  





