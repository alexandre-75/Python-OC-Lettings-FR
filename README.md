<p align="center"><img src="picture\16004295603423_P11.png" alt="logo" /></p>

## 1 . The Project

- Use the **Django** framework.
- Using **SQLite3** as a database.
- Using **Flake8** linting tool for Python programming language.
- Using **Pytest** for testing.
- Using **GitHub** for version control.
- Using **CircleCI** as a continuous integration (CI) and continuous deployment (CD) platform.
- Using **Docker** for creating containers.
- Using **Heroku** for host the site.
- Using **Sentry** to capture errors and exceptions.

## 2 . Context

- Orange County Lettings is a real estate company.
- I am considered a junior developer.
- I need to improve the company's site (code and deployment).
- In the project, I have to focus on :
  - **Reduction of various technical debts on the project**.
  - **Redesign of the modular architecture**.
  - **Adding a CI/CD pipeline and deployment**.
  - **Application monitoring and error tracking via Sentry**.

## 3 . Database

- SQLite is a **lightweight relational database** library.
- It is used for light applications and small projects.
- SQLite does not require any complex configuration.
- SQLite databases are stored in a **single local file on the file system**.

## 4 . Django

- Django is an **open-source web development framework** written in Python.
- Django follows the **MVT architectural pattern**.
- **Django ORM, which allows data to be manipulated using Python objects rather than direct SQL queries**.
- Django provides an **automatically generated administration interface**.
- Django incorporates security features such as **protection against CSRF attacks**, and **SQL injections**.

## 5 . Github

- GitHub is a web-based source code **versioning platform**.
- GitHub allows you to **host Git repositories**.
- GitHub makes it easy for developers to collaborate.
- GitHub offers a problem management system (issues).

## 6 . Flake8 

- Flake8 is a **linting tool** for the Python programming language.
- It **looks at each file** and generates warnings and errors based on style rules.
- These rules are based on the **PEP 8 coding style**.
- You can run Flake8 specifying the directory or files you want to scan.

```
flake8 <file>.py
```

## 7 . Pytest

- Pytest is a **testing framework** for the Python programming language.
- **It provides a set of advanced features to write and run tests.**
- Pytest is used in the Python community because of its simplicity and flexibility.

```
Pytest tests
```

## 8 . Docker 

- Docker is an open source platform.
- It is used for deploying applications in the form of **containers**.
- Containers are isolated environments that **hold an application and all of its dependencies**.
- They allow applications to run independently of differences in infrastructure.

#### 8 . 1 - DockerFile

- A Dockerfile is a **text file** that specifies the steps to build a Docker image.
- It contains instructions for copying files, installing dependencies, running commands, setting environment variables, etc.

#### 8 . 2 - Docker Image
- A Docker image is a static template that contains all the instructions and dependencies needed to run an application.
- Docker images are stored in a registry, such as Docker Hub, where they can be downloaded.

#### 8 . 3 - Docker Container
- A Docker container is a running **instance** of a Docker image. 
- This is an isolated environment that runs the application with all of its dependencies.
- Docker containers are lightweight, and provide an extra level of isolation between applications and the infrastructure.

#### 8 . 4 - Docker Registry
- A Docker registry is a centralized location where **Docker images are stored**.

## 9 . CircleCI
- CircleCI **automates tasks** related to building, testing, and deploying software.
- CircleCI sets up workflows that specify development stages.
- CircleCI is a platform that **accelerates application deployment**.
- Create a **config.yml file** in a **circleci folder** in the **root** of your Git repository.

 For example :
  - Fetch source code from a repository (GitHub).
  - Run automatic tests to verify the proper functioning of the application.
  - Deploy the application to a production  environment.
  - CircleCI can also connect to cloud services such as Heroku, Docker to facilitate your application deployment.

## 10 . Heroku
- It is used to **host** websites.
- Heroku **simplifies the process of deploying** web applications.
- Heroku makes it easy to manage your app's dependencies.

## 11 . Sentry
- Sentry is an **error and exception management platform**.
- It **collects, sorts and analyzes errors** encountered by users of your application.
- Sentry allows you to track errors that occur in your application in **real time**.

##  12 . Project download
_Tested on Windows 10, Python 3.10.6. / Django 3.0_
####  12 . 1 - project recovery
    $ git clone https://github.com/alexandre-75/Scale_a_Django_application_using_a_modular_architecture.git
####  12 . 2 - Creating a virtual environment
    python<version> -m venv nom_env_virtuel
    Activate the environment  `mon_env_virtuel\Scripts\activate` (Windows)
####  12 . 3 - Installing packages
    pip<version> install -r requirements.txt
####  12 . 4 - Start the program
 - migrations for database initialization:
    ```
    python manage.py makemigrations
    ```
    Then:
    ```bash 
    python manage.py migrate
    ```    
- ***Run the server*** by executing the command :
  ```
  python manage.py runserver
  ```
- Open your favorite browser and navigate to the ***local development server*** at :
  ```
  http://127.0.0.1:8000/
  ```  
#### 12 . 5 - create a superuser
  - create your own content and for this, you need to create a superuser with :
    ```
    python manage.py createsuperuser
    ```
#### 12 . 6 - Admin interface
  -   access the login page :
  
    ``` 
    http://127.0.0.1:8000/admin/
    ```
    
- Login with username `admin`, password `Abc1234!`

## 13 . Deployment

In order to perform the deployment and continuous integration of the app, the following accounts are required:

- [GitHub](https://github.com/) account
- [CircleCI](https://circleci.com) account (linked to GitHub account)
- [Docker](https://www.docker.com) account
- [Heroku](https://www.heroku.com) account
- [Sentry](https://sentry.io/welcome/) account
  
- The deployment of the app is automated by the CircleCI pipeline.
- When updates are pushed to the GitHub repository, the pipeline triggers the test suite and code linting for **all project branches**.
- If updates are made on the **master branch**, and **if and only if** the tests and linting pass, the workflow:
  - Builds a Docker image and pushes it to DockerHub
  - **If and only if** the previous step passes, deploys the app on Heroku

### 13 . 1 Configuration

#### 13 . 1 . 1 CircleCI

- Environment variables in CircleCI are values you can store securely and reuse
- By using environment variables you can avoid storing this information directly in your file
- To run the CircleCI pipeline, set up the following environment variables:

| CircleCI variable | Description                                                              |
|-------------------|--------------------------------------------------------------------------|
| SECRET_KEY        | project Django                                                           |
| SENTRY_DSN        | Sentry project URL                                                       |
| DOCKER_LOGIN      | Docker account username                                                  |
| DOCKER_PASSWORD   | Docker account password                                                  |
| HEROKU_APP_NAME   | Heroku app name                                                          |
| HEROKU_API_KEY    | can be found in account settings (*Heroku API Key*)                      |


#### 13 . 1 . 2 Docker

- Create a DockerHub repository. 
- The repository contains a Dockerfile that allows to easily build a Docker container and locally run the application.
-  All images are tagged with the CircleCI commit “hash” ($CIRCLE_SHA1). 
- The same container can be used for deployement for production.
- Navigate to the application root folder and build the container named img_docker: 

####  13 . 1 . 3 Heroku

- The application is pre-configured to be deployed on Heroku for production.
- Create the app manually on the Heroku website.
- The name of the app must match the **HEROKU_APP_NAME** variable set in CircleCI.
- You can now check the website from the following address: **https://<app_name>.herokuapp.com**.


####  13 . 1 . 4 Sentry 
- A simple surveillance process is implemented.
- To configure Sentry and see the errors captured by your application, you must follow these steps:
  - **Create an account** on the Sentry platform
  - **Create a project** in your Sentry account. 
  - A project represents the application you want to monitor.
  - In your application, **you must integrate the appropriate Sentry SDK**. 
  - Once the Sentry SDK is integrated into your application, it **automatically captures errors** and sends them to your Sentry account.
  - Log in to your Sentry account and navigate to the project dashboard. 
  - **Use the dashboard to explore and analyze errors**. 
  - You can **sort, filter, and search** for errors.