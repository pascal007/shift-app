
## Worker API

This project performs CRUD operations on book information. Also, it has user authentication enabled

### Technologies Used

- Python (version 3.10)
- Django (version 4.2.1)
- Docker (version 20.10.16)
- Database (SQLite3)

## Requirements

All requirements/dependencies used in the project can be found in the `requirements.txt` file
in the project root directory


## Installation

First, clone the repo using command below

`git clone https://github.com/pascal007/teamway-shift-app.git`

NB: If you are using a windows machine, change the entrypoint.sh end of line sequence 
from CRLF to LF

The project was containerized using docker. The project can be started by running the 
command below in the project root directory

`docker compose build`
`docker compose up`

## Usage

Once the application is up. You can use the app by accessing 
the swagger doc

`http://localhost:8000/docs/`

authentication - `JWT`



