#!/bin/bash

# AirBnB Clone v4 - Complete Setup Script
# This script handles installation, data setup, and server management

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_info() { echo -e "${BLUE}  $1${NC}"; }
print_success() { echo -e "${GREEN} $1${NC}"; }
print_warning() { echo -e "${YELLOW}  $1${NC}"; }
print_error() { echo -e "${RED}❌ $1${NC}"; }

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check if port is in use
check_port() {
    if lsof -Pi :$1 -sTCP:LISTEN -t >/dev/null 2>&1; then
        return 0
    else
        return 1
    fi
}

# Function to stop servers
stop_servers() {
    print_info "Stopping AirBnB Clone v4 servers..."
    pkill -f "api.v1.app" 2>/dev/null || true
    pkill -f "web_dynamic.100-hbnb" 2>/dev/null || true
    sleep 2
    print_success "All servers stopped"
}

# Function to start servers
start_servers() {
    print_info "Starting AirBnB Clone v4 servers..."
    
    # Stop any existing servers first
    stop_servers
    
    # Start API server
    print_info "Starting API server on port 5002..."
    HBNB_TYPE_STORAGE=file HBNB_API_HOST=0.0.0.0 HBNB_API_PORT=5002 python3 -m api.v1.app &
    API_PID=$!
    sleep 3
    
    # Start web server
    print_info "Starting web server on port 5001..."
    HBNB_TYPE_STORAGE=file python3 -m web_dynamic.100-hbnb &
    WEB_PID=$!
    sleep 3
    
    # Test connectivity
    print_info "Testing server connectivity..."
    
    if curl -s http://localhost:5002/api/v1/status > /dev/null 2>&1; then
        print_success "API Server is responding (PID: $API_PID)"
    else
        print_error "API Server is not responding"
        return 1
    fi
    
    if curl -s http://localhost:5001/100-hbnb/ > /dev/null 2>&1; then
        print_success "Web Server is responding (PID: $WEB_PID)"
    else
        print_error "Web Server is not responding"
        return 1
    fi
    
    echo ""
    print_success "🎉 All servers are running!"
    echo ""
    echo " Access Points:"
    echo "   🌐 Web Interface: http://localhost:5001/100-hbnb/"
    echo "   🔧 API Status:    http://localhost:5002/api/v1/status"
    echo ""
    echo "To stop: $0 stop"
    echo "Server PIDs: API=$API_PID, Web=$WEB_PID"
}

# Function to setup environment
setup_environment() {
    print_info "Setting up AirBnB Clone v4 environment..."
    
    # Check Python 3
    if ! command_exists python3; then
        print_error "Python 3 is required but not installed"
        exit 1
    fi
    print_success "Python 3 found: $(python3 --version)"
    
    # Check pip
    if ! command_exists pip3 && ! command_exists pip; then
        print_error "pip is required but not installed"
        exit 1
    fi
    print_success "pip found"
    
    # Install dependencies
    if [ -f "requirements.txt" ]; then
        print_info "Installing Python dependencies..."
        pip3 install -r requirements.txt || pip install -r requirements.txt
        print_success "Dependencies installed"
    else
        print_warning "requirements.txt not found, skipping dependency installation"
    fi
    
    # Setup sample data
    if [ -f "populate_sample_data.py" ]; then
        print_info "Setting up sample data..."
        python3 populate_sample_data.py
        print_success "Sample data populated"
    else
        print_warning "populate_sample_data.py not found, skipping data setup"
    fi
    
    print_success "Environment setup complete!"
}

# Function to show status
show_status() {
    print_info "Checking AirBnB Clone v4 status..."
    echo ""
    
    # Check API server
    if check_port 5002; then
        if curl -s http://localhost:5002/api/v1/status > /dev/null 2>&1; then
            print_success "API Server: Running and responding on port 5002"
        else
            print_warning "API Server: Port 5002 in use but not responding to API calls"
        fi
    else
        print_error "API Server: Not running on port 5002"
    fi
    
    # Check web server
    if check_port 5001; then
        if curl -s http://localhost:5001/100-hbnb/ > /dev/null 2>&1; then
            print_success "Web Server: Running and responding on port 5001"
        else
            print_warning "Web Server: Port 5001 in use but not responding to web requests"
        fi
    else
        print_error "Web Server: Not running on port 5001"
    fi
    
    # Check data file
    if [ -f "dev/file.json" ]; then
        PLACE_COUNT=$(python3 -c "import json; data=json.load(open('dev/file.json')); print(len([k for k in data.keys() if k.startswith('Place.')]))" 2>/dev/null || echo "unknown")
        print_success "Data File: Found with $PLACE_COUNT places"
    else
        print_error "Data File: dev/file.json not found"
    fi
    
    echo ""
    if check_port 5001 && check_port 5002; then
        echo "🎯 Ready to use: http://localhost:5001/100-hbnb/"
    else
        echo "🚀 Run '$0 start' to start the servers"
    fi
}

# Function to show help
show_help() {
    echo "AirBnB Clone v4 - Setup and Management Script"
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  setup     - Install dependencies and setup environment"
    echo "  start     - Start both API and web servers"
    echo "  stop      - Stop all servers"
    echo "  restart   - Stop and start servers"
    echo "  status    - Show current status"
    echo "  help      - Show this help message"
    echo ""
    echo "Quick Start:"
    echo "  $0 setup    # First time setup"
    echo "  $0 start    # Start servers"
    echo ""
    echo "Access:"
    echo "  Web App: http://localhost:5001/100-hbnb/"
    echo "  API:     http://localhost:5002/api/v1/status"
}

# Main script logic
case "${1:-help}" in
    "setup")
        setup_environment
        ;;
    "start")
        start_servers
        ;;
    "stop")
        stop_servers
        ;;
    "restart")
        stop_servers
        sleep 2
        start_servers
        ;;
    "status")
        show_status
        ;;
    "help"|"--help"|"-h"|"")
        show_help
        ;;
    *)
        print_error "Unknown command: $1"
        echo ""
        show_help
        exit 1
        ;;
esac
