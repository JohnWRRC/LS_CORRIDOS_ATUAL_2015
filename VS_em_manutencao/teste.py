import grass.script as grass
import numpy as np
import random
#from __future__ import print_function
from grass.script import array as garray


expression7="aleat2=(aleat/100.0)*2.0"
grass.mapcalc(expression7, overwrite = True, quiet = True)
















#inputFile=r"E:\__data_2016\__Brenda\LS_corridors_test_bba\temp/map_cen4_cost_tif___asc.asc"
#expression7="randon=0.1"
#grass.mapcalc(expression7, overwrite = True, quiet = True)

#expression7="randon2=rand(0,1)"
#expression7="randon=Clip_map_cen4_cost_tif_res7[1,50]"#.format(random.uniform(0, 1))
grass.mapcalc(expression7, overwrite = True, quiet = True)


#f = open (inputFile , 'r')
#tab_fid00 =[]
#for i in f:
    #tab_fid00.append(i)
##tab_fid00 = [ line.split(' ') for line in f ]
##del tab_fid00[0:6]#removenedo cabecalho
##tab_fid00_arry=np.array(f) #convertendo pra array

##Nrows,Ncols=tab_fid00_arry.shape

##for i in xrange(Nrows):
    ##for j in xrange(Ncols):
        ##tab_fid00_arry[i][j]=random.uniform(0, 1)
        
        
