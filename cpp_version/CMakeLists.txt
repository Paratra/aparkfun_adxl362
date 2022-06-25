###  UGA 2022
#__author__: Ming Song
#__function__: 

set(CMAKE_CXX_STANDARD 14)
cmake_minimum_required(VERSION 2.8)
project( ADXL362_measure )

# find_package( OpenCV REQUIRED )

# message( ${OpenCV_VERSION} )

include_directories(
  include
)

add_executable( ADXL362_measure
  src/ADXL362_measure_xyztemp.cpp
  include/ADXL362_test/ADXL362_measure_xyztemp.h
)

#target_link_libraries(
#  visualize_consistency ${OpenCV_LIBS}
#)