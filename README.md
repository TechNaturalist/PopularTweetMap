# nlpFinalProject

# Flask

The web application for this project will be a Flask Python application. For more information, see the [documentation](https://flask.palletsprojects.com/en/2.0.x/). The [Visual Studio Code Flask tutuorial](https://code.visualstudio.com/docs/python/tutorial-flask) is also a good resource.

## Requirements

To install the requirements for this project, run `pip install -r requirements.txt`. Make sure as dependencies are added to add those to the requirements file.

## Creating a virtual environment

[Python virtual environments](https://docs.python.org/3/library/venv.html) isolate packages installed for specific purposes. This isn't required.

## Folder structure
With flask you typically have a static folder with static files (css etc.) and a templates folder with html. See the Project Layout section of [this tutorial ]https://flask.(palletsprojects.com/en/2.0.x/tutorial/index.html)for more information.

## Running the App
There is a configuration for debugging the app in Visual Studio Code. To run from the command line from the `src` directory use the command `flask run`. The default file name is app.py. Otherwise we can use:
```
$ export FLASK_APP=my_flask_app
$ flask run
```