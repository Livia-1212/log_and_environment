# Calc_Design_Patterns

## Calculator includes function: add, subtract, multiply, divide

### Project Structure
cal_design_patterns - Multiprocess
##
>app/ 
>>    __init__.py         &nbsp; &nbsp; Package-level initialization code \
>>   calculator.py        &nbsp; &nbsp; Core calculator logic (Receiver) \
>>   command_handler.py   &nbsp; &nbsp; CommandHandler class to manage command registration and execution \
>>   commands.py          &nbsp; &nbsp; Command classes (Add, Subtract, Multiply, Divide) \
>>    multiprocess.py     &nbsp; &nbsp; Include invoker class and import multiprocess to manage commands independently \
>>    plugin_loader.py    &nbsp; &nbsp; Dynamically loads all command plugins from the specified plugins package.
##
>tests/ 
>>   __init__.py           &nbsp; &nbsp; Indicates that 'tests' is a  package (optional) \
>>    conftest.py          &nbsp; &nbsp; Test fixtures shared across multiple test files \
>>    test_calculator.py   &nbsp; &nbsp; Unit tests for Calculator class \
>>    test_commands.py     &nbsp; &nbsp; Unit tests for Command classes \
>>    test_multiprocess.py      &nbsp; &nbsp; Unit tests for the Invoker and REPL interface 
##
>plugins/
>>__init__.py              &nbsp; &nbsp; plugins package file    \  

>arithmetic/
>>__init__.py            &nbsp; &nbsp; plugins for add, subtract, multiply, divide \

>exponent/
>>__init__.py            &nbsp; &nbsp; plugins of exponent function \

>reset/
>>__init__.py             &nbsp; &nbsp; plugins reset current value to 0 

>square/
>>__init__.py             &nbsp; &nbsp; plugins square function      

##
> README.md                 &nbsp; &nbsp; Project documentation \
> main.py                 &nbsp; &nbsp; Entry point for the application 

##
### Project Details
Language: Python \
Design Pattern Used: Command Pattern \
Purpose: Demonstrate a modular, pattern-based design using a simple calculator.

# log_and_environment
