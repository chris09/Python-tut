# Flask

### 01. Introduction - get digitalocean droplet
### 02. Basic Flask Website tutorial
    > I do this in aws

    > $ sudo apt-get install apache2 mysql-client mysql-server
    > $ sudo apt-get install libapache2-mod-wsgi
    > $ sudo a2enmod wsgi
    > $ cd /var/www/
    > $ sudo mkdir FlaskApp
    > $ cd FlaskApp
    > $ sudo mkdir FlaskApp
    > $ cd FlaskApp    
    > $ sudo mkdir static templates
    > $ sudo nano __init__.py
    <!--
        from flask import Flask
        app = Flask(__name__)
        @app.route("/")
        def hello():
            return "Hello, I love Digital Ocean!"
        if __name__ == "__main__":
            app.run()    
     -->
    > $ sudo apt-get install python-pip
    > $ sudo pip install virtualenv
    > $ sudo virtualenv venv
    > $ source venv/bin/activate
    > $ sudo pip install flask
    > $ sudo python __init__.py
    > $ deactivate
    > $ sudo nano /etc/apache2/sites-available/FlaskApp.conf
    <!--   172.31.19.222
     <VirtualHost *:80>
    		ServerName 52.198.162.76
    		ServerAdmin chris09.yu@gmail.com
    		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
    		<Directory /var/www/FlaskApp/FlaskApp/>
    			Order allow,deny
    			Allow from all
    		</Directory>
    		Alias /static /var/www/FlaskApp/FlaskApp/static
    		<Directory /var/www/FlaskApp/FlaskApp/static/>
    			Order allow,deny
    			Allow from all
    		</Directory>
    		ErrorLog ${APACHE_LOG_DIR}/error.log
    		LogLevel warn
    		CustomLog ${APACHE_LOG_DIR}/access.log combined
        </VirtualHost>
    -->    
    > $ cd /var/www/FlaskApp
    > $ sudo nano flaskapp.wsgi
    <!--  
        #!/usr/bin/python
        import sys
        import logging
        logging.basicConfig(stream=sys.stderr)
        sys.path.insert(0,"/var/www/FlaskApp/")

        from FlaskApp import app as application
        application.secret_key = 'Add your secret key'
        <!-- e%jdrqo^u=(by621-^28bkt*#!&=_=##qje7+w95%*&^a8(c+g -->
    -->
    > $ sudo service apache2 restart


### 03.
### 04. Web Forms
### 05. Databases
### 06. Email
### 07. Large Application Structure
### 08. User Authentication
### 09. User Roles
### 10. User Profiles
### 11. Blog Posts
### 12. Followers
### 13. User Comments
### 14. Application Programming Interfaces
### 15. Testing
### 16. Performance
### 17. Deployment
### 18. Additional Resources
