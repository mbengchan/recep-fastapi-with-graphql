# Create a virtual environment
virtualenv .venv

# Activate a virtual environment
source .venv/bin/activate

# Install FastAPI
pip install fastapi

# Install Uvicorn (Asynchronous Web Server for Python)
pip install uvicorn

# Run the App
uvicorn main:app --reload