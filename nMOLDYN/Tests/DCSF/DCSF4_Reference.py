import os
import tempfile
from nMOLDYN.GlobalVariables import GVAR

title = 'Coherent Scattering Function'
trajectory = [os.path.join(GVAR['nmoldyn_trajs'], "TrajectoryTest1.nc")]
units_q = 1.0
weights = 'coherent'
frequency_points = 1000000
log_file = 'logfile.log'
units_frequency = 1.0
output_files = {'csf': os.path.join(tempfile.gettempdir(),'DCSF_Reference.nc')}
q_vector_set = ([4.0, 5.0, 6.0, 7.0, 8.0], 1.2, 500, None)
deuter = None
atoms = {'Protein.0': ['Oxygen', 'Nitrogen']}
ft_window = 50.0
time_info = (0, 9, 1)
