# catch-tag
Show the relationship between hashtags and word importance in tweets using those hashtags.

Setup Node
==========
Make sure you have node installed. If not, run:
```
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm
```
Get the Code
============
Clone the repository:
```
git clone git@github.com:ayc92/catch-tag.git catch-tag
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
```python app.py```
