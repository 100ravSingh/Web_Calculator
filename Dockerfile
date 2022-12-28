FROM python:3.8

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Copy the source code
COPY . /app

# Set the working directory
WORKDIR /app

# Run the program
CMD ["python", "app.py"]
