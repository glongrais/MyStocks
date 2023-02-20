# My Stocks Portfolio

## Requirements  
* To install the Python librairies for the backend:  
<code>pip3 install -r ./requirements.txt</code>

* To install ```npm``` and ```Node.js``` for the frontend:  
<code>brew update</code>  
<code>brew install node</code>

## Setup
* Before running the backend server for the first time, the database needs to be migrated to create the tables:  
<code>python3 ./mystocks_proj/manage.py migrate</code>  
Then run the server:  
<code>python3 ./mystocks_proj/manage.py runserver</code>

* Before running the node server for the first time, install the modules of the project. In the ```./mystocks_fe/``` folder run:  
<code>npm install</code>  
Then run the node server:  
<code>npm start</code>