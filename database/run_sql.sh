#!/bin/bash
set -e

# Define the database credentials
DB_NAME="food_helper"
DB_USER="homersimpson"

# Run SQL files
psql -U $DB_USER -d $DB_NAME -f create_table.sql
psql -U $DB_USER -d $DB_NAME -f insert_data.sql
psql -U $DB_USER -d $DB_NAME -f test_sql.sql
