# Alfred AI FastAPI Project Management API

This project is a Project Management API built with FastAPI, SQLAlchemy, and SQLite. The API allows users to manage projects and their associated tickets.

## Folder Structure
```bash
app/
├── api/
│ ├── errors/
│ │ ├── http_error.py
│ │ ├── validation_error.py
│ ├── routes/
│ │ ├── api.py
│ │ ├── home.py
├── core/
│ ├── config.py
│ ├── events.py
├── db_models/
│ ├── base.py
│ ├── crud.py
│ ├── session.py
├── main.py
├── project_management.db
```

## .env Instructions

Create a `.env` file in the `app/` directory with the following contents:

```env
APP_ENV=dev
```

## Using the Dockerfile

### Build the Docker Image
To build the image, navigate to the root directory of the project and run:

```bash
docker build -t <image_name> .
```

### Run the Docker Image
To run the docker container with the environment variables, run:

```bash
docker run --env-file app/.env -p 8000:8000 <image_name>
```

This command will:
- Use the environment variables in the `.env` file
- Map the container's port 8000 to the host's port 8000
- Run the container in the background
- Start the FastAPI application with the `dev` flag for FastAPI (separate from the environment variable to enable debug mode)

# Project Management API Documentation

The Project Management API is designed to facilitate the management of projects and tickets within those projects. It provides a set of endpoints for creating, retrieving, updating, and deleting both projects and tickets.

## Endpoints

### Project Endpoints

| Operation                | HTTP Method | Endpoint                   | Description                |
|--------------------------|-------------|----------------------------|----------------------------|
| **Create a new project** | `POST`      | `/projects/`               | Create a new project       |
| **Retrieve a project**   | `GET`       | `/projects/{project_id}`   | Retrieve a specific project by ID |
| **Update a project**     | `PUT`       | `/projects/{project_id}`   | Update a specific project by ID   |
| **Delete a project**     | `DELETE`    | `/projects/{project_id}`   | Delete a specific project by ID   |

### Ticket Endpoints

| Operation                | HTTP Method | Endpoint                   | Description                |
|--------------------------|-------------|----------------------------|----------------------------|
| **Create a new ticket**  |             |                            |                            |
| **Retrieve a ticket**    |             |                            |                            |
| **Update a ticket**      |             |                            |                            |
| **Delete a ticket**      |             |                            |                            |

## Running the Application Locally
To run the application locally, make sure you have Python installed. Then follow these steps at the root directory of the project:

1. Install depdencies: `pip install -r requirements.txt`
2. Run the application: `fastapi dev app/main.py` You may use `dev` or `prod` as the `fastapi` argument
3. Navigate to `http://localhost:8000` to view the application

* Note: The application will run in debug mode by default. To disable debug mode, set the `APP_ENV` environment variable to `prod`.

## License
This project is licensed under the MIT License. See the License file for details.

## Documentation
## Project Endpoints

### Create a New Project
- **Endpoint:** `POST /projects`
- **Description:** Create a new project.
- **Request Body:**
  - `name` (string): The name of the project.
  - `description` (string): The description of the project.
- **Response:**
  - `200 OK`: The created project.
- **Errors:**
  - `500 Internal Server Error`: If there is a database error.

### Retrieve a Project
- **Endpoint:** `GET /projects/{project_id}`
- **Description:** Retrieve a project by its ID.
- **Path Parameters:**
  - `project_id` (int): The ID of the project to retrieve.
- **Response:**
  - `200 OK`: The retrieved project.
- **Errors:**
  - `404 Not Found`: If the project is not found.
  - `500 Internal Server Error`: If there is a database error.

### Update a Project
- **Endpoint:** `PUT /projects/{project_id}`
- **Description:** Update a project by its ID.
- **Path Parameters:**
  - `project_id` (int): The ID of the project to update.
- **Request Body:**
  - `name` (string): The updated name of the project.
  - `description` (string): The updated description of the project.
- **Response:**
  - `200 OK`: The updated project.
- **Errors:**
  - `404 Not Found`: If the project is not found.
  - `500 Internal Server Error`: If there is a database error.

### Delete a Project
- **Endpoint:** `DELETE /projects/{project_id}`
- **Description:** Delete a project by its ID.
- **Path Parameters:**
  - `project_id` (int): The ID of the project to delete.
- **Response:**
  - `200 OK`: A message indicating the project was deleted.
- **Errors:**
  - `500 Internal Server Error`: If there is a database error.
