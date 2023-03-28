# M4I Data Management Quality rules

link to m4i_atlas_core: https://github.com/aureliusenterprise/m4i_atlas_core

link to m4i_data_management: 

## Installation

Please ensure your `Python` environment is on version `3.7`. Some dependencies do not work with any later versions of `Python`.

install `m4i-data-management`,`m4i_atlas_core` all required dependencies to your active `Python` environment, please run the following command from the project root folder:

1)Set up a virtual environment: Use this command in the root folder,
```
virtualenv --python "C:\\Python37\\python.exe" venv.
```

2) Then activate the virtual enviroment with this command: 
```
.\env\Scripts\activate  
```

3) Install the library
```
pip install -e .
```

To install `m4i-data-management` including development dependencies, please run the following command instead:

```
pip install -e .[dev]

```
 Install m4i_data_management:
 You can clone m4i_data_management from this link https://gitlab.com/m4i/m4i_data_management
 Then you install with this command
 ```
 pip install {path to m4i_data_management}
 ```


Please make a copy of `config.sample.py` and `credentials.sample.py` and rename the files to `config.py` and `credentials.py` respectively.

The `config.py` and `credentials.py` files should be located in the root folder of the project, or otherwise on the `PYTHON_PATH`.

Please remember to set the configuration parameters you want to use.

Here is an example an explanation on how to set config and cedentials:

#use guid of dataset! not system!

# provide uid of data set you pushed on aurelius atlas2 ,https://aureliusdev.westeurope.cloudapp.azure.com/anwo/atlas2/ (The admin can provide you with username and password to log in)
    1.You provide `atlas_dataset_guid` with the guid which you can find at the link provided. You have to find the dataset you have pushed to atlas with the corresponding guid.

    2. "dataset_quality_name". You can give it any name you want.

    3. "atlas". Provide link to atlas server "https://aureliusdev.westeurope.cloudapp.azure.com/anwo/atlas/atlas"

    4. We then have to provide kecloak credentials, which is the link to the server  "https://aureliusdev.westeurope.cloudapp.azure.com/anwo/auth/", the keycloak id "m4i_public", the keycloak real name "m4i" and the keycloak secret key which is empty here.

config = {


     "atlas_dataset_guid": "f686adca-00c4-4509-b73b-1c51ae597ebe",
    "dataset_quality_name": "example_name",
    "atlas": {
        "atlas.server.url": "https://aureliusdev.westeurope.cloudapp.azure.com/anwo/atlas/atlas",
    
    },




    "keycloak.server.url": "https://aureliusdev.westeurope.cloudapp.azure.com/anwo/auth/",
    "keycloak.client.id": "m4i_public",
    "keycloak.realm.name": "m4i",
    "keycloak.client.secret.key": ""


## In our credentials file we provide The server link of atlas,username,password and the keycloak username and password.

credentials = {
    
    "keycloak.credentials.username": "atlas",
    "keycloak.credentials.password": "4n6ERGJJPDWV4ijK",
     "atlas.server.url":"https://aureliusdev.westeurope.cloudapp.azure.com/anwo/atlas/atlas", 
    "atlas.credentials.username":"atlas",
    "atlas.credentials.password":"4n6ERGJJPDWV4ijK"
}


## How to use quality rules

Our tool checks the quality of your data. To use it, you need to provide a csv file with your data and the rules you want to apply to it. The rules are basically the type of checks you want to do on the attributes of your dataset. We store your data and rules on Atlas and use our tool to apply the rules to your data. We then calculate the quality score of your data based on the applied rules and provied a csv output with the results.

These are the steps on how to do it:

    1. Use command change directory cd m4i-data-management
    
    1. First you have to push a dataset with the data quality rules you define and push it to atlas. This can be done using the m4_data_dictionary
    repository. 

    
    2. In the run_quality_rules.py we can now run our check. We have to provide a dataset so we can do a quality check.

    
    3. Finally we run our check in the run_quality_rules.py In debug mode run the 'asyncio.run(atlas_dataset_quality.run())' it's on line 87

    



