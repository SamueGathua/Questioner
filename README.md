# Questioner
[![Build Status](https://travis-ci.org/SamueGathua/Questioner.svg?branch=develop)](https://travis-ci.org/SamueGathua/Questioner)
[![Coverage Status](https://coveralls.io/repos/github/SamueGathua/Questioner/badge.svg?branch=develop)](https://coveralls.io/github/SamueGathua/Questioner?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/03cd5ce808b7bd12e7c7/maintainability)](https://codeclimate.com/github/SamueGathua/Questioner/maintainability)

## About the project
This is a platform meant to cloud source and prioritize questions to be answered during a specific meetup or forum.The subscribed user can login to the platform view the upcoming meetup ,post questions to the upcoming meetups ,comment on question posted by other user or upvote/downvote a question posted by other users.

## Key principles observed during the development ofthis project:

    a) Pivotal tracker [here](https://www.pivotaltracker.com/n/projects/2235471)
    b) Workflow -Version control
    c) Test Driven Development(TDD).
    d) Object Oriented Programming.
    e) Data structures.
    f) Continuous Integration.
    g) Flask-restful.

### Project requirements
1. Python 3.6

### Getting Started
1. Clone this repository https://github.com/SamueGathua/Questioner.git' to your local machine.
2. Install a virtual environment 'pip install virtualenv'.
3. Create a virtual environment 'virtualenv myenv'.
4. Activate the environment 'source myenv/bin/activate'.
5. Install the required  project packages 'pip install -r requirements.txt'.
6. Setup the database environment variables
7. Enter 'Flask run' to test the API.

### API Endpoints(v1)
| **HTTP METHOD**  | **URI**                                    |  **DESCRIPTION**           |
| -----------      | -----------                                |  ---------------           |
| **POST**         | /api/v1/user/signup                        |  Create a new user.        |  
| **POST**         | /api/v1/user/login                         |  Login a user.             |
| **POST**         | /api/v1/meetups                            |  Create a new meetup.      |
| **GET**          | /api/v1/meetups                            |  Get all the meetups.      |
| **GET**          | /api/v1/meetups/<int:id>                   |  Get a specific meetup.    |
| **PUT**          | /api/v1/meetups/<int:id>                   |  Update a meetup record.   |
| **POST**         | /api/v1/meetups/<int:id>/confirms          |  Confirms attendance.     |
| **POST**         | /api/v1/meetups/<int:id>/questions         |  Create a question record. |
| **PATCH**        | /api/v1/questions/<int:id>/upvotes         |  Upvote a qustion.         |
| **PATCH**        | /api/v1//questions/<int:id>/downvotes      |  Downvote a question.      |

### API Endpoints(v2)
| **HTTP METHOD**  | **URI**                                    |  **DESCRIPTION**           |
| -----------      | -----------                                |  ---------------           |
| **POST**         | /api/v2/user/signup                        |  Creates a new user.        |  


### Running Tests
Enter 'coverage run --source=app -m pytest && coverage report' command to run tests.

### Author

Samuel Gathua
