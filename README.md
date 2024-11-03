
# Project Title

Django Assessment


## Dependency

Before running this project **Docker** needs to be installed first

- [Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Ubuntu](https://docs.docker.com/desktop/install/linux/)



## Installation

Install The Django project

```bash
  docker compose build
  docker compose up
```
    
## Usage

1. **API Endpoint User Registration**
- Endpoint: `/api/user/`
- HTTP Method: **POST**
- Payload Type: **JSON**
- Payload: 
    ```json
    {
        "email": "test@mail.com",
        "password": "1234",
        "first_name": "Test",
        "last_name": "User",
        "phone": "01732653834"
    }
    ```
- Response:
    - **Sucess**: 
    ```json
    {
        "user_id": 4,
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0LCJleHAiOjE3MzA2NDQ3MTMsImlhdCI6MTczMDY0NDExM30.3sVm6ZMUs0x_lwoEO9rVd3RqgIsgVkjpLkpBEgWFjzE"
    }
    ```
- Screenshot
    ![Logo](https://i.ibb.co.com/MMz17sK/Screenshot-5.png)

2. **API Endpoint User Status Check**

- Endpoint: `/api/user/status/`
- HTTP Method: **GET**
- Header Type: **Authorization**
- Header Value:
    ```bash
    Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0LCJleHAiOjE3MzA2NDQ3MTMsImlhdCI6MTczMDY0NDExM30.3sVm6ZMUs0x_lwoEO9rVd3RqgIsgVkjpLkpBEgWFjzE
    ```
- Response:
    - **Sucess**: 
    ```json
    {
        "id": 4,
        "email": "test2@mail.com",
        "first_name": "Test 2",
        "last_name": "User 2",
        "phone": "01732653834",
        "created_at": "2024-11-03T14:28:33.596355Z"
    }
    ```
- Screenshot
    ![Logo](https://i.ibb.co.com/TcvmdJ4/Screenshot-6.png)