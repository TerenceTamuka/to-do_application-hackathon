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
The To-Do List Application offers a comprehensive set of features designed to enhance user productivity and task management. Users can easily register and authenticate, ensuring that each user's data is secure and private. Once logged in, users can create new tasks, edit existing ones, and delete tasks that are no longer needed. Additionally, users have the ability to mark tasks as completed, helping them keep track of their progress. The application also provides a clear and organized view of all tasks, making it easy for users to manage their to-do lists. Furthermore, the responsive design ensures that the application is accessible and user-friendly across various devices, including desktops, tablets, and smartphones.



### Existing Features

User Registration and Authentication
The To-Do List application includes a robust user registration and authentication system. This feature allows users to create an account by providing necessary details such as a username, email, and password. Once registered, users can log in to the application using their credentials. Authentication ensures that each user's data is secure and private, allowing only authorized users to access and manage their tasks. This feature is crucial for maintaining the integrity and confidentiality of user data.

Create, Edit, and Delete Tasks
The core functionality of the To-Do List application revolves around task management. Users can create new tasks by providing details such as the task name, description, and due date. Once a task is created, users can edit the task to update any information. This might include changing the task name, description, or due date. Additionally, users can delete tasks that are no longer needed. This CRUD (Create, Read, Update, Delete) functionality provides users with complete control over their task list, ensuring that they can manage their tasks efficiently.

Mark Tasks as Completed
To help users keep track of their progress, the application allows tasks to be marked as completed. This feature is particularly useful for users who want to visually distinguish between tasks that are still pending and those that have been finished. By marking a task as completed, users can easily see which tasks have been accomplished, providing a sense of achievement and helping to prioritize remaining tasks.

View a List of Tasks
The application provides a clear and organized view of all tasks. Users can see a list of their tasks, including details such as the task name, description, due date, and completion status. This list view helps users to quickly assess their workload and plan their activities accordingly. The interface is designed to be user-friendly and intuitive, making it easy for users to navigate through their tasks and manage them effectively.

__How features support User Stories__
User Story 1: User Registration

US01: As a new user, I want to register an account, so that I can create and manage my to-do list.

User Registration: The application provides a registration page with fields for username, email, and password. Upon successful registration, the user receives a confirmation message and is redirected to the login page. This ensures that new users can create an account and start managing their to-do lists.
User Story 2: User Login

US02: As a registered user, I want to log in to my account, so that I can access my to-do list.

User Authentication: The application provides a login page with fields for username and password. Upon successful authentication, the user is redirected to their dashboard. If the login credentials are incorrect, an error message is displayed. This ensures that registered users can securely access their to-do lists.

User Story 3: Create Task
US03: As a logged-in user, I want to create a new task, so that I can add it to my to-do list.

Create Task: The application provides a form with fields for task title, description, and completion status. Users can submit the form to create a new task, which then appears in their task list. This allows users to add new tasks to their to-do lists.

User Story 4: View Task List
US04: As a logged-in user, I want to view my list of tasks, so that I can see all my to-do items.

View Task List: The application displays a list of all tasks created by the user, including the task title, description, and completion status. This list is accessible from the user's dashboard, allowing users to easily view and manage their to-do items.

User Story 5: Edit Task
US05: As a logged-in user, I want to edit an existing task, so that I can update its details.

Edit Task: The application provides an edit button/link next to each task in the task list. Clicking the edit button opens a form pre-filled with the task's current details. Users can update the task's title, description, and completion status, and the updated task appears in the task list after saving changes. This allows users to keep their tasks up to date.
User Story 6: Delete Task

US06: As a logged-in user, I want to delete a task, so that I can remove it from my to-do list.

Delete Task: The application provides a delete button/link next to each task in the task list. Clicking the delete button prompts the user to confirm the deletion. Upon confirmation, the task is removed from the task list. This allows users to remove tasks that are no longer needed.

User Story 7: Mark Task as Completed
US07: As a logged-in user, I want to mark a task as completed, so that I can keep track of my progress.

Mark Tasks as Completed: The application provides a checkbox or button to mark tasks as completed. When a task is marked as completed, its completion status is updated, and the task visually indicates that it is completed (e.g., strikethrough text or a different color). This helps users keep track of their progress.

User Story 8: User Logout

US08: As a logged-in user, I want to log out of my account, so that I can end my session securely.

User Logout: The application provides a logout button/link in the navigation menu. Clicking the logout button logs the user out and redirects them to the login page. Upon successful logout, the user sees a confirmation message. This ensures that users can securely end their sessions.

Bootstrap Responsive Design

Bootstrap is a popular front-end framework that helps developers create responsive and mobile-first web applications. It includes a collection of CSS and JavaScript components that make it easy to design and implement responsive layouts.

Key Concepts of Bootstrap Responsive Design

Grid System:

Bootstrap's grid system allows you to create flexible and responsive layouts. It uses a series of containers, rows, and columns to layout and align content.
The grid system is based on a 12-column layout, and you can specify how many columns an element should span at different screen sizes (e.g., col-md-6 for medium screens, col-lg-4 for large screens).
Responsive Utilities:

Bootstrap provides utility classes that allow you to show or hide content based on the screen size. For example, d-none d-md-block hides an element on small screens but shows it on medium and larger screens.
Components:

Bootstrap includes a variety of pre-designed components such as navigation bars, buttons, forms, and modals that are responsive by default. These components adapt to different screen sizes and provide a consistent user experience.

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
