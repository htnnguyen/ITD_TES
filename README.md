# ISU_PNNL-TESP
This is the repository of ISU-PNNL project.

The "Matlab and Python Files" Folder has 2 files:
      1) IEEE13_glm_writer.m creates 180 houses adding to the IEEE13 test system. The topology checking can be done in this file
      2) The price_generator.py generate price.txt with dynamic pricing signal for 48h with 1 min interval.
      
The "Modified_IEEE13_with180houses" folder contains program that simulates the "close_loop" market clearing simulation for 48 h, 
which is similar to te30. We test for the extended IEEE13 with 180 houses.

The "Open_Loop with Price.txt" folder contains a program that only tests the response of the IEEE13 system with pricing signal. 
No market clearing (auction.py) is considered.

The "Version 0" folder contains a program that constructs the baseload of all 180 houses given weather scenarios, thermal intergrity level, and thermal setpoints.

The "Version 1" contain a direct load control example where different houses are represented by different processes (house_controller.py +houseID)

The "Version 2" contain a price based control example where different houses are represented by different processes (house_controller.py +houseID) using PowerMatcher framework. There are subfolders:
  1) Version 2.0 Loadshed example using price signal. Instead of direct load control signals, the DSO sends price which can adjust the number of HVACs turning off. The price is cleared by considering the submitted bid of each house.
