<img src="https://github.com/jarehec/AirBnB_clone_v3/blob/master/dev/HBTN-hbnb-Final.png" width="160" height=auto />

# AirBnB Clone v4 - Complete Web Application

A full-stack web application clone of AirBnB with dynamic search functionality, built with Python Flask, JavaScript, and file-based storage.

![AirBnB Clone](https://img.shields.io/badge/Status-Fully%20Functional-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-red)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow)

## 🚀 Quick Start

### Prerequisites

-   Python 3.9+
-   Flask
-   jQuery (included via CDN)

### Installation & Setup

#### 🚀 Quick Setup (Recommended)

```bash
git clone https://github.com/kazeneza-zephilin/AirBnB_clone_v4.git
cd AirBnB_clone_v4
./setup.sh setup    # Install dependencies and setup data
./setup.sh start    # Start both servers
```

#### 📖 Manual Setup (Alternative)

1. **Clone the repository**

    ```bash
    git clone https://github.com/kazeneza-zephilin/AirBnB_clone_v4.git
    cd AirBnB_clone_v4
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Setup sample data**

    ```bash
    python3 populate_sample_data.py
    ```

4. **Start servers**
    ```bash
    ./setup.sh start
    ```

#### 🎯 Access Application

```
http://localhost:5001/100-hbnb/
```

## 🌟 Features

### ✅ Fully Functional

-   **Dynamic Search**: Filter by states, cities, and amenities
-   **Real-time Updates**: Search results update without page refresh
-   **RESTful API**: Complete CRUD operations for all resources
-   **Interactive UI**: Responsive design with jQuery
-   **File Storage**: Persistent data storage in JSON format

### 🔍 Search Functionality

-   **States Filter**: Dropdown selection of available states
-   **Cities Filter**: Dynamic cities based on selected states
-   **Amenities Filter**: Multiple checkbox selection (WiFi, Pool, Kitchen, etc.)
-   **Combined Filtering**: Use multiple filters simultaneously
-   **Live Results**: Instant search results display

## 📁 Project Structure

```
AirBnB_clone_v4/
├── � setup.sh               # 🚀 One-command setup & management
├── �📁 api/                   # REST API backend
│   └── v1/
│       ├── app.py           # API server entry point
│       └── views/           # API endpoints
├── 📁 models/               # Data models
│   ├── base_model.py       # Base class
│   ├── place.py            # Place model (with amenities)
│   ├── state.py            # State model
│   ├── city.py             # City model
│   ├── amenity.py          # Amenity model
│   └── engine/             # Storage engine
├── 📁 web_dynamic/         # Dynamic web interface
│   ├── 100-hbnb.py        # Web server
│   ├── static/scripts/     # JavaScript files
│   └── templates/          # HTML templates
├── 📁 dev/                 # Development data
│   └── file.json          # Sample data storage
├── 📄 populate_sample_data.py # Data population script
├── 📄 requirements.txt     # Python dependencies
├── 📄 DEVELOPMENT.md       # Developer guide
└── 📄 README.md           # This file
```

## 🖥️ Usage Guide

### 🚀 Starting the Application (Easy Way)

```bash
./setup.sh start    # Starts both servers
./setup.sh status   # Check if everything is running
```

### 🔧 Manual Server Management

1. **API Server** (Port 5002)

    - Provides REST endpoints for data
    - Handles search filtering logic

2. **Web Server** (Port 5001)
    - Serves the HTML interface
    - Route: `/100-hbnb/`

### Using the Search Interface

1. **Access the Application**

    ```
    http://localhost:5001/100-hbnb/
    ```

2. **Search Options**

    - **States**: Select from dropdown (California, New York, etc.)
    - **Cities**: Auto-populated based on selected states
    - **Amenities**: Check desired amenities (WiFi, Pool, Kitchen, etc.)

3. **Search Process**
    - Select your desired filters
    - Click the red "Search" button
    - Results appear instantly below

### Sample Data

The application comes with sample data including:

-   **8 Places**: Diverse properties across different states
-   **4 States**: California, New York, Louisiana, Florida
-   **20 Amenities**: WiFi, TV, Kitchen, Pool, Parking, etc.
-   **Multiple Cities**: San Francisco, Los Angeles, New York, Miami, etc.

## 🔧 API Endpoints

### Places

-   `GET /api/v1/places/` - Get all places
-   `POST /api/v1/places_search/` - Search places with filters

### States & Cities

-   `GET /api/v1/states/` - Get all states
-   `GET /api/v1/cities/` - Get all cities

### Amenities

-   `GET /api/v1/amenities/` - Get all amenities

### Search Example

```bash
curl -X POST http://localhost:5002/api/v1/places_search/
  -H "Content-Type: application/json"
  -d '{"amenities": ["wifi_id"], "states": ["state_id"]}'
```

## 🛠️ Technical Details

### Backend

-   **Framework**: Flask 2.0+
-   **Storage**: File-based JSON storage
-   **Models**: Object-oriented design with relationships
-   **API**: RESTful endpoints with JSON responses

### Frontend

-   **Framework**: jQuery 3.x
-   **AJAX**: Asynchronous search requests
-   **UI**: Dynamic content updates
-   **Responsive**: Mobile-friendly design

### Data Model Relationships

-   **Place → City → State**: Geographic hierarchy
-   **Place ↔ Amenities**: Many-to-many relationship
-   **Place → User**: Ownership relationship

## 🚨 Troubleshooting

### Common Issues

1. **Port Already in Use**

    ```bash
    # Check what's using the port
    lsof -i :5001
    lsof -i :5002

    # Kill the process
    kill -9 <PID>
    ```

2. **No Search Results**

    - Ensure API server is running on port 5002
    - Check browser console for JavaScript errors
    - Verify sample data exists in `dev/file.json`

3. **404 Not Found**
    - Use the correct URL: `http://localhost:5001/100-hbnb/`
    - Ensure web server is running

### Debug Mode

Run servers with debug output:

```bash
# API Server with debug
FLASK_DEBUG=1 HBNB_TYPE_STORAGE=file python3 -m api.v1.app

# Web Server with debug
FLASK_DEBUG=1 HBNB_TYPE_STORAGE=file python3 -m web_dynamic.100-hbnb
```

## 📋 Development

### Adding New Data

1. Run the sample data script:

    ```bash
    python3 populate_sample_data.py
    ```

2. Or manually edit `dev/file.json`

### Testing Search Functionality

1. **Basic Search**: No filters (returns all places)
2. **State Filter**: Select a state
3. **Amenity Filter**: Check WiFi or Pool
4. **Combined**: Use multiple filters together

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

See [AUTHORS](AUTHORS) file for the list of contributors.

---

**🎉 Enjoy your AirBnB Clone experience!**

For questions or issues, please open a GitHub issue or contact the maintainers.

: API with Swagger

## Description

Project attempts to clone the the AirBnB application and website, including the
database, storage, RESTful API, Web Framework, and Front End. Currently the
application is designed to run with 2 storage engine models:

-   File Storage Engine:

    -   `/models/engine/file_storage.py`

-   Database Storage Engine:

    -   `/models/engine/db_storage.py`

    -   To Setup the DataBase for testing and development, there are 2 setup
        scripts that setup a database with certain privileges: `setup_mysql_test.sql`
        & `setup_mysql_test.sql` (for more on setup, see below).

    -   The Database uses Environmental Variables for tests. To execute tests with
        the environmental variables prepend these declarations to the execution
        command:

```
$ HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd \
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db \
[COMMAND HERE]
```

## Environment

-   **OS:** Ubuntu 14.04 LTS
-   **language:** Python 3.4.3
-   **web server:** nginx/1.4.6
-   **application server:** Flask 0.12.2, Jinja2 2.9.6
-   **web server gateway:** gunicorn (version 19.7.1)
-   **database:** mysql Ver 14.14 Distrib 5.7.18
-   **documentation:** Swagger (flasgger==0.6.6)
-   **style:**
    -   **python:** PEP 8 (v. 1.7.0)
    -   **web static:** [W3C Validator](https://validator.w3.org/)
    -   **bash:** ShellCheck 0.3.3

<img src="https://github.com/jarehec/AirBnB_clone_v3/blob/master/dev/hbnb_step5.png" />

## Configuration Files

The `/config/` directory contains configuration files for `nginx` and the
Upstart scripts. The nginx configuration file is for the configuration file in
the path: `/etc/nginx/sites-available/default`. The enabled site is a sym link
to that configuration file. The upstart script should be saved in the path:
`/etc/init/[FILE_NAME.conf]`. To begin this service, execute:

```
$ sudo start airbnb.conf
```

This script's main task is to execute the following `gunicorn` command:

```
$ gunicorn --bind 127.0.0.1:8001 wsgi.wsgi:web_flask.app
```

The `gunicorn` command starts an instance of a Flask Application.

---

### Web Server Gateway Interface (WSGI)

All integration with gunicorn occurs with `Upstart` `.conf` files. The python
code for the WSGI is listed in the `/wsgi/` directory. These python files run
the designated Flask Application.

## Setup

This project comes with various setup scripts to support automation, especially
during maintanence or to scale the entire project. The following files are the
setupfiles along with a brief explanation:

-   **`dev/setup.sql`:** Drops test and dev databases, and then reinitializes
    the datbase.

    -   Usage: `$ cat dev/setup.sql | mysql -uroot -p`

-   **`setup_mysql_dev.sql`:** initialiezs dev database with mysql for testing

    -   Usage: `$ cat setup_mysql_dev.sql | mysql -uroot -p`

-   **`setup_mysql_test.sql`:** initializes test database with mysql for testing

    -   Usage: `$ cat setup_mysql_test.sql | mysql -uroot -p`

-   **`0-setup_web_static.sh`:** sets up nginx web server config file & the file
    structure.

    -   Usage: `$ sudo ./0-setup_web_static.sh`

-   **`3-deploy_web_static.py`:** uses 2 functions from (1-pack_web_static.py &
    2-do_deploy_web_static.py) that use the fabric3 python integration, to create
    a `.tgz` file on local host of all the local web static fils, and then calls
    the other function to deploy the compressed web static files. Command must
    be executed from the `AirBnB_clone` root directory.

    -   Usage: `$ fab -f 3-deploy_web_static.py deploy -i ~/.ssh/holberton -u ubuntu`

## Testing

### `unittest`

This project uses python library, `unittest` to run tests on all python files.
All unittests are in the `./tests` directory with the command:

-   File Storage Engine Model:

    -   `$ python3 -m unittest discover -v ./tests/`

-   DataBase Storage Engine Model

```
$ HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd \
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db \
python3 -m unittest discover -v ./tests/
```

---

### All Tests

The bash script `init_test.sh` executes all these tests for both File Storage &
DataBase Engine Models:

-   checks `pep8` style

-   runs all unittests

-   runs all w3c_validator tests

-   cleans up all `__pycache__` directories and the storage file, `file.json`

-   **Usage `init_test.sh`:**

```
$ ./dev/init_test.sh
```

---

### CLI Interactive Tests

-   This project uses python library, `cmd` to run tests in an interactive command
    line interface. To begin tests with the CLI, run this script:

#### File Storage Engine Model

```
$ ./console.py
```

#### To execute the CLI using the Database Storage Engine Model:

```
$ HBNB_MYSQL_USER=hbnb_test HBNB_MYSQL_PWD=hbnb_test_pwd \
HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_test_db HBNB_TYPE_STORAGE=db \
./console.py
```

#### For a detailed description of all tests, run these commands in the CLI:

```
(hbnb) help help
List available commands with "help" or detailed help with "help cmd".
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  airbnb  create   help  show
BaseModel  EOF   Review  User   all     destroy  quit  update

(hbnb) help User
class method with .function() syntax
        Usage: User.<command>(<id>)
(hbnb) help create
create: create [ARG] [PARAM 1] [PARAM 2] ...
        ARG = Class Name
        PARAM = <key name>=<value>
                value syntax: "<value>"
        SYNOPSIS: Creates a new instance of the Class from given input ARG
                  and PARAMS. Key in PARAM = an instance attribute.
        EXAMPLE: create City name="Chicago"
                 City.create(name="Chicago")
```

-   Tests in the CLI may also be executed with this syntax:

        -   **destroy:** `<class name>.destroy(<id>)`

        -   **update:** `<class name>.update(<id>, <attribute name>, <attribute value>)`

        -   **update with dictionary:** `<class name>.update(<id>,

    <dictionary representation>)`

---

### Continuous Integration Tests

Uses [Travis-CI](https://travis-ci.org/) to run all tests on all commits to the
github repo

## Authors :black_nib:

-   **MJ Johnson** - <[@mj31508](https://github.com/mj31508)>
-   **David John Coleman II** - <[davidjohncoleman.com](http://www.davidjohncoleman.com/)> | <[@djohncoleman](https://twitter.com/djohncoleman)>
-   **Kimberly Wong** - <[kjowong](https://github.com/kjowong)> | <[@kjowong](https://twitter.com/kjowong)> | <[kjowong@gmail.com](kjowong@gmail.com)>
-   **Carrie Ybay** - <[hicarrie](https://github.com/hicarrie)> | <[@hicarrie_](https://twitter.com/hicarrie_)>
-   **Jared Heck** - <[jarehec](https://github.com/jarehec)> | <[@jarehec](https://twitter.com/jarehec)>
-   **Brennan D Baraban** - <[bdbaraban](https://github.com/bdbaraban)> | <[@bdov_](https://twitter.com/bdov_)>
-   **Derrick Gee** - <[kai-dg](https://github.com/kai-dg)> | <[@the_haru_kai](https://twitter.com/the_haru_kai)>

## License

MIT License
