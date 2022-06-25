#ifndef __ADXL362_MEASURE__
#define __ADXL362_MEASURE__

// #ifdef __APPLE__
//         #include <sys/uio.h>
// #else
//         #include <sys/io.h>
// #endif

#include <iostream>

// #include <algorithm>
#include <stdio.h>
#include <fstream>
#include <string>
#include <sstream>
#include <typeinfo>
#include <vector>


using namespace std;
// using namespace cv;

// global Parameters
vector<string> _img_list; // name of all images.
const char * _corr_file_path;
string _ikg_data_path;
string _local_data_path;
string testmsg;

struct file_info{

	string img_date;
	string img_camera_id;

	string scan_row;
	string scan_col;
	string image_row;
	string image_col;

};





class ADXL362_MEASURE_XYZTEMP
{
public: //Accessable for all entities.

//Parameters

    // char TESTMSG = 'H';

//Functions
	void test(string test_msg);



private: //Only accessable for this class members.

	// Parameters
	vector<const char*>_content;
	vector<file_info>_corr_info;

	stringstream file_name;
	stringstream temp_name;

	// char TESTMSG = 'H';



	// Mat _current_img;

	file_info _file_info;
	string str;



	// functions

	// void find_img_and_copy(string img_date, string img_camera_id);
    // void sear_coordinates(vector<file_info>corr_info);
	// void TEST;


};

#endif // endif __VISUALIZE_CONSISTENCY__