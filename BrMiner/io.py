import pymzml
import pandas as pd
from collections import namedtuple
import math
import numpy as np

MS1Spec = namedtuple('MS1Spec', ['RT', 'MZ', 'INT'])
MS2Spec = namedtuple('MS2Spec', ['RT', 'Procursor', 'ProcuroseInt', 'Charge', 'MZ', 'INT'])

def load_mzml(filepath, **pymzml_kwargs):
    run = pymzml.run.Reader(filepath, **pymzml_kwargs)
    ms1 = []
    ms2 = []
    for spec in run:
        mslevel = spec.ms_level
        mz = spec.mz
        int_ = spec.i
        rt = spec.scan_time_in_minutes() * 60
        sortarg = mz.argsort()
        mz = mz[sortarg]
        int_ = int_[sortarg]
        
        if mslevel == 1:
            ms1.append(MS1Spec(rt, mz, int_))
        elif mslevel == 2:
            procursor, = spec.selected_precursors
            ms2.append(MS2Spec(rt, procursor['mz'], procursor['i'], procursor.get('charge', math.nan), mz, int_))
    ms1 = pd.DataFrame(ms1)
    ms2 = pd.DataFrame(ms2)
    ms1.sort_values('RT', inplace=True, ignore_index=True)
    ms2.sort_values('RT', inplace=True, ignore_index=True)

    ms2['MS1_IDX'] = ms1['RT'].searchsorted(ms2['RT']) - 1

    def find_int_in_ms1(ms2_s, ms1):
        ms1_s = ms1.loc[ms2_s.MS1_IDX, ['MZ', 'INT']]
        return ms1_s.INT[np.argmin(np.abs(ms2_s.Procursor - ms1_s.MZ))]

    ms2.insert(3, 'MS1Int', ms2.apply(find_int_in_ms1, axis=1, args=(ms1,)))

    ms1['Products_IDX'] = [ms2.index[ms2['MS1_IDX'] == idx].to_list() for idx in ms1.index]
    
    return ms1, ms2