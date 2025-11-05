# Live Cricket Score Webpage

This is a Flask application that fetches live cricket scores from an RSS feed and displays them on a webpage.

## Setup Instructions

1.  **Clone the repository (if applicable) or navigate to the project directory.**

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Flask application:**
    ```bash
    python app.py
    ```

6.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:5000/`.

## Project Structure

```
live_cricket_scores/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    └── (empty - for future static files like CSS/JS)
```
