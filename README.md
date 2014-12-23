codecorvallis.com
=================

The website!

Development
------------
This site uses [Flask](http://flask.pocoo.org/), a Python web framework, and it's hosted on [Heroku](https://www.heroku.com/).

To get started, install the [Heroku Toolbelt](https://toolbelt.heroku.com/). I'm assuming you're using OS X, so if you're on Linux or Windows, you might have to do a little bit extra, but the same idea should be possible.

Next, open a terminal session, and pull this repo from GitHub, like so:
    
    git clone https://github.com/codecorvallis/codecorvallis.com.git

Then setup your Python environment. 

    virtualenv venv
    source venv/bin/activate

Start the app using foreman:

    foreman start

And you'll see it running locally at [http://localhost:5000](http://localhost:5000).


Deployment
-------------
Currently, deployment requires access to the Heroku account that hosts the site, so if you made some changes that you want pushed into deployment, either make a pull request or send Phil a note.