simulator
=========

py3.3-tornado server

This is a Python3 Tornado Web Server to run sockjs with sockjs-tornado

To run the server locally:
Create a virtual environment
pyvenv-3.3 {/path/to/your/venv}

Activate your venv
source {/path/to/your/venv}/bin/activate

Install dependencies into the venv
easy_install pip3
pip3 tornado
pip3 sockjs-tornado

Clone repository:
git clone {http://repo.url}

Start local server:
cd simulator
python3.3 wsgi.py

Check if working:
go to localhost:8080 in your browser
