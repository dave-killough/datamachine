# datamachine
#! migrate .net to .org, start with bundle  

from datetime import datetime
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor
from urllib.request import urlopen
import glob
import importlib 
import json
import nbformat
import os
import random
import shutil
import sys 

GOOGLE_EXPORT = 'https://docs.google.com/uc?export=download&id='
MACHINE_INDEX = 'https://colab.research.google.com/drive/1L3l50wwh6M9cK02cFn0dJ0DUVLHEGCcc'

def trace(line):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S  ')
    with open('request.txt', 'a') as f:
        f.write(ts + line + '\n')  

def get_request(): 
    req = None
    if os.path.exists('request.json'):
        with open('request.json') as f:
            request = f.read()
            req = json.loads(request)
    return req

PREAMBLE=\
"""
##############################################################################
# This source has been auto generated from an IPython/Jupyter notebook file. #
# Please modify the origin file                                              #
##############################################################################
"""

def code_from_ipynb(nb):
    code = PREAMBLE
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            # transform the input to executable Python
            src = cell['source']
            if src[0].startswith('#run'): 
                code += '\n# ' + '# '.join(cell['source'])
            elif src[0].startswith('#test'):
                code += '\n# ' + '# '.join(cell['source'])
            else: 
                code += ''.join(cell['source'])
        if cell['cell_type'] == 'markdown':
            code += '\n# ' + '# '.join(cell['source'])
        # We want a blank newline after each cell's output.
        # And the last line of source doesn't have a newline usually.
        code += '\n\n'
    return code

def import_notebook(link, attr = None):
    folder = 'datamachine_temp'
    if not os.path.exists(folder):
        os.makedirs(folder)
    if '//colab.' in link:
        file_id = link.split('/')[-1] # get ID 
        url = GOOGLE_EXPORT + file_id
    elif '//raw.github' in link:
        url = link
    else: # search the index 
        index = import_notebook(MACHINE_INDEX) 
        if link not in index.IMPORTS:
            print(link,' is not in the machine index')
            return
        i = index.IMPORTS[link]['link'] 
        ret = import_notebook(i)
        return ret
    rint = random.randint(10_000_000, 99_999_999) 
    name = folder + os.path.sep + 'import' + str(rint)
    filename = name + '.ipynb'
    with urlopen(url) as r:
        with open(filename, 'wb') as out_file:
            shutil.copyfileobj(r, out_file) 
    with open(filename) as f:
        nb = json.load(f)
        with open(name + '.py','w') as text_file:
            text_file.write(code_from_ipynb(nb))
    module = importlib.import_module(name.replace(os.path.sep,'.'))
    loaded = [key for key in sys.modules.keys() 
                if key.startswith('datamachine_temp.import')]
    delete = [f for f in glob.glob("datamachine_temp/import*") 
                if f.split('.')[0].replace(os.path.sep,'.') not in loaded]
    #print(loaded, delete) 
    for f in delete:
        os.remove(f)    
    if attr == None:
        return module
    else:
        return getattr(module, attr)

def run(request=None):
    output = request['output']
    runner = request['runner']
    with open('request.json', 'w') as f:
        json.dump(request, f, indent=4)

    file_id = runner.split('/')[-1] # get ID
    url = GOOGLE_EXPORT + file_id
    file = 'runner.ipynb'
    
    src = ''
    with urlopen(url) as r:
        src = r.read().decode()

    src = src.replace("'colab'","'notebook'")
    nb = nbformat.reads(src, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb)
    with open(file, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    # the following nonsense is to work around issue with ipynb.. ugh 
    with open(file) as f:
        newText=f.read().replace('"python3"','"python3", "language": "python"')
    with open(file, "w") as f:
        f.write(newText)    
    
    html_exporter = HTMLExporter()
    html_exporter.exclude_input = True
    html_data, resources = html_exporter.from_notebook_node(nb)
    html_data = html_data.replace('</head>',"""
        <style>
            .container { width: 100% } 
            .prompt { min-width: 0 } 
            div.output_subarea { max-width: 100% }
            body { margin: 0; padding: 0; }
            div#notebook { padding-top: 0; }
        </style>
        </head>
    """)
    html_data = html_data.replace('''
<div class="cell border-box-sizing code_cell rendered">

</div>''','')
    with open(output, "w") as f:
        f.write(html_data)  
    trace('run completed')        