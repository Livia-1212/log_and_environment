# Getting Ready for Production

## Function of Calculator
> Based on Calc_Design_Pattern 
>> Implementation of command pattern and REPL \
>> Calculator (add, subtract, multiply, divide) \
>> plugin architecture for dynamic command loading \
>> Added functions: GitHub Action && .env File \
>> test coverage 

## Project Structure
.log_and_environment \
├── app \
|   ├── commands \
|   |   ├── commands \
|   |   |   └── calc_commands.py \
|   |   ├── command_handler.py \
|   |   └── plugins \
|   |       └── greet \
|   ├── app.py \
|   └── logging_config.py \
├── tests \
|   ├── conftest.py \
|   ├── test_app.py \
|   └── test_plugins.py \
├── main.py \
├── logging.conf \
├── pytest.ini \
├── requirements.txt \
├── .coveragerc \
└── .gitignore \
