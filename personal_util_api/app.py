from fastapi import FastAPI

from personal_util_api.routes import auth, users, visit_places

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(visit_places.router)


@app.get('/')
def main():
    return {'message': 'Olá Mundo!'}
