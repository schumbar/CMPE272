# HW2: Twitter Service
**Class**: CMPE 272   
**Group Name**: Bay Area Rockers   
**Team Members**:  
1. Shawn Chumbar 
2. Dhruval Shah
3. Sajal Agarwal

### Assignment Prompt
1. Develop a simple twitter service that implement any Twitter API to to programmatically create, retrieve and delete a Tweet in the Twitter Sandbox environment.   
2. Develop a simple Web UI that implements your service and demonstrates the functions.   
3. Include in the source code comments, i.e. who wrote which code.
4. Code should include Unit tests (e.g. jUnit, TestNG, unittest, etc..)
5. Submit a Word Document of UI interaction, with screenshots


### Assignment Deliverables
Please see below for the list of assignment deliverables. Please note that all files listed are within the **CMPE272/assignment_02** folder within the associated [GitHub Repository](https://github.com/schumbar/CMPE272/blob/main/assignment_02).

1. **README.md**: README for this homework assignment
2. **.env**: environment file containing the list of keys and secrets needed for the webapp to work.
3. **authorization_information.py**: Python class that allows us to easily reference the keys and secrets within the .env file.
4. **test_twitter_client.py**: unit tests for the twitter_client class.
5. **twitter_client.py**: contains code for creating and deleting a tweet. For ease of use, we have bundled this all up into it's own class. 
6. **webapp.py**: Flask web app containing the UI which calls our service.
7. **templates/index.html**: html file containing the frontend of our webapp.
8. **venv**: folder containing our virtual python environment
9. **screenshots**: folder containing all screenshots of us interacting with the webapp's UI.

### Setup
In order to set up the project, you must perform the following steps:
1. Ensure python is installed on your machine. 
2. Navigate to the **assignment_02** directory.
3. Activate the python virtual environment:   
```source venv/bin/activate```
4. Run the following command:  
```python webapp.py```
5. Navigate to the following URL within your browser:  
```http://127.0.0.1:5000/``` 
6. Use the UI to create and delete a tweet.
7. Navigate to the [272BayAreaRockers Twitter Account](https://twitter.com/CMPE272BAR) to view the tweet updates (NOTE: You may need to refresh the page to view newly posted tweets).