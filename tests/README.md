# CloudFabrix API Automation Testing

Things to be checked before executing api testcases (Manual Execution) :
1. Add Worker if not already present. Needed for running pipeline API
2. Add Organization in the portal. Needed for creating user group
3. Add User Group as "test_user_group". Needed for adding user via users API 
4. Publish `generate-alerts-suppression-policy-dataset` of `version` pipeline from draft pipelines. Remember to change version of pipeline as it is present in draft pipelines.
5. Make sure to Deactivate & Delete in the portal. USER: `user_test@cfx.com` created via API after every run of api automation.

## Steps to follow to launch the API automation

### Prerequisite 
1. Check Git version: 

    `git -version` // If not installed, goto link for installation: https://git-scm.com/downloads

2. Check for python version by performing:
        
    `python3 --version` // If not installed, goto link for installation: https://www.python.org/downloads/

### Git clone & install packages
3. Copy git clone api_postman repository link -> open terminal/cmd in your local system -> paste copied git clone command & clone the repository.

4. After successfully cloning repository. Change directory into root folder: 

    `cd api_postman/`

5. Execute required packages installation command:

    `python3 -m pip install -r requirements.txt`
  
        pytest==7.1.3
        pytest-order==1.0.1  
        pytest-metadata==2.0.4  
        pytest-html==3.2.0
        slack-sdk==3.21.2
        requests==2.31.0

### Automation Run Command & below is breakdown of command and options with their usecase:
6. Run the command from `project_directory` folder to trigger automation  

    To run particular testcase  
    `pytest -vv -s tests/{test_file_name}.py --hostip=10.95.00.000 --user=admin@cfx.com --password=admin1234`
    
    or 
    
    To run all testcases  
    `cd tests/`  
    `pytest -vv -s --hostip=10.95.00.000 --user=admin@cfx.com --password=admin1234`  


#### CFX API Swagger Documentation:
- http://{platform-hostip}/swagger/docs
