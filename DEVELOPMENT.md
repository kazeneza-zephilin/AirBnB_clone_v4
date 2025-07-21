# Development Guide

## Quick Development Setup

###  One-Command Setup

```bash
./setup.sh setup    # First time setup
./setup.sh start    # Start servers
```

###  Available Commands

```bash
./setup.sh setup     # Install dependencies and setup environment
./setup.sh start     # Start both API and web servers
./setup.sh stop      # Stop all servers
./setup.sh restart   # Restart servers
./setup.sh status    # Check server status
./setup.sh help      # Show help
```

###  Access Points

-   Web Interface: http://localhost:5001/100-hbnb/
-   API Status: http://localhost:5002/api/v1/status

## Development Workflow

### Adding Sample Data

```bash
python3 populate_sample_data.py
```

### Testing API Endpoints

```bash
# Get all places
curl http://localhost:5002/api/v1/places/

# Search with filters
curl -X POST http://localhost:5002/api/v1/places_search/ \
  -H "Content-Type: application/json" \
  -d '{"amenities": ["amenity_id"]}'
```

### File Structure

-   **Data**: `dev/file.json` - All application data
-   **API**: `api/v1/` - REST API endpoints
-   **Web**: `web_dynamic/` - Frontend application
-   **Models**: `models/` - Data models and storage

### Common Tasks

#### Reset Data

```bash
rm dev/file.json
python3 populate_sample_data.py
```

#### Debug Mode

```bash
FLASK_DEBUG=1 ./setup.sh start
```

#### View Logs

Check terminal output where servers are running.

## Troubleshooting

### Port Issues

```bash
./setup.sh status    # Check current status
./setup.sh stop      # Stop all servers
./setup.sh start     # Restart servers
```

### Search Not Working

1. Check server status: `./setup.sh status`
2. Check browser console for JavaScript errors
3. Verify data exists: `./setup.sh status`

### Data Issues

```bash
./setup.sh setup     # Re-setup environment and data
./setup.sh restart   # Restart servers
```
