
# Project Structure

```bash
C:\path\to\project\folder	
├── .gitignore
├── environment.yml                     # conda env config
├── LICENSE
├── Makefile                                    
├── pyproject.toml                      # config for linters
├── README.md
├── requirements.txt                    # local package requirements
├── setup.py                            # local package install 
├── config
│   ├── catalog.yaml                    # data and metadata catalog
│   ├── credentials.yaml            
│   ├── logging.yaml                    
│   ├── parameters.yaml                 # project parameters
│   └── template.env                    # environment variables do NOT commit
├── docs
│   └── project_structure.md
├── log
│   └── .gitkeep
├── notebooks
└── src
    ├── config.py                       # load project config
    ├── decorators.py                   # project decorators
    ├── logger.py                       # logging config
    ├── utils.py                        # project utility methods       
    ├── __init__.py
    └── sub-package
        └── __init__.py
```


The following files are included in this template:

1. **Makefile** to setup, configure and run linters on your project

2. Configuration files:
    - [config/catalog.yaml](config/config.yaml) to set your project data and metadata catalog. 
    - [config/parameters.yaml](config/parameters.yaml) to set your project parameters.
    - [config/credentials.yaml](config/credentials.yaml) to set your project credentials.
    - [config/template.env](config/template.env) to set your environment variables. 
    - [config/logging.yaml](config/logging.yaml) to set your logging configuration.
    - [pyproject.toml](pyproject.toml) to set your linting configuration 

3. Environment Configuration files:
    - [environment.yml](environment.yml) to set your conda environment.
    - [setup.py](setup.py) and [requirements.txt](requirements.txt) to install your project packages. 

4. Python files:
    - [config.py](src/config.py) to load your project configuration.
    - [logger.py](src/logger.py) to set up your logging configuration.
    - [utils.py](src/utils.py) project utility methods.
    - [decorators.py](src/decorators.py) project decorators.

-------