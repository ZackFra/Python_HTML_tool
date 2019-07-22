from shutil import copy
import os

if __name__ == '__main__':
    files = ['index.html', 'styles.css', 'script.js']
    tools_dir = os.path.expanduser('~/tools/HTML_tools/')
    
    for template in files:
        file_exists = os.path.exists(template)
        if file_exists:
            overwrite = input('overwrite {}?'.format(template))
        if not file_exists or overwrite == 'y':
            copy(tools_dir + template, './')
        
