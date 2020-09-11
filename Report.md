# Sensor Miniproject Report
#### By: Celia Wilkins and Grayson Wiggins

#### Task 0 Results:
After setting up the repository and python websockets, our team ran the client and server files. The greeting code was:
>ECE Senior Capstone IoT simulator

#### Task 1 Results/Commentary:

#### Task 2 Results/Commentary:

#### Task 3 Results/Commentary:
For this task, our team created a new python file called __Report.py__ - this file contains code that detects temperature anamolies and records them in a .csv file called __anamolies_log.csv__. Anamolies are defined as data that deviates from what is expected. When taking a look at the temperature recordings over time, there appear to be several extreme data points. The __Report.py__ file outputs a line plot of the temperature; when looking at this ![plot](https://github.com/graysonw15/2020-sensor-miniproject/tree/main/output_plots/Raw_TPlot.png), there are readings over 2000 degrees celcius. Since these readings cannot physically occur, our team dropped these outliers from the data. More specifically, temperatures between -31.5°C (-25°F) and 65.5°C (150°F) were dropped.

Next, our team reexamined the modified temperature plot to check for more anomalies. The __Report.py__ file outputs a modified temperature plot as well as a modified temperature PDF plot. Assessing the modified temperature ![plot](https://github.com/graysonw15/2020-sensor-miniproject/tree/main/output_plots/Modified_TPlot.png), there still appear to be large fluctuations in temperature. For example, class1 has temperatures that range from 0°C and 50°C. These large spikes are possible to occur, but not likely since most data points are between 25°C and 30°C. Thus, applying adding an unbiased filter will be useful. The modified temperature ![PDF Plot](https://github.com/graysonw15/2020-sensor-miniproject/tree/main/output_plots/Modified_PDF.png) indicates the temperature distributions in all three rooms are gaussian-shaped. By dropping data that is further than 2 standard deviations from the mean, we effectively detect more of these anomalies. 

Finally, the gaussian-filtered temperature ![plot](https://github.com/graysonw15/2020-sensor-miniproject/tree/main/output_plots/Gauss_Filter_TPlot.png) is assessed for accurate temperature fluctuations. Here, you can see that class1 has the highest room temperature at around 27°C, followed by the office with 23°C and the lab with 20°C. There are still some fluctuations, but they are more persistant than the outliers seen before. Our team believes that the persistent fluctuations from this plot are actual changes in room temperatures, not failed sensor readings. For instance, at the 22:05 time stamp, the class1 has an increase in temperature from 26°C to 29°C. This increase makes sense because factors like air conditioning or even occupancy can have these sized effects. With all the anomalies filtered, our team was able to predict accurate bounds on room temperature. The bounds are recorded as ![print](https://github.com/graysonw15/2020-sensor-miniproject/blob/main/output_plots/Command_Output.png) statements in the __design.py__ code. 

#### Conclusions

This simulation was a great exercise for our team to practice Github, websockets, and Python data-analytic modules. Using Github is reflective of a real-world application because companies often have multiple coworkers editing the same code. Learning to work around merge conflicts is a great skill and will be useful for the Senior Design project. Sensor anomalies also reflect real-world problems because hardware does not function the way we expect it to. Working on this simulation gave our team intuition for identifying outliers that negatively impact our data. For example, dropping a few temperature data points that were not physically possible decreased our variance from 70,000°C to 9°C. One aspect of these simulation that is not reflective of real applications is the magnitude of some of these anomalies. Looking at the most common IoT temperature sensors, their range is generally -50°C to 150°C. Some of our data points recorded in the anomalies_log.csv file had values like 6000°C. It seems unlikely that a normal IoT sensor would output such a large value. Another factor that this simulation fails to account for is:

Since both of us are fairly new to socket programming, we thought that the Python websocket library was nice because it is very high-level. For example, we were able to create a websocket with one line of code. Neither of us have used C++ before so we do not have much to compare to when it comes to socket programming.


