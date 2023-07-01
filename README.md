# Grashboard

My personal dashboard / homepage as a simple static html page.
I want to quickly acces my personal services hosted on my homelab.
I also want a search bar so that this dashboard can be my newtab page on chrome.

## Technicalities

I need a static home page but i want it to be easily modifiable.
I use jinja2-render to produce my home page from a python context and a template, so that i can easily add application in python and make loops in the template for repeatable content.

## Install

Developped on Python 3.10.11 but should work with elder versions.

create virtual env :

```py
python -m venv env
```

from the venv, install the dependencys :

```py
pip install -r requirements.txt
```

## Build homepage

```py
jinja2-render -f dashboard.j2 -o dashboard.html [dashboradname]
```

for Grashboard:

```py
jinja2-render -f dashboard.j2 -o grashboard.html Grashboard
```
