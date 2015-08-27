import os
import tempfile
from nMOLDYN.GlobalVariables import GVAR

title = 'Angular Velocity Autocorrelation Function'
trajectory = [os.path.join(GVAR['nmoldyn_trajs'], "TrajectoryTest1.nc")]
ft_window = 40.0
time_steps = None
frequency_points = 1000000
log_file = 'logfile.log'
units_frequency = 1.0
projection_vector = None
output_files = {'savacf': os.path.join(tempfile.gettempdir(),'test.plot')}
differentiation = 'order 3'
reference = [{'Protein.0 SideChain': {'aspartic_acid': None}}]
groups = [{'Protein.0 SideChain': ['aspartic_acid']}]
time_info = (1, 20, 2)
