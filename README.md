[![Build Status](https://travis-ci.com/Livinglist/social_note.svg?branch=master)](https://travis-ci.com/Livinglist/social_note)

# social_note

To run the program, execute ```python3 myblog.py```

Link to the website: [Social Note](https://team7-social-note.herokuapp.com/login?next=%2F)

HASH: 4a5f4ed0523760b727437c3df164b91880943a37

OUR FEATURES
------------------------------------------------------------------------------------------------------------------------------
The login page is used to grab the data entered and verify if the username and password entered are stored in the SQLite database. If the data entered is in the SQLite database, the user can now access the rest of the features within the app. If the user is not found in the SQLite database, the system will prompt the user to register. This feature was coded by using the given template in flask and adding our own HTML and CSS elements. We organized the page in a more unique way and gave it a design by adding CSS styles to the site.

The register page for new users to create an account. It required them to enter their email, create a username, and enter a password twice. This feature was coded by using the given template in flask and adding our own HTML and CSS elements. We organized the page in a more unique way and gave it a design by adding CSS styles to the site. All new users are stored in the database. 

The to-do list page where the user will be able to see all the content provided on one page. This feature allows for minimal searching/confusion on the app and promotes using the app quickly and on-the-go. This feature was coded using Python, flask, and local database. 

Our Creation page allows users to create new to-do items they hope to accomplish. Using python and flask, we created a feature that can create new tasks with the displayed time. Once the data field (name of task) have been entered, the program will send the entry to the local database to store for later. This feature was coded using Python, flask, and local database. 

Based on a 24-hour timer, to-dos will move to the "failed" section on the page to show tasks that were not completed on time. For each task, there is an attribuite called creation data, if the creation data is greater than the current date, the task will instantly be transferred to the failed to-dos section. 

Counter keeps track of the quantity of completed and incomplete to-dos. This feature was coded by using the given template in flask and adding our own HTML and CSS elements. We organized the page in a more unique way and gave it a design by adding CSS styles to the site.

Created to-dos will move do their designated location based on "completed" and "incomplete" status to allow users to visually see their progress made. Once the user has checked the box field (represented by true and false), the to-do will move to the new location or stay in its current section.

We used CRUD operations with SQLite Database to create, update, read, and delete operations. This is used to implement features like saving new users to the database, and accessing users when logging in. Rach user has a unique table named after
them. The table is used to access the user's data. 

Once a to-do is moved to the "failed section," to remind the user of their failed attempts (motivation and reminder), the user will be able to see all the times they have failed to complete a task due to procrastination. This was implemented the same way as the "completed" and "incomplete" sections. 

Creation date displays the time that been passed since the creation time. This is done by comparing the time that the to-do was created to the current time. The time that is displayed will update whenever the user visits the page. 

Content will be highlighted when cursor is hovering over content to keep track of where the user is looking when there is an excessive number of to-dos on the webpage. This feature was implemented using HTML/CSS.

The option of completed the task is "greyed" out for failed to-do items. This was implemented similarly to the regular check box; however, it is always "greyed" out. This feature was implemented using HTML/CSS to block the ability of selecting the box. Since the user is unable to select the box, the to-do will remain in "failed" forever. 


