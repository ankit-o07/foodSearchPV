import os
import httpx
from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv


load_dotenv()

# FatSecret API Credentials
CLIENT_ID = os.getenv("FATSECRET_CLIENT_ID")
CLIENT_SECRET = os.getenv("FATSECRET_CLIENT_SECRET")

# FatSecret API URLs
TOKEN_URL = "https://oauth.fatsecret.com/connect/token"
URL_BASE = "https://platform.fatsecret.com/rest/"
METHOD_BASE = "https://platform.fatsecret.com/rest/server.api"

app = FastAPI()

# Set up static and template directories
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# to get the access token from FatSecret API
async def get_access_token():
    async with httpx.AsyncClient() as client:
        response = await client.post(
            TOKEN_URL,
            data={"grant_type": "client_credentials"},
            auth=(CLIENT_ID, CLIENT_SECRET),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        
        response_data = response.json()
        return response_data.get("access_token")


# search page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# search for food items
@app.get("/food/search/")
async def search_food(
    search_expression: str,
    page_number: int = 2,
    max_results: int = 20,
    access_token: str = Depends(get_access_token)
):
    print(search_expression)
    async with httpx.AsyncClient() as client:
        response = await client.get(
            METHOD_BASE,
            params={
                "method": "foods.search",
                "search_expression": search_expression,
                "page_number": page_number,
                "max_results": max_results,
                "format": "json",
            },
            headers={"Authorization": f"Bearer {access_token}"},
        )
        print(response.json());
        return response.json()
    

    
# Find food by food_id
@app.get("/food/{food_id}",response_class=HTMLResponse)
async def get_food_details(
    food_id: int, 
    request:Request,
    access_token: str = Depends(get_access_token)
):
    
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{URL_BASE}food/v3",
            params={"food_id": food_id, "format": "json"},
            headers={"Authorization": f"Bearer {access_token}"},
        )
        
        food_data = response.json()
        return templates.TemplateResponse(
            "food_details.html",
            {"request": request, "food": food_data["food"], "food_json": food_data}
        )
