import os
import random

import httpx

from fastapi import FastAPI
from httpx import Response
from starlette.responses import FileResponse

app = FastAPI()

FIRST_VAR = 11623703
LAST_VAR = 12452485
FOLDER_FOR_VARIANTS = "variants_from_oge"


@app.on_event("startup")
def check_folder():
    if not os.path.isdir(FOLDER_FOR_VARIANTS):
        os.makedirs(FOLDER_FOR_VARIANTS)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/get-random-var")
async def random_var():
    random_variant = random.randint(FIRST_VAR, LAST_VAR + 1)
    async with httpx.AsyncClient() as client:
        response: Response = await client.get(f"https://inf-oge.sdamgia.ru/test?id={random_variant}"
                                              f"&print=true&udiff=1&pdf=h&num=true")

    path_to_file = f"{FOLDER_FOR_VARIANTS}/{random_variant}.pdf"
    with open(path_to_file, "wb") as file:
        file.write(response.read())
    return FileResponse(path_to_file)
