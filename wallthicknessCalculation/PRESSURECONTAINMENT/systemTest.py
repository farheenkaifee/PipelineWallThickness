from ast import Str
from cmath import sqrt
import math
from cgitb import small
from unittest import result
import numpy as np  
import numpy.polynomial.polynomial  as roots



def pressure_sysTest(Outside_Diameter_OD, Nominal_Wall_Thickness_tnom, Fabrication_Thickness_Tolerance_tfab, Corrosion_Allowance_tcorr, Ovality_of_Pipe_Oo,SMYS_σsmys,SMTS_σsmts,Derating_value_temp_yieldStress_fy_temp,Derating_value_temp_tensileStress_fu_temp,Youngs_Modulus_E ,Poission_s_Ratio_ν ,Maximum_Fabrication_Factor_alpha_fab,Pd,Pmin,Elevation_at_Pressure_Reference_Level_href,Elevation_level_at_Pressure_Point_hl ,Product_Density_ρcont,Hydrotest_Water_Density_ρt,Incidental_to_Design_Pressure_Ratio_gamma_inc,Water_Depth_WD,Sea_Water_Density_ρsea,Min_Elevation_wrt_MSL_hmin,Safety_Class_RF_gamma_SCPC,Material_Strength_Factor_alpha_u,Material_resistant_factor_gamma_m):
    
    
    
    try:

        # Material_Strength_Factor_alpha_u = 1.15
        Gravity_of_Acceleration_g = 9.81
        Constant_for_Mill_Pressure_test_k = 1
        # Safety_Class_RF_gamma_SCPC = 1.046

        Outside_Diameter_OD = float(Outside_Diameter_OD) 
        # print(O.utside_Diameter_OD) 
        Nominal_Wall_Thickness_tnom = float(Nominal_Wall_Thickness_tnom) 
        # print("t_nom  ", Nominal_Wall_Thickness_tnom)
        Fabrication_Thickness_Tolerance_tfab = float(Fabrication_Thickness_Tolerance_tfab) 
        # print("t_fab ", Fabrication_Thickness_Tolerance_tfab)
        Corrosion_Allowance_tcorr = float(Corrosion_Allowance_tcorr) 
        # print("t_corr",Corrosion_Allowance_tcorr)
        Ovality_of_Pipe_Oo = float(Ovality_of_Pipe_Oo) 
        # print("oo ",Ovality_of_Pipe_Oo)
        SMYS_σsmys = float(SMYS_σsmys) 
        # print("smys ",SMYS_σsmys)
        SMTS_σsmts = float(SMTS_σsmts) 
        # print("smts ",SMTS_σsmts)
        Derating_value_temp_yieldStress_fy_temp = float(Derating_value_temp_yieldStress_fy_temp) 
        # print("fy_temp ",Derating_value_temp_yieldStress_fy_temp)
        Derating_value_temp_tensileStress_fu_temp = float(Derating_value_temp_tensileStress_fu_temp) 
        # print("fu_temp ",Derating_value_temp_tensileStress_fu_temp)
        Youngs_Modulus_E = float(Youngs_Modulus_E) 
        # print("E ",Youngs_Modulus_E)
        Poission_s_Ratio_ν = float(Poission_s_Ratio_ν) 
        # print("v ",Poission_s_Ratio_ν)
        Maximum_Fabrication_Factor_alpha_fab = float(Maximum_Fabrication_Factor_alpha_fab) 
        # print("alpha_fab ",Maximum_Fabrication_Factor_alpha_fab)
        Material_Strength_Factor_alpha_u = float(Material_Strength_Factor_alpha_u) 
        # print("alpha_u ",Material_Strength_Factor_alpha_u)
        Pd = float(Pd) 
        # print("Pd ",Pd)
        Material_resistant_factor_gamma_m = float(Material_resistant_factor_gamma_m) 
        # print("gamma_m ",Material_resistant_factor_gamma_m)
        Pmin = float(Pmin) 
        # print("Pmin ",Pmin)
        Elevation_at_Pressure_Reference_Level_href = float(Elevation_at_Pressure_Reference_Level_href) 
        # print("href ",Elevation_at_Pressure_Reference_Level_href)
        Elevation_level_at_Pressure_Point_hl = float(Elevation_level_at_Pressure_Point_hl) 
        # print("hl ",Elevation_level_at_Pressure_Point_hl)
        Product_Density_ρcont = float(Product_Density_ρcont) 
        # print("rho_cont ",Product_Density_ρcont)
        Hydrotest_Water_Density_ρt = float(Hydrotest_Water_Density_ρt) 
        # print("rho_t ",Hydrotest_Water_Density_ρt)
        Incidental_to_Design_Pressure_Ratio_gamma_inc = float(Incidental_to_Design_Pressure_Ratio_gamma_inc) 
        # print("gamma_inc ",Incidental_to_Design_Pressure_Ratio_gamma_inc)
        Water_Depth_WD = float(Water_Depth_WD) 
        # print("WDmin ",Water_Depth_WD)
        Sea_Water_Density_ρsea = float(Sea_Water_Density_ρsea) 
        # print("rho_sea ",Sea_Water_Density_ρsea)
        Min_Elevation_wrt_MSL_hmin = float(Min_Elevation_wrt_MSL_hmin)
        # print("hmin ",Min_Elevation_wrt_MSL_hmin)

        Safety_Class_RF_gamma_SCPC = float(Safety_Class_RF_gamma_SCPC) 
        # print("gamma_SCPC ",Safety_Class_RF_gamma_SCPC)
    
    # print("___________________PIPELINE INPUTS___________________")

        Measured_Minimum_Thickness_for_Test_Pressure_t1 = round((Nominal_Wall_Thickness_tnom - Fabrication_Thickness_Tolerance_tfab),3)
        print(f"Measured Minimum Thickness for Test Pressure : {Measured_Minimum_Thickness_for_Test_Pressure_t1}")


    # print("___________________________ENVIRONMENTAL INPUTS______________________________")

       

        Depth = round(float(Water_Depth_WD + Min_Elevation_wrt_MSL_hmin),3)
        print(Depth)

        
    # print("_____________________________DESIGNS FACTOR AS PER DNGVL____________________")

        # print("\n\tSAFETY CLASS : 'Medium'")

        
        # #  Stresses

        # print("_________________STRESSES_______________________")

        fy= round((float(SMYS_σsmys-Derating_value_temp_yieldStress_fy_temp)*Material_Strength_Factor_alpha_u),3)
        print("fy",fy)
        fu=round((float(SMTS_σsmts-Derating_value_temp_tensileStress_fu_temp)*Material_Strength_Factor_alpha_u),3)
        print("fu",fu)
        fcb=min(fy,(fu/1.15))
        print("fcb",fcb)




        # print("__________________________________PRESSURE_____________________________")

        # Pd = float(input("Enter Design Pressure : ")) 
        Pt = round(float(1.155*Pd),3)
        print("Pt",Pt)
        Plt = round(float(Incidental_to_Design_Pressure_Ratio_gamma_inc * Pd),3)
        print("Plt",Plt)
        Pe = round(float(((Sea_Water_Density_ρsea*Gravity_of_Acceleration_g*Depth))/1000000),3)
        print("Pe",Pe)

        if(Pe>0):
            ExternalPressure = Pe
            
        else:
            ExternalPressure = 0


        print("External Pressure : ",ExternalPressure)

        Pb_t1 = round(float(((2*Measured_Minimum_Thickness_for_Test_Pressure_t1)/(Outside_Diameter_OD-Measured_Minimum_Thickness_for_Test_Pressure_t1)) * fcb * 2/(math.sqrt(3))),3)
        print("Pb_t1",Pb_t1)

        Pmpt = round(float(Constant_for_Mill_Pressure_test_k * (2*Measured_Minimum_Thickness_for_Test_Pressure_t1/(Outside_Diameter_OD - Measured_Minimum_Thickness_for_Test_Pressure_t1)) * min(SMYS_σsmys * 0.96, SMTS_σsmts * 0.84)),3)
        print(Pmpt)


        # # Hydrotest Checks

        # # Pressure Containment

        # print("_______Pressure Containment check___________")





        if((Plt - Pe ) <= min((Pb_t1/Safety_Class_RF_gamma_SCPC),(Pmpt))):
            P_check = "Wall Thickness Accepted ✅"
            
        else:
            P_check = "Redesign Wall Thickness ❌"

           
            


        # Utility Check

        UC_prss_cont = round((Plt-Pe)/min((Pb_t1/Safety_Class_RF_gamma_SCPC),(Pmpt)),3)

        print("UC_prss_cont",UC_prss_cont)

        return UC_prss_cont, P_check
    
        



    except:
        print("Error in Pressure Containment System check...")
