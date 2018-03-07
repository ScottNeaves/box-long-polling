# Box Platform Programming Exercise - Long Polling

This script implements the Box User Events Long Polling technique, as outlined in the following documentation: https://developer.box.com/docs/using-long-polling-to-monitor-events.

## Setup

### Prerequisites
- python3: You'll need python 3 installed on your machine to run this project. If you don't have python 3, you can get it [here](https://www.python.org/downloads/release/python-364/).
- pipenv: This python project uses [pipenv](https://pipenv.readthedocs.io/en/latest/) as its dependency management tool. To install pipenv on your machine, just do `brew install pipenv` (on MacOS), or `pip install pipenv`. See the [installation instructions](https://pipenv.readthedocs.io/en/latest/install/) for additional details.

## Running it

In order to run this script, you'll need a valid Box Developer Token that you can use to programmatically connect to your personal Box account. Developer Tokens are only valid for 60 minutes, so go ahead and create a new one before you run this application. You can find documentation on how to generate a Developer Token here: https://developer.box.com/docs/getting-started-box-integration#section-using-the-box-api. Yours should look something like this: WSWcDy2ebdzGmUpH93bs9kuTGr1hIlxd. Once you have it, run the following command in this directory.

`pipenv run python long-poll.py <<YOUR_DEVELOPER_TOKEN_HERE>>`

Now go do some things in your Box account (like rename files, delete files, preview files, share files), and watch the events roll in. Enjoy!
