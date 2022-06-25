###  UGA 2022
#__author__: Ming Song
#__function__: 

set(CMAKE_CXX_STANDARD 14)
cmake_minimum_required(VERSION 2.8)
project( ADXL362_measure )

# find_package( OpenCV REQUIRED )

# message( ${OpenCV_VERSION} )

include_directories(
  src
  include
  libs/spidev-lib
)

# add_library(spidev-lib libs/spidev-lib/spidev_lib.c)
add_library(spidev-lib++ libs/spidev-lib/spidev_lib++.cc)
# target_link_libraries(ADXL362_measure spidev-lib++)
# add_dependencies(ADXL362_measure spidev-lib++)
# target_link_libraries( spi-testc spidev-lib)


add_executable( ADXL362_measure
  src/ADXL362_measure_xyztemp.cpp
  include/ADXL362_test/ADXL362_measure_xyztemp.h
  libs/spidev-lib/spidev_lib++.h
  libs/spidev-lib/spidev_lib++.cc
)

#target_link_libraries(
#  visualize_consistency ${OpenCV_LIBS}
#)

# INSTALL(TARGETS  spidev-lib++
#   RUNTIME DESTINATION bin
#   LIBRARY DESTINATION lib
#   ARCHIVE DESTINATION lib
# )

# INSTALL( FILES src/spidev_lib++.h DESTINATION include)