# Run this script instead of 'make html' to build full source files in .rst

import os
import shutil

def clean():
    ''' Clean out current /build, source/modules.rst, and package*.rst(s) 

    '''
    if os.path.exists('./build'):
        shutil.rmtree('./build')

    if os.path.exists('./source/modules.rst'):
        os.system('rm ./source/modules.rst')

    if os.path.exists('./source/'+repopath+'.rst'):
        os.system('rm ./source/'+repopath+'*')

def main():
    clean()
    if os.path.exists('./source') == False:
        os.system('sphinx-quickstart')

    # sphinx-apidoc -o <output_path> <module_path>
    os.system('sphinx-apidoc -ef -o ./source ../'+repopath)
    os.system('make html')

if __name__ == '__main__':
    repopath = os.getcwd().split(os.sep)[-2]
    main()