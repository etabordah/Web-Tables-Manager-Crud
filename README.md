
# Web Tables Manager Crud

This project is intendend to be just a brief example of the interaction of a webpage to a database and showing some insights on it.

This will integrate some other local tools that could run on console with information provided inside the webpage and the database.


## Tech Stack

**Client:** jinja2

**Server:** fastApi, uvicorn


## Installation

After the installation of python 3.11 run the batch file "install.bat" who already has the virtual Enviroment installation and all their dependencys listed in "requirements.txt" wich can be extendend if needed.

To add a new package to the project it is possible to just update the list and re-run the installation batch file.

Batch file content and commands is as follows:
```bash
  @echo off
    python.exe -m venv virtualEnviroment
    call virtualEnviroment\Scripts\activate.bat
    python.exe -m pip install --upgrade pip
    python.exe -m pip install -r requirements.txt
    start run.bat
```
## Run Locally

Starting the server with the batch file "run.bat" will just call the virtual Enviroment and open the webpage for you before starting the app.

To start the server manually just introduce the command executed in the project folder:

```bash
    virtualEnviroment\Scripts\activate.bat
    uvicorn main:app --host 127.0.0.1 --reload
```

The Batch file content and commands are as follows:
```bash
    @echo off
    call virtualEnviroment\Scripts\activate.bat
    start "" http://127.0.0.1:8000
    uvicorn main:app --host 127.0.0.1 --reload
```
