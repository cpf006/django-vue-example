# django-vue-example
Example app written in Django and Vue 3.

## Running Application

### Backend
To start the backend server:
```bash
cd backend
python manage.py runserver
```

### Frontend
To start the frontend application:
```bash
cd frontend
npm run serve
```

## API Documentation

### Number to English Words Conversion API

This API converts numeric integers into their English words representation.

#### Supported Methods

- **GET**: Retrieves the English word equivalent of the number provided as a query parameter.
- **POST**: Accepts a JSON object with a number and returns its English word equivalent.

#### Usage

##### GET Request

**Parameters**:
- `number` (required): The integer you want to convert to words.

**Example Request**:
```
GET /api/num_to_english?number=123
```

**Example Response**:
```json
{
  "status": "ok",
  "num_in_english": "one hundred twenty three"
}
```

**Error Response**:
If an invalid number or no number is provided, the API responds with:
```json
{
  "status": "error",
  "message": "Invalid input"
}
```

##### POST Request

**Body**:
- JSON object containing the key `number`.

**Headers**:
- Content-Type: application/json

**Example Request**:
```
POST /api/num_to_english
Content-Type: application/json

{
  "number": "123"
}
```

**Example Response**:
```json
{
  "status": "ok",
  "num_in_english": "one hundred twenty three"
}
```

**Error Response**:
For missing or non-integer values:
```json
{
  "status": "error",
  "message": "Invalid input"
}
```

### Error Codes

- **400 Bad Request**: Input validation failed.
- **405 Method Not Allowed**: If an HTTP method other than GET or POST is used.
- **500 Internal Server Error**: General server errors.


## Backend Tests

To run backend tests:
```bash
python manage.py test converter.tests
```
