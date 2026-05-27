# AI-Powered Mental Wellness Screening

This Django-based web application provides an AI-powered mental health risk assessment tool designed to identify potential depression risks based on user-provided lifestyle and behavioral data. It combines a machine learning model with a rule-based scoring system to offer a more nuanced and reliable prediction.

## Key Features

*   **Hybrid AI Model:** Integrates a `scikit-learn` RandomForestClassifier with a transparent, rule-based system to flag high-risk profiles that the model alone might miss.
*   **Interactive Screening Form:** A user-friendly form to collect data on factors like sleep, social media usage, academic performance, and more.
*   **Dynamic Risk & Confidence Scoring:** The application calculates a final risk level (Low, Moderate, High) and a corresponding confidence score to make the results more intuitive.
*   **Immediate Feedback:** Users receive an instant prediction and a summary of the findings upon form submission.
*   **Built-in Grounding Tools:** Includes interactive tools like a guided box-breathing exercise and a gratitude journal to offer immediate, practical support.
*   **Django-Powered:** Built on the robust and scalable Django web framework.

## Screenshots

Here are a couple of screenshots of the application in action:

![Screenshot of the main page](screenshots/Screenshot%202026-05-27%20213136.png)
_The main interface of the wellness screening tool._

![Screenshot of the prediction result](screenshots/Screenshot%202026-05-27%20213152.png)
_Our ai model is loaded here._

## Project Structure

```
/
|-- db.sqlite3
|-- manage.py
|-- requirements.txt
|-- Dataset/
|   `-- StudentPerformanceFactors.csv
|-- mindease_project/
|   |-- settings.py
|   `-- urls.py
|-- models/
|   |-- depression_model.pkl
|   |-- scaler.pkl
|   |-- feature_names.pkl
|   `-- ... (label encoders)
`-- wellness/
    |-- ml_service.py   # Core prediction logic
    |-- views.py        # Handles form submission and renders pages
    |-- forms.py        # Defines the assessment and gratitude forms
    |-- models.py       # Database models for gratitude entries
    |-- urls.py
    `-- templates/
        `-- wellness/
            |-- home.html
            `-- partials/
                |-- assessment.html
                `-- tools.html
```

## Technology Stack

*   **Backend:** Python, Django
*   **Machine Learning:** Scikit-learn, Pandas, NumPy
*   **Frontend:** HTML, Tailwind CSS
*   **Database:** SQLite (default)

## Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-folder>
    ```

2.  **Create and Activate a Virtual Environment:**
    *   **Windows:**
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

3.  **Install Dependencies:**
    The `requirements.txt` file contains all necessary packages. Make sure `scikit-learn` is pinned to version `1.6.1` to match the saved model.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations:**
    This will set up the necessary tables for the gratitude journal feature.
    ```bash
    python manage.py migrate
    ```

5.  **Run the Development Server:**
    ```bash
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

## How It Works

The core logic resides in `wellness/ml_service.py`. When a user submits the assessment form:

1.  **Model Prediction:** The saved `RandomForestClassifier` model predicts the raw probability of depression risk.
2.  **Rule-Based Scoring:** A separate function calculates a risk score based on predefined rules for high-risk indicators (e.g., very low sleep hours, poor sleep quality).
3.  **Hybrid Score Calculation:** The model's probability and the rule-based score are blended to create a final, more sensitive hybrid score.
4.  **Confidence Inversion:** The "confidence" percentage is intelligently adjusted. For a "Low Risk" result, confidence is inverted (100% - probability) to be more intuitive.
5.  **Result Display:** The final risk level, a summary, and the confidence score are displayed to the user.
