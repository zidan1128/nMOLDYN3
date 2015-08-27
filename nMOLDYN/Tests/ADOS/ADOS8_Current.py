# ADOS test 8

import os
import tempfile

from nMOLDYN.GlobalVariables import GVAR

from nMOLDYN.Analysis.Templates import AngularDensityOfStates_serial

parameters = {}

parameters['version'] = "3.0.9"
parameters['estimate'] = "no"

parameters['projection'] = None
parameters['output'] = os.path.join(tempfile.gettempdir(),"ADOS_Current.nc")
parameters['pyroserver'] = 'monoprocessor'
parameters['normalize'] = 'no'
parameters['frequencyunits'] = 'THz'
parameters['stepwiserbt'] = 'no'

parameters['trajectory'] = os.path.join(GVAR['nmoldyn_trajs'], 'TrajectoryTest1.nc')
parameters['timeinfo'] = "2:40:2"
parameters['group'] = 'object objectname P892 restype Leu,Met groupinglevel residue'
parameters['referenceframe'] = 2
parameters['differentiation'] = 4
parameters['resolution'] = 40.78871761

analysis = AngularDensityOfStates_serial(parameters)
analysis.runAnalysis()

