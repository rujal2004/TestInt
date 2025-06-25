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





