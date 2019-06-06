# GameEventWeb

This is the CMPM 131 Project done by 'Group 2' at UCSC by the following students:

```
Akash Bellippady, Curtis Lee, Xintong (Brian) Liu, and Viren Singh
```

## Files

In this repository, you will find 3 files/folders.

* EventsSiteFolder - A folder with all files extracted from the EventSiteFinal.w2p, you can inspect our specific code with this.
* web2py - The web2py application (with all its fragments, remnants, and artefacts) that we used to build and run our application. We recommend using your own installation of web2py and installing EventSiteFinal.w2p.
* EventSiteFinal.w2p - The 'Pack All' version of our website, this is the tarball/zip file that contains all our source code. The extracted contents are in the 'EventsSiteFolder' directory.
* README.md - This file. Hi!

## Important Source Code Locations

When you're looking for our main source code, the following places will be helpful in the EventsSiteFolder directory.

* controllers/default.py - the 'base' controller for our website
* controllers/api.py - the means with which we communicate from our js to our database
* models/tables.py - the definitions for our database tables
* views/* - contains all our html pages. The views/default/* folder contains all pages displayed by /default.py
* static/css/* - our css, stupid.css, etc.
* static/js/* - our js. Most relevant should be default_index.js, which gets all events from the db and passes them to our homepage, and create_event.js, which handles creating an event and posting it to the database - both of these js files utilize api.py, mentioned earlier.

Additional inspection, especially of databases, can be done through the admin application of web2py.

## Hey thanks for reading.

Hope the readme was useful. We did what we could in the few weeks at the end of the term. Thanks as well to our professor, Sean Smith.
