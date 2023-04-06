AWS Scripts
================

* [Introduction](#introduction)
* [Quickstart](#quickstart)
    + [Download](#download)


Introduction
----------

The objective from repository Aws-Scripts is create backups from data bases.



Quickstart
----------

### Download

Configure the ssh to create a new conection with the repository on github.

- [How generate a new key SSH.](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [How connect a key SSH on Github's account](https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)

Clones the repository:
        
    git clone git@github.com:eskolare/aws-scripts.git


### Environment

    sudo apt install virtualenv

- Create virtualenv with python version >= 3.9.

        sudo apt install python3.9
        virtualenv -p /usr/bin/python3.9 .venv
        source .venv/bin/activate
        pip install -r requirements/production.txt
        sudo apt-get install zip

### .ENV

DBNAME - Database's name.

HOSTNAME - localhost.

PGUSERNAME - User's name.

PGPASSWORD - User's password.

BUCKET - Bucket name to save the files dump.tar.gz.

BUCKET_FOLDER - Configure the directory where you'll save the files. Ex: bucket_root/dumps/

SENTRY_DSN - You can integrate with sentry log.

EC2_NAME - EC2 name.

TIME_ZONE - Ex: America/Sao_Paulo


### Start

    python ./setup.py 5 production

    """
    Parameters
    ----------
    arg1: TYPE, int
          DESCRIPTION, limit of days to keep the files on bucket.
    
    arg2: TYPE, str
          DESCRIPTION, 
          production activates the Sentry log.
          debug doesn't activates the Sentry log.
    """

