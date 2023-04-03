# How to perform a data quality check of your data

Here is a link of the repositories you will need:

     https://github.com/aureliusenterprise/m4i_atlas_core

     https://gitlab.com/m4i/m4i-data-management




# M4I Data Management

This library contains all core functionality around data management.

Installation 

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



# How to set up config and credentials file


Here is the exact configuration of the config and credentials, use this to run the example.



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



# How to run data quality check




Our tool checks the quality of your data. To use it, you need to provide a csv file with your data and the rules you want to apply to it. The rules are basically the type of checks you want to do on the attributes of your dataset. We store your data and rules on Atlas and use our tool to apply the rules to your data. We then calculate the quality score of your data based on the applied rules and provied a csv output with the results.

These are the steps on how to do it
    
    

    
    1. In the run_quality_rules.py we can now run our check. We have to provide a dataset so we can do a quality check.
       Fill in the path in the get_data_csv(). You will see it on line 63. Make a csv file with example data. Here is a simple example below.



    Just One Column named UID and provide a name. Make an excel file.

       UID
       example_name


    
    2. Finally we run our check in the run_quality_rules.py In debug mode run the 'asyncio.run(atlas_dataset_quality.run())' it's on line 59





# How to create entities and relationships


In the create_push_to_atlas.py a user can create a dataset, field and data quality rule entity and push it to atlas. He can create a relationship between the field and dataset. I will explain how to do it with an example.


# 1.First we define the attributes for each instance

## Define the attributes for the dataset instance
 .. code-block:: python
        json_dataset={
            "attributes": {
                "name": "example",
                "qualifiedName": "example100"
            },
            "typeName": "m4i_dataset"
            }

## Define the attributes for the field instance
 .. code-block:: python
        json_field={
            "attributes": {
                "name": "field",
                "qualifiedName": "example--field"
            },
            "typeName": "m4i_field",
            "relationshipAttributes": {
                "dataset": {
                    "guid": "<guid-of-json_dataset>",
                    "typeName": "m4i_dataset",
                    "relationshipType": "m4i_dataset_fields"
                }
            }
        }

## Define the attributes for the data quality instance
 .. code-block:: python
        json_quality={
            "attributes": {
                "name": "field",
                "qualifiedName": "example--quality",
                "id": 1
            },
            "typeName": "m4i_data_quality"
            }

# 2. Create instances 

## Create instances of BusinessDataset, BusinessField, and BusinessDataQuality using the from_json method
json_str = json.dumps(json_dataset)
dataset_instance = BusinessDataset.from_json(json_str)

json_str1 = json.dumps(json_field)
field_instance= BusinessField.from_json(json_str1)

json_str2 = json.dumps(json_quality)
quality_instance = BusinessDataQuality.from_json(json_str2)

## Add relationship between the field and dataset instances
field_attributes=field_instance.attributes
field_attributes.datasets= [ObjectId(
            type_name="m4i_dataset",
            unique_attributes= M4IAttributes(
            qualified_name="example100"
        )
        )]



# 3. Push the entities to atlas.

 We use the create_entities function that can be found in the m4i_atlas_core. It is important to undertstand what are the inputs.
    create_entites(dataset_instance,referred_entites,accesss_token). The first input is the instance we created, then the referred entities, which here are non because we are just creating an entity with no relationships and finally the access token.

## Push the dataset instance to Atlas
     .. code-block:: python
        async def create_in_atlas(dataset,access_token=access_token):
            mutations_dataset = await create_entities(dataset,referred_entities=None,access_token=access_token)
            print(mutations_dataset)
        push_to_atlas= asyncio.run(create_in_atlas(dataset_instance,access_token=access_token))

## Push the field instance to Atlas

     .. code-block:: python
        async def create_in_atlas_field(field,access_token=access_token):
            mutations_field = await create_entities(field,field,referred_entities=None,access_token=access_token)
            print(mutations_field)
        push_field = asyncio.run(create_in_atlas_field(field_instance,access_token=access_token))

## Push the data quality instance to Atlas
     .. code-block:: python
        async def create_in_atlas_rule(rule,access_token=access_token):
            for i in range(100):
                try:
                    mutations_rule = await create_entities(rule,referred_entities=None,access_token=access_token)
                    break
                except:
                    print("This is not working")
            print(mutations_rule)
        push_rule = asyncio.run(create_in_atlas_rule(rule,access_token=access_token))
        











    



