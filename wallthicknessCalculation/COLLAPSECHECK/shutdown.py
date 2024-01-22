from ast import Str
from cmath import sqrt
import math
from cgitb import small
from unittest import result
import numpy as np  
import numpy.polynomial.polynomial  as roots


def collapse_shutdown():
    return print("Collapsecheck shutdown..!!!")

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
# Fabrication_Thickness_Tolerance_tfab =float(input("Enter Fabrication Thickness Tolerance : "))
# print(Fabrication_Thickness_Tolerance_tfab)
# Nominal_Wall_Thickness_tnom =float(input("Enter Nominal wall thickness : "))
# print(Nominal_Wall_Thickness_tnom)
# Measured_Minimum_Thickness_for_Test_Pressure_t1 = (Nominal_Wall_Thickness_tnom - Fabrication_Thickness_Tolerance_tfab - Corrosion_Allowance_tcorr)
# print(f"Measured Minimum Thickness for Test Pressure : {Measured_Minimum_Thickness_for_Test_Pressure_t1}")






# print("___________________________ENVIRONMENTAL INPUTS______________________________")

# print("\n\t****...Environmental Data....****")

# Sea_Water_Density_ρsea =float(input("Enter Sea Water Density : "))
# Max_Water_Depth_WDmax =float(input("Enter Maximum water Depth : "))
# # Min_Water_Depth_WDmin =float(input("Enter Minimum Water Depth : "))
# Max_Elevation_wrt_MSL_hmax =float(input("Enter Maximum elevation wrt MSL : "))
# # Highest_Astronomical_Tide_HAT =float(input("Enter Highest Astronomical Tide : "))

# Depth = float(Max_Water_Depth_WDmax + Max_Elevation_wrt_MSL_hmax)
# print(Depth)

# Lowest_Astronomical_Tide_LAT =float(input("Enter Lowest Astronomical Tide : "))
# Max_Wave_Height_Hmax =float(input("Enter Maximum Wave Height Hmax : "))
# Gravity_of_Acceleration_g =float(input("Enter Gravity of Acceleration : "))



# Elevation_level_at_Pressure_Point_hl =float(input("Enter Elevation level at Pressure Point : "))
# # Elevation level at pressure point  = Maximum water depth + Jetti Height + Barrel Height..
# Elevation_at_Pressure_Reference_Level_href =float(input("Enter Elevated at pressure level : "))
# Density_of_relevant_test_medium_ρt =float(input("Enter Density of relevant test medium :"))



# print(Sea_Water_Density_ρsea)
# print(Max_Water_Depth_WDmax)
# # print(Min_Water_Depth_WDmin)
# # print(Highest_Astronomical_Tide_HAT)
# print(Lowest_Astronomical_Tide_LAT)
# print(Max_Wave_Height_Hmax)
# print(Gravity_of_Acceleration_g)
# print(Elevation_level_at_Pressure_Point_hl)
# print(Elevation_at_Pressure_Reference_Level_href)
# print(Elevation_level_at_Pressure_Point_hl)

# print("_____________________________DESIGNS FACTOR AS PER DNGVL____________________")

# print("\n\tSAFETY CLASS : 'Medium'")

# Derating_value_temp_yieldStress_fy_temp =float(input("Enter Derating value due to temperature of yield Stress : "))
# Derating_value_temp_tensileStress_fu_temp =float(input("Enter Derating value due to temperature of tensile Stress : "))
# Pressure_testFactor_alpha_mpt =float(input("Enter Pressure Test Factor for Alpha mpt : "))
# Pressure_testFactor_alpha_spt =float(input("Enter Pressure Test Factor for Alpha spt : "))
# Pressure_testFactor_gamma_m =float(input("Enter Pressure Test Factor for Gamma m : "))
# Pressure_testFactor_gamma_SC_LB =float(input("Enter Pressure Test Factor for Gamma SC.LB : "))
# Pressure_testFactor_gamma_m_SCLB = Pressure_testFactor_gamma_m * Pressure_testFactor_gamma_SC_LB
# Incidental_to_Design_Pressure_Ratio_gamma_inc =float(input("Enter Incidental to design pressure ratio : "))
# Material_Strength_Factor_alpha_u =float(input("Enter Material Strength factor : "))
# Maximum_Fabrication_Factor_alpha_fab =float(input("Enter Maximum Fabrication Factor : "))
# Constant_for_Mill_Pressure_test_k =float(input("Enter Constant for Mill Pressure Task : "))

# print(Derating_value_temp_yieldStress_fy_temp)
# print(Derating_value_temp_tensileStress_fu_temp)
# print(Pressure_testFactor_alpha_mpt)
# print(Pressure_testFactor_alpha_spt)
# print(Pressure_testFactor_gamma_m)
# print(Pressure_testFactor_gamma_SC_LB)
# print("Pressure_testFactor_gamma_m_SCLB",Pressure_testFactor_gamma_m_SCLB)
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

# Pd = float(input("Enter Design Pressure Pd: ")) 
# Pinc = float(Incidental_to_Design_Pressure_Ratio_gamma_inc * Pd)
# print(Pinc)

# # ρemp = float(input("Enter Design for empty state : ")) 
# Pli = float(Pinc-(Product_Density_ρcont*Gravity_of_Acceleration_g*(Elevation_level_at_Pressure_Point_hl-Elevation_at_Pressure_Reference_Level_href)))
# print("Pli",Pli)
# Pe = float(((Sea_Water_Density_ρsea*Gravity_of_Acceleration_g*Depth))/1000000)
# print("Pe",Pe)
# # Pb_t1 = float((2*Measured_Minimum_Thickness_for_Test_Pressure_t1)/(Outside_Diameter_OD-Measured_Minimum_Thickness_for_Test_Pressure_t1) * fcb * 2/(math.sqrt(3)))
# # print("Pb_t1",Pb_t1)
# Pt = float(1.155*Pd)
# print("Pt",Pt)
# Plt = float(Pt-((Density_of_relevant_test_medium_ρt*Gravity_of_Acceleration_g*(Elevation_level_at_Pressure_Point_hl-Elevation_at_Pressure_Reference_Level_href))/10**6))
# print("Plt",Plt)
# # Pmpt = float(Constant_for_Mill_Pressure_test_k*((2*Measured_Minimum_Thickness_for_Test_Pressure_t1)/(Outside_Diameter_OD-Measured_Minimum_Thickness_for_Test_Pressure_t1))*min(SMYS_σsmys*0.96,SMTS_σsmts*0.84))
# # print(Pmpt)



# #Section A : SHUT DOWN CHECKS
# print("------------SHUT DOWN CHECK--------------")
# t1 = float(Nominal_Wall_Thickness_tnom - Fabrication_Thickness_Tolerance_tfab - Corrosion_Allowance_tcorr)
# print("t1",t1)

# t2 = float(Nominal_Wall_Thickness_tnom - Corrosion_Allowance_tcorr)
# print("t2", t2)


# print("_______EXTERNAL PRESSURE COLLAPSE CHECK___________")
# Pmin = float(input("Enter Minimum Internal pressure : "))
# γSC_LB = Pressure_testFactor_gamma_SC_LB

# # System_Collapse_Check_Pc_ti  = 8.7

# # (Pe <= Pb_t1/(Pressure_testFactor_gamma_m*γSC_LB))

# Pel_t1 =  float(2*Youngs_Modulus_E*((Measured_Minimum_Thickness_for_Test_Pressure_t1/Outside_Diameter_OD)**3))/(1-Poission_s_Ratio_ν**2)
# print("Pel_t1",Pel_t1)

# Pp_t1 = float(fy*Maximum_Fabrication_Factor_alpha_fab*2*(Measured_Minimum_Thickness_for_Test_Pressure_t1/Outside_Diameter_OD))
# print("Pp_t1",Pp_t1)

# # Ovality_Oo = 0.02

# # [System_Collapse_Check_Pc_ti-Pel_t][(System_Collapse_Check_Pc_ti)**2-Pp_t]
# Collapse_Pressure_y1 = float(Pel_t1*Pp_t1*Ovality_of_Pipe_Oo*(Outside_Diameter_OD/t2))
# print("Collapse_Pressure_y1",Collapse_Pressure_y1)

# Collapse_Pressure_Pp_t_sq = float((Pp_t1)**2)
# print("Collapse_Pressure_Pp_t_sq",Collapse_Pressure_Pp_t_sq)

# Collapse_Pressure_y2 = float(Pel_t1*Collapse_Pressure_Pp_t_sq)
# print("Collapse_Pressure_y2",Collapse_Pressure_y2)

# s = (Collapse_Pressure_y2,-(Collapse_Pressure_Pp_t_sq+Collapse_Pressure_y1), -Pel_t1,1)

# smallNumber = []

# result = roots.polyroots(s)
# print("result",result.real)

# for positiveNum_1 in result:
#     if positiveNum_1 >= 0:
#         print(positiveNum_1)
#         smallNumber.append(positiveNum_1)
#     else:
#         print("negative number")
# print(smallNumber)
# print(min(smallNumber))

# Pc_t1_1 = result[0]
# Pc_t1_2 = result[1]
# Pc_t1_3 = result[2]
# print(Pc_t1_1,Pc_t1_2,Pc_t1_3)

# Collapse_Pressure_result_1 = float(Pc_t1_1/(Pressure_testFactor_gamma_m*γSC_LB))
# print(Collapse_Pressure_result_1)

# Collapse_Pressure_result_2 = float(Pc_t1_2/(Pressure_testFactor_gamma_m*γSC_LB))
# print(Collapse_Pressure_result_2)

# Collapse_Pressure_result_3 = float(Pc_t1_3/(Pressure_testFactor_gamma_m*γSC_LB))
# print(Collapse_Pressure_result_3)

# Collapse_Pressure_result_list = []
# smallNumber_2  = []
# Collapse_Pressure_result_list.append(Collapse_Pressure_result_1)
# Collapse_Pressure_result_list.append(Collapse_Pressure_result_2)
# Collapse_Pressure_result_list.append(Collapse_Pressure_result_3)
# print("Collapse_Pressure_result_list" , Collapse_Pressure_result_list)


# for positiveNum_2 in Collapse_Pressure_result_list:
#     if positiveNum_2 >= 0:
#         print(positiveNum_2)
#         smallNumber_2.append(positiveNum_2)
#     else:
#         print("negative number")
# print(smallNumber_2)
# Pc_t1_at_γm_γSC_LB = min(smallNumber_2)
# print(min(smallNumber_2))


# if(Pe-Pmin <= min(smallNumber_2)/(Pressure_testFactor_gamma_m*γSC_LB)):

#     Pel_t =  float(2*Youngs_Modulus_E*((Measured_Minimum_Thickness_for_Test_Pressure_t1/Outside_Diameter_OD)**3))/(1-Poission_s_Ratio_ν**2)
#     print(Pel_t)
#     Pp_t = float(fy*Maximum_Fabrication_Factor_alpha_fab*2*(Measured_Minimum_Thickness_for_Test_Pressure_t1/Outside_Diameter_OD))
#     print(Pp_t)

# else :
#     print("External Pressure criteria not fulfilled")



# # __________________________________________



# #  Utility Check in externakl pressure  Collapse check

# UC_coll = float(Pe/Pc_t1_at_γm_γSC_LB)
# print("UC_coll" , UC_coll)

# # Collapse Check 

# if(Pe <= Pc_t1_at_γm_γSC_LB ):
#     print("Wall Thickness Accepted")

# else:
#     print("Redesign Wall Thickness")

# # ____________Propagation Buckling Check___________________

# # ++++++++++++++++++++ Using DNGVL - ST - F101 ++++++++++++++++++

# print("_____________Propagation Buckling Check___________________")

# # Propagating Buckling Criteria

# D = Outside_Diameter_OD
# t2 = float(Nominal_Wall_Thickness_tnom-Corrosion_Allowance_tcorr)
# print("t2",t2)
# Effective_wall_Thickness_Ppr_t2 = 35*fy*Maximum_Fabrication_Factor_alpha_fab*((t2/Outside_Diameter_OD)**2.5)
# print("Effective_wall_Thickness_Ppr_t2",Effective_wall_Thickness_Ppr_t2)
# # if(Pe - Pmin <= Effective_wall_Thickness_Ppr_t2/Pressure_testFactor_gamma_m*γSC_LB):
# #     print("Effective_wall_Thickness_Ppr_t2")
# # else:
# #     print("External Pressure Exceeds")

# D_upon_t2 = float(D/t2)
# print("D_upon_t2",D_upon_t2)


#     # Utility Check
# UC_buck = float(Pe/(Effective_wall_Thickness_Ppr_t2/(1.15*1.14)))
# print("UC_buck",UC_buck)

# # PBuckle
# if(Pe <= Effective_wall_Thickness_Ppr_t2/(Pressure_testFactor_gamma_m*γSC_LB)):
#     print("Wall Thickness Accepted")
# else:
#     print("Redesign Wall Thickness, considering" ,t2, "mm thickness")


