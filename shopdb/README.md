# ShopDB Micro Application

## Overview

ShopDB is a micro application designed to manage and analyze sales orders using a SQLite database. The application allows you to create and manage order records, including both detailed orders and company (wholesale) orders. It also provides tools for analyzing the data using Python's built-in `collections.Counter` to generate insights into product sales by category.

## Features

- **Order Management**: Create, insert, and manage detailed and company orders in a SQLite database.
- **Data Analysis**: Analyze product sales by category using Python's `Counter`.
- **Random Data Generation**: Generate random sales data for testing and development.
- **Modular Design**: Clean and modular design for easy extension and maintenance.

## Installation

### Prerequisites

- Python 3.x
- SQLite (bundled with Python via the `sqlite3` module)

### Clone the Repository

```bash
git clone https://github.com/yourusername/shopdb.git
cd shopdb
```

### Project Structure

shopdb/
│
├── ShopDB.py           # Core database management class
├── utils.py            # Utility functions for data preparation
├── variables.py        # Schemas and constants
├── main.py             # Example usage and workflow
├── README.md           # Project documentation
└── example.db          # SQLite database file (generated after running the script)