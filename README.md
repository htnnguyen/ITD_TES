# ISU_PNNL-TESP
This is the repository of ISU-PNNL project. Doucmentation can be found in https://itd-tes.readthedocs.io/en/latest/TESP_DesignDoc.html

The complete version 1.0 of the ITD TES System is located in the zipped file: ITD_TES_version_1.0

We also provided the Preliminary_ITD_Test_System_Work that includes the following folders and zipped files:

The "Matlab and Python Files" Folder has 2 files:
      1) IEEE13_glm_writer.m creates 180 houses adding to the IEEE13 test system. The topology checking can be done in this file
      2) The price_generator.py generate price.txt with dynamic pricing signal for 48h with 1 min interval.
      
The "Modified_IEEE13_with180houses" folder contains program that simulates the "close_loop" market clearing simulation for 48 h, 
which is similar to te30. We test for the extended IEEE13 with 180 houses. All progamming aspects of TE30 example such as json communcation, agent registration are considered. 

The "Open_Loop with Price.txt" folder contains a program that only tests the response of the IEEE13 system with pricing signal. 
No market clearing (auction.py) is considered.

The "Version 0" folder contains a program that constructs the baseload of all 180 houses given weather scenarios, thermal intergrity level, and thermal setpoints.

The "Version 1" contains a direct load control example where different houses are represented by different processes (house_controller.py +houseID)

The "Version 2" contains a price based control example where different houses are represented by different processes (house_controller.py +houseID) using PowerMatcher framework. Instead of direct load control signals, the DSO sends price which can adjust the number of HVACs turning on/off. The price is cleared by considering aggregated bids of all HVACs.
