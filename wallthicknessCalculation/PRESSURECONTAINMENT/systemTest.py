from ast import Str
from cmath import sqrt
import math
from cgitb import small
from unittest import result
import numpy as np  
import numpy.polynomial.polynomial  as roots



def pressure_sysTest(Outside_Diameter_OD, Nominal_Wall_Thickness_tnom, Fabrication_Thickness_Tolerance_tfab, Corrosion_Allowance_tcorr, Ovality_of_Pipe_Oo,SMYS_σsmys,SMTS_σsmts,Derating_value_temp_yieldStress_fy_temp,Derating_value_temp_tensileStress_fu_temp,Youngs_Modulus_E ,Poission_s_Ratio_ν ,Maximum_Fabrication_Factor_alpha_fab,Pd,ptest_value,Pmin,Elevation_at_Pressure_Reference_Level_href,Elevation_level_at_Pressure_Point_hl ,Product_Density_ρcont,Hydrotest_Water_Density_ρt,Incidental_to_Design_Pressure_Ratio_gamma_inc,Max_Water_Depth_WDmax,Sea_Water_Density_ρsea,Max_Elevation_wrt_MSL_hmax,Min_Elevation_wrt_MSL_hmin,Plt):
    
        Material_Strength_Factor_alpha_u = 1.15
        Gravity_of_Acceleration_g = 9.81
        Constant_for_Mill_Pressure_test_k = 1
        Pressure_testFactor_gamma_m_SCPC = 1.046
    
    # print("___________________PIPELINE INPUTS___________________")

        Measured_Minimum_Thickness_for_Test_Pressure_t1 = (Nominal_Wall_Thickness_tnom - Fabrication_Thickness_Tolerance_tfab - Corrosion_Allowance_tcorr)
        print(f"Measured Minimum Thickness for Test Pressure : {Measured_Minimum_Thickness_for_Test_Pressure_t1}")


    # print("___________________________ENVIRONMENTAL INPUTS______________________________")

       

        Depth = float(Max_Water_Depth_WDmax + Min_Elevation_wrt_MSL_hmin)
        print(Depth)

        
    # print("_____________________________DESIGNS FACTOR AS PER DNGVL____________________")

        # print("\n\tSAFETY CLASS : 'Medium'")

        
        # #  Stresses

        # print("_________________STRESSES_______________________")

        fy= float(SMYS_σsmys-Derating_value_temp_yieldStress_fy_temp)*Material_Strength_Factor_alpha_u
        print("fy",fy)
        fu=float(SMTS_σsmts-Derating_value_temp_tensileStress_fu_temp)*Material_Strength_Factor_alpha_u
        print("fu",fu)
        fcb=min(fy,(fu/1.15))
        print("fcb",fcb)




        # print("__________________________________PRESSURE_____________________________")

        # Pd = float(input("Enter Design Pressure : ")) 
        Pt = float(1.155*Pd)
        print("Pt",Pt)
        Plt = float(Incidental_to_Design_Pressure_Ratio_gamma_inc * Pd)
        print("Plt",Plt)
        Pe = float(((Sea_Water_Density_ρsea*Gravity_of_Acceleration_g*Depth))/1000000)
        print("Pe",Pe)

        if(Pe>0):
            ExternalPressure = Pe
            
        else:
            ExternalPressure = 0


        print("External Pressure : ",ExternalPressure)

        Pb_t1 = float(((2*Measured_Minimum_Thickness_for_Test_Pressure_t1)/(Outside_Diameter_OD-Measured_Minimum_Thickness_for_Test_Pressure_t1)) * fcb * 2/(math.sqrt(3)))
        print("Pb_t1",Pb_t1)

        Pmpt = float(Constant_for_Mill_Pressure_test_k * (2*Measured_Minimum_Thickness_for_Test_Pressure_t1/(Outside_Diameter_OD - Measured_Minimum_Thickness_for_Test_Pressure_t1)) * min(SMYS_σsmys * 0.96, SMTS_σsmts * 0.84))
        print(Pmpt)


        # # Hydrotest Checks

        # # Pressure Containment

        # print("_______Pressure Containment check___________")



        if((Plt - Pe ) <= min((Pb_t1/Pressure_testFactor_gamma_m_SCPC),(Pmpt))):
            P_check = print(" P_check : Wall thickness accepted")
            
        else:
            P_check =print("  P_check : Redesign wall  thickness")


        # Utility Check

        UC_prss_cont = (Plt-Pe)/min((Pb_t1/Pressure_testFactor_gamma_m_SCPC),(Pmpt))

        print("UC_prss_cont",UC_prss_cont)