# Search Gene API

This is a JSON REST API that retrieves gene information from the public Ensembl database, 'ensembl_website_97', when provided with parameters 'name' and 'species' of the gene.
<Additional information about your API call. Try to use verbs that match both request type (fetching vs modifying) and plurality (one vs multiple).>

## Demo with terminalizer
https://github.com/faressoft/terminalizer

### URL
localhost:5000/searchgene

## Table of Contents

## Getting Started

To run this API you need to have python 3 installed.
To clone the repository on your local machine,

```
git clone https://github.com/sobia20/EMBL-Python_Developer-Test
```

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them are mentioned in the requirements.txt file. 

```
pip install -r requirements.txt
```

Time out is 30 minutes so it will automatically stop querying if timeout is reached. 
##Run the Flask API
```
flask run
```
### Swagger API
Searchgene API is documented using Swagger API. Please go to the localhost:5000/swagger url to see.
This is just a get request.

GET Request:
 Query String Parameters: 
 name: It is the name or similar to the name of the gene
 species: It is the full name of the species (Optional)

Success Response:
Code: 200
Error Response:
Code: 400 (Query parameters that do not specify requirements)
Code: 405 (Method not allowed)
Sample Call:

Notes:

<This is where all uncertainties, commentary, discussion etc. can go. 
I recommend timestamping and identifying oneself when leaving comments here.>

## Test Cases

To run the test cases we have to run. There are 15 test cases and the API passes all. 
```
nose2 -v
```

## Deployed on Docker

## How to run on Vagrant

## Run from Heroku



