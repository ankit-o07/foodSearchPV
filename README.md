# Food Search Application

A web application built with **FastAPI** to search for food items from the FatSecret API, allowing users to view food details with pagination support.

## Features

- **Search Food**: Users can search for food items based on a search term.
- **Pagination**: Results are displayed with pagination, allowing users to navigate through multiple pages of results.
- **Results per Page**: Users can choose the number of results per page (10, 20, 30, 40, or 50).
- **Food Details**: Each food item links to a detailed page where more information can be found.
- **Dynamic Result Range**: Displays the range of results shown, such as `1 to 20 of 100`.

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: HTML, JavaScript (Vanilla JS)
- **API**: FatSecret API
- **Environment**: `.env` for storing sensitive credentials

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/food-search-app.git
```
2.	Navigate into the project directory:
```bash
cd food-search-app
```
3.	Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

4.	Install the required dependencies:

```bash
pip install -r requirements.txt
```

5.	Create a .env file in the root directory and add your FatSecret API credentials:
```bash
FATSECRET_CLIENT_ID=your_client_id
FATSECRET_CLIENT_SECRET=your_client_secret
```

Usage
1.	Run the FastAPI server:
```bash
uvicorn main:app --reload
```

2.	Open your browser and go to http://127.0.0.1:8000 to access the application.

3.	Enter a food name in the search bar, select results per page, and navigate through the pages using the pagination buttons.
API Endpoints
•	GET /: Displays the search page.
•	GET /food/search/: Searches for food items based on the provided search_expression query parameter.
o	Query Parameters:
	search_expression: Food name to search for.
	max_results: Number of results per page (e.g., 10, 20, 30, etc.).
	page_number: The page number to display results for (index starts from 0).
•	GET /food/{food_id}: Displays detailed information about a specific food item.
Environment Variables
The application uses the following environment variables:
•	FATSECRET_CLIENT_ID: Your FatSecret API client ID.
•	FATSECRET_CLIENT_SECRET: Your FatSecret API client secret.


Acknowledgements
•	FastAPI: For building modern, fast APIs with Python .
•	FatSecret API: For providing the food search data.
•	Jinja2: For templating HTML in the frontend.


# Virtual Environment
venv/

# Environment Variables
.env


