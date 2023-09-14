# CloudFabrix API Automation Testing

## Steps to follow to launch the API automation

### Prerequisite 
1. Check Git version: 

    `git -version` // If not installed, goto link for installation: https://git-scm.com/downloads

2. Check for python version by performing:
        
    `python3 --version` // If not installed, goto link for installation: https://www.python.org/downloads/

3. after installing infra, platform, app and worker, go to ui and create a organization and create a user group with name "test_user_group"

### Git clone & install packages


4. Execute required packages installation command:

    `python3 -m pip install -r requirements.txt`
  
        pytest==7.1.3
        pytest-order==1.0.1  
        pytest-metadata==2.0.4  
        pytest-html==3.2.0
        slack-sdk==3.21.2
        requests==2.31.0

### Automation Run Command & below is breakdown of command and options with their usecase:
5. Run the command from `project_directory` folder to trigger automation  

    `pytest -vv -s tests/ --hostip=10.95.00.00 --user=admin@cfx.com --password=abcd123$ --post-to-slack --cleanup`


#### CFX API Swagger Documentation:
- http://{cfx-portal-hostip}/swagger/docs