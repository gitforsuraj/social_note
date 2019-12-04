[![Build Status](https://travis-ci.com/Livinglist/social_note.svg?branch=master)](https://travis-ci.com/Livinglist/social_note)

# social_note

To run the program, execute ```python3 myblog.py```

Link to the website: [Social Note](https://team7-social-note.herokuapp.com/login?next=%2F)

OUR FEATURES
------------------------------------------------------------------------------------------------------------------------------
The login page is used to grab the data entered and verify if the username and password entered are stored in the SQLite database. If the data entered is in the SQLite database, the user can now access the rest of the features within the app. If the user is not found in the SQLite database, the system will prompt the user to register. This feature was coded by using the given template in flask and adding our own HTML and CSS elements. We organized the page in a more unique way and gave it a design by adding CSS styles to the site.

The register page for new users to create an account. It required them to enter their email, create a username, and enter a password twice. This feature was coded by using the given template in flask and adding our own HTML and CSS elements. We organized the page in a more unique way and gave it a design by adding CSS styles to the site. All new users are stored in the SQLite Database. 

The to-do list page where the user will open an entry and fill out the field with data requested. Once the data fields like (name of task, etc) have been entered, the program will send the entry to the local database to store for later. This feature was coded using Python, flask, and local database. 

Our Creation page allows users to create new todo items they hope to accomplish. Using python and flask, we created a feature that can create new tasks with times and dates, can alert the user, and set its priority to other tasks. The tasks that are created are stored in the SQLite database and can be seen by other users on their feeds when they are accomplished. 

Based on a 24 hour timer, to-dos will move to the "failed" section on the page to show tasks that were not completed on time. For each task, there is an atribuite called creation datd, if the creation data is greater than the current date, the task will instantly be transfered to the failed to-dos section. 

Counter keeps track of the quantity of completed and incompleted to-dos. This feature was coded by using the given template in flask and adding our own HTML and CSS elements. We organized the page in a more unique way and gave it a design by adding CSS styles to the site.

Created to-dos will move do their designated location based on "completed" and "incompleted" status to allow users to visually see their progress made. One the user has check the box field(represented by true and false), the to-do will move to the new location or stay in its current section.

We used CRUD operations with SQLite Database to create, update, read, and delete operations. This is used to implement features like saving new users to the database, and accessing users when logging in. Rach user has a unique table named after
them. The table is used to access the user's data. 


