# Search Gene API

This is a JSON REST API that retrieves gene information from the public Ensembl database, `ensembl_website_97`, when provided with parameters `name` and/or `species` of the gene.

### URL
Navigate to URL `/searchgene/?name=<value>&species=<value>` to run the API. Go to `/swagger` for its documentation through Swagger API.

## Table of Contents
* [Getting Started](#gettingstarted)
 * [Prerequisites] (#prepreqs)
 * [Run the Flask API] (#run)
* [Swagger API Documentation](#swagger)
* [Test Cases](#test)
* [Deploying on Docker and Vagrant](#dockervagrant)
   
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
Now, you can access the API by going to localhost:5000/

## Swagger API Documentation
Searchgene API is documented using Swagger API. Please go to the localhost:5000/swagger url to see.
<p align="center">
<img src="./app/static/swagger.png?raw=true" width="200"/></p>

**GET Request:**
 Query String Parameters: 
 name: It is the name or similar to the name of the gene
 species: It is the full name of the species (Optional)

*Success Response:*
Code: 200
Error Response:
Code: 400 (Query parameters that do not specify requirements)
Code: 405 (Method not allowed)

## Test Cases

To run the test cases, run this command in the root directory of the project,
```
nose2 -v
```
This will run all test cases defined in the app/tests/test_run.py file. It has 15 test cases and all pass. 
<p align="center">
<img src="./app/static/test_cases.png?raw=true" width="200"/></p>
## Deploying on Docker and Vagrant

Install Vagrant and Virtualbox and clone this repository https://github.com/joanmarcriera/vagrant-file on your machine.
Then run
```
$ cd vagrant-file
$ vagrant up
$ vagrant ssh
[vagrant@localhost ~]$ sudo su -
```
To run this application inside vagrant, please do the following,
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
The image contains the test cases as well, so you will notice them during the build, 
>Ran 15 tests in 7.176s
OK

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
[root@localhost Gene-Search-API]# docker exec <container-id> bash -c 'curl -X GET '0.0.0.0/5000/searchgene/?name=brc'
```
To run it from vagrant, use the port 80
```
[root@localhost Gene-Search-API]#curl -X GET "0.0.0.0:80/searchgene/?name=tbpl2"
```
On the external OS, go to http://localhost:8080 to access the API. 


