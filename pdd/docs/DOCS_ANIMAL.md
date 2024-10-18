# Animal Disease Detection

## Frontend

The front of this animal disease detection system allows users to interact with the application by uploading images of plant parts (leaves, stems, fruits) to detect and classify diseases. The interface is designed to be intuitive, providing disease detection results, historical data, and relevant information in a user-friendly manner.

### Technologies Used

*Framework/Library*: React.js
*CSS Framework*: Bootstrap + Tailwind CSS (for responsive design).
*API Interaction*: Axios (for communicating with the backend).

Other Tools:
*HTML5* for the structure of the web pages.
*JavaScript* for interaction logic.

#### User Interface (UI)

The frontend has various components to handle user interactions.

1. **File Uploader**
The website contains a method to upload images through a file picker with a button.
2. **Results Tab**
The results tab reports the final result of the module's prediction.

### Flow (Front-end)

1. The front-end makes a request to the backend with the input image.
2. Once the backend finishes its computation, the prediction is returned in the form of a JSON output. The front-end is responsible to rendering this output in a human-readable way.

 ```json
 "payload": {
   "disease": "<disease name>",
   "confidence": 0.01, // any number between 0.0 and 1.0 
   "treatment": "<insert treatment>"
 }
 ```

## Backend

The backend of this animal disease detection project is responsible for processing input data (plant images), applying machine learning models to detect and classify plant diseases, and returning results to the user interface.

### Architecture

- Input: The system accepts images of animals (leaves, stems, etc.) either uploaded via a user interface (web or mobile) or from external sources like drones or cameras.

- Model: A pre-trained or custom machine learning model (e.g., Convolutional Neural Networks - CNN) processes the images to classify diseases.

- Output: The result, including disease type and severity level, is sent back to the user.

Tech Stack:

- *Programming Language*: Python (for model inference and backend logic).
- *Web Framework*: FastAPI for creating RESTful APIs and handling HTTP requests).
- *Machine Learning Framework*: TensorFlow + Keras  (for running the trained model)

### Endpoints

 The backend implements an endpoint for the frontend to make requests to.

1. `/process`
 The front-end supplies the image at this endpoint which returns a JSON payload with the appropriate headers and payload assuming successful model inference.
 Error Header Example:

 ```json
 // Response Status Code 415: Unsupported Media Type
 {
    "status": 415,
    "message": "failed image validation due to unsupported media type",
 }
 ```

 This error would be returned if the received input was malformed or in an invalid/unsupported format.

### Model Integration

The backend integrates the machine learning (CNN) model that detects and classifies animal diseases.
The model is loaded into memory on the server and is used to infer predictions from uploaded images.

1. Load the model
The model is loaded in the server memory if it isn't already.

1. Error Handling

 Invalid Input: The backend checks for valid image formats (e.g., .jpg, .png) and returns appropriate error messages for invalid inputs.
 If input is found to be invalid, the appropriate JSON response and headers are returned.

1. Preprocess the image
The input image is preprocessed and normalized for the model to perform accurate analysis.

1. Perform prediction
The model then outputs values which can be inferred to be classification of the animal such as: *CowHealthy* or *CowLumpy*

 If the model fails to make a prediction, the backend will terminate the computation and return an error.

Example:

```json
// Reponse Status Code 500: Internal Server Error
{
    "status": 500,
    "message": "Model prediction failed, please try again."
}
```

### Flow (Backend)

1. **Receive Image**: The backend receives the image from the frontend through the `/process` endpoint. The image is sent as part of the HTTP request.

2. **Validate Input**: The backend checks if the image format is supported (e.g., .jpg, .png). If the image is invalid or unsupported, it returns an error response (`415: Unsupported Media Type`).

3. **Preprocess Image**: If the image is valid, the backend preprocesses it. This involves steps like resizing, normalization, and any other preprocessing required by the machine learning model to ensure consistent input data.

4. **Load Model**: The pre-trained Convolutional Neural Network (CNN) model is loaded into memory. If it’s already loaded, this step is skipped.

5. **Run Inference**: The backend passes the preprocessed image to the model for inference. The model processes the image and outputs predictions, such as the detected animal, disease classification, and confidence level.

6. **Prepare Response**: The backend formats the model's predictions into a JSON payload, which includes disease, confidence score, and treatment suggestion.

7. **Return Response**: The JSON response is sent back to the frontend. If the model fails to make a prediction or encounters any internal error, a `500: Internal Server Error` is returned with an error message.

8. **Error Handling**: In case of any errors, such as unsupported image formats, invalid input, or model inference failure, the backend returns an appropriate error message (e.g., `415` for invalid format, `500` for internal server errors).
