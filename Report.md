# Sensor Miniproject Report
#### By: Celia Wilkins and Grayson Wiggins

#### Task 0 Results:
After setting up the repository and python websockets, our team ran the client and server files. The greeting code was:
>ECE Senior Capstone IoT simulator

#### Task 1 Results/Commentary:

#### Task 2 Results/Commentary:

#### Task 3 Results/Commentary:
For this task, our team created a new python file called __Report.py__ - this file contains code that detects temperature anamolies and records them in a .csv file called __anamolies_log.csv__. Anamolies are defined as data that deviates from what is expected. When taking a look at the temperature recordings over time, there appear to be several extreme data points. The __Report.py__ file outputs a line plot of the temperature; when looking at this plot, there are readings over 2000 degrees celcius. Since these readings cannot physically occur, our team dropped these outliers from the data. More specifically, temperatures between -31.5°C (-25°F) and 65.5°C (150°F) were dropped.

Next, our team reexamined the modified temperature plot to check for more anomalies. The __Report.py__ file outputs a modified temperature plot as well as a modified temperature PDF plot. Assessing the modified temperature plot, there still appear to be large fluctuations in temperature. For example, class1 has temperatures that range from 0°C and 50°C. These large spikes are possible to occur, but not likely since most data points are between 25°C and 30°C. Thus, applying adding an unbiased filter will be useful. The modified temperature PDF plot indicates the temperature distributions in all three rooms are gaussian-shaped. See below:
![PDF Plot](https://github.com/graysonw15/2020-sensor-miniproject/tree/main/output_plots)
