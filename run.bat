@echo off
call virtualEnviroment\Scripts\activate.bat
start "" http://127.0.0.1:8000
uvicorn main:app --host 127.0.0.1 --reload