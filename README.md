# Coverage Utilities

Created by: Nare Karapetyan
Maintained by: Nare Karapetyan
contact: nare@email.sc.edu

Created on July 16 2018

---
## Intruduction

Python scripts for generating waypoints and coordinate conversions used for coverage experiments.
NOTE: this is a temporary access to the some functionality of this utility.

### Structure
The structure of this pakage is as follows:
- convert_coordinates.py
- generate_waypoints.py
- test_generate_waypoints.py
- input/ 
- outputs/
- trials/ 
- README.md

- all_code_and_more/ (utilities in this folder have not been tested in very long time and here are just for authors reference)
---
## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
- OpenCV (3.x recommended)

- python (3 recommended)

- pandas

### How to Use

In order to work with this script one need to create a config file. 
Sample config file can be found in "input/2021_simple_patterns_exp/murray_sensor_location.wf"

Sample execution and mission file creation can be found in test_generate_waypoints.py.
Simply create your own experiment function similar to `generate_Feb_21_2021_simple_patterns() ` and execute it.

### License
