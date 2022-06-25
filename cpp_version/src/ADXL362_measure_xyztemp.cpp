// COPYRIGHT: Ming Song
// UGA Peter Kner Group 2022
// __function__: measure through ADXL362
// __author__:  MingSong
#include "ADXL362_test/ADXL362_measure_xyztemp.h"

// ############################################################

// bool is_file_exist(string fileName)
// {
//     std::ifstream infile(fileName);
//     return infile.good();
// }

// // ############################################################

// stringstream VISUALIZE_CONSISTENCY::get_filename_from_date_cameranNum(string img_date, string img_camera_id){

//   stringstream file_name;
//   file_name << "170331_" << img_date << "_Camera_" << img_camera_id << ".png";
//   return file_name;
// }


void ADXL362_MEASURE_XYZTEMP::test(string test_msg){
    std::cout<< test_msg << '\n';
}

// ############################################################

int main() {
//   _corr_file_path = "../data/170331_092835_Scanner_2.corr";
//   _ikg_data_path = "/Volumes/mingdisk/ImagesMaster/20170331_icsens/";
//   _local_data_path = "../data/20170331_icsens/";


//   VISUALIZE_CONSISTENCY visualize_consistency;
//   visualize_consistency.read_corr(_corr_file_path);

    ADXL362_MEASURE_XYZTEMP adxl362;
    testmsg = "Where is your father?";
    adxl362.test(testmsg);

  return 0;

}