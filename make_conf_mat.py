import scipy.io as sio
import datetime as dt

from simul_conf import simul

def date2wrfname(start_time, minutes, domain = 1, ens = 0):
  """Construct file names from simulation start time, minutes of run
  and ensemble member (ens = 0 for no ensemble run)
  example name: wrfout_d01_2014-04-22_11:00:00.e009"""

  simul_time = start_time + dt.timedelta(minutes = minutes)
  wrf_name = "wrfout_d{0:02d}_{1:04d}-{2:02d}-{3:02d}_{4:02d}:00:00".format(domain,
      simul_time.year, simul_time.month, simul_time.day, simul_time.hour) 
  # wrf_name = "wrfout_d{}".format(domain) 
  return wrf_name



def make_conf_mat():
  """Read config files for ensemble assimilation run and create conf.mat
  file"""
  # see http://docs.scipy.org/doc/scipy/reference/tutorial/io.html
  sio.savemat('conf.mat', {'simul': simul})




if __name__ == '__main__':
  make_conf_mat() 
  start_time = dt.datetime(*simul['start_simul'])  # shortcut to convert start_simul array to function arguments
  print(start_time)
  print(date2wrfname(start_time, 60))
