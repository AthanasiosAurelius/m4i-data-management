# M4I Data Management Quality rules

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
How do i install this, do i add a path?
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


In our credentials file we provide The server link of atlas,username,password and the keycloak username and password.

credentials = {
    
    "keycloak.credentials.username": "atlas",
    "keycloak.credentials.password": "4n6ERGJJPDWV4ijK",
     "atlas.server.url":"https://aureliusdev.westeurope.cloudapp.azure.com/anwo/atlas/atlas", 
    "atlas.credentials.username":"atlas",
    "atlas.credentials.password":"4n6ERGJJPDWV4ijK"
}


## Testing

This project uses `pytest` as its unit testing framework.
To run the unit tests, please install `pytest` and then execute the `pytest` command from the project root folder.

Unit tests are grouped per module.
Unit test modules are located in the same folder as their respective covered modules.
They can be recognized by the `test__` module name prefix, followed by the name of the covered module.