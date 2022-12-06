# Firebase + Python
This is a project I worked on to understand how to use Cloud Databases through Python.

# Overview

With this project I learned how to use Python to insert, query, modify, and delete things in the Google Firestore Cloud Database. 

I wrote software that takes inputs from a user to build and maintain a Google Firestore Database. It inegrates with the database with the firebase_admin Python package. To use my program you just place whatever function you want to run at the end of it and what collection you want to modify.
Example: If you want to insert something with the collection of 'A01' it would be insert('A01')

I wrote this software so I could learn more about Cloud Databases and how to CRUD in them. I am very familiar with SQL databases and use Snowflake at work but had never worked on a 'traditional' Cloud Database so I decided to learn it.

[Python Firebase Demo](https://youtu.be/4jLoNMC-tiY)

# Cloud Database

I am using Google Firebase as my database because it's free and has fairly simple integration with most programming languages.

The structure of my database is very simple. It is a main collection called 'programmer details', documents of programmer codes, then information about the programmer. 

# Development Environment

VScode code editor with Python 3.10.x 

Language: Python
Libraries: firebase_admin, pip install firebase_admin

# Useful Websites

* [Google Firebase Documentation](https://firebase.google.com/docs/reference/admin/python)
* [Analytics Vidhya](https://www.analyticsvidhya.com/blog/2022/07/introduction-to-google-firebase-firestore-using-python/?)

# Future Work

* I want to modify the program to use games instead of programmer details.
* I want to connect it to a website so things are only being edited through the terminal of the code editor or IDE.
* I need to Make the editing at a bit higher level so it isn't required to be hard-coded in what you want to modify. Ex. call the database for things to edit. Not have to hard-code 'name', or 'country'.
