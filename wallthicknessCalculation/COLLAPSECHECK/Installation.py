from ast import Str
from cmath import sqrt
import math
from cgitb import small
from unittest import result
import numpy as np  
import numpy.polynomial.polynomial  as roots


def collapse_installation(Outside_Diameter_OD, Nominal_Wall_Thickness_tnom, Fabrication_Thickness_Tolerance_tfab, Corrosion_Allowance_tcorr, Ovality_of_Pipe_Oo,SMYS_σsmys,SMTS_σsmts,Derating_value_temp_yieldStress_fy_temp,Derating_value_temp_tensileStress_fu_temp,Youngs_Modulus_E ,Poission_s_Ratio_ν ,Maximum_Fabrication_Factor_alpha_fab,Pd,Pmin,Elevation_at_Pressure_Reference_Level_href,Elevation_level_at_Pressure_Point_hl ,Product_Density_ρcont,Hydrotest_Water_Density_ρt,Incidental_to_Design_Pressure_Ratio_gamma_inc,Water_Depth_WD,Sea_Water_Density_ρsea,Max_Elevation_wrt_MSL_hmax,Safety_Class_RF_gamma_SCLB,Mill_Pressure_Test_Factor_alpha_mpt,Material_Strength_Factor_alpha_u,Material_resistant_factor_gamma_m,System_Pressure_Test_Factor_alpha_spt):
    # return print("Collapsecheck Installation..!!!")
        
        # Material_Strength_Factor_alpha_u = 1
        Gravity_of_Acceleration_g = 9.81
        # Pressure_testFactor_gamma_SC_LB = 1.04
        # Pressure_testFactor_gamma_m = 1.15
        ρemp = 0

        Outside_Diameter_OD = float(Outside_Diameter_OD) 
        # print(Outside_Diameter_OD) 
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
        Max_Elevation_wrt_MSL_hmax = float(Max_Elevation_wrt_MSL_hmax)
        # print("hmin ",Min_Elevation_wrt_MSL_hmin)

        Safety_Class_RF_gamma_SCLB = float(Safety_Class_RF_gamma_SCLB) 
        # print("gamma_SCPC ",Safety_Class_RF_gamma_SCPC)
        
        Mill_Pressure_Test_Factor_alpha_mpt = float(Mill_Pressure_Test_Factor_alpha_mpt) 

        System_Pressure_Test_Factor_alpha_spt = float(System_Pressure_Test_Factor_alpha_spt)


        # print("___________________PIPELINE INPUTS___________________")

        Measured_Minimum_Thickness_for_Test_Pressure_t1 = (Nominal_Wall_Thickness_tnom - Fabrication_Thickness_Tolerance_tfab - Corrosion_Allowance_tcorr)
        print(f"Measured Minimum Thickness for Test Pressure : {Measured_Minimum_Thickness_for_Test_Pressure_t1}")


        # print("___________________________ENVIRONMENTAL INPUTS______________________________")

        # print("\n\t****...Environmental Data....****")

        Depth = float(Water_Depth_WD + Max_Elevation_wrt_MSL_hmax)
        print(Depth)

     

        # print("_____________________________DESIGNS FACTOR AS PER DNGVL____________________")

        # print("\n\tSAFETY CLASS : 'Low'")


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
        Pinc = float(Incidental_to_Design_Pressure_Ratio_gamma_inc*Pd)
        print(Pinc)
        # ρemp = float(input("Enter Design for empty state : ")) 
        Pli = float(Pinc-(ρemp*Gravity_of_Acceleration_g*(Elevation_level_at_Pressure_Point_hl-Elevation_at_Pressure_Reference_Level_href)))
        print("Pli",Pli)
        Pe = float(((Sea_Water_Density_ρsea*Gravity_of_Acceleration_g*Depth))/1000000)
        print("Pe",Pe)
        Pb_t1 = float(((2*Measured_Minimum_Thickness_for_Test_Pressure_t1)/(Outside_Diameter_OD-Measured_Minimum_Thickness_for_Test_Pressure_t1)) * fcb * 2/(math.sqrt(3)))
        print("Pb_t1",Pb_t1)
        Pt = float(1.25*Pd)
        print("Pt",Pt)
        Plt = float(Pt-((Hydrotest_Water_Density_ρt*Gravity_of_Acceleration_g*(Elevation_level_at_Pressure_Point_hl-Elevation_at_Pressure_Reference_Level_href))/10**6))
        print("Plt",Plt)
        # Pmpt = float(Constant_for_Mill_Pressure_test_k*((2*Measured_Minimum_Thickness_for_Test_Pressure_t1)/(Outside_Diameter_OD-Measured_Minimum_Thickness_for_Test_Pressure_t1))*min(SMYS_σsmys*0.96,SMTS_σsmts*0.84))
        # print(Pmpt)



        # print("_______EXTERNAL PRESSURE COLLAPSE CHECK___________")
        # Pmin = float(input("Enter Minimum Internal pressure : "))
        γSC_LB = Safety_Class_RF_gamma_SCLB

        System_Collapse_Check_Pc_ti  = 8.7

        # (Pe <= Pb_t1/(Pressure_testFactor_gamma_m*γSC_LB))

        Pel_t =  float(2*Youngs_Modulus_E*((Measured_Minimum_Thickness_for_Test_Pressure_t1/Outside_Diameter_OD)**3))/(1-Poission_s_Ratio_ν**2)
        print(Pel_t)
        Pp_t = float(fy*Maximum_Fabrication_Factor_alpha_fab*2*(Measured_Minimum_Thickness_for_Test_Pressure_t1/Outside_Diameter_OD))
        print(Pp_t)

        Ovality_Oo = 0.02

        # [System_Collapse_Check_Pc_ti-Pel_t][(System_Collapse_Check_Pc_ti)**2-Pp_t]
        Collapse_Pressure_y1 = float(Pel_t*Pp_t*Ovality_of_Pipe_Oo*(Outside_Diameter_OD/Measured_Minimum_Thickness_for_Test_Pressure_t1))
        print("Collapse_Pressure_y1",Collapse_Pressure_y1)

        Collapse_Pressure_Pp_t_sq = float((Pp_t)**2)
        print("Collapse_Pressure_Pp_t_sq",Collapse_Pressure_Pp_t_sq)

        Collapse_Pressure_y2 = float(Pel_t*Collapse_Pressure_Pp_t_sq)
        print("Collapse_Pressure_y2",Collapse_Pressure_y2)

        s = (Collapse_Pressure_y2,-(Collapse_Pressure_Pp_t_sq+Collapse_Pressure_y1), -Pel_t,1)

        smallNumber = []

        result = roots.polyroots(s)
        print("result",result.real)

        for positiveNum_1 in result:
            if positiveNum_1 >= 0:
                print(positiveNum_1)
                smallNumber.append(positiveNum_1)
            else:
                print("negative number")
        print(smallNumber)
        print(min(smallNumber))

        Pc_t1_1 = result[0]
        Pc_t1_2 = result[1]
        Pc_t1_3 = result[2]
        print(Pc_t1_1,Pc_t1_2,Pc_t1_3)

        Collapse_Pressure_result_1 = float(Pc_t1_1/(Material_resistant_factor_gamma_m*γSC_LB))
        print(Collapse_Pressure_result_1)

        Collapse_Pressure_result_2 = float(Pc_t1_2/(Material_resistant_factor_gamma_m*γSC_LB))
        print(Collapse_Pressure_result_2)

        Collapse_Pressure_result_3 = float(Pc_t1_3/(Material_resistant_factor_gamma_m*γSC_LB))
        print(Collapse_Pressure_result_3)

        Collapse_Pressure_result_list = []
        smallNumber_2  = []
        Collapse_Pressure_result_list.append(Collapse_Pressure_result_1)
        Collapse_Pressure_result_list.append(Collapse_Pressure_result_2)
        Collapse_Pressure_result_list.append(Collapse_Pressure_result_3)
        print("Collapse_Pressure_result_list" , Collapse_Pressure_result_list)


        for positiveNum_2 in Collapse_Pressure_result_list:
            if positiveNum_2 >= 0:
                print(positiveNum_2)
                smallNumber_2.append(positiveNum_2)
            else:
                print("negative number")
        print(smallNumber_2)
        Pc_t1_at_γm_γSC_LB = min(smallNumber_2)
        print(min(smallNumber_2))


        if(Pe-Pmin <= min(smallNumber_2)/(Material_resistant_factor_gamma_m*γSC_LB)):

            Pel_t =  float(2*Youngs_Modulus_E*((Measured_Minimum_Thickness_for_Test_Pressure_t1/Outside_Diameter_OD)**3))/(1-Poission_s_Ratio_ν**2)
            print(Pel_t)
            Pp_t = float(fy*Maximum_Fabrication_Factor_alpha_fab*2*(Measured_Minimum_Thickness_for_Test_Pressure_t1/Outside_Diameter_OD))
            print(Pp_t)

        else :
            print("External Pressure criteria not fulfilled")



        # # __________________________________________



        # #  Utility Check in externakl pressure  Collapse check

        UC_coll = float(Pe/Pc_t1_at_γm_γSC_LB)
        print("UC_coll" , UC_coll)

        # Collapse Check 

        if(Pe <= Pc_t1_at_γm_γSC_LB ):
            print("Wall Thickness Accepted")

        else:
            print("Redesign Wall Thickness")

        # ____________Propagation Buckling Check___________________

        # ++++++++++++++++++++ Using DNGVL - ST - F101 ++++++++++++++++++

        print("_____________Propagation Buckling Check___________________")

        # Propagating Buckling Criteria

        D = Outside_Diameter_OD
        t2 = float(Nominal_Wall_Thickness_tnom-Corrosion_Allowance_tcorr)
        print("t2",t2)
        Effective_wall_Thickness_Ppr_t2 = 35*fy*Maximum_Fabrication_Factor_alpha_fab*((t2/Outside_Diameter_OD)**2.5)
        print("Effective_wall_Thickness_Ppr_t2",Effective_wall_Thickness_Ppr_t2)
        # if(Pe - Pmin <= Effective_wall_Thickness_Ppr_t2/Pressure_testFactor_gamma_m*γSC_LB):
        #     print("Effective_wall_Thickness_Ppr_t2")
        # else:
        #     print("External Pressure Exceeds")

        D_upon_t2 = float(D/t2)
        print("D_upon_t2",D_upon_t2)


        # Utility Check
        UC_buck = float(Pe/(Effective_wall_Thickness_Ppr_t2/(1.15*1.14)))
        print("UC_buck",UC_buck)

        # PBuckle
        if(Pe <= Effective_wall_Thickness_Ppr_t2/(Material_resistant_factor_gamma_m*γSC_LB)):
            print("Wall Thickness Accepted")
        else:
            print("Redesign Wall Thickness, considering" ,t2, "mm thickness")

