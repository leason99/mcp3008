## MCP3008

- it is raspberrypi project use mcp3008 to read the Analogy signal through C Library
- After read data form mcp3008 ,it will conduct FFT to Analysis the signal
- the FFT result will be save as picture

## Start 
  > sudo python3 readMcp3008.py



##  Notice
- [py-libbcm2835](https://github.com/mubeta06/py-libbcm2835)
this is python interface to use the c library bcm2835   
(libbcm2835 need to install by yourself)
- you have to install matplotlib if you haven't install ever,because picture function base on it
    
    > pip install matplotlib

## Other information
  [Analyzing SPI driver performance on the Raspberry Pi](http://www.jumpnowtek.com/rpi/Analyzing-raspberry-pi-spi-performance.html)
  
