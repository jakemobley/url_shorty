# URL Shorty
URL Shortening with Style

## GETTING STARTED

These instructions will get you a copy of the project up and running on your local machine.

This assumes you have python3 and pip already installed on your machine.

### Clone repository to desired location
```
git clone https://github.com/jakemobley/url_shorty.git
```

### Setup virtual environment

I use virtualenv to create isolated project environments. Use whatever virtual environment you prefer.
```
python -m venv env
source ./env/bin/activate
```

### Install dependencies 
```
pip3 install -r requirements.txt
```

This version uses an api key assigned in config.py.
(I would normally not include an API Key in plain-text nor in git)


### Initialize Flask development server
```
python3 run.py
```

With your development server open you can now visit the landing page in your local browser.
```
	localhost:5000/
```

## FAQ / CONTACT / TROUBLESHOOT

Contact me with questions at jakemobley[at]gmail[dot]com and I will answer as best I can.