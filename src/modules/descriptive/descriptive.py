from logs import logDecorator as lD 
import jsonref, pprint
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

config = jsonref.load(open('../config/config.json'))
logBase = config['logging']['logBase'] + '.modules.descriptive.descriptive'
module_config = jsonref.load(open('../config/modules/descriptive.json'))



@lD.log(logBase + '.describe')
def describe(logger):
    '''print a line
    
    This function simply prints a single line
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    '''
    
    print('We are in module: describe')

    datapath = module_config['inputs']['dataset']
    data = pd.read_csv(datapath)
    describe_table = data.describe()
    

    return

@lD.log(logBase + '.corr')
def corr(logger):
    '''print a line
    
    This function simply prints a single line
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    '''
    
    print('We are in module: corr')

    datapath = module_config['inputs']['dataset']
    data = pd.read_csv(datapath, index_col = False)
    corr = data.corr()
    ax = sns.heatmap(corr, 
    xticklabels=corr.columns, yticklabels=corr.columns, 
    annot=True, vmax=1, vmin=-1, center=0, cmap='vlag')
    outFigure = plt.savefig('corrplot.png', bbox_inches='tight', pad_inches=0.0);

    return

@lD.log(logBase + '.main')
def main(logger, resultsDict):
    '''main function for module1
    
    This function finishes all the tasks for the
    main function. This is a way in which a 
    particular module is going to be executed. 
    
    Parameters
    ----------
    logger : {logging.Logger}
        The logger used for logging error information
    resultsDict: {dict}
        A dintionary containing information about the 
        command line arguments. These can be used for
        overwriting command line arguments as needed.
    '''

    print('='*30)
    print('Main function of descriptive')
    print('Main function of corr')
    print('='*30)

    datapath = module_config['inputs']['dataset']
    describe()
    corr()

    print('Getting out of descriptive module')
    print('Getting out of corr module')
    print('-'*30)

    return

