# ISU_PNNL-TESP
This is the repository of ISU-PNNL project.

The "Matlab and Python FileS" Folder has 2 files:
      1) IEEE13_glm_writer.m creates 180 houses adding to the IEEE13 test system. The topology checking can be done in this file
      2) The price_generator.py generate price.txt with dynamic pricing signal for 48h with 1 min interval.
      
The "Modified_IEEE13_with180houses" folder contains program that simulates the "close_loop" market clearing simulation for 48 h, 
which is similar to te30. We test for the extended IEEE13 with 180 houses.

The "Open_Loop with Price.txt" folder contains a program that only tests the response of the IEEE13 system with pricing signal. 
No market clearing (auction.py) is considered.

