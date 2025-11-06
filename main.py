from fastapi import FastAPI

app = FastAPI(title="My Data Service")

# Just some example data
users = [
    {"userId": 1, "firstName": "Youssef", "lastName": "Ben"},
    {"userId": 2, "firstName": "Sara", "lastName": "Lee"},
]

companies = [
    {"companyId": 1, "name": "Google", "industry": "Tech"},
    {"companyId": 2, "name": "Netflix", "industry": "Media"},
]

@app.get("/")
def read_root():
    return {"message": "Data Service is running!"}

@app.get("/users")
def get_users():
    return users

@app.get("/companies")
def get_companies():
    return companies
