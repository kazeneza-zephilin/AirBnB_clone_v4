#!/bin/bash

# AirBnB Clone v4 - Start Server with Database
# This script starts the API server with database configuration

echo "🚀 Starting AirBnB Clone v4 API Server with Database..."

# Set environment variables for database storage
export HBNB_TYPE_STORAGE=db
export HBNB_MYSQL_USER=hbnb_dev
export HBNB_MYSQL_PWD=hbnb_dev_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_dev_db
export HBNB_API_HOST=0.0.0.0
export HBNB_API_PORT=5002

# Start the API server
echo "Starting API server on port $HBNB_API_PORT with database storage..."
python3 -m api.v1.app &

echo "✅ API Server started with database storage"
echo "   - API running on: http://localhost:$HBNB_API_PORT"
echo "   - Storage type: Database"
echo "   - Database: $HBNB_MYSQL_DB"
echo ""
echo "Press Ctrl+C to stop the server"

wait
