from typing import Optional
from typing import Annotated
from datetime import timedelta
from datetime import date
from fastapi import Form
from fastapi import FastAPI, Request, UploadFile, File

import json
import pandas as pd

from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from Scripts.database import DataBase

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")

db = DataBase('Scripts/database.db')


@app.get("/")
def raiz(request: Request):

    return templates.TemplateResponse("Components/waitingsign.html",
                                      {"request": request,
                                       'message': {'title': 'HOME'}})


@app.get("/tables1")
def tables1(request: Request):

    tables = []
    tables.append(db.get_table('tasks', config=True))

    rows = tables[0]['rows']
    summary_column = 'status'
    values = list({row[summary_column]: 0 for row in rows})
    pie_tasks = {'title': 'Progress',
                 'labels': values,
                 'data': [len([row for row in rows if row[summary_column] == value]) for value in values],
                 'ctx': 'chart-tasks'
                 }
    print(pie_tasks)
    pies = [pie_tasks]

    return templates.TemplateResponse("tasks.html",
                                      {"request": request,
                                       'tables': tables,
                                       'pies': pies
                                       })


@app.get("/tables2")
def tables2(request: Request):

    tables = []
    for table in ['users',
                  'projects'
                  ]:
        tables.append(db.get_table(table, config=True))

    return templates.TemplateResponse("Components/tablemanager.html",
                                      {"request": request,
                                       'tables': tables})


@app.post("/insert")
async def agregar(request: Request, json: str = None):
    data = await request.json()
    data = json if json else data
    db.insert(data)

    return RedirectResponse("/", 303)


@app.post("/delete/{table}/{key}")
async def eliminar(request: Request, key: str, table: str):
    db.delete(table, key)
    return RedirectResponse("/", 303)


@app.post("/edit/{table}/{key}")
async def eliminar(request: Request, key: str, table: str, json: str = None):
    data = await request.json()
    data = json if json else data

    db.edit(table, key, data)

    return RedirectResponse("/", 303)


if __name__ == "__main__":
    pass
