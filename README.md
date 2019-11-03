# Search Gene API

This is a JSON REST API that retrieves gene information from the public Ensembl database, `ensembl_website_97`, when provided with parameters `name` and/or `species` of the gene.

### URL
Navigate to URL `/searchgene/?name=<value>&species=<value>` to run the API. Go to `/swagger` for its documentation through Swagger API.

## Table of Contents
* [Getting Started](#getting-started)
   * [Prerequisites](#prerequisites)
   * [Run the Flask API](#run-the-flask-api)
* [Swagger API Documentation](#swagger-api-documentation)
* [Test Cases](#test-cases)
* [Deploying on Docker and Vagrant](#deploying-on-docker-and-vagrant)

## Getting Started
To run this API you need to have python 3 installed.
To clone the repository on your local machine,
```
git clone https://github.com/sobia20/Gene-Search-API
cd Gene-Search-API
```

#### Prerequisites

Install dependencies from the requirements.txt through pip,
```
pip install -r requirements.txt
```

#### Run the Flask API
```
flask run
```
Now, you can access the API by going to http://localhost:5000/

## Swagger API Documentation
Searchgene API is documented using Swagger API. Please go to the http://localhost:5000/swagger url to see.

![Swagger_URL](https://i.imgur.com/zpydFm9.png)

**GET Request:**<br>
 Query String Parameters: <br>
 name: It is the name or similar to the name of the gene <br>
 species: It is the full name of the species (Optional)

*Success Response:*
Code: 200 <br>

*Error Response:*<br>
Code: 400 (Query parameters that do not satisfy requirements) <br>
Code: 405 (Method not allowed)

## Test Cases

To run the test cases, run this command in the root directory of the project,
```
nose2 -v
```
This will run all test cases defined in the app/tests/test_run.py file. It has 15 test cases and all pass. 
>...
>Ran 15 tests in 5.853s    <br>
>OK 

## Deploying on Docker and Vagrant

Install Vagrant and Virtualbox on your machine.
Then run
```
$ git clone https://github.com/joanmarcriera/vagrant-file 
$ cd vagrant-file
$ vagrant up
$ vagrant ssh
[vagrant@localhost ~]$ sudo su -
```
To run this application inside vagrant, do the following,
```
[root@localhost ~]# git clone https://github.com/sobia20/Gene-Search-API
[root@localhost ~]# cd Gene-Search-API
[root@localhost Gene-Search-API]# docker build -t super_api .
```
If you run into errors like
 >"E: Release file for http://security.ubuntu.com/ubuntu/dists/bionic-security/InRelease is not valid yet (invalid for another 10h 7min 50s). Updates for this repository will not be applied."
 
you need to change the System clock in Vagrant. You can do that by finding out the date in UTC and then running the command
```
sudo date "MMDDhhmmyyyy.ss"
```
where MM is month, DD is date, hh is hours, mm is minutes, yyyy is years and ss is seconds.

In the end, run
```
[root@localhost Gene-Search-API]# docker run -p 80:5000 --name myapp super_api
```
 To check if it's working on docker properly, first get the container id from 
```
[root@localhost Gene-Search-API]# docker ps
```
Then, send a get request to the application,
```
[root@localhost Gene-Search-API]# docker exec <container-id> bash -c 'curl -X GET '0.0.0.0/5000/searchgene/?name=brc''
```
To run it from vagrant, use the port 80
```
[root@localhost Gene-Search-API]#curl -X GET "0.0.0.0:80/searchgene/?name=tbpl2"
```
On the external OS, go to http://localhost:8080 to access the API. 


 
