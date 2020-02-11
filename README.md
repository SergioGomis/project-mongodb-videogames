
![logo](https://github.com/SergioGomis/project-mongodb-videogames/blob/master/src/logo.png)

This repo is a project for developing skills at the Data Analytics bootcamp of Ironhack Madrid by querying a MongoDB database and doing some geospacial analysis with maps in jupyter notebook.

## Challenge: New office location

Our brand-new videogames company, **Fictional Games Ltd.**, need a nice location for its headquarters and we have a bunch of suggestions of our employees. A little weird suggestions, to be said. We'll try to make the most of them happy.

### The scope

We have a huge database of the most outstanding companies worldwide. On the first step, we'll load it on MongoDB, and will clean their locations attributes working with pypmongo in jupyter.

### The big search

With our 2.0 database we'll learn how to perform our first geoqueries with MongoDB and plot a few maps in jupyter. With some candidate cities on mind, we'll focus on the services they provide (they sure have a Starbucks but we'll check anyway).

### The conclusions

We'll show how many near schools, airports, starbucks and design companies are near those points and choose our favourite.




#### Usage

First of all, you'll need to load on your local MongoDB server the initial companies database. Unzip the 'Crunchbase Dataset.zip' file in the inputs folder and launch in shell the following command:

```bash
mongoimport --db companies --collection companies inputs/companies.json
```

In order to perform requests to the Google Places API, you'll need an API key on a .env file.

*.env file:*
```bash
PLACES_API_TOKEN=XXXXXX
```

