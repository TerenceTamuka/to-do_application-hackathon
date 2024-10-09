<h1 align ="center">My To-Do Management Application</h1>

[View the live project here](https://to-do-fullstack-application-e112b6500c74.herokuapp.com/)

The To-Do List Application is a robust and user-friendly web application built with Django, designed to help users efficiently manage their tasks. It offers features such as user registration and authentication, allowing each user to have a personalized task management experience. Users can create, edit, and delete tasks. The application ensures that each user's data is secure and private. The interface is designed to be responsive, providing a seamless experience across various devices, whether on a desktop or mobile. This application is ideal for anyone looking to organize their tasks and improve productivity.

![Mockup]()

## Index – Table of Contents
* [User Experience UX](#user-experience-ux)
* [Features](#features)
* [Design](#design)
* [Planning](#planning)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


## User Experience (UX)

### User stories :
US01: As a new user, I want to register an account, so that I can create and manage my to-do list.

Acceptance Criteria:
1.	The registration page should have fields for username, email, and password.
2.	The user should receive a confirmation message upon successful registration.
3.	The user should be redirected to the login page after registration.

US02: As a registered user, I want to log in to my account, so that I can access my to-do list.

Acceptance Criteria:
1.	The login page should have fields for username and password.
2.	The user should be authenticated and redirected to their dashboard upon successful login.
3.	The user should see an error message if the login credentials are incorrect.

US03: As a logged-in user, I want to create a new task, so that I can add it to my to-do list.

Acceptance Criteria:
1.	The user should see a form with fields for task title, description, and completion status.
2.	The user should be able to submit the form to create a new task.
3.	The new task should appear in the user's task list after creation.

US04: As a logged-in user, I want to view my list of tasks, so that I can see all my to-do items.

Acceptance Criteria:
1.	The user should see a list of all tasks they have created.
2.	Each task should display the title, description, and completion status.
3.	The list should be accessible from the user's dashboard.

US05: As a logged-in user, I want to edit an existing task, so that I can update its details.

Acceptance Criteria:
1.	The user should see an edit button/link next to each task in the task list.
2.	Clicking the edit button/link should open a form pre-filled with the task's current details.
3.	The user should be able to update the task's title, description, and completion status.
4.	The updated task should appear in the task list after saving changes.

US06: As a logged-in user, I want to delete a task, so that I can remove it from my to-do list.

Acceptance Criteria:
1.	The user should see a delete button/link next to each task in the task list.
2.	Clicking the delete button/link should prompt the user to confirm the deletion.
3.	The task should be removed from the task list upon confirmation.

US07: As a logged-in user, I want to mark a task as completed, so that I can keep track of my progress.

Acceptance Criteria:
1.	The user should see a checkbox or button to mark a task as completed.
2.	The task's completion status should be updated when the user marks it as completed.
3.	The task should visually indicate that it is completed (e.g., strikethrough text or a different color

US08: As a logged-in user, I want to log out of my account, so that I can end my session securely.

Acceptance Criteria:
1.	The user should see a logout button/link in the navigation menu.
2.	Clicking the logout button/link should log the user out and redirect them to the login page.
3.	The user should see a confirmation message upon successful logout.

## Features



### Existing Features


__How features support User Stories__


### Features for future implementation


## Design

### Wireframes

Desktop Wireframes
iPad View Wireframes
Mobile View Wireframes
Entity-Relationship diagrams and summarisation for DBMS
Entity-Relationships Schematic Graphic of the Entity-Relationships Diagram

### ER Diagram Breakdown

__Entities:__


__-Relationships:__



__-Summary Methodology:__

## Planning

A GitHub Project with linked Issues was used as the Agile tool for this project. User Stories with acceptance criteria were defined using GitHub Issues and development of code for these stories was managed using a Kanban board. All of the User Stories were linked to a 'parent' Epic issue to show how they all supported the over-arching goal of the project. The acceptance criteria were tested as each story moved to 'Done' and were also included in the final pre-submission manual testing documented in the Testing section of this README.

The Epic, User Stories and Kanban board can be accessed here : [My To-Do Management Agile Tool](https://github.com/users/TerenceTamuka/projects/6)

## Technologies Used


### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jquery](https://jquery.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

Google Fonts: used for the Josefin Sans font
Font Awesome: was used to add icons for aesthetic and UX purposes.
Git: was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
GitHub: is used as the respository for the project code after being pushed from Git. In addition, for this project GitHub was used for the agile development aspect through the use of User Stories (GitHub Issues) and tracking them on a Kanban board.
dbdiagram.io was used to create the Entity Relationship diagrams for the application data model
Balsamiq: was used to create the wireframes during the design process.
Django was used as the framework to support rapid and secure development of the application
Bootstrap was used to build responsive web pages
Gunicorn was used as the Web Server to run Django on Heroku
dj_database_url library used to allow database urls to connect to the postgres db
psycopg2 database adapter used to support the connection to the postgres db
Cloudinary used to store the images used by the application
Summernote used to have rich text for users when creating or editing their booking for a service in the ADDITIONAL TEXT filed.
Django allauth used for account registration and authentication
Django crispy forms used to simplify form rendering
jquery library used to fade out alert messages
Django testing tools used for python mvt testing
Jest - used to test jquery in script.js functions
coverage used to check how much of the python code has been covered by automated tests

## Testing

## Validator Testing

- [HTML Validator](https://validator.w3.org/)
- [CSS Validator](https://validator.w3.org/nu/#textarea)
- [Python Validator](https://pep8ci.herokuapp.com/)

### Browser Compatibility

### Manual Testing Test Cases and Results

| **User Story (US)** | **Test Case** | **Acceptance Criteria** | **Expected Outcome** | **Actual Outcome** | **Pass/Fail** |
| ------ | ------ | ------ | ------ | ------ | ------ |

__Summary of Testing__

| **Category** | **Pass** | **Fail** | **Total Tests** |
| ---- | ---- | ---- | ---- |

__Overall Conclusion__


## Deployment

### Create Application and Postgres DB on Heroku

### Configure Cloudinary to host images used by the application

### Connect the Heroku app to the GitHub repository

### Final Deployment steps


#### The live link to the application can be found here - [My To-Do Management App](https://to-do-fullstack-application-e112b6500c74.herokuapp.com/)

## Credits 

### Media 

### Acknowledgments
