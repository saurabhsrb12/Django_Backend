# Django_Backend
# APIs
This Django project provides the following APIs:

## API Reference

#### GET method to retrieve a list of works.

```http
  GET /api/works/
```


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `artist` | `string` | **Required**. Filter works by artist name. Example: /works/?artist=John%20Doe. |
| `work_type` | `string` | **Required**.  Filter works by type. Example: /works/?work_type=YT. |

#### POST method to create a new user with a JSON body like {"username": "testuser", "password": "12345678"}.

```http
  GET /api/register/
```


## Running the project
#### To run this project on your local machine:

Clone this repository using the command: 

git clone https://github.com/<your_username>/<repository_name>.git.

#### Install the required packages using the command: 

pip install -r requirements.txt.

#### Run the server using the command: 

python manage.py runserver.




## API Reference

#### Get all items

```http
  GET /api/items
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |

#### Get item

```http
  GET /api/items/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

#### add(num1, num2)

Takes two numbers and returns the sum.

