[![Build Status](https://travis-ci.com/Livinglist/social_note.svg?branch=master)](https://travis-ci.com/Livinglist/social_note)

# social_note

To run the program, execute ```python3 my_app.py```

OUR FEATURES
------------------------------------------------------------------------------------------------------------------------------
The login page is used to grab the data entered and verify if the username and password entered are stored in the Firebase database. If the data entered is in the Firebase database, the user can now access the rest of the features within the app. If the user is not found in the Firebase database, the system will prompt the user to register. This feature was coded by using the given template in flask and adding our own HTML and CSS elements. We organized the page in a more unique way and gave it a design by adding CSS styles to the site.

The register page for new users to create an account. It required them to enter their email, create a username, and enter a password twice. This feature was coded by using the given template in flask and adding our own HTML and CSS elements. We organized the page in a more unique way and gave it a design by adding CSS styles to the site. All new users are stored in the Firebase Database. 

The to-do list page where the user will open an entry and fill out the field with data requested. Once the data fields like (name of task, etc) have been entered, the program will send the entry to the local database to store for later. This feature was coded using Python, flask, and local database. 

Our Creation page allows users to create new todo items they hope to accomplish. Using python and flask, we created a feature that can create new tasks with times and dates, can alert the user, and set its priority to other tasks. The tasks that are created are stored in the Firebase database and can be seen by other users on their feeds when they are accomplished.

The Clap feature was coded using Python and Flask. Its purpose is to act as a way for users to interact with other people’s completed tasks. It acts as a way of liking a post but instead you are “clapping” for accomplished tasks.

We had a page for the user profile that was created in both Python and Flask. This page allowed the user to view their profile and the amount of tasks they completed. They were also given an award for the number of tasks completed and can be displayed on their profile page. 

The page that shows friend’s shared to-dos will update shared to-dos using firebase database. It will grab to-dos that other people have pushed to the cloud and return the to-dos as text. This feature was coded using Python, Flask, and firebase database.

We used CRUD operations with Firebase Database to create, update, read, and delete operations. This is used to implement features like sharing tasks with your friends, saving new users to the database, and accessing users when logging in. 
