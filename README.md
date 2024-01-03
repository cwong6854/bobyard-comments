# Bobyard Fullstack Code Challenge

## After 2 Hours:
- Installed packages necessary for virtual environment, in this case `Django` and `psycopg2`
- set up local database named `bobyard` for postgresql server
- wrote a script to transform `comments.json` inside app directory (See below on why we need to transform the current JSON file)
- created a model for the `comment` table for each entry of comments from `comments.json`
- able to upload `comments.json` into local database with the necessary Django app settings.

## Beekeeper Studio GUI on Database

![Screen Shot 2024-01-02 at 3 37 03 PM](https://github.com/cwong6854/bobyard-comments/assets/96265081/2ae76589-7038-4291-8301-7ab2c64d049b)

## Setting Up Database

1. Git clone the repo: `git clone https://github.com/cwong6854/bobyard-comments.git`
2. Create the database: `createdb bobyard`
3. Go to parent directory: `cd path/to/comments`
4. Make database migration: `python manage.py makemigrations` (There should be no changes)
5. Load the data to local database: `python manage.py loaddata comments.json`
   

## Moving Forward

My initial time was spent setting up the actual packages required to work on the Django app. After reading through some documentation on Django's set up, I was able to get the app going. However, much of my time within 2 hours was spent on conforming with the deserialization of the current `comments.json` file to match with Django's expected JSON `loaddata` method for data migration. Unless there's a better solution, each comment entry had to contain the `model`, `pk`, and `field` column, where `field` includes the original columns such as `author`, `text`, `date`, and the rest. Likewise, it expected an array of entries (in this case, the comments) rather than an Object the key `comments`, with the value containing the array of comments. As a result, the original `comments.json` file was transformed, which you can see under the `app/fixtures` path.

Unfortunately I was not able to work on the Backend edit, add and delete API methods. However, I believe it's crucial that the database and schema, at a high overview, is needed to have an actual working backend followed by the frontend. If I had a few more hours, I would be able to create the actual logic of the app, and write the methods and urls for the backend for the user to interact with the comment (testable on Postman). From there, I would create a simple UI with the list of comments that users can scroll down to look, add, edit, and delete. I would then test the functionality of the app to replicate the user experience and test from there, while enhancing the app experience. 

