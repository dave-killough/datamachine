<p align="left" >
  <img src="https://storage.googleapis.com/benevolentmachines/datamachine2.svg" 
       title="BenevolentMachines.Org">
</p>

## Welcome to the Machine!

datamachine is a powerful Python package that allows you to execute cloud Python notebooks with parameters and import cloud notebooks as modules. With datamachine, you can reference notebooks from various sources such as local files, Colab links, Github links, and HTTP links, and execute or import them with ease. You can also assign codes to files or links and store them in a library, which is a collection of codes and their corresponding links. Libraries are stored in JSON format with a dictionary of notebooks to their links. 

## Features

- Execute cloud notebooks with parameters: With datamachine, you can execute cloud notebooks with parameters, which is particularly useful when you want to run a notebook multiple times with different inputs.

- Import cloud notebooks as modules: Importing cloud notebooks as modules is a breeze with datamachine. You can import notebooks from various sources such as local files, Colab links, Github links, and HTTP links.

- Library and Index: datamachine supports library and index features, making it easier to organize your code. You can store collections of code and their corresponding links in a library and index them for easy access.

- JSON support: All libraries and indexes are stored in JSON format, making it easy to read, write, and share with others.

## Installation

To install datamachine, run the following command:

``` python
%pip install datamachine
```

## Importing datamachine

Once you've installed datamachine, you can import it.  
The convention is to name the module instance `dm`.  

```python
import datamachine as dm
```
### Importing a Notebook as a Module

To import a notebook as a module, use the `import_notebook` function:

```python
nbo = dm.import_notebook(
    "https://colab.research.google.com/drive/1y7x3BDkmaz6k93QjENanKHudLV8xB96Q?usp=sharing",
)
```

This command imports the notebook located at `"./module.ipynb"` as a module named `"nbo"`.
### Executing a Notebook

To execute a notebook with parameters, use the `execute_notebook` function:

```python
import datamachine as dm
dm.execute_notebook(
    "execute.ipynb", html="output.html",
    params={"EIN": "200549531","TYPE": "summary"},
)
```

This function executes the notebook located at `"execute.ipynb"` with the parameter `"EIN"` 
set to `"200549531"`. The output is saved in an HTML file named `"output.html"`.

In order to receive the EIN parameter in the executed notebook, simply invoke 
the `execute_params` function with a passed dictionary containing the parameter.
This function provides the test values when you're directly running the notebook, 
and uses the passed values when invoked via `execute_notebook`.    
```python
import datamachine as dm
params = dm.execute_params({"EIN": "454547709","TYPE": "detail"})
EIN = params["EIN"]
```



## Conclusion

datamachine is a powerful tool for anyone who works with cloud Python notebooks. With its flexible features and easy-to-use commands, datamachine makes it easy to execute and import notebooks from various sources, store collections of code and their corresponding links in a library, and organize your code with an index. So why wait? Install datamachine today and take your cloud notebook experience to the next level!
