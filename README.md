# ApritiSesamo

<!-- PROJECT SHIELDS -->
<!--
*** This template uses markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url]

<!-- ABOUT THE PROJECT -->
## About The Project

This project is a basic API for interacting with the GPIO pins of a RaspberryPi. The initial Idea is to have this as gateway to a "non-smart" garage door. Simply hook up a relay, an ultrsonic distance sensor and you are good to go.

### Built With

* 📞 Flask
* 💾 SQLite

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Git
```sh
sudo apt-get install git
```

* Python3
```sh
sudo apt-get install python3
```

* Pip3
```sh
sudo apt-get install python3-pip
```

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/fabio-anzola/ApritiSesamo.git
cd ApritiSesamo/
```
2. Edit your .env file
```sh
cp .env.example .env
vim .env
```
3. Copy the Database
```sh
cp accesscontrol.db.example accesscontrol.db
```
4. Install all dependencies
```sh
pip3 install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage

Start the server:
```sh
sudo chmod +x run.sh
./run.sh
```

Default login credentials are: (Please make shure to change the password)
```
admin
passw0rd
```

The following endpoints are provided:
 - (GET) / -> Checksum
 - (GET) /robots.txt -> Robots file
 - (GET) /login -> Login route (basic auth)
 - (GET) /whoami -> Who am I logged in as?
 - (GET) /door/trigger -> Toggle the relay
 - (GET) /door/status -> Check the distance from the sensor
 - (GET) /user -> Get all users
 - (POST) /user -> Create a new user (name, password)
 - (DELETE) /user/<public_id> -> Delete the user with the public id
 - (GET) /user/<public_id> -> Show the user with the public id
 - (PUT) /user/<public_id> -> Make the user with the public id an admin
 - (PATCH) /user/<public_id> -> Change the password of the user with the public id


<!-- CONTACT -->
## Contact

ANZOLA Fabio - [@anzolafabio04](https://twitter.com/anzolafabio04)

Project Link: [https://github.com/fabio-anzola/ApritiSesamo](https://github.com/fabio-anzola/ApritiSesamo)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* This readme version is a simplified version of this [github repository](https://github.com/othneildrew/Best-README-Template) by Othneildrew


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/fabio-anzola/ApritiSesamo.svg?style=flat-square
[contributors-url]: https://github.com/fabio-anzola/ApritiSesamo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/fabio-anzola/ApritiSesamo.svg?style=flat-square
[forks-url]: https://github.com/fabio-anzola/ApritiSesamo/network/members
[stars-shield]: https://img.shields.io/github/stars/fabio-anzola/ApritiSesamo.svg?style=flat-square
[stars-url]: https://github.com/fabio-anzola/ApritiSesamo/stargazers
[issues-shield]: https://img.shields.io/github/issues/fabio-anzola/ApritiSesamo.svg?style=flat-square
[issues-url]: https://github.com/fabio-anzola/ApritiSesamo/issues
