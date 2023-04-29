<p align="left" style="width: 20%; max-width: 240px; min-width: 80px;" >
  <img src="https://storage.googleapis.com/benevolent-machines/bm.svg" 
       title="BenevolentMachines.Org">
</p>

# datamachine 

## Welcome to the Machine!

datamachine is a powerful Python package that allows you to execute cloud Python notebooks with parameters and import cloud notebooks as modules. With datamachine, you can reference notebooks from various sources such as local files, Colab links, Github links, and HTTP links, and execute or import them with ease. You can also assign codes to files or links and store them in a library, which is a collection of codes and their corresponding links. Libraries are stored in JSON format with a dictionary of libraries to their links. An index is a collection of libraries that is also stored in a JSON file.

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

## Usage

Once you have installed datamachine, you can use it to execute and import notebooks.

### Executing a Notebook

To execute a notebook, use the `execute_notebook` function:

```python
import datamachine as dm

dm.execute_notebook(
    "execute.ipynb", 
    params={
        "EIN": "343434343"
    },
    html="output.html",
)
```

This command executes the notebook located at `"execute.ipynb"` with the parameter `"EIN"` set to `"343434343"`. The output is saved in an HTML file named `"output.html"`.

### Importing a Notebook as a Module

To import a notebook as a module, use the `import_notebook` function:

```python
import datamachine as dm

nbo = dm.import_notebook("./module.ipynb")
```

This command imports the notebook located at `"./module.ipynb"` as a module named `"nbo"`.

## Conclusion

datamachine is a powerful tool for anyone who works with cloud Python notebooks. With its flexible features and easy-to-use commands, datamachine makes it easy to execute and import notebooks from various sources, store collections of code and their corresponding links in a library, and organize your code with an index. So why wait? Install datamachine today and take your cloud notebook experience to the next level!
