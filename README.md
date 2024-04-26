# EMS
Event Management System Application

Welcome to the wiki for our Event Management System Application developed using Django!

Overview

Our application is designed to streamline the management of events, catering to three main user roles: Admin, Event Manager, and Event Participant.

Modules

Admin Module
   -Responsible for overall system management and user management.
   
Event Manager Module
   -Event managers are identified by their unique four-digit usernames.
    Features:
    -Posting, editing, and deleting events.
    -Viewing applications from event participants.
    -Accepting or rejecting event applications.
    
Event Participant Module
  -Event participants are identified by their unique ten-digit usernames.
   Features:
   -Viewing available events.
   -Submitting event application forms.
   -Receiving email notifications for event registrations and application status updates.
   
User Authentication

Event managers and participants can only access the system using their designated username formats, ensuring secure and efficient login processes.

Design

The application boasts a sleek and intuitive design, featuring a responsive navigation bar with options like Home, About Us, Contact Us, and an Image Gallery, providing users with easy access to essential information and functionalities.

Email Notifications

Users receive email notifications for event registrations and application status updates, enhancing communication and user experience.

Repository Structure

/src: Contains the source code for the Django application.
/docs: Documentation and resources for the project.
/tests: Test cases for ensuring the robustness of the application.
/config: Configuration files for deployment and development environments.


Getting Started
To run the application locally or deploy it, follow the instructions provided in the README.md file.
Running the Application
Before running the application, ensure that your terminal recognizes the pip command and that you have the required dependencies installed. Follow these steps:

Install Dependencies:
Navigate to the project directory.
Use the appropriate commands to install the required dependencies for the Django application. For example:
pip install -r requirements.txt

If you're using PostgreSQL as the database, install the psycopg2 package:

pip install psycopg2


Database Configuration:

If you're using PostgreSQL:
Ensure that you have PostgreSQL installed on your system.
Configure the database settings in the settings.py file of your Django project.
Alternatively, if you prefer using SQLite:
Django by default uses SQLite. You don't need to install any additional packages for it.

Running the Server:
Once dependencies are installed and database configured, run the Django development server:
python manage.py runserver

Switching Database Engines

If you decide to switch between PostgreSQL and SQLite, update the database settings in the settings.py file accordingly.
Remember to install the necessary packages (psycopg2 for PostgreSQL) if you make any changes to the database engine.

Contributors
List of contributors who have contributed to the development of this application.

SAKETH KUNUKU  - https://github.com/SakethKunuku

NISWANTHSAI DANDAMUDI - https://github.com/dniswant

MUPPIDI SAI SRUTHIK - https://github.com/Sruthik2004

Support
For any queries, issues, or suggestions, please feel free to reach out to us via the provided contact information.
