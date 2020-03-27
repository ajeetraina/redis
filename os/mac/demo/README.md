# Geolocation-Aware Demo Applications with Redis

This repository provides some exercises around Redis commands that are related to geospatial search.

This repository is just sharing the exercises of the 'Geolocation-Aware Applications with Redis' training. The learning objectives of the entire training are:

- Know how Geo-aware solutions are used and which problems are addressed by them
- Understand and be able to present the technology basics
- Understand the technical details of the Redis Geo* commands and their approach to support geo-spatial use cases
- Understand the data modeling basics
- Get insights how geo-spatial solutions are implemented with traditional vendors
- Know where to find additional resources about how to implement location-aware applications with Redis

# Pre-requisite



- Prepare a Python 3.x development environment! The Python dependencies need to be installed:
- Flask
- Redis

```
pip install flask
```

- Setting up virtualenv

```
cd geoapp
sudo easy_install virtualenv
virtualenv --python=python3 geoappvenv
```

```
$ virtualenv  geoappvenv
created virtual environment CPython2.7.16.final.0-64 in 512ms
  creator CPython2macOsFramework(dest=/Users/ajeetraina/training-geo-public/geoapp/geoappvenv, clear=False, global=False)
  seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/Users/ajeetraina/Library/Application Support/virtualenv/seed-app-data/v1.0.1)
  activators PythonActivator,CShellActivator,FishActivator,PowerShellActivator,BashActivator
ajeetraina@Ajeet-Rainas-Macbook-Pro geoapp %
```

```
$ source geoappvenv/bin/activate
(geoappvenv) ajeetraina@Ajeet-Rainas-Macbook-Pro geoapp %
```

```
$ pip install -r requirements.txt
DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
Collecting flask
  Using cached Flask-1.1.1-py2.py3-none-any.whl (94 kB)
Collecting redis
  Using cached redis-3.4.1-py2.py3-none-any.whl (71 kB)
Collecting Werkzeug>=0.15
  Using cached Werkzeug-1.0.0-py2.py3-none-any.whl (298 kB)
Collecting click>=5.1
  Using cached click-7.1.1-py2.py3-none-any.whl (82 kB)
Collecting itsdangerous>=0.24
  Using cached itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting Jinja2>=2.10.1
  Using cached Jinja2-2.11.1-py2.py3-none-any.whl (126 kB)
Collecting MarkupSafe>=0.23
  Using cached MarkupSafe-1.1.1-cp27-cp27m-macosx_10_6_intel.whl (17 kB)
Installing collected packages: Werkzeug, click, itsdangerous, MarkupSafe, Jinja2, flask, redis
Successfully installed Jinja2-2.11.1 MarkupSafe-1.1.1 Werkzeug-1.0.0 click-7.1.1 flask-1.1.1 itsdangerous-1.1.0 redis-3.4.1
(geoappvenv) ajeetraina@Ajeet-Rainas-Macbook-Pro geoapp %
```

```
python --version
```

# Run Redis with authentication

```
redis-server --requirepass redis12#
```

# Cloning the Repository

```
https://github.com/redislabs-training/training-geo-public
```

#  Redis Configuration File 

Configure the application to use your Redis database via the file ‘config.py’!


Open config.py placed under geo-public/geoapp

```
ajeetraina@Ajeet-Rainas-Macbook-Pro geoapp % pwd
/Users/ajeetraina/training-geo-public/geoapp
ajeetraina@Ajeet-Rainas-Macbook-Pro geoapp % cat config.py
REDIS_CFG = {
	"host" : "localhost",
	"port" : 6379,
	"password" : "redis12#"
}
ajeetraina@Ajeet-Rainas-Macbook-Pro geoapp %
```

# Verify the Database connectivity

```
python config.py
```

# Import Data 

- Change the directory to the source code directory ‘geo-app’!
- Take a look at the Python script ‘importer.py’!
- Run the Python script ‘importer.py’ via python importer.py!
- Wait until the import completes. The importer shows the message ‘Import of 16790 records completed’.


```
id = 355, name = Cedar Brewing, lng = -91.6918, lat = 41.9625
id = 505, name = English Ales Brewery, lng = -121.804, lat = 36.6802
id = 545, name = Fort Collins Brewery, lng = -105.042, lat = 40.5832
id = 563, name = Fuller, Smith & Turner PBC, lng = -0.2498, lat = 51.4877
id = 720, name = John Harvard's Brew House - Harvard Square, lng = -71.1193, lat = 42.3724
id = 1028, name = Pumphouse Pizza and Brewing, lng = -89.7937, lat = 43.6011
id = 1229, name = T-Bonz Gill, Grill and Brewery, lng = -79.875, lat = 32.8091
id = 421, name = Cugino Brewing Company, lng = -88.2776, lat = 41.8539
id = 626, name = Hambleton Ales, lng = -1.4844, lat = 54.1744
id = 762, name = Labatt Ontario Breweries, lng = -81.2467, lat = 42.9778
id = 915, name = Ninkasi Brewing, lng = -123.11, lat = 44.0569
id = 930, name = Oaken Barrel Brewing, lng = -86.0901, lat = 39.615
Import of 16790 records completed.
```

# Testing the application

- Change the directory to the source code directory ‘geo-app’!
- Run the command python app.py
- The application listens on port 5000, so you will be able to reach it via http://localhost:5000

```
open http://0.0.0.0:5000
```

Click on "Test DB Connectivity"

```
Database connectivity works as expected!
```

