# Provisioning a new site

## Required packages

- Python 3
- Git
- nginx
- pip
- virtualenvwrapper
- uwsgi

**Ubuntu and Python packages**

> `sudo apt-get install nginx`  
> `sudo apt-get install vim git python3 python3-pip`  
> `sudo pip install virtualenvwrapper`  

**Add to `~/.bashrc`**

> `export WORKON_HOME=$HOME/dev/virtenvs`  
> `source /usr/local/bin/virtualenvwrapper.sh`

## nginx virtual host configuration

- See the `nginx/template.conf` for template.

## uWSGI compilation and configuration

- Download uWSGI and build with no Python, so custom plugins ca be created.
- Unzip source to `/usr/local/lib/uwsgi-<version>`
- Run this command: `make PROFILE=nolang`
- Then build plugin for Python 3.3, 3.4, etc:
    `PYTHON=python3.3 ./uwsgi --build-plugin "plugins/python python33"`
- Create directory to store plugins: `mkdir /usr/lib/uwsgi/plugins`
- Move recently created plugin(s) to this directory:
    `mv python33_plugin.so /usr/lib/uwsgi/plugins/`
- Make sure to adjust permissions: `root:root 644`
- Finally, add plugin declaration to uwsgi INI file. See `uwsgi/template.ini` for template.

## Upstart scripts

- See `upstart/nginx.conf` and `upstart/uwsgi.conf` for templates.

## Source tree

- See `source_tree.md` for more information.

