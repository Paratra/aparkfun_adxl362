// COPYRIGHT: Ming Song
// UGA Peter Kner Group 2022
// __function__: measure through ADXL362
// __author__:  MingSong
#include "ADXL362_test/ADXL362_measure_xyztemp.h"


void ADXL362_MEASURE_XYZTEMP::test(string test_msg){
    std::cout<< test_msg << '\n';
}

// ############################################################

int main() {

  ADXL362_MEASURE_XYZTEMP adxl362;
  testmsg = "Where is your father?";
  adxl362.test(testmsg);




  spi_config_t spi_config;
  uint8_t tx_buffer[32];
  uint8_t rx_buffer[32];

  SPI *mySPI = NULL;

  spi_config.mode=0;
  spi_config.speed=1000000;
  spi_config.delay=0;
  spi_config.bits_per_word=8;

  mySPI=new SPI("/dev/spidev0.0",&spi_config);

  // std::cout << typeid(mySPI).name() << std::endl; 

  if (mySPI->begin())
  {
    memset(tx_buffer,0,32);
    memset(rx_buffer,0,32);
    sprintf((char*)tx_buffer,"hello world");
    printf("sending %s, to spidev2.0 in full duplex \n ",(char*)tx_buffer); 
    mySPI->xfer(tx_buffer,strlen((char*)tx_buffer),rx_buffer,strlen((char*)tx_buffer));
    printf("rx_buffer=%s\n",(char *)rx_buffer);
    //mySPI->end();
    delete mySPI; 
  }
 return 0;

}