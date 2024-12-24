# ASSIGNMENT - Introduction to APIs, CRUD Operations, and Flask
### (Flask CRUD API for Laptops - Testing With Postman)
this Flask Laptop API provides a set of endpoints to efficiently manage laptop records. You can add new laptops, retrieve all laptops, search for laptops by name or number, update laptop details, and delete laptops—all through simple HTTP requests. Below are the step-by-step instructions for testing these API endpoints using Postman.

## AUTHOR
* [BEATRICE NAA-MERYEA APPIAH](https://www.linkedin.com/in/beatrice-naa-meryea-appiah-468a5431b?trk=contact-inf)

## Endpoints
1. **Add a Laptop**
   - Route: `/laptops/add`
   - Method: `POST`
   - Payload Example:
     ```json
     {
       "name": "Dell XPS 13",
       "laptop_number": "DXP13",
       "specifications": {
         "CPU": "Intel i7",
         "RAM": "16GB",
         "Storage": "512GB SSD"
       }
     }
     ```
   - Response:
     - Success: `201 Created`
     - Error: `400 Bad Request`

2. **Get All Laptops**
   - Route: `/laptops`
   - Method: `GET`
   - Response: `200 OK`

3. **Get a Laptop by Name**
   - Route: `/laptops/name/<name>`
   - Method: `GET`
   - Response: 
     - Success: `200 OK`
     - Error: `404 Not Found`

4. **Get a Laptop by Laptop Number**
   - Route: `/laptops/number/<laptop_number>`
   - Method: `GET`
   - Response: 
     - Success: `200 OK`
     - Error: `404 Not Found`

5. **Update a Laptop by Laptop Number**
   - Route: `/laptops/update/<laptop_number>`
   - Method: `PUT`
   - Payload Example:
     ```json
     {
       "specifications": {
         "RAM": "32GB"
       }
     }
     ```
   - Response:
     - Success: `200 OK`
     - Error: `404 Not Found`

6. **Delete a Laptop by Laptop Number**
   - Route: `/laptops/delete/<laptop_number>`
   - Method: `DELETE`
   - Response: 
     - Success: `200 OK`
     - Error: `404 Not Found`

## Testing with Postman
1. **Add a Laptop**: Use the POST method and the appropriate payload.
2. **Get All Laptops**: Use the GET method on the `/laptops` route.
3. **Get a Laptop by Name**: Use the GET method on `/laptops/name/<name>`.
4. **Get a Laptop by Laptop Number**: Use the GET method on `/laptops/number/<laptop_number>`.
5. **Update a Laptop**: Use the PUT method on `/laptops/update/<laptop_number>` with the updated payload.
6. **Delete a Laptop**: Use the DELETE method on `/laptops/delete/<laptop_number>`.

## Tech Stack
* Flask (Python)
* Postman
* Database
  - SQL
* Local development with Node.js
* JSON

## ASSIGNMENT OVERVIEW
- app.py
- config.py
- laptops_blueprint.py
- laptops_crud.py
- README.MD
- session_crud.py

## HOW TO USE THIS DIRECTORY
- Clone the repository.
```bash
First, fork this repository, then clone it locally:
git clone https://github.com/Beatrice-Appiah/Tech4Girls_Backend.git
```

- Navigate to the Flask_CRUD_API directory.

- Run the following command:
```bash
python app.py
```