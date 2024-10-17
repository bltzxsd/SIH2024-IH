# Plant Disease Detection

This document describes the high-level architecture of the Plant Disease Detection Project.

## Bird's Eye View

On the highest-level the project is a program which accepts an image input from the user and
predicts diseases (early blight, late blight) in the plant.

![image](resources/architect-overview.png)

More specifically the program returns a JSON payload such as:

```json
"payload": {
    "detected_plant": "<plant name>",
    "disease": "<disease name>",
    "confidence": 0.01, // any number between 0.0 and 1.0 
    "treatment": "<insert treatment>"
}
```

This JSON string is then rendered in the website frontend.

## Codebase Overview

This section is intended to be an introduction to all the code present in the repository.

```txt
.
├── LICENSE
├── README.md
└── pdd
    ├── docs
    │   ├── ARCHITECTURE.md
    │   ├── DOCS.md
    │   └── resources/
    │       └── <resources for builidng documents>
    ├── frontend/
    │   └── *.js
    ├── notebooks/
    │   └── *.ipynb
    ├── pdd/
    │   └── *.py
    └── requirements.txt
```

### `pdd/`

Stores the main source code for the models, and the python server.

Divided into:

- `pdd/pdd/`: stores the main python source code the FastAPI server
- `pdd/models/`: stores the finished model training code

### `docs/`

Contains documentation for the entire project.

- `docs/ARCHITECTURE.md`: contains an overview of the entire project architecture
- `docs/DOCS.md`: contains in-depth documentation for the implementation details of the project.

### `notebooks/`

Contains Jupyter Notebooks used for development of the model used in the project.

### `frontend/`

Contains all the frontend components needed to build the website.
