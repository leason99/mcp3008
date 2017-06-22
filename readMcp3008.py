import pandas as pd
import numpy as np
import matplotlib
# solve the bug for myself 
# It maybe not necessary 
matplotlib.use("Pdf")
import matplotlib.pyplot as plt
import time
import os
import sys
import readline
import glob
from BCMMCP3008 import MCP3008


times=10000
SPI_PORT= 0
SPI_DEVICE = 0
chnum=1  #ch1

mcp = MCP3008()
result=mcp.read_adc_loop(chnum,times) #read data from mcp3008
data=np.array(result["data"]) #translate to nparray
rate=result["samplerate"]

#pic set
fig, (ax0, ax1) = plt.subplots(nrows=2 ,figsize=(12,8 ))
ax0.plot(range(len(data)), data*5/1024)
ax0.set_ylabel('voltage(V)')
ax0.set_xlabel('tissme(n)')
n=data.shape[0]

#fft
p = np.abs(np.fft.fft(data))/n
f = np.linspace(0, rate/2, len(p))
freqs = np.fft.fftfreq(data.size, 1/rate)

#set the fft result to pic
idx = np.argsort(freqs)
idx2=idx[int(idx.shape[0]/2):int(idx.shape[0]/2)+20]
ax1.set_xlabel("Frequence(Hz)")
ax1.set_ylabel("Amplitude")
ax1.set_title('Samplerate: {}   N: {}  '.format(rate,n), fontsize=16)
ax1.bar(freqs[idx2], p[idx2])
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

#save the pic
filename=time.strftime("%Y%m%d_%H%M%S",time.localtime())
dirPath=os.path.dirname(os.path.abspath(sys.argv[0]))
filePath=os.path.join(dirPath,filename+".jpg")
plt.savefig(filePath)
print("file: {}".format(filePath))
