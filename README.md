# JSON to PostgreSQL and Reverse Transformation

This project demonstrates how to insert large datasets from JSON files into a PostgreSQL database and extract selected data back into a JSON file. It includes database table creation, data insertion, and JSON conversion.

## Features

- **Data Ingestion**: Inserts data from JSON files into PostgreSQL tables.
- **Data Extraction**: Exports filtered data from the database to a JSON file.
- **Structured Code**: Organized into reusable utilities for database and file operations.

## System Requirements

- Python 3.x
- PostgreSQL (latest version recommended)
- Docker Desktop (optional, if running PostgreSQL in a container)

## Project Structure
    ```bash
    .
    ├── main.py                   # Entry point of the application
    ├── .env                      # Environment variables (not in repo)
    ├── data/                     # JSON files for input/output
    ├── db/                       # SQL scripts for creating tables
    ├── src/
    │   ├── __init__.py           # Module initialization
    │   ├── app.py                # Main logic for running insertions and extraction
    │   ├── utils/
    │       ├── __init__.py       # Utility initialization
    │       ├── database_functions.py
    │       └── file_functions.py

## Setup

1. Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/JorgeAJT/sql-fundamentals-final-project.git
    cd sql-fundamentals-final-project

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    
3. Create a .env file with your PostgreSQL credentials:
    ```makefile
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    
4. Set up the database by running the SQL scripts in the db/ folder.
5. Place your JSON data files in the data/ folder.

## Usage

Run the main script to insert data and extract selected rows:

    ```bash
    python main.py
    
- Data is inserted into the meter_data, meter_readings, and mandate_data tables.
- Filtered data (e.g., rows with mandate_status = 'N') is exported to data/selected_data.json.

## Key Components

### Database Operations

- **Connection Handling**: database_functions.py manages PostgreSQL connections and bulk insertions.
- **Dynamic Insertions**: Supports inserting complex data structures.

### File Operations

- **JSON Handling**: file_functions.py reads and writes JSON data efficiently.
- **Flexible Querying**: Exports results of custom SQL queries to JSON.

## Logging

Logs are generated during database connections, insertions, and file operations for easier debugging.

## Contributions

Feel free to fork this repository, open issues, or submit pull requests. All contributions are welcome!

Please follow these steps:

1. Fork the project.

2. Create a new branch with your changes:
   
   ```bash
   git checkout -b my-branch
   
3. Make your changes and commit them:
   
   ```bash
   git commit -m "Description of my changes"
   
4. Push your changes to your forked repository:
   
   ```bash
   git push origin my-branch
   
5. Create a Pull Request on GitHub.

## Author

Jorge Jiménez - JorgeAJT
