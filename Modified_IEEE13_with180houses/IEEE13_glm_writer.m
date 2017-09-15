clear;
clc;
fid_name = 'IEEE13VariableData.glm';
k=['CS','AS','BS','CS','BS','CS','BS','CS','AS','AS','BS','CS','AS','BS','CS'];   
write_file = fopen(fid_name,'w');

% 
% for i=1:15
%     fprintf(write_file,'object triplex_line {\n');
% fprintf(write_file,'name trip_line');
% fprintf(write_file,'%u',i);
% fprintf(write_file,';\n');
% fprintf(write_file,'phases ');
%                 fprintf(write_file,'%s%s',k(2*i-1:2*i));
%                 fprintf(write_file,';\n');
% fprintf(write_file,'from trip_node');
% fprintf(write_file,'%u',i);
% fprintf(write_file,';\n');
% fprintf(write_file,'to trip_meter');
% fprintf(write_file,'%u',i);
% fprintf(write_file,';\n');
% fprintf(write_file,'length 0;\n');
% fprintf(write_file,'configuration triplex_line_configuration_1;\n');
% fprintf(write_file,'}\n');
% fprintf(write_file,'object triplex_meter {\n');     
%      fprintf(write_file,'name trip_meter');
%      fprintf(write_file,'%u',i);
%      fprintf(write_file,';\n');
%      fprintf(write_file,'phases ');
%                 fprintf(write_file,'%s%s',k(2*i-1:2*i));
%                 fprintf(write_file,';\n');
%      fprintf(write_file,'nominal_voltage 124.00;\n');     
% fprintf(write_file,'}\n'); 
% 
%     for j=1:12
% fprintf(write_file,'object triplex_line {\n');
% fprintf(write_file,'name meter_house');
% fprintf(write_file,'%u',i);
%                 fprintf(write_file,'_');
%                 fprintf(write_file,'%u',j);
%                 fprintf(write_file,';\n');
% fprintf(write_file,'phases ');
%                 fprintf(write_file,'%s%s',k(2*i-1:2*i));
%                 fprintf(write_file,';\n');
% fprintf(write_file,'from trip_meter');
% fprintf(write_file,'%u',i);
% fprintf(write_file,';\n');
% fprintf(write_file,'to trip_node');
% fprintf(write_file,'%u',i);
%                 fprintf(write_file,'_');
%                 fprintf(write_file,'%u',j);
%                 fprintf(write_file,';\n');
% fprintf(write_file,'length 0;\n');
% fprintf(write_file,'configuration triplex_line_configuration_1;\n');
% fprintf(write_file,'}\n');
% fprintf(write_file,'object triplex_meter {\n');     
%      fprintf(write_file,'name trip_node');
%      fprintf(write_file,'%u',i);
%                 fprintf(write_file,'_');
%                 fprintf(write_file,'%u',j);
%                 fprintf(write_file,';\n');
%      fprintf(write_file,'groupid trip_node_meter');
%      fprintf(write_file,'%u',i);
%      fprintf(write_file,';\n');
%      fprintf(write_file,'phases ');
%                 fprintf(write_file,'%s%s',k(2*i-1:2*i));
%                 fprintf(write_file,';\n');
%      fprintf(write_file,'nominal_voltage 124.00;\n');     
% fprintf(write_file,'}\n'); 
% 
% fprintf(write_file,'object triplex_line {\n');
% 	fprintf(write_file,'name trip_line');
%                 fprintf(write_file,'%u',i);
%                 fprintf(write_file,'_');
%                 fprintf(write_file,'%u',j);
%                 fprintf(write_file,';\n');
% 	
%                 fprintf(write_file,'phases ');
%                 fprintf(write_file,'%s%s',k(2*i-1:2*i));
%                 fprintf(write_file,';\n');
% 	fprintf(write_file,'from trip_node');
%     fprintf(write_file,'%u',i);
%                 fprintf(write_file,'_');
%                 fprintf(write_file,'%u',j);
%     fprintf(write_file,';\n');
% 	fprintf(write_file,'to trip_meter');
%     fprintf(write_file,'%u',i);
%                 fprintf(write_file,'_');
%                 fprintf(write_file,'%u',j);
%                 fprintf(write_file,';\n');
% 	fprintf(write_file,'length 0;\n'); 
% 	fprintf(write_file,'configuration triplex_line_configuration_1;\n');
%     fprintf(write_file,'}\n');
% 
% fprintf(write_file,'object triplex_meter {\n');
% 	fprintf(write_file, 'name trip_meter');
%      fprintf(write_file,'%u',i);
%                 fprintf(write_file,'_');
%                 fprintf(write_file,'%u',j);
%                 fprintf(write_file,';\n'); 
% 	 fprintf(write_file,'phases ');
%                 fprintf(write_file,'%s%s',k(2*i-1:2*i));
%                 fprintf(write_file,';\n');
% 	fprintf(write_file,'nominal_voltage 124.00;\n');
%     fprintf(write_file,'}\n');
%     end
% end

for i=1:15
    for j=1:12
        
                fprintf(write_file,'object house {\n');
                fprintf(write_file,'name house_');
                fprintf(write_file,'%u',i);
                fprintf(write_file,'_');
                fprintf(write_file,'%u',j);
                fprintf(write_file,';\n');
                
                fprintf(write_file,'parent trip_meter');
                fprintf(write_file,'%u',i);
                fprintf(write_file,'_');
                fprintf(write_file,'%u',j);
                fprintf(write_file,';\n');
                
                fprintf(write_file,'thermostat_control NONE;\n');
                fprintf(write_file,'system_mode COOL;\n');
                
     fprintf(write_file,'hvac_power_factor 0.97;\n');
     fprintf(write_file,'heating_system_type ');
     x=rand;
     
     if x<0.7112
         fprintf(write_file,'GAS;\n');
     elseif x>=0.7112&&x<0.8722
         fprintf(write_file,'HEAT_PUMP;\n');
     else
         fprintf(write_file,'RESISTANCE;\n');
     end
     %fprintf(write_file,'thermal');
     fprintf(write_file,'cooling_system_type ');
     %if x<0.947
     if x <= 1
         fprintf(write_file,'ELECTRIC;\n');
     else
         fprintf(write_file,'NONE;\n');
     end
     
     fprintf(write_file,'cooling_COP 3.90;\n');
     fprintf(write_file,'floor_area random.normal(1700,400);\n');
     s1 =strcat({'floor_area '},{''},{num2str(normrnd(1700,400))});
     %fprintf(write_file,'%s;\n',s1);
     %fprintf(write_file,'\n');
%	 fprintf(write_file,strcat({'cooling_setpoint '},{''},{num2str(unifrnd(74,78))}));
%     fprintf(write_file,'\n');
	 %fprintf(write_file,'thermostat_deadband 1;\n');
     fprintf(write_file,'ceiling_height 10;\n');
     fprintf(write_file,'window_wall_ratio 0.1;\n');
     
     
     fprintf(write_file,'Rwall random.uniform(13,15);\n');
%     fprintf(write_file,strcat({'Rwall '},{''},{num2str(unifrnd(13,15))}));
 %    fprintf(write_file,'\n');
     
     
     fprintf(write_file,'Rwindows random.uniform(0.8,1);\n');

   %  fprintf(write_file,strcat({'Rwindow '},{''},{num2str(unifrnd(0.8,1))}));
   %  fprintf(write_file,'\n');     
     
     fprintf(write_file,'Rroof random.uniform(38,60);\n');
     
	 fprintf(write_file,'object ZIPload {\n');
           fprintf(write_file,'schedule_skew random.uniform(-1000,1000);\n');
           fprintf(write_file,'base_power LIGHTS*');
           y1=0.087*randi([70,120],1)/100;
           fprintf(write_file,'%f',y1);
           fprintf(write_file,';\n');
           
           fprintf(write_file,'power_fraction -0.04000;\n');
           fprintf(write_file,'impedance_fraction 0.540000;\n');
           fprintf(write_file,'current_fraction 0.50000;\n');
           fprintf(write_file,'power_pf -1;\n');
           fprintf(write_file,'current_pf 1;\n');
           fprintf(write_file,'impedance_pf 1;\n');
           fprintf(write_file,'heat_fraction 0.91;\n');
     fprintf(write_file,'};\n');
     
     
     
     fprintf(write_file,'object waterheater {\n');
      fprintf(write_file,'schedule_skew random.uniform(-1000,1000);\n');
      
      fprintf(write_file,'heat_mode ');
      x1=rand;
      if x1<0.43
          fprintf(write_file,'ELECTRIC;\n');
      else
          fprintf(write_file,'GASHEAT;\n');
      end
      
      
      fprintf(write_file,'tank_volume random.uniform(20,80);\n');
      fprintf(write_file,'heating_element_capacity random.uniform(4,5);\n');
      fprintf(write_file,'tank_setpoint random.uniform(110,120);\n');
      fprintf(write_file,'temperature 135;\n');
      fprintf(write_file,'thermostat_deadband random.uniform(5,10);\n');
      fprintf(write_file,'location INSIDE;\n');
      fprintf(write_file,'tank_UA 3.7;\n');
      fprintf(write_file,'demand water*1;\n');
     fprintf(write_file,'};\n');
     
     x2=rand;
     if x2<0.9536
          fprintf(write_file,'object ZIPload {\n');
          fprintf(write_file,'schedule_skew random.uniform(-1000,1000);\n');
          fprintf(write_file,'base_power CLOTHESWASHER*0.4354;\n');
          fprintf(write_file,'power_fraction 1.000000;\n');
          fprintf(write_file,'impedance_fraction 0.000000;\n');
          fprintf(write_file,'current_fraction 0.000000;\n');
          fprintf(write_file,'power_pf 0.970;\n');
          fprintf(write_file,'current_pf 0.970;\n');
          fprintf(write_file,'impedance_pf 0.970;\n');
          fprintf(write_file,'heat_fraction 0.70;\n');
          fprintf(write_file,'};\n');
     end
     
     x3=rand;
     if x3<0.997
          fprintf(write_file,'object ZIPload {\n');
          fprintf(write_file,'schedule_skew random.uniform(-1000,1000);\n');
          fprintf(write_file,'base_power REFRIGERATOR*');
           y2=0.12*randi([70,120],1)/100;
           fprintf(write_file,'%f',y2);
           fprintf(write_file,';\n');
          fprintf(write_file,'power_fraction 4.450000;\n');
          fprintf(write_file,'impedance_fraction 5.030000;\n');
          fprintf(write_file,'current_fraction -8.480000;\n');
          fprintf(write_file,'power_pf 0.640;\n');
          fprintf(write_file,'current_pf 0.560;\n');
          fprintf(write_file,'impedance_pf 0.550;\n');
          fprintf(write_file,'heat_fraction 0.86;\n');
          fprintf(write_file,'};\n');
     end
     
     x4=rand;
     if x4<0.9503
          fprintf(write_file,'object ZIPload {\n');
          fprintf(write_file,'schedule_skew random.uniform(-1000,1000);\n');
          fprintf(write_file,'base_power DRYER*1.0019;\n');
          fprintf(write_file,'power_fraction 0.100000;\n');
          fprintf(write_file,'impedance_fraction 0.800000;\n');
          fprintf(write_file,'current_fraction 0.100000;\n');
          fprintf(write_file,'power_pf 0.900;\n');
          fprintf(write_file,'current_pf 0.900;\n');
          fprintf(write_file,'impedance_pf 1.000;\n');
          fprintf(write_file,'heat_fraction 0.77;\n');
          fprintf(write_file,'};\n');
     end
     
     x5=rand;
     if x5<0.95
          fprintf(write_file,'object ZIPload {\n');
          fprintf(write_file,'schedule_skew random.uniform(-1000,1000);\n');
          fprintf(write_file,'base_power FREEZER*0.9110;\n');
          fprintf(write_file,'power_fraction 1.000000;\n');
          fprintf(write_file,'impedance_fraction 0.000000;\n');
          fprintf(write_file,'current_fraction 0.000000;\n');
          fprintf(write_file,'power_pf 0.970;\n');
          fprintf(write_file,'current_pf 0.970;\n');
          fprintf(write_file,'impedance_pf 0.970;\n');
          fprintf(write_file,'heat_fraction 0.80;\n');
          fprintf(write_file,'};\n');
     end
     
     x6=rand;
     if x6<0.997
          fprintf(write_file,'object ZIPload {\n');
          fprintf(write_file,'schedule_skew random.uniform(-1000,1000);\n');
          fprintf(write_file,'base_power RANGE*1.0590;\n');
          fprintf(write_file,'power_fraction 0.000000;\n');
          fprintf(write_file,'impedance_fraction 1.000000;\n');
          fprintf(write_file,'current_fraction 0.000000;\n');
          fprintf(write_file,'power_pf 0.000;\n');
          fprintf(write_file,'current_pf 0.000;\n');
          fprintf(write_file,'impedance_pf 1.000;\n');
          fprintf(write_file,'heat_fraction 0.86;\n');
          fprintf(write_file,'};\n');
     end
     
          fprintf(write_file,'object ZIPload {\n');
          fprintf(write_file,'schedule_skew random.uniform(-1000,1000);\n');
          fprintf(write_file,'base_power MICROWAVE*');
          y3=1.36553*randi([70,120],1)/100;
           fprintf(write_file,'%f',y3);
           fprintf(write_file,';\n');
          fprintf(write_file,'power_fraction 0.110000;\n');
          fprintf(write_file,'impedance_fraction 1.160000;\n');
          fprintf(write_file,'current_fraction -0.270000;\n');
          fprintf(write_file,'power_pf 0.02540;\n');
          fprintf(write_file,'current_pf -0.12560;\n');
          fprintf(write_file,'impedance_pf -0.05220;\n');
          fprintf(write_file,'heat_fraction 0.94;\n');
     fprintf(write_file,'};\n');
fprintf(write_file,'}\n');

               
                
    end
end

fprintf(write_file, '#include "outputs_te.glm";');
% 
% 
% fprintf(write_file,'object recorder {\n');
% 	fprintf(write_file,'name climate_recorder;\n');
% 	fprintf(write_file,'parent "Spokane WA";\n');
%     fprintf(write_file,'file climate_data.csv;\n');
%     fprintf(write_file,'interval 3600;\n');
%     fprintf(write_file,'property temperature, humidity, solar_direct, extraterrestrial_direct_normal;\n');
% fprintf(write_file,'\n}\n'); 
% % 
% fprintf(write_file,'object multi_recorder {\n');
% 		 fprintf(write_file,'file "multirecorder.csv";\n');
% 		 fprintf(write_file,'property meter_645:measured_voltage_B,meter_646:measured_voltage_B,meter_611:measured_voltage_C,meter_652:measured_voltage_A,meter_692:measured_voltage_A,meter_675:measured_voltage_A,meter_634:measured_voltage_A;\n');
% 		 fprintf(write_file,'interval 60;\n');
% fprintf(write_file,'}\n');
% 
% fprintf(write_file,'object recorder {\n');
%          fprintf(write_file,'parent network_node;\n');
% 		 fprintf(write_file,'file "substation_load.csv";\n');
% 		 fprintf(write_file,'property distribution_load;\n');
% 		 fprintf(write_file,'interval 60;\n');
% fprintf(write_file,'}\n');



fclose(write_file);