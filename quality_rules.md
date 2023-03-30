Here is a detailed guide on how to perform a data quality check of your data

Here is a link of the repositories you will need:

    1. https://github.com/aureliusenterprise/m4i_atlas_core

    2. https://gitlab.com/m4i/m4i-data-management


Clone all of these repositories

M4I Data Management
~~~~~~~~~~~~~~~~~~~~

This library contains all core functionality around data management for Models4Insight.

Installation 
~~~~~~~~~~~~~

Please ensure your `Python` environment is on version `3.7`. Some dependencies do not work with any later versions of `Python`.

To install `m4i-data-management` and all required dependencies to your active `Python` environment, please run the following command from the project root folder:


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

 Do the same for m4i_atlas_core

 ```
 pip install {path to m4i_atlas_core}
 
 ```


Please make a copy of `config.sample.py` and `credentials.sample.py` and rename the files to `config.py` and `credentials.py` respectively.

The `config.py` and `credentials.py` files should be located in the root folder of the project, or otherwise on the `PYTHON_PATH`.

Please remember to set the configuration parameters you want to use.



How to set up config and credentials file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the exact configuration of the config and credentials, use this to run the example.

.. code-block:: python

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
    }

    credentials = {
        "keycloak.credentials.username": "atlas",
        "keycloak.credentials.password": "",
        "atlas.server.url":"https://aureliusdev.westeurope.cloudapp.azure.com/anwo/atlas/atlas", 
        "atlas.credentials.username":"atlas",
        "atlas.credentials.password":""
    }

How to run data quality check
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



Our tool checks the quality of your data. To use it, you need to provide a csv file with your data and the rules you want to apply to it. The rules are basically the type of checks you want to do on the attributes of your dataset. We store your data and rules on Atlas and use our tool to apply the rules to your data. We then calculate the quality score of your data based on the applied rules and provied a csv output with the results.

These are the steps on how to do it:
    
    

    
    1. In the run_quality_rules.py we can now run our check. We have to provide a dataset so we can do a quality check.
       Fill in the path in the get_data_csv(). You will see it on line 63. Make a csv file with example data. Here is a simple example below.

       .. image:: imgs/sample_data_pic.png


    Just One Column named UID and provide a name.


    
    2. Finally we run our check in the run_quality_rules.py In debug mode run the 'asyncio.run(atlas_dataset_quality.run())' it's on line 59

    



