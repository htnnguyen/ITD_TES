set FNCS_FATAL=yes
set FNCS_LOG_STDOUT=yes
set FNCS_LOG_LEVEL=DEBUG4
set FNCS_TRACE=yes
set FNCS_TIME_DELTA=


set FNCS_CONFIG_FILE=
start /b cmd /c fncs_broker 183 ^>broker.log 2^>^&1

set FNCS_CONFIG_FILE=
start /b cmd /c fncs_player 6h loadshed.player ^>player.log 2^>^&1

set FNCS_CONFIG_FILE=DSO.yaml
start /b cmd /c python DSO.py 21600 1 ^>DSO.log 2^>^&1

set FNCS_CONFIG_FILE=
set FNCS_LOG_LEVEL=DEBUG4
set FNCS_LOG_STDOUT=yes
start /b cmd /c gridlabd IEEE13.glm ^>gridlabd.log 2^>^&1 

set FNCS_LOG_STDOUT=no
set FNCS_LOG_LEVEL=


set FNCS_CONFIG_FILE=house_1_1.yaml
start /b cmd /c python house_controller.py house_1_1 ^>house_controller1_1.log 2^>^&1

set FNCS_CONFIG_FILE=house_1_2.yaml
start /b cmd /c python house_controller.py house_1_2 ^>house_controller1_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_1_3.yaml
start /b cmd /c python house_controller.py house_1_3 ^>house_controller1_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_1_4.yaml
start /b cmd /c python house_controller.py house_1_4 ^>house_controller1_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_1_5.yaml
start /b cmd /c python house_controller.py house_1_5 ^>house_controller1_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_1_6.yaml
start /b cmd /c python house_controller.py house_1_6 ^>house_controller1_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_1_7.yaml
start /b cmd /c python house_controller.py house_1_7 ^>house_controller1_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_1_8.yaml
start /b cmd /c python house_controller.py house_1_8 ^>house_controller1_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_1_9.yaml
start /b cmd /c python house_controller.py house_1_9 ^>house_controller1_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_1_10.yaml
start /b cmd /c python house_controller.py house_1_10 ^>house_controller1_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_1_11.yaml
start /b cmd /c python house_controller.py house_1_11 ^>house_controller1_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_1_12.yaml
start /b cmd /c python house_controller.py house_1_12 ^>house_controller1_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_1.yaml
start /b cmd /c python house_controller.py house_2_1 ^>house_controller2_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_2.yaml
start /b cmd /c python house_controller.py house_2_2 ^>house_controller2_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_3.yaml
start /b cmd /c python house_controller.py house_2_3 ^>house_controller2_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_4.yaml
start /b cmd /c python house_controller.py house_2_4 ^>house_controller2_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_5.yaml
start /b cmd /c python house_controller.py house_2_5 ^>house_controller2_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_6.yaml
start /b cmd /c python house_controller.py house_2_6 ^>house_controller2_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_7.yaml
start /b cmd /c python house_controller.py house_2_7 ^>house_controller2_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_8.yaml
start /b cmd /c python house_controller.py house_2_8 ^>house_controller2_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_9.yaml
start /b cmd /c python house_controller.py house_2_9 ^>house_controller2_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_10.yaml
start /b cmd /c python house_controller.py house_2_10 ^>house_controller2_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_11.yaml
start /b cmd /c python house_controller.py house_2_11 ^>house_controller2_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_2_12.yaml
start /b cmd /c python house_controller.py house_2_12 ^>house_controller2_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_1.yaml
start /b cmd /c python house_controller.py house_3_1 ^>house_controller3_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_2.yaml
start /b cmd /c python house_controller.py house_3_2 ^>house_controller3_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_3.yaml
start /b cmd /c python house_controller.py house_3_3 ^>house_controller3_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_4.yaml
start /b cmd /c python house_controller.py house_3_4 ^>house_controller3_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_5.yaml
start /b cmd /c python house_controller.py house_3_5 ^>house_controller3_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_6.yaml
start /b cmd /c python house_controller.py house_3_6 ^>house_controller3_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_7.yaml
start /b cmd /c python house_controller.py house_3_7 ^>house_controller3_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_8.yaml
start /b cmd /c python house_controller.py house_3_8 ^>house_controller3_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_9.yaml
start /b cmd /c python house_controller.py house_3_9 ^>house_controller3_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_10.yaml
start /b cmd /c python house_controller.py house_3_10 ^>house_controller3_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_11.yaml
start /b cmd /c python house_controller.py house_3_11 ^>house_controller3_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_3_12.yaml
start /b cmd /c python house_controller.py house_3_12 ^>house_controller3_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_1.yaml
start /b cmd /c python house_controller.py house_4_1 ^>house_controller4_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_2.yaml
start /b cmd /c python house_controller.py house_4_2 ^>house_controller4_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_3.yaml
start /b cmd /c python house_controller.py house_4_3 ^>house_controller4_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_4.yaml
start /b cmd /c python house_controller.py house_4_4 ^>house_controller4_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_5.yaml
start /b cmd /c python house_controller.py house_4_5 ^>house_controller4_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_6.yaml
start /b cmd /c python house_controller.py house_4_6 ^>house_controller4_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_7.yaml
start /b cmd /c python house_controller.py house_4_7 ^>house_controller4_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_8.yaml
start /b cmd /c python house_controller.py house_4_8 ^>house_controller4_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_9.yaml
start /b cmd /c python house_controller.py house_4_9 ^>house_controller4_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_10.yaml
start /b cmd /c python house_controller.py house_4_10 ^>house_controller4_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_11.yaml
start /b cmd /c python house_controller.py house_4_11 ^>house_controller4_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_4_12.yaml
start /b cmd /c python house_controller.py house_4_12 ^>house_controller4_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_1.yaml
start /b cmd /c python house_controller.py house_5_1 ^>house_controller5_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_2.yaml
start /b cmd /c python house_controller.py house_5_2 ^>house_controller5_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_3.yaml
start /b cmd /c python house_controller.py house_5_3 ^>house_controller5_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_4.yaml
start /b cmd /c python house_controller.py house_5_4 ^>house_controller5_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_5.yaml
start /b cmd /c python house_controller.py house_5_5 ^>house_controller5_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_6.yaml
start /b cmd /c python house_controller.py house_5_6 ^>house_controller5_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_7.yaml
start /b cmd /c python house_controller.py house_5_7 ^>house_controller5_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_8.yaml
start /b cmd /c python house_controller.py house_5_8 ^>house_controller5_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_9.yaml
start /b cmd /c python house_controller.py house_5_9 ^>house_controller5_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_10.yaml
start /b cmd /c python house_controller.py house_5_10 ^>house_controller5_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_11.yaml
start /b cmd /c python house_controller.py house_5_11 ^>house_controller5_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_5_12.yaml
start /b cmd /c python house_controller.py house_5_12 ^>house_controller5_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_1.yaml
start /b cmd /c python house_controller.py house_6_1 ^>house_controller6_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_2.yaml
start /b cmd /c python house_controller.py house_6_2 ^>house_controller6_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_3.yaml
start /b cmd /c python house_controller.py house_6_3 ^>house_controller6_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_4.yaml
start /b cmd /c python house_controller.py house_6_4 ^>house_controller6_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_5.yaml
start /b cmd /c python house_controller.py house_6_5 ^>house_controller6_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_6.yaml
start /b cmd /c python house_controller.py house_6_6 ^>house_controller6_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_7.yaml
start /b cmd /c python house_controller.py house_6_7 ^>house_controller6_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_8.yaml
start /b cmd /c python house_controller.py house_6_8 ^>house_controller6_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_9.yaml
start /b cmd /c python house_controller.py house_6_9 ^>house_controller6_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_10.yaml
start /b cmd /c python house_controller.py house_6_10 ^>house_controller6_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_11.yaml
start /b cmd /c python house_controller.py house_6_11 ^>house_controller6_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_6_12.yaml
start /b cmd /c python house_controller.py house_6_12 ^>house_controller6_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_1.yaml
start /b cmd /c python house_controller.py house_7_1 ^>house_controller7_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_2.yaml
start /b cmd /c python house_controller.py house_7_2 ^>house_controller7_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_3.yaml
start /b cmd /c python house_controller.py house_7_3 ^>house_controller7_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_4.yaml
start /b cmd /c python house_controller.py house_7_4 ^>house_controller7_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_5.yaml
start /b cmd /c python house_controller.py house_7_5 ^>house_controller7_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_6.yaml
start /b cmd /c python house_controller.py house_7_6 ^>house_controller7_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_7.yaml
start /b cmd /c python house_controller.py house_7_7 ^>house_controller7_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_8.yaml
start /b cmd /c python house_controller.py house_7_8 ^>house_controller7_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_9.yaml
start /b cmd /c python house_controller.py house_7_9 ^>house_controller7_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_10.yaml
start /b cmd /c python house_controller.py house_7_10 ^>house_controller7_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_11.yaml
start /b cmd /c python house_controller.py house_7_11 ^>house_controller7_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_7_12.yaml
start /b cmd /c python house_controller.py house_7_12 ^>house_controller7_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_1.yaml
start /b cmd /c python house_controller.py house_8_1 ^>house_controller8_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_2.yaml
start /b cmd /c python house_controller.py house_8_2 ^>house_controller8_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_3.yaml
start /b cmd /c python house_controller.py house_8_3 ^>house_controller8_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_4.yaml
start /b cmd /c python house_controller.py house_8_4 ^>house_controller8_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_5.yaml
start /b cmd /c python house_controller.py house_8_5 ^>house_controller8_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_6.yaml
start /b cmd /c python house_controller.py house_8_6 ^>house_controller8_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_7.yaml
start /b cmd /c python house_controller.py house_8_7 ^>house_controller8_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_8.yaml
start /b cmd /c python house_controller.py house_8_8 ^>house_controller8_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_9.yaml
start /b cmd /c python house_controller.py house_8_9 ^>house_controller8_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_10.yaml
start /b cmd /c python house_controller.py house_8_10 ^>house_controller8_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_11.yaml
start /b cmd /c python house_controller.py house_8_11 ^>house_controller8_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_8_12.yaml
start /b cmd /c python house_controller.py house_8_12 ^>house_controller8_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_1.yaml
start /b cmd /c python house_controller.py house_9_1 ^>house_controller9_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_2.yaml
start /b cmd /c python house_controller.py house_9_2 ^>house_controller9_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_3.yaml
start /b cmd /c python house_controller.py house_9_3 ^>house_controller9_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_4.yaml
start /b cmd /c python house_controller.py house_9_4 ^>house_controller9_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_5.yaml
start /b cmd /c python house_controller.py house_9_5 ^>house_controller9_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_6.yaml
start /b cmd /c python house_controller.py house_9_6 ^>house_controller9_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_7.yaml
start /b cmd /c python house_controller.py house_9_7 ^>house_controller9_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_8.yaml
start /b cmd /c python house_controller.py house_9_8 ^>house_controller9_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_9.yaml
start /b cmd /c python house_controller.py house_9_9 ^>house_controller9_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_10.yaml
start /b cmd /c python house_controller.py house_9_10 ^>house_controller9_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_11.yaml
start /b cmd /c python house_controller.py house_9_11 ^>house_controller9_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_9_12.yaml
start /b cmd /c python house_controller.py house_9_12 ^>house_controller9_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_1.yaml
start /b cmd /c python house_controller.py house_10_1 ^>house_controller10_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_2.yaml
start /b cmd /c python house_controller.py house_10_2 ^>house_controller10_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_3.yaml
start /b cmd /c python house_controller.py house_10_3 ^>house_controller10_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_4.yaml
start /b cmd /c python house_controller.py house_10_4 ^>house_controller10_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_5.yaml
start /b cmd /c python house_controller.py house_10_5 ^>house_controller10_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_6.yaml
start /b cmd /c python house_controller.py house_10_6 ^>house_controller10_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_7.yaml
start /b cmd /c python house_controller.py house_10_7 ^>house_controller10_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_8.yaml
start /b cmd /c python house_controller.py house_10_8 ^>house_controller10_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_9.yaml
start /b cmd /c python house_controller.py house_10_9 ^>house_controller10_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_10.yaml
start /b cmd /c python house_controller.py house_10_10 ^>house_controller10_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_11.yaml
start /b cmd /c python house_controller.py house_10_11 ^>house_controller10_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_10_12.yaml
start /b cmd /c python house_controller.py house_10_12 ^>house_controller10_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_1.yaml
start /b cmd /c python house_controller.py house_11_1 ^>house_controller11_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_2.yaml
start /b cmd /c python house_controller.py house_11_2 ^>house_controller11_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_3.yaml
start /b cmd /c python house_controller.py house_11_3 ^>house_controller11_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_4.yaml
start /b cmd /c python house_controller.py house_11_4 ^>house_controller11_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_5.yaml
start /b cmd /c python house_controller.py house_11_5 ^>house_controller11_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_6.yaml
start /b cmd /c python house_controller.py house_11_6 ^>house_controller11_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_7.yaml
start /b cmd /c python house_controller.py house_11_7 ^>house_controller11_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_8.yaml
start /b cmd /c python house_controller.py house_11_8 ^>house_controller11_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_9.yaml
start /b cmd /c python house_controller.py house_11_9 ^>house_controller11_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_10.yaml
start /b cmd /c python house_controller.py house_11_10 ^>house_controller11_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_11.yaml
start /b cmd /c python house_controller.py house_11_11 ^>house_controller11_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_11_12.yaml
start /b cmd /c python house_controller.py house_11_12 ^>house_controller11_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_1.yaml
start /b cmd /c python house_controller.py house_12_1 ^>house_controller12_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_2.yaml
start /b cmd /c python house_controller.py house_12_2 ^>house_controller12_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_3.yaml
start /b cmd /c python house_controller.py house_12_3 ^>house_controller12_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_4.yaml
start /b cmd /c python house_controller.py house_12_4 ^>house_controller12_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_5.yaml
start /b cmd /c python house_controller.py house_12_5 ^>house_controller12_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_6.yaml
start /b cmd /c python house_controller.py house_12_6 ^>house_controller12_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_7.yaml
start /b cmd /c python house_controller.py house_12_7 ^>house_controller12_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_8.yaml
start /b cmd /c python house_controller.py house_12_8 ^>house_controller12_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_9.yaml
start /b cmd /c python house_controller.py house_12_9 ^>house_controller12_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_10.yaml
start /b cmd /c python house_controller.py house_12_10 ^>house_controller12_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_11.yaml
start /b cmd /c python house_controller.py house_12_11 ^>house_controller12_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_12_12.yaml
start /b cmd /c python house_controller.py house_12_12 ^>house_controller12_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_1.yaml
start /b cmd /c python house_controller.py house_13_1 ^>house_controller13_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_2.yaml
start /b cmd /c python house_controller.py house_13_2 ^>house_controller13_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_3.yaml
start /b cmd /c python house_controller.py house_13_3 ^>house_controller13_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_4.yaml
start /b cmd /c python house_controller.py house_13_4 ^>house_controller13_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_5.yaml
start /b cmd /c python house_controller.py house_13_5 ^>house_controller13_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_6.yaml
start /b cmd /c python house_controller.py house_13_6 ^>house_controller13_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_7.yaml
start /b cmd /c python house_controller.py house_13_7 ^>house_controller13_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_8.yaml
start /b cmd /c python house_controller.py house_13_8 ^>house_controller13_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_9.yaml
start /b cmd /c python house_controller.py house_13_9 ^>house_controller13_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_10.yaml
start /b cmd /c python house_controller.py house_13_10 ^>house_controller13_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_11.yaml
start /b cmd /c python house_controller.py house_13_11 ^>house_controller13_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_13_12.yaml
start /b cmd /c python house_controller.py house_13_12 ^>house_controller13_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_1.yaml
start /b cmd /c python house_controller.py house_14_1 ^>house_controller14_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_2.yaml
start /b cmd /c python house_controller.py house_14_2 ^>house_controller14_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_3.yaml
start /b cmd /c python house_controller.py house_14_3 ^>house_controller14_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_4.yaml
start /b cmd /c python house_controller.py house_14_4 ^>house_controller14_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_5.yaml
start /b cmd /c python house_controller.py house_14_5 ^>house_controller14_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_6.yaml
start /b cmd /c python house_controller.py house_14_6 ^>house_controller14_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_7.yaml
start /b cmd /c python house_controller.py house_14_7 ^>house_controller14_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_8.yaml
start /b cmd /c python house_controller.py house_14_8 ^>house_controller14_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_9.yaml
start /b cmd /c python house_controller.py house_14_9 ^>house_controller14_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_10.yaml
start /b cmd /c python house_controller.py house_14_10 ^>house_controller14_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_11.yaml
start /b cmd /c python house_controller.py house_14_11 ^>house_controller14_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_14_12.yaml
start /b cmd /c python house_controller.py house_14_12 ^>house_controller14_12.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_1.yaml
start /b cmd /c python house_controller.py house_15_1 ^>house_controller15_1.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_2.yaml
start /b cmd /c python house_controller.py house_15_2 ^>house_controller15_2.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_3.yaml
start /b cmd /c python house_controller.py house_15_3 ^>house_controller15_3.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_4.yaml
start /b cmd /c python house_controller.py house_15_4 ^>house_controller15_4.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_5.yaml
start /b cmd /c python house_controller.py house_15_5 ^>house_controller15_5.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_6.yaml
start /b cmd /c python house_controller.py house_15_6 ^>house_controller15_6.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_7.yaml
start /b cmd /c python house_controller.py house_15_7 ^>house_controller15_7.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_8.yaml
start /b cmd /c python house_controller.py house_15_8 ^>house_controller15_8.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_9.yaml
start /b cmd /c python house_controller.py house_15_9 ^>house_controller15_9.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_10.yaml
start /b cmd /c python house_controller.py house_15_10 ^>house_controller15_10.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_11.yaml
start /b cmd /c python house_controller.py house_15_11 ^>house_controller15_11.log 2^>^&1
set FNCS_CONFIG_FILE=house_15_12.yaml
start /b cmd /c python house_controller.py house_15_12 ^>house_controller15_12.log 2^>^&1





