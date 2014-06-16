make_conf_mat
=============

Creating Matlab conf.mat files containing configuration variables for WRF assimilation runs.

Simple script for passing information between Python, Bash and Matlab components of WRF assimilation.

simul_conf.py -- configuration file containing description WRF assimilation run, this should be modified
                 for different assimilation experiments.
make_conf_mat.py -- contains various helper functions and scripts for creation of configuration files. 
                    It currently contains just a simple script for creation of conf.mat config file (which should
                    be read by any Matlab component of data assimilation).

