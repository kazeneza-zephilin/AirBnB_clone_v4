# Holberton Tests Directory

This directory contains unit tests for the AirBnB Clone v4 project.

## Test Files

### Core Model Tests

-   `test_base_model.py` - Tests for BaseModel class basic functionality
-   `test_base_model_dict.py` - Tests for BaseModel dictionary conversion
-   `test_bm_args_params.py` - Tests for BaseModel with various arguments and parameters
-   `test_save_reload_base_model.py` - Tests for BaseModel save and reload functionality
-   `test_save_reload_user.py` - Tests for User save and reload functionality

### Storage Tests

-   `test_get_count.py` - Tests for storage get() and count() methods

### Deployment Tests

-   `test_deploy_web_static.py` - Tests for web static deployment
-   `test_do_deploy_web_static.py` - Tests for deployment execution
-   `test_pack_web_static.py` - Tests for web static packaging

### Utility Scripts

-   `start_server_with_db.sh` - Start server with database configuration
-   `test_params_create` - Test script for parameter creation functionality
-   `run_tests.sh` - Run all unit tests

## Running Tests

### Run All Tests

```bash
cd dev/hbtn_tests
./run_tests.sh
```

### Run Individual Tests

```bash
python3 -m unittest test_base_model.py
python3 -m unittest test_get_count.py
```

### Run Tests with Verbose Output

```bash
python3 -m unittest test_base_model.py -v
```

## Test Environment

The tests are configured to use file storage by default. To test with database storage, modify the environment variables in the individual test files or run:

```bash
export HBNB_TYPE_STORAGE=db
export HBNB_MYSQL_USER=hbnb_test
export HBNB_MYSQL_PWD=hbnb_test_pwd
export HBNB_MYSQL_HOST=localhost
export HBNB_MYSQL_DB=hbnb_test_db
```

## Notes

-   Tests create temporary files and clean up after themselves
-   Some tests may require the API server to be running
-   Database tests require proper MySQL setup and permissions
