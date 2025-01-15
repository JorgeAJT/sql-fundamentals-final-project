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
    pip install uvicorn psycopg2
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

Ensure PostgreSQL is running (either locally or via Docker).
Run the SQL scripts located in the db/ folder to create the required tables (meter_data, meter_readings, mandate_data, etc.).
Verify that your user has permission to read/write these tables.
Prepare JSON Data

Place your source JSON files into the data/ folder.
The scripts will look for these files when inserting records.

## Usage

Run the main script to insert data and extract selected rows:

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

:man_technologist: Jorge Jiménez - [JorgeAJT](https://github.com/JorgeAJT) :weight_lifting_man:
