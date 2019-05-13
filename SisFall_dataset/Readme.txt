
---- SisFall: A Fall and Movement Dataset ----

Created by:
A. Sucerquia, J.D. López, J.F. Vargas-Bonilla
SISTEMIC, Faculty of Engineering, Universidad de Antiquia UDEA
josedavid@udea.edu.co

February 2016 - Version 1.0

---------------------------------------------------------------------------


This database consists of 4,510 files, each file with a single activity.


File name format:
<ADL OR FALL_CODE>_<SUBJECT_ID>_<TRIAL_NO>.txt

Activities of Daily Living (ADL):
 
+------+------------------------------------------------------------------------------------------+--------+----------+
| Code | Activity                                                                                 | Trials | Duration |
+------+------------------------------------------------------------------------------------------+--------+----------+
| D01  | Walking slowly                                                                           | 1      | 100s     |
| D02  | Walking quickly                                                                          | 1      | 100s     |
| D03  | Jogging slowly                                                                           | 1      | 100s     |
| D04  | Jogging quickly                                                                          | 1      | 100s     |
| D05  | Walking upstairs and downstairs slowly                                                   | 5      | 25s      |
| D06  | Walking upstairs and downstairs quickly                                                  | 5      | 25s      |
| D07  | Slowly sit in a half height chair, wait a moment, and up slowly                          | 5      | 12s      |
| D08  | Quickly sit in a half height chair, wait a moment, and up quickly                        | 5      | 12s      |
| D09  | Slowly sit in a low height chair, wait a moment, and up slowly                           | 5      | 12s      |
| D10  | Quickly sit in a low height chair, wait a moment, and up quickly                         | 5      | 12s      |
| D11  | Sitting a moment, trying to get up, and collapse into a chair                            | 5      | 12s      |
| D12  | Sitting a moment, lying slowly, wait a moment, and sit again                             | 5      | 12s      |
| D13  | Sitting a moment, lying quickly, wait a moment, and sit again                            | 5      | 12s      |
| D14  | Being on one’s back change to lateral position, wait a moment, and change to one’s back  | 5      | 12s      |
| D15  | Standing, slowly bending at knees, and getting up                                        | 5      | 12s      |
| D16  | Standing, slowly bending without bending knees, and getting up                           | 5      | 12s      |
| D17  | Standing, get into a car, remain seated and get out of the car                           | 5      | 25s      |
| D18  | Stumble while walking                                                                    | 5      | 12s      |
| D19  | Gently jump without falling (trying to reach a high object)                              | 5      | 12s      |
+------+------------------------------------------------------------------------------------------+--------+----------+

Falls:

+------+------------------------------------------------------------------------------------------+--------+----------+
| Code | Activity                                                                                 | Trials | Duration |
+------+------------------------------------------------------------------------------------------+--------+----------+
| F01  | Fall forward while walking caused by a slip                                              | 5      | 15s      |
| F02  | Fall backward while walking caused by a slip                                             | 5      | 15s      |
| F03  | Lateral fall while walking caused by a slip                                              | 5      | 15s      |
| F04  | Fall forward while walking caused by a trip                                              | 5      | 15s      |
| F05  | Fall forward while jogging caused by a trip                                              | 5      | 15s      |
| F06  | Vertical fall while walking caused by fainting                                           | 5      | 15s      |
| F07  | Fall while walking, with use of hands in a table to dampen fall, caused by fainting      | 5      | 15s      |
| F08  | Fall forward when trying to get up                                                       | 5      | 15s      |
| F09  | Lateral fall when trying to get up                                                       | 5      | 15s      |
| F10  | Fall forward when trying to sit down                                                     | 5      | 15s      |
| F11  | Fall backward when trying to sit down                                                    | 5      | 15s      |
| F12  | Lateral fall when trying to sit down                                                     | 5      | 15s      |
| F13  | Fall forward while sitting, caused by fainting or falling asleep                         | 5      | 15s      |
| F14  | Fall backward while sitting, caused by fainting or falling asleep                        | 5      | 15s      |
| F15  | Lateral fall while sitting, caused by fainting or falling asleep                         | 5      | 15s      |
+------+------------------------------------------------------------------------------------------+--------+----------+

Subjects:

The SUBJECT_ID depends of the age of the subjects. 

SA: Adults subjects between 19 and 30 years old
SE: Elderly people between 60 and 75 years old

Elderly people only simulated ADLs except SE06, who is an expert in Judo that also simulated falls. Elderly people did not 
perform activities D06, D13, D18, and D19 due to recommendations of a physician specialized in sports. Additionally, some 
elderly people did not perform some activities due to personal impairments (or medical recommendation).

+---------+-----+--------+--------+--------+
| Subject | Age | Height | Weight | Gender |
+---------+-----+--------+--------+--------+
| SA01    | 26  | 165    | 53     | F      |
| SA02    | 23  | 176    | 58.5   | M      |
| SA03    | 19  | 156    | 48     | F      |
| SA04    | 23  | 170    | 72     | M      |
| SA05    | 22  | 172    | 69.5   | M      |
| SA06    | 21  | 169    | 58     | M      |
| SA07    | 21  | 156    | 63     | F      |
| SA08    | 21  | 149    | 41.5   | F      |
| SA09    | 24  | 165    | 64     | M      |
| SA10    | 21  | 177    | 67     | M      |
| SA11    | 19  | 170    | 80.5   | M      |
| SA12    | 25  | 153    | 47     | F      |
| SA13    | 22  | 157    | 55     | F      |
| SA14    | 27  | 160    | 46     | F      |
| SA15    | 25  | 160    | 52     | F      |
| SA16    | 20  | 169    | 61     | F      |
| SA17    | 23  | 182    | 75     | M      |
| SA18    | 23  | 181    | 73     | M      |
| SA19    | 30  | 170    | 76     | M      |
| SA20    | 30  | 150    | 42     | F      |
| SA21    | 30  | 183    | 68     | M      |
| SA22    | 19  | 158    | 50.5   | F      |
| SA23    | 24  | 156    | 48     | F      |
| SE01    | 71  | 171    | 102    | M      |
| SE02    | 75  | 150    | 57     | F      |
| SE03    | 62  | 150    | 51     | F      |
| SE04    | 63  | 160    | 59     | F      |
| SE05    | 63  | 165    | 72     | M      |
| SE06    | 60  | 163    | 79     | M      |
| SE07    | 65  | 168    | 76     | M      |
| SE08    | 68  | 163    | 72     | F      |
| SE09    | 66  | 167    | 65     | M      |
| SE10    | 64  | 156    | 66     | F      |
| SE11    | 66  | 169    | 63     | F      |
| SE12    | 69  | 164    | 56.5   | M      |
| SE13    | 65  | 171    | 72.5   | M      |
| SE14    | 67  | 163    | 58     | M      |
| SE15    | 64  | 150    | 50     | F      |
+---------+-----+--------+--------+--------+
* Height in cm and Weight in kg.

Examples:

F05_SA01_R04.txt
F05: Fall. Description: Fall forward while jogging caused by a trip
SA01: Adult subject 01.
R04: Trial 04


D17_SE04_R02.txt
D17: ADL. Description: Standing, get into a car, remain seated and get out of the car
SE04: Elderly person 04
R02: Trial 02


Sensors:

Data were acquired with three sensors (2 accelerometers and 1 gyroscope) at a frequency sample of 200 Hz.

Each file contains nine columns and a different number of rows depending on the test length.

1st column is the acceleration data in the X axis measured by the sensor ADXL345.
2nd column is the acceleration data in the Y axis measured by the sensor ADXL345.
3rd column is the acceleration data in the Z axis measured by the sensor ADXL345.

4th column is the rotation data in the X axis measured by the sensor ITG3200.
5th column is the rotation data in the Y axis measured by the sensor ITG3200.
6th column is the rotation data in the Z axis measured by the sensor ITG3200.

7th column is the acceleration data in the X axis measured by the sensor MMA8451Q.
8th column is the acceleration data in the Y axis measured by the sensor MMA8451Q.
9th column is the acceleration data in the Z axis measured by the sensor MMA8451Q.

Data are in bits with the following characteristics:

ADXL345:
Resolution: 13 bits
Range: +-16g

ITG3200
Resolution: 16 bits
Range: +-2000°/s

MMA8451Q:
Resolution: 14 bits
Range: +-8g


In order to convert the acceleration data (AD) given in bits into gravity, use this equation: 

Acceleration [g]: [(2*Range)/(2^Resolution)]*AD

In order to convert the rotation data (RD) given in bits into angular velocity, use this equation:

Angular velocity [°/s]: [(2*Range)/(2^Resolution)]*RD

