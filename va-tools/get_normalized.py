# Windows
# ArcPy

# Parameters:
### number of brgys = num
### layer name = nso_muni
### field name = BrgyNo

__version__ = "0.1"

import arcpy
def getNorm(num):
    muni_list = arcpy.da.TableToNumPyArray ("nso_muni", "BrgyNo")
    max_num = muni_list["BrgyNo"].max()
    min_num = muni_list["BrgyNo"].min()
    return ((num - min_num) / (max_num - min_num))