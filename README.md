# KSU-Event-API and Event-SCRAPER

## Project Overview

This project comprises a set of interconnected applications designed to **automate the collection, storage, and retrieval of event data from the KSU Events Website**. The primary goal is to build a robust system for **tracking events**, providing structured access to this information through APIs. This initiative demonstrates an end-to-end data pipeline, from web scraping and data persistence to API development for data consumption.

The system is engineered to provide reliable and timely access to event information, which can serve as a foundation for various event-tracking applications or analytical tools.

## Features

* **Automated Web Scraping:** Extracts event details from the KSU Events Website.

* **Structured Data Storage:** Dumps scraped event data into a relational database.

* **Event Data API:** Provides programmatic access to event information via a RESTful API.

* **Data Orchestration:** Utilizes cron jobs for scheduled and automated data updates.

* **Scalable Database:** Leverages Amazon RDS for a managed and scalable MySQL database.

* **Efficient Data Querying:** Implements SQLAlchemy for seamless database interactions.

* **Foundation for Event Tracking App:** Designed as the backend for a potential event tracking application.

## Technologies Used

* **Programming Language:** Python

* **Web Scraping:** Beautiful Soup

* **Web Framework (APIs):** FastAPI

* **Database:** MySQL (hosted on Amazon RDS)

* **ORM / Database Toolkit:** SQLAlchemy

* **Orchestration:** Cron Jobs

* **Version Control:** Git, GitHub

## Architecture

The project's architecture is composed of two primary interacting components: the Event Scraper and the Event API, orchestrated to ensure continuous data flow.

1.  **Event-SCRAPER:**

    * A Python-based web scraper built with **Beautiful Soup** extracts event details from the KSU Events Website.

    * This scraper is scheduled to run periodically via **cron jobs** to ensure data freshness.

    * Successfully parsed event data is then loaded into a **MySQL database** instance hosted on **Amazon RDS**.

2.  **KSU-Event-API:**

    * A **FastAPI** application exposes endpoints for querying the event data.

    * All database interactions and data querying are handled efficiently using **SQLAlchemy**, providing an abstraction layer over the raw SQL.

## Current Accomplishments

As of now, the following core functionalities are successfully implemented and operational:

* **Web Scraping & Parsing:** The web scraper can successfully extract and parse relevant event data from the KSU Events Website.

* **Database Integration:** Scraped and parsed data is reliably dumped into the MySQL database hosted on AWS RDS.

* **API Functionality:** The FastAPI application is fully functional, allowing users to query event data directly from the MySQL database through defined API endpoints.

* **Robust Querying:** All data retrieval from the database is managed through SQLAlchemy, ensuring efficient and structured querying.

## Installation & Setup

To set up and run components of this project:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/SP-32-Event-Tracker-App/KSU_Event_API.git](https://github.com/SP-32-Event-Tracker-App/KSU_Event_API.git)
    cd KSU_Event_API
    ```

2.  **Python Environment:**

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate # On macOS/Linux
    pip install -r requirements.txt
    ```

    *(Create a `requirements.txt` file in your repository listing `fastapi`, `uvicorn`, `beautifulsoup4`, `mysql-connector-python` or `pymysql`, `SQLAlchemy`.)*

3.  **MySQL on Amazon RDS Setup:**

    * Set up a MySQL instance on AWS RDS.

    * Ensure proper security group configurations to allow access from your application's environment.

    * Obtain the database endpoint, port, username, and password.

    * **Environment Variables:** Store database credentials and other sensitive information securely as environment variables (e.g., `DB_HOST`, `DB_USER`, `DB_PASSWORD`, `DB_NAME`).

4.  **Database Schema:**

    * Ensure your MySQL database has the necessary table schema (e.g., `events` table with columns like `event_id`, `title`, `date`, `time`, `location`, `description`, `url`). You might include a SQL script for table creation in your repository.

## Usage

### Running the Event Scraper

To manually run the scraper (for testing or initial data population):

```bash
python scraper/main_scraper.py
```
### Setting up Cron Jobs for Orchestration

To automate the scraper, configure a cron job on your server:

```bash
# Example cron job entry (run daily at 2 AM)  0 2 * * * /path/to/your/project/venv/bin/python /path/to/your/project/scraper/main_scraper.py >> /path/to/your/project/scraper.log 2>&1   `
```
_(Adjust paths and schedule as needed.)_

### Running the FastAPI Event API

To start the API server:

```bash
uvicorn api/main_api:app --host 0.0.0.0 --port 8000
```
_(Adjust the path if your API main script is located elsewhere.)_

Once the API is running, you can access the interactive API documentation at http://localhost:8000/docs to test endpoints.

Future Enhancements
-------------------

*   **Event Tracking Application:** Develop a front-end application (web or mobile) that consumes the KSU-Event-API to provide a user-friendly interface for tracking, searching, and filtering events.
    
*   **Advanced Filtering & Search:** Implement more sophisticated search capabilities within the API (e.g., by date range, category, keyword).
    
*   **Notifications:** Add functionality for users to receive notifications about upcoming events.
    
*   **Error Handling & Logging:** Enhance robust error handling and comprehensive logging for both the scraper and API.
    
*   **Authentication & Authorization:** Implement security measures for API access.
    
*   **Dockerization:** Containerize the scraper and API for easier deployment and management.
    
*   **Deployment Automation:** Automate deployment to a cloud environment (e.g., EC2, ECS, or serverless functions like AWS Lambda for the API).
