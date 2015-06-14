# catch-tag
Show the relationship between hashtags and word importance in tweets using those hashtags.

Setup Play Scala Framework
==========================
1. Download Activator from https://www.playframework.com/download
2. Unzip the folder
3. Add the activator to PATH. On linux, add the following to ~/.bashrc
```export PATH=$PATH:<pathToActivator>```

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
1. Install the necessary node modules by running:
```
npm install
```
2. Last but not least, build the front end. Run the following command to build and watch for changes to js or less:
```
npm run watch
```

Run Flask App
==============
```python app.py```
