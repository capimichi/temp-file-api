# FastAPI Image Upload Service

This is a simple FastAPI application that allows users to upload and retrieve images.

## Features

- Upload images in base64 format
- Retrieve images by their unique ID

## Endpoints

### POST /upload

This endpoint accepts a POST request with a JSON body containing a base64 encoded image. The image is decoded and saved to a media directory. The unique ID of the image is returned in the response.

Request body:

```json
{
    "image": "base64_encoded_image"
}
```

Response:

```json
{
    "id": "unique_image_id"
}
```

### GET /medias/{id}

This endpoint accepts a GET request with an image ID in the URL. It returns the image file associated with the given ID.

## Running the Application
To run the application, use the following command:

To run the application, use the following command:

> main.py

By default, the application runs on 127.0.0.1:8500. You can change the host and port by setting the HOST and PORT environment variables respectively.

