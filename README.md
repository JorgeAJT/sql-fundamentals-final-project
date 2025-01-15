# JSON to PostgreSQL and Reverse Transformation

This project demonstrates how to insert large datasets from JSON files into a **PostgreSQL** database and extract selected data back into a JSON file. It includes **database table creation**, **data insertion**, and **JSON conversion** processes, organized with clear, reusable utility modules.

## Table of Contents

1. [Overview](#overview)

2. [Features](#features)

3. [Requirements](#requirements)

4. [Project Structure](#project-structure)

5. [Installation](#installation)

6. [Usage](#usage)

7. [Key Components](#key-components)

    - [Database Operations](#database-operations)

    - [File Operations](#file-operations)

    - [Logging](#logging)

8. [Contributing](#contributing)

9. [Author](#author)

## Overview

The goal of this project is to **automate** the process of importing JSON data into a PostgreSQL database and exporting filtered rows back to a JSON file. This setup is useful for scenarios where large or complex JSON structures need to be stored, queried, and partially retrieved. The process is broken down into two major steps:
1. **Data Ingestion**: Reads JSON files and inserts data into relevant PostgreSQL tables.
2. **Data Extraction**: Performs custom SQL queries on these tables and saves the results into a new JSON file.

By following the steps below, you’ll be able to replicate or extend this functionality in your own PostgreSQL environment.

## Features

- **Data Ingestion**: Inserts data from JSON files into PostgreSQL tables.
- **Data Extraction**: Exports filtered data from the database to a JSON file.
- **Structured Code**: Organized into reusable utilities for database and file operations.
- **Logging**: Generates logs to help trace the data flow and debug issues.
- **Flexible Querying**: Easily configure which rows or columns get exported.

## Requirements

- **Python 3.x**
- **PostgreSQL** (latest version recommended)
- **Docker Desktop** *(optional, if running PostgreSQL in a container)*

## Project Structure
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
    └── requirements.txt           # Python dependencies
    
### Main Files

1. `main.py`
    
    - Runs the primary flow: reads JSON files, inserts data, and optionally extracts data to a new JSON file.

2. `.env`

    - Holds PostgreSQL credentials (`DB_NAME`, `DB_USER`, `DB_PASSWORD`) and other environment variables.
      
3. `data/`

    - Contains JSON files to be ingested, and where the output JSON file (with filtered data) is generated.

4. `db/`

    - Contains SQL scripts for creating the **meter_data**, **meter_readings**, and **mandate_data** tables (or any additional tables).

5. `src/`

    - `app.py`: Central logic for coordinating reading JSON, inserting records, and exporting results.

    - `utils/`: Utility modules for database connections/operations and file handling.


## Installation

1. Clone the Repository:
    ```bash
    git clone https://github.com/JorgeAJT/sql-fundamentals-final-project.git
    cd sql-fundamentals-final-project
    
2. **Install dependencies** (if you have a `requirements.txt`):
    ```bash
    pip install -r requirements.txt
    ```
    Or install manually:
    ```bash
    pip install psycopg2-binary python-dotenv
    ```

3. Create a `.env` File  
In the project root, create a file named `.env` with your PostgreSQL credentials:
    ```bash
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    ```
    *These values are used by the utility functions to connect to your PostgreSQL database.*

4. Set Up the Database

    - Ensure PostgreSQL is running (either locally or via Docker).
    - Run the SQL scripts located in the `db/` folder to create the required tables (`meter_data`, `meter_readings`, `mandate_data`, etc.).
    - Verify that your user has permission to read/write these tables.
      
5. Prepare JSON Data

    - Place your source JSON files into the `data/` folder.
    - The scripts will look for these files when inserting records.

## Usage

1. **Execute the Main Script**
    ```bash
    python main.py
    ```
    By default, it will:
   
    - Read the specified JSON files (e.g., `data/meter_data.json`)
      
    - Insert the data into the corresponding tables (`meter_data`, `meter_readings`, `mandate_data`)
      
    - Filter rows based on certain conditions (for example, `mandate_status = 'N'`)
      
    - Export the filtered rows to a JSON file (e.g., `data/selected_data.json`)
   
3. **Customize Queries/Logic**

    - Edit `src/app.py` or the utility functions in `src/utils/database_functions.py` to change how data is inserted or which rows are extracted.
      
    - Modify `src/utils/file_functions.py` to customize file paths or handle different file formats.

4. **Review Logs (Optional)**

    - Depending on your implementation, you may have logging statements in these utility functions.
      
    - Check the logs to confirm data was processed successfully or diagnose issues if something goes wrong.

## Key Components

### Database Operations

Located in `src/utils/database_functions.py`:
    
- **Connection Handling**: Manages PostgreSQL connections using credentials from `.env`.
    
- **Bulk Insertions**: Functions to insert complex JSON data into tables without manually specifying each column.
    
- **Custom Queries**: Methods for running queries to filter or transform data before exporting.
    
### File Operations

Located in `src/utils/file_functions.py`:

- **JSON Handling**: Reads input JSON files and writes output JSON files.
    
- **Data Validation**: Optionally checks file structure before processing.
    
- **Flexible Querying**: Allows you to export the results of custom SQL queries to new JSON files.

### Logging

- **Debugging**: Log messages (if configured) let you see each step: connection to the database, reading files, inserting rows, exporting JSON, etc.
    
- **Troubleshooting**: Errors are logged to help identify where a failure occurred (e.g., invalid file format, connection issues).

## Contributing

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

:man_technologist: Jorge Jiménez - [JorgeAJT](https://github.com/JorgeAJT) :weight_lifting_man:

Questions or suggestions? Feel free to open an issue or submit a pull request!
