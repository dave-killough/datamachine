<p align="left" >
  <img src="https://storage.googleapis.com/benevolentmachines/datamachine.svg" 
       title="datamachine">
</p>

## Modular Notebooks

Imagine an easy way to reuse Python notebooks in the cloud. datamachine is a useful Python package that enables you to import notebooks as modules. With datamachine, you can load notebooks from various sources such as local files, Colab links, and Github links, and then import them with ease. You can also organize notebooks into libraries that use simple codes for easy access to commonly used notebooks. 
<p align="left" >
  <img src="https://storage.googleapis.com/benevolentmachines/dm_overview.png">
</p>

## Features

- **Import notebooks as modules**: Importing notebooks as modules is a breeze with datamachine. You can import notebooks from various sources such as local files, Colab links, Github links, and HTTP links.

- **Libraries**: datamachine supports user-defined libraries that will make your reusable notebook modules much easier to publish and use by others.   

- **Notebook sources**: You can currently source public notebooks from GitHub, Colab, and notebooks in your local file system.  I plan on adding secure notebook access and extending storage options to S3, Azure, GCP, and other cloud-based systems.  Please add an issue to GitHub if you're intersted in support for a particular source.  

## Installation

To install datamachine, run the following command:

``` python
pip install datamachine
```

## Importing datamachine

Once you've installed datamachine, you can import it. The convention is to name the module instance `dm`.  

```python
import datamachine as dm
```

### Notebook Locations

datamachine currrently supports notebook links from Github, Google Colab, local file paths, and public `https` links with raw content.  
### Importing a Notebook as a Module

To import a notebook as a module, use the `import_notebook` function:

```python
nbo = dm.import_notebook(
    "https://colab.research.google.com/drive/1y7x3BDkmaz6k93QjENanKHudLV8xB96Q?usp=sharing",
)
```

This function imports the notebook located at the specified location and returns a module reference like the native import command.  The Colab notebook used above provides sample analytics that can be accessed by using methods in the module.  For instance, you could run the following function

```python
nbo.monthly_rulings()
```
<p align="left" >
  <img src="https://storage.googleapis.com/benevolentmachines/dm_module2.gif">
</p>

## Conclusion

datamachine is a powerful tool for anyone who wants to reuse Python notebooks. With its flexible features and easy-to-use commands, datamachine makes it easy to import notebooks from various sources, store collections of code and their corresponding links in a library, and organize your code with an index. So why wait? Install datamachine today and take your notebook experience to the next level!
