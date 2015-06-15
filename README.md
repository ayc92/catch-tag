# catch-tag
Show the relationship between hashtags and word importance in tweets using those hashtags.

Get the Code
============
Clone the repository:
```
git clone git@github.com:ayc92/catch-tag.git catch-tag
```

Setup Virtualenv, Flask, and UWSGI
==================================
First, make sure you have `virtualenv` installed:
```
sudo pip install virtualenv
```
Now, at the project root, create a fresh virtualenv by running:
```
virtualenv env
```
There should now be a folder called `env` at the project root level.
To activate the environment, making sure you're in the project root, run:
```
. env/bin/activate
```
Then install python dependencies in the env by running:
```
pip install -r requirements.txt
```
The main dependencies to note are `flask` and `uwsgi`.
For simplicity's sake, the catch-tag flask app runs solely on a uwsgi server. `nginx` is a bit overkill, since we most likely won't be servicing a high load of requests.


Setup Node
==========
Make sure you have node installed. If not, run:
```
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm
```

Build Js and Less
====================
1. ```cd web```
2. Install the necessary node modules by running:
```
npm install
```
3. Last but not least, build the front end. Run the following command to build and watch for changes to js or less:
```
npm run watch
```

Run Flask App
==============
To run the Flask app, just run the UWSGI server.
```
bin/runserver
```
This is just a shell script that starts the uwsgi server using `catch_tag.ini` as the configuration file.
Now if you navigate over to `localhost:8000` in the browser, you should be able to see the app.
