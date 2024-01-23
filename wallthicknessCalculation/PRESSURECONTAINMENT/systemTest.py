from ast import Str
from cmath import sqrt
import math
from cgitb import small
from unittest import result
import numpy as np  
import numpy.polynomial.polynomial  as roots



def pressure_sysTest(Plt, Pe, Pb, tnom, tfab, Ym, Yscpc, Pmpt):
    t1 = tnom - tfab
    
    if (Plt - Pe) <= min((Pb * t1)/(Ym * Yscpc), Pmpt) :
        return ("Wall Thickness Accepted..!!")
    else:
        return ("Redesign Wall Thickness..!!")
    # return print("Pressure containment System Test..!!!")


# print("___________________PIPELINE INPUTS___________________")

# print("\n\t***...PIPELINE INPUTS...***")
# Outside_Diameter_OD=float(input("Enter outer Diameter : "))
# print(Outside_Diameter_OD)
# SMYS_σsmys=float(input("Enter SMYS : "))
# print(SMYS_σsmys)
# SMTS_σsmts=float(input("Enter SMTS : "))
# print(SMTS_σsmts)
# Youngs_Modulus_E =float(input("Enter Young's Modulus : "))
# print(Youngs_Modulus_E)
# Corrosion_Allowance_tcorr =float(input("Enter Corrosion Allowance : "))
# print(Corrosion_Allowance_tcorr)
# Poission_s_Ratio_ν =float(input("Enter Poission's Ratio : "))
# print(Poission_s_Ratio_ν)
# Ovality_of_Pipe_Oo =float(input("Enter Ovality of Pipe : "))
# print(Ovality_of_Pipe_Oo)
# Product_Density_ρcont =float(input("Enter Product Density : "))
# print(Product_Density_ρcont)
# Hydrotest_Water_Density_ρt =float(input("Enter Hydrotest_Water Density : "))
# print(Hydrotest_Water_Density_ρt)
# Fabrication_Thickness_Tolerance_tfab =float(input("Enter Fabrication Thickness Tolerance : "))
# print(Fabrication_Thickness_Tolerance_tfab)
# Nominal_Wall_Thickness_tnom =float(input("Enter Nominal wall thickness : "))
# print(Nominal_Wall_Thickness_tnom)
# Measured_Minimum_Thickness_for_Test_Pressure_t1 = (Nominal_Wall_Thickness_tnom - Fabrication_Thickness_Tolerance_tfab - Corrosion_Allowance_tcorr)
# print(f"Measured Minimum Thickness for Test Pressure : {Measured_Minimum_Thickness_for_Test_Pressure_t1}")


# print("___________________________ENVIRONMENTAL INPUTS______________________________")

# print("\n\t****...Environmental Data....****")

# Sea_Water_Density_ρsea =float(input("Enter Sea Water Density : "))
# Min_Water_Depth_WDmin =float(input("Enter Minimum Water Depth : "))
# Min_Elevation_wrt_MSL_hmin =float(input("Enter Minimum elevation wrt MSL : "))
# # Highest_Astronomical_Tide_HAT =float(input("Enter Highest Astronomical Tide : "))

# Depth = float(Min_Water_Depth_WDmin + Min_Elevation_wrt_MSL_hmin)
# print(Depth)


# Gravity_of_Acceleration_g =float(input("Enter Gravity of Acceleration : "))
# Elevation_level_at_Pressure_Point_hl =float(input("Enter Elevation level at Pressure Point : "))
# # Elevation level at pressure point  = Maximum water depth + Jetti Height + Barrel Height..
# Elevation_at_Pressure_Reference_Level_href =float(input("Enter Elevated at pressure level : "))


# print(type(Sea_Water_Density_ρsea))
# print(Min_Water_Depth_WDmin)
# # print(Highest_Astronomical_Tide_HAT)
# print(Gravity_of_Acceleration_g)
# print(Elevation_level_at_Pressure_Point_hl)
# print(Elevation_at_Pressure_Reference_Level_href)
# print(Elevation_level_at_Pressure_Point_hl)
 
# #rint("_____________________________DESIGNS FACTOR AS PER DNGVL____________________")

# print("\n\tSAFETY CLASS : 'Medium'")

# Derating_value_temp_yieldStress_fy_temp =float(input("Enter Derating value due to temperature of yield Stress : "))
# Derating_value_temp_tensileStress_fu_temp =float(input("Enter Derating value due to temperature of tensile Stress : "))
# Pressure_testFactor_alpha_mpt =float(input("Enter Pressure Test Factor for Alpha mpt : "))
# Pressure_testFactor_alpha_spt =float(input("Enter Pressure Test Factor for Alpha spt : "))
# Pressure_testFactor_gamma_m =float(input("Enter Pressure Test Factor for Gamma m : "))
# Pressure_testFactor_gamma_SC_PC =float(input("Enter Pressure Test Factor for Gamma SC.PC : "))
# Pressure_testFactor_gamma_m_SCPC = Pressure_testFactor_gamma_m * Pressure_testFactor_gamma_SC_PC
# Incidental_to_Design_Pressure_Ratio_gamma_inc =float(input("Enter Incidental to design pressure ratio : "))
# Material_Strength_Factor_alpha_u =float(input("Enter Material Strength factor : "))
# Maximum_Fabrication_Factor_alpha_fab =float(input("Enter Maximum Fabrication Factor : "))
# Constant_for_Mill_Pressure_test_k =float(input("Enter Constant for Mill Pressure Task : "))

# print(Derating_value_temp_yieldStress_fy_temp)
# print(Derating_value_temp_tensileStress_fu_temp)
# print(Pressure_testFactor_alpha_mpt)
# print(Pressure_testFactor_alpha_spt)
# print(Pressure_testFactor_gamma_m)
# print(Pressure_testFactor_gamma_SC_PC)
# print("Pressure_testFactor_gamma_m_SCPC",Pressure_testFactor_gamma_m_SCPC)
# print(Incidental_to_Design_Pressure_Ratio_gamma_inc)
# print(Material_Strength_Factor_alpha_u)
# print(Maximum_Fabrication_Factor_alpha_fab)
# print(Constant_for_Mill_Pressure_test_k)


# #  Stresses

# print("_________________STRESSES_______________________")

# fy= float(SMYS_σsmys-Derating_value_temp_yieldStress_fy_temp)*Material_Strength_Factor_alpha_u
# print("fy",fy)
# fu=float(SMTS_σsmts-Derating_value_temp_tensileStress_fu_temp)*Material_Strength_Factor_alpha_u
# print("fu",fu)
# fcb=min(fy,(fu/1.15))
# print("fcb",fcb)




# print("__________________________________PRESSURE_____________________________")

# Pd = float(input("Enter Design Pressure : ")) 
# Pt = float(1.155*Pd)
# print("Pt",Pt)
# Plt = float(Incidental_to_Design_Pressure_Ratio_gamma_inc * Pd)
# print("Plt",Plt)
# Pe = float(((Sea_Water_Density_ρsea*Gravity_of_Acceleration_g*Depth))/1000000)
# print("Pe",Pe)

# if(Pe>0):
#     ExternalPressure = Pe
    
# else:
#     ExternalPressure = 0


# print("External Pressure : ",ExternalPressure)

# Pb_t1 = float(((2*Measured_Minimum_Thickness_for_Test_Pressure_t1)/(Outside_Diameter_OD-Measured_Minimum_Thickness_for_Test_Pressure_t1)) * fcb * 2/(math.sqrt(3)))
# print("Pb_t1",Pb_t1)

# Pmpt = float(Constant_for_Mill_Pressure_test_k * (2*Measured_Minimum_Thickness_for_Test_Pressure_t1/(Outside_Diameter_OD - Measured_Minimum_Thickness_for_Test_Pressure_t1)) * min(SMYS_σsmys * 0.96, SMTS_σsmts * 0.84))
# print(Pmpt)


# # Hydrotest Checks

# # Pressure Containment

# print("_______Pressure Containment check___________")



# if((Plt - Pe ) <= min((Pb_t1/Pressure_testFactor_gamma_m_SCPC),(Pmpt))):
#     P_check = print(" P_check : Wall thickness accepted")
# else:
#     P_check =print("  P_check : Redesign wall  thickness")


# # Utility Check

# UC_prss_cont = (Plt-Pe)/min((Pb_t1/Pressure_testFactor_gamma_m_SCPC),(Pmpt))

# print("UC_prss_cont",UC_prss_cont)