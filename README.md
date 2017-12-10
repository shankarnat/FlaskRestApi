# FlaskRestApi

First Rest API would convert Celcius to Farenheit and ViceVersa

I am using Mriguel Grinberg's post as a basis for this - https://blog.miguelgrinberg.com/post/designing-a-restful-api-using-flask-restful
Also, I have Dockerized the Application for ease of distribution.


Create a Docker Image (run from the main folder of FlaskRestApi). Also ensure the docker in the system is up and running before this. 

docker build -t flask-sample-one:latest .   

Note: Donot forget the .(dot) at the end

Run the Docker Image - to start the flask application

docker run -d -p 5000:5000 flask-sample-one

To see if the application is running try 
docker ps -a [lists this application]

To test the Rest API 

curl http://localhost:5000/todo/api/v1.0/temp ; triggers the GET Method
