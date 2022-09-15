# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:45:50 2022

@author: giova
"""

import configparser
config = configparser.ConfigParser()



config['polyfit_global config'] = {'filepath': 'filename.csv',
                     'header1': 'header1',
                     'header2': 'header2',
                     'header3': 'header3',
                     'degree': '4'}
config['plots_that config'] = {'plot' :'True',
                               'whichplot': 'lin',
                               'labelx': 'xlabel',
                               'labely': 'ylabel',
                               'legend': 'True',
                               'legend_data': 'experimental values',
                               'legend_fit': 'fitting curve',
                               'title': 'title',
                               'grid': 'yes',
                               'uncertainties_cap': 'yes',
                               'legend_position': 'upper right'
                                    }
with open('polyfit_config.ini', 'w') as configfile:
  config.write(configfile)
  
