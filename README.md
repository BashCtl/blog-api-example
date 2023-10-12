# Example of FastAPI framework: blog api

Project structure:
````
app/
├── api
│   └── api_v1
│       └── handlers
├── core
├── models
├── schemas
└── services

````

Clone project
````
git clone git@github.com:bohdan-sk7/blog-api-example.git
cd blog-api-example
````

Install project requirements
````
pip install -r requirements.txt
````

Start application
````
 uvicorn app.run:app --reload
````

Swagger docs - navigate to:
````
http://localhost:8000/docs
````
