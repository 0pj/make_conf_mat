# configuration file for assimilation runs

simul = {
    'start_simul': [2014, 4, 21, 18],
    'flags': {
      'get_grib' : 0,
      'preproc'  : 0,
      'filter_obs' : 1,
      'prepare_omb' : 1,
      'run_analysis' : 1
      },
    'asim_info': {
      'n_ens' : 9,
      'assim_method' : 'etkf'
      },
    # assimilation time, assimilation flag, observation time
    'assim_times' : [  
      { 'time': 360,  'assim': 1, 'obs_time' : 360},
      { 'time': 540,  'assim': 1, 'obs_time' : 360},
      { 'time': 600,  'assim': 1, 'obs_time' : 720},
      { 'time': 660,  'assim': 1, 'obs_time' : 720},
      { 'time': 720,  'assim': 1, 'obs_time' : 720},
      { 'time': 780,  'assim': 1, 'obs_time' : 720},
      { 'time': 1400, 'assim': 0, 'obs_time' : 1440}
      ]
    }






