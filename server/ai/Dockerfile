# Use the official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install the Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY illness.txt .
COPY medicines.txt .
COPY signs.txt .

# Copy the entire FastAPI application code into the container
COPY . .

# Expose the port that the FastAPI application will run on
EXPOSE 8001

# Specify the command to run the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
