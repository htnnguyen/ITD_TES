set FNCS_FATAL=yes
set FNCS_LOG_STDOUT=yes
set FNCS_LOG_LEVEL=DEBUG2
set FNCS_TRACE=yes

set FNCS_CONFIG_FILE=
start /b cmd /c fncs_broker 1 ^>broker.log 2^>^&1

REM set FNCS_CONFIG_FILE=
REM start /b cmd /c fncs_player 2d prices.txt ^>player.log 2^>^&1

REM set FNCS_CONFIG_FILE=eplus.yaml
REM start /b cmd /c python eplus_control.py 172800 60 ^>eplus_control.log 2^>^&1

set FNCS_CONFIG_FILE=
set FNCS_LOG_LEVEL=DEBUG4
set FNCS_LOG_STDOUT=yes
start /b cmd /c gridlabd IEEE13_B.glm ^>gridlabd.log 2^>^&1 