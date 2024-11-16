## **SampleShare**
SampleShare is an audio sample sharing social media web application in development. 

<img width="256" alt="ss-logo" src="https://github.com/user-attachments/assets/36bfaa1e-85f8-4bb6-a5b6-68188bf9a72c">


## **What is it?**
SampleShare is a web application that uses Python's famous open-source Django web framework, MySQL for its backend database, and Docker for containerizing the project to simplify deployment and development. 
SampleShare facilitates an artistic community by enabling music enthusiasts to connect, collaborate, and share their collections of music samples. If you want to create or discover new sounds for your personal projects or showcase your developed samples, sign up with SampleShare today.

## Prerequisites

Before setting up the project, make sure you have the following installed on your respective system:
- **Git**: Required to clone the repository
- **Python 3.x**: Required to run Django and install dependencies.
- **Docker**: Used to containerize the web server and database.

### Installing Git
To install Git, visit the [official Git website](https://git-scm.com/) and download the latest version for your operating system.

### Installing Python
To install Python, visit the [official Python website](https://www.python.org/downloads/) and download the latest version for your operating system.

### Installing Docker
Follow the instructions on the [Docker website](https://docs.docker.com/get-docker/) to install Docker.

## **Installation**
To install the project follow these steps.

1. In your chosen directory clone the project.
```
git clone git@github.com:SampleShare/SampleShare.git
```
2. Go into the project directory. 
```
cd SampleShare
```
3. The project needs a .env file for correctly setting up the containers to run the web application and database. Run the create_env.py file to auto generate one for you.
```
python create_env.py
```
> [!caution] 
> This project is not ready for production, so the auto generated .env file should not be used when deploying the project for production as it is just a baseline to get the project installed and running. Always read the contents of any script before running them blindly.

4. In your chosen terminal/command prompt run this command inside the directory with the docker files to build and run the project.
```
docker compose up --build
```
> [!note] 
> For Windows/Mac users, make sure you have Docker Desktop installed and run it as an adminstrator before running the command. This will take some time depending on your internet speed and hardware.

## **Post-Installation**
Upon a successful run, your chosen terminal should look like this:

![snapshot_2024-11-15_16-54-52](https://github.com/user-attachments/assets/46afe0ef-5a1d-400f-a116-682eb5e3fc80)

Open up a browser and type in 
`
0.0.0.0:8000
`
or 
`
localhost:8000
`
to view the site. You will be presented with the view of the home page like this:

![snapshot_2024-11-15_17-00-22](https://github.com/user-attachments/assets/040e02d1-9f2b-4235-9f1d-a5b4fc66cb25)


If the results above is not what you got then retry the steps from the beginning.

## **Authors and Acknowledgment**

SampleShare was created by:

- **[Chris Pugliese](https://github.com/chrispugliese)**
- **[Saul Gonzalez](https://github.com/saul178)**
- **[Matthew Bustamante](https://github.com/Matthew-Bustamante)**
- **[Jacob Reed](https://github.com/BeachPeddler)**
- **[Dylan Reed](https://github.com/DylanCReed)**
- **[Gabriel Pantoja](https://github.com/Jeze2)**

Thank you to all the contributors for their hard work and dedication to the project.

## **Further credit towards** 
- [Wavesurfer.js](https://wavesurfer.xyz/) for their amazing audio/waveform library.
- [Matthew Ström](https://css-tricks.com/making-an-audio-waveform-visualizer-with-vanilla-javascript/) for his amazing article on waveforms and creating a unique looking waveform.
- [Bootstrap](https://getbootstrap.com/) for their free amazing web framework.
- [Django](https://www.djangoproject.com/) for their amazing Python web framework
- [FontAwesome](https://fontawesome.com/) for their amazing icons.
- [Codemy.com](https://www.youtube.com/@Codemycom) for his amazing tutorials.
- ChatGPT AI was used in CSS styling, JavaScript, and wherever we lacked knowledge.

