
# -*- coding: utf8 -*- 
#parameter for 2015r2
class Constant():
    PARMTYPE = "2014"
    NO_BP = 0 #无刹车
    GOP = 21   #并网发电
    GRID_OPER_NO_REDUCE = '.CON_iGridOperationNoRedu' #无限功率编号
    GRID_OPER_GEARBOX  = '.CON_iGearBoxPowerReduction'#齿轮箱限功率编号
    IP = '172.16.43.186.1.1:801'
    PATH = '.\Reports'
    #NI设备IP
    NiIP = '172.16.43.81'   
    BP_50 = 50
    #YLJ
    BP_51 = 51
    BP_100 = 100
    iPCH_HubType2 = 2
    CON_iStandby = 11
    CON_iSumPitch = 17    
class Variable():
    #叶片角度    
    test = "1"
    pitch = '.grpitchangle'
    PitchAngleBlade1 = '.grPitchAngleBlade1'
    PitchAngleBlade2 = '.grPitchAngleBlade2'
    PitchAngleBlade3 = '.grPitchAngleBlade3'
    pitch_set = '.grENVin_Blade1Setpoint'
    #扭矩
    gen_torque = '.grConverter_GeneratorTorque_Nm'
    gen_torque_set = '.grGenTorqueSetValue'
    #当前功率
    gen_power='.grGenPowerForProcess'
    gen_speedPDM1 = '.grGenSpeedPDM'
    RotorSpeedPDM = '.grRotorSpeedPDM'
    #变频器扭矩实际值
    CVT_ActualTorque = '.grConverter_GeneratorTorque_NmSetPointValue'
    #安全链复位
    safety_chain_reset = '.gbsimu_TowerSafetyChain_RESET'
    
    #版本号
    code_build_no ='.gsControlCodeBuildNo'
    
    #刹车等级
    bp_level = '.giBPLevel'
    #50号刹车
    bp_50 = '.diTargetVISU_TriggerBP50'
    
    #风机状态
    operation_mode = '.giTurbineOperationMode'
    
    #当前限功率模式
    powerredu_mode = 'PRG_PowerReduction.iPowerReductionMode'
    #一分钟平均油池温度
    temp_gear_oilsump = '.grTempGearOilSump_1min'
    #10min平均风速
    windspeed_10min = '.grWindSpeed_10min'
    windspeed_1s = '.grWindSpeed_30sec'
    WindSpeed = '.grWindSpeed'
    #齿轮箱限功率使能‘
    gearbox_repower_enbale = '.SCADA.GEARBOX.PAR.Ctrl_PAR_bEnablePowerReduByGearbox' 
    #PLC系统时间
    data_Time = '.gsDataTime'    
    #风向
    WindDirection = '.grWindDirection'
    #机舱夹角
    VaneDirection = '.grVaneDirection'
    #偏航位置
    YawPosition = '.grYawPosition'
    #机械刹车
    DI_NacelleRotorBrakeOpen = '.gbDI_NacelleRotorBrakeOpen'
    #机舱振动加速度x
    OmniDirection_PCH = '.grCurrentVibrationOmniDirection_PCH'
    #Y
    ForeaftDirection_PCH = '.grCurrentVibrationForeaftDirection_PCH'
    #电网频率
    GridFrequencyForProcess = '.grGridFrequencyForProcess'
    #电网三相电压
    UL1ForProcess = '.grUL1ForProcess'
    UL2ForProcess = '.grUL2ForProcess'
    UL3ForProcess = '.grUL3ForProcess'
    SafetyChainNacelleEmergencySTOP = '.gbDI_SafetyChainNacelleEmergencySTOP'
    NacelleCableTwist_CW_MAX2 = '.gbDI_NacelleCableTwist_CW_MAX2'
    #ylj新增
    peakAlertBlade1_PCH_Hub = '.gbPeakAlertBlade1_PCH_Hub' 
    PPAlertBlade1_PCH_Hub = '.gbPPAlertBlade1_PCH_Hub'	
    PeakAlertBlade2_PCH_Hub = '.gbPeakAlertBlade2_PCH_Hub'	
    PPAlertBlade2_PCH_Hub = '.gbPPAlertBlade2_PCH_Hub'	
    PeakAlertBlade3_PCH_Hub = '.gbPeakAlertBlade3_PCH_Hub'	
    PPAlertBlade3_PCH_Hub = '.gbPPAlertBlade3_PCH_Hub'	
    PeakDangerBlade1_PCH_Hub = '.gbPeakDangerBlade1_PCH_Hub'
    PPDangerBlade1_PCH_Hub = '.gbPPDangerBlade1_PCH_Hub'	
    PeakDangerBlade2_PCH_Hub = '.gbPeakDangerBlade2_PCH_Hub'	
    PPDangerBlade2_PCH_Hub = '.gbPPDangerBlade2_PCH_Hub'	
    PeakDangerBlade3_PCH_Hub = '.gbPeakDangerBlade3_PCH_Hub'	
    PPDangerBlade3_PCH_Hub = '.gbPPDangerBlade3_PCH_Hub' 
    FFT1_DetLevel_PCH_Hub =  '.grFFT1_DetLevel_PCH_Hub'
    FFT2_DetLevel_PCH_Hub =  '.grFFT2_DetLevel_PCH_Hub'
    gbRepeat_04_15_016 = '.gbRepeat_04_15_016'
    
    #Intern parm
    #//
    #ControlOfGenHeater:
    BlockIOPoweringUP='.gbBlockIOPoweringUP'
    TriggerBP50='.diTargetVISU_TriggerBP50'
    
    #ManualControlOfGenHeater
    FORCE_NacelleGenSpaceHeater='.diTargetVISU_FORCE_NacelleGenSpaceHeater'
    NacelleGenSpaceHeater='.gbDQ_NacelleGenSpaceHeater'
    Heater_ManualON='PRG_ControlOfGenHeater.bHeater_ManualON'
    ManualCtrl_GenHeater='.gbRelManualCtrl_GenHeater'
    #AutoControlOfGenWCSHeater:
    HeaterControlByEnvision_WCS='.PAR_bHeaterControlByEnvision_WCS'
    GenWCSTempIn_1min='.grGenWCSTempIn_1min'
    GenWCSTempOut_1min='.grGenWCSTempOut_1min'
    NumFan='PRG_ControlGENGLWCSFan.iNumFan'
    counter1='PRG_ControlGENGLWCSFan.counter1'
    counter2='PRG_ControlGENGLWCSFan.counter2'
    counter3='PRG_ControlGENGLWCSFan.counter3'
    #AutoControlOfGENGLWCSTripleValve
    ManualCtrl_GenWaterCoolValve='.gbRelManualCtrl_GenWaterCoolValve'
    #Auto control of hydraulics pump
    Selftest3_StopHydrPump='.gb_Selftest3_StopHydrPump'
    BlockPumpForYaw='.gbBlockPumpForYaw'
    UnfilHydraulicLoad='.PAR_UnfilHydraulicLoad'
    DI_UnfilHydraulicLoad='.gbDI_UnfilHydraulicLoad'
    GridFailure_UnfillHydrAccu='.gb_GridFailure_UnfillHydrAccu'
    HYDSumpLevel='.gbDI_HYDSumpLevel'
    SystemPressureSTOP_HydrPump='SIMU_Hydraulics.con_rSystemPressureSTOP_HydrPump'
    SystemPressureSTART_HydrPump='SIMU_Hydraulics.con_rSystemPressureSTART_HydrPump'
    DiskBrakeActiveAtSelftest1='.gbDiskBrakeActiveAtSelftest1'
    FORCE_NacelleHydrPump='.diTargetVISU_FORCE_NacelleHydrPump'
    Selftest3_UnfillHydrAccu='.gb_Selftest3_UnfillHydrAccu'
    #//
    
    
    #LiuFeng
    ZYD = ".CON_iConverterCoolingType2"
    GL = ".CON_iConverterCoolingType3"
    StartWCSCHeater = ".gbDQ_TowerStartWCSCHeater"
    Temp = ".grConWCSTempOut_1min"
    CON_Standby = ".CON_iStandby"
    CON_iBrakeMode50  = ".CON_iBrakeMode50"
    StartWCSC = ".gbDQ_TowerStartWCSC"
    StopWCSC = ".gbDQ_TowerStopWCSC"
    StartWCS = ".gbDQ_GLCVTWaterCool_FanStart"
    Enable_Manual = ".gbRelManualCtrl_CVTWaterCoolPump"
    CoolPump = ".diTargetVISU_FORCE_CVTWaterCoolPump"
    Temp_Open = ".PAR_rWCSCVTTripleValveOpen"
    Temp_Close = ".PAR_rWCSCVTTripleValveClose"
    Temp_1 = ".PAR_rWCSCVTHysteresisTripleValve" 
    Ethercat_OK = ".gbEthercat_OK"
    InvalidPT100_TempNacelle = ".gbInvalidPT100_TempNacelle"
    CON_iBrakeMode210 = ".CON_iBrakeMode210"
    CON_iBrakeMode200 = ".CON_iBrakeMode200"
    CON_iBrakeMode199 = ".CON_iBrakeMode199"
    CON_iBrakeMode150 = ".CON_iBrakeMode150"
    CON_iBrakeMode100 = ".CON_iBrakeMode100"
    CON_iBrakeMode51  = ".CON_iBrakeMode51"  
    TempNacelle_10min = ".grTempNacelle_10min"
    Gistate = ".gistate"
    KeySC = ".garrKeySCStr[1]"
    SC_ACTIVE = "SC_ACTIVE"
    SC_REACTIVE = "SC_REACTIVE"
    SC_PLACEHOLD = "SC_PLACEHOLD"
    HeatSinkTempPowerLimitation=".CON_iCVTHeatSinkTempPowerLimitation"
    Gen_CoilTempLow='.PAR_Gen_CoilTempLow'
    Gen_CoilTempHigh='.PAR_Gen_CoilTempHigh'
    Gen_ReducedPower='.PAR_Gen_ReducedPower'
    GeneratorPowerReduction='.CON_iGeneratorPowerReduction'
    PowerReduction='.CON_iSCADAPowerReduction'
    WindfarmControlActivePowerLastValue='.PAR_rWindfarmControlActivePowerLastValue'
    ReleaseActivePowerControl='.PAR_bReleaseActivePowerControl'
    WFMSPowerReduction='.CON_iWFMSPowerReduction'
    SafetyChain='.gbDQ_SafetyChainOpenByPLC'
    Reset_SafetyChain = ".gbDQ_SafetyChainResetByPLC"
    #51号刹车
    bp_51 =".diTargetVISU_TriggerBP51"    
    #100号刹车
    bp_100 ='.diTargetVISU_TriggerBP100'
    #150号刹车
    bp_150 ='.diTargetVISU_TriggerBP150'  
    #199号刹车
    bp_199 ='.diTargetVISU_TriggerBP199'      
    CON_iSumPitch = ".CON_iSumPitch"
    CON_iDFIG_RunUp = ".CON_iDFIG_RunUp"
    CON_iDFIG_GridOp = ".CON_iDFIG_GridOp"
    CON_iDFIG_LVRT = ".CON_iDFIG_LVRT"    
    CON_iDFIG_Trundle = ".CON_iDFIG_Trundle"
    CON_iService_ManualCtrl = ".CON_iService_ManualCtrl"
    CON_iSelftest1 = ".CON_iSelftest1"
    CON_iSelftest2 = ".CON_iSelftest2"
    CON_iSelftest3 = ".CON_iSelftest3"
    CON_iSelftest4 = ".CON_iSelftest4"    
    To_Manual = ".gbReleaseManualControl"
    Selftest_Wind_speed = ".PAR_rSelftestMaxWindspeed"
    Selftest_AfterGapTime = ".gbSelftestAfterGapTime"
    Wind_speed_1min = ".grWindSpeed_1min"
    Position = ".grsimuYawPosition"
    #shanyue
    GearOilpump='.gbRelManualCtrl_GearOilpump'
    GearOilPumpHS='.gbDQ_NacelleGearOilPumpHS'
    TempGearOilPump_HS_ON='.PAR_rTempGearOilPump_HS_ON'
    TempGearBearingNDE_1min='.grTempGearBearingNDE_1min'
    TempGearbox_BearingNDE_FanHS_ON='.PAR_rTempGearbox_BearingNDE_FanHS_ON'
    TowerLampErrorCodeActive='.gbDQ_TowerLampErrorCodeActive'
    Blade1_EndPos95Deg='.di_Blade1_EndPos95Deg'
    Blade2_EndPos95Deg='.di_Blade2_EndPos95Deg'
    Blade3_EndPos95Deg='.di_Blade3_EndPos95Deg'
    NacelleLampBypassFeatherLimitSwitch='.gbDQ_NacelleLampBypassFeatherLimitSwitch'
    TempGearbox_OilSink_FanHS_ON='.PAR_rTempGearbox_OilSink_FanHS_ON'
    NacelleGearFanHS='.gbDQ_NacelleGearFanHS'
    RelManualCtrl_GearboxFanHS='.gbRelManualCtrl_GearboxFanHS'
    TargetVISU_FORCE_NacelleGearFanLS='.diTargetVISU_FORCE_NacelleGearFanLS'
    TargetVISU_FORCE_NacelleGearFanHS='.diTargetVISU_FORCE_NacelleGearFanHS'
    NacelleGearFanLS='.gbDQ_NacelleGearFanLS'
    RelManualCtrl_GearboxFanLS='.gbRelManualCtrl_GearboxFanLS'
    RelManualCtrl_GearOilFilter='.gbRelManualCtrl_GearOilFilter'
    NacelleGearOilFilter='.gbDQ_NacelleGearOilFilter'
    GBX_OilFilter_StartTemp='.PAR_rGBX_OilFilter_StartTemp'
    GenSpeedForProcess_1min='.grGenSpeedForProcess_1min'
    GBX_OilFilter_EndTemp='.PAR_rGBX_OilFilter_EndTemp'
    TempGearOilPump_LS_ON='.PAR_rTempGearOilPump_LS_ON'
    TargetVISU_FORCE_NacelleGearOilFilter='.diTargetVISU_FORCE_NacelleGearOilFilter'
    TargetVISU_FORCE_NacelleGearOilPumpLS='.diTargetVISU_FORCE_NacelleGearOilPumpLS'
    TargetVISU_FORCE_NacelleGearOilPumpHS='.diTargetVISU_FORCE_NacelleGearOilPumpHS'
    NacelleGearOilPumpLS='.gbDQ_NacelleGearOilPumpLS'
    GenRPMSwitchPumpMode_LS='.PAR_rGenRPMSwitchPumpMode_LS'
    GenRPMSwitchPumpModeLS_OFF='.PAR_rGenRPMSwitchPumpModeLS_OFF'
    NacelleGearHeaterFan='.gbDQ_NacelleGearHeaterFan'
    RelManualCtrl_GearFanHeater='.gbRelManualCtrl_GearFanHeater'
    TargetVISU_FORCE_NacelleGearHeaterFan='.diTargetVISU_FORCE_NacelleGearHeaterFan'
    RelManualCtrl_GearOilpumpHeater='.gbRelManualCtrl_GearOilpumpHeater'
    TargetVISU_FORCE_NacelleGearHeaterOilPump='.diTargetVISU_FORCE_NacelleGearHeaterOilPump'
    RelManualCtrl_GearboxHeater='.gbRelManualCtrl_GearboxHeater'
    TargetVISU_FORCE_NacelleGearHeaterGearOil='.diTargetVISU_FORCE_NacelleGearHeaterGearOil'
    NacelleGearHeaterGearOil='.gbDQ_NacelleGearHeaterGearOil'
    ManualControlGearboxHeater='.PAR_bManualControlGearboxHeater'
    iHydraulicType='.PAR_iHydraulicType'
    RelManualCtrl_HeaterWindSensor='.gbRelManualCtrl_HeaterWindSensor'
    NacelleHeaterWindSensors='.gbDQ_NacelleHeaterWindSensors'
    TempOutdoor_1min='.grTempOutdoor_1min'
    TempWindsensors_HeaterON='.PAR_rTempWindsensors_HeaterON'
    TempCabinetTowerBase_1min='.grTempCabinetTowerBase_1min'
    TargetVISU_FORCE_NacelleHeaterWindSensors='.diTargetVISU_FORCE_NacelleHeaterWindSensors'
    bBlockofGearFan = 'PRG_ControlOfGearboxFan.bBlockForFailures'
    bBlockofGearboxHeater = 'PRG_ControlOfGearboxHeater.bBlockForFailures'
    grGenSpeedForProcess_100ms = '.grGenSpeedForProcess_100ms'
    GearboxheaterAutoON = 'PRG_ControlOfGearboxHeater.bHeater_AutoON'
    
class  Sc():    
    shutdown_lowwindspeed = '.SC_ShutDownWindspeed_10minMin'
    #ylj新增
    SC_PCH_HubBlade1_PeakAlert = '.SC_PCH_HubBlade1_PeakAlert'
    SC_PCH_HubBlade1_PeakDanger = '.SC_PCH_HubBlade1_PeakDanger'
    SC_PCH_HubBlade1_PPAlert = '.SC_PCH_HubBlade1_PPAlert'
    SC_PCH_HubBlade1_PPDanger = '.SC_PCH_HubBlade1_PPDanger'
    SC_PCH_HubBlade2_PeakAlert = '.SC_PCH_HubBlade2_PeakAlert'
    SC_PCH_HubBlade2_PeakDanger = '.SC_PCH_HubBlade2_PeakDanger'
    SC_PCH_HubBlade2_PPAlert = '.SC_PCH_HubBlade2_PPAlert'
    SC_PCH_HubBlade2_PPDanger = '.SC_PCH_HubBlade2_PPDanger'
    SC_PCH_HubBlade3_PeakAlert = '.SC_PCH_HubBlade3_PeakAlert'
    SC_PCH_HubBlade3_PeakDanger = '.SC_PCH_HubBlade3_PeakDanger'
    SC_PCH_HubBlade3_PPAlert = '.SC_PCH_HubBlade3_PPAlert'
    SC_PCH_HubBlade3_PPDanger = '.SC_PCH_HubBlade3_PPDanger'
    SC_PCH_HubFFTBlade1_Alert = '.SC_PCH_HubFFTBlade1_Alert'
    SC_PCH_HubFFTBlade1_Danger = '.SC_PCH_HubFFTBlade1_Danger'
    SC_PCH_HubFFTBlade2_Alert = '.SC_PCH_HubFFTBlade2_Alert'
    SC_PCH_HubFFTBlade2_Danger = '.SC_PCH_HubFFTBlade2_Danger'
    SC_PCH_HubFFTDangerRepeat = '.SC_PCH_HubFFTDangerRepeat'
    SC_PCH_HubBadDataDetected =  '.SC_PCH_HubBadDataDetected'
    
    SC_CableTwistMax_CW = '.SC_CableTwistMax_CW'
    SC_CableTwistMax_CCW = '.SC_CableTwistMax_CCW'
    #Intern parm
    #//
    #AutoControlOfGenHeater:
    ShutDownOutput='.OC_ShutDownOutput'
    GenWaterCoolPumpAlarm='.SC_GenWaterCoolPumpAlarm'
    NacelleFuseGenSpaceHeater='.SC_NacelleFuseGenSpaceHeater'
    TempGenStatorU_high='.SC_TempGenStatorU_high'
    TempGenStatorV_high='.SC_TempGenStatorV_high'
    TempGenStatorW_high='.SC_TempGenStatorW_high'
    FaultInputPT100_GeneratorStatorU='.SC_FaultInputPT100_GeneratorStatorU'
    FaultInputPT100_GeneratorStatorV='.SC_FaultInputPT100_GeneratorStatorV'
    FaultInputPT100_GeneratorStatorW='.SC_FaultInputPT100_GeneratorStatorW'
    #AutoControlOfGenFanExternal:
    MotorProtection_GenFanExternal='.SC_MotorProtection_GenFanExternal'
    #AutoControlOfGENGLWCSFan:
    GenWaterCoolInletTemp='.SC_GenWaterCoolInletTemp'
    GenWaterCoolInletPreHigh2='.SC_GenWaterCoolInletPreHigh2'
    GenWaterCoolInletPreLow2='.SC_GenWaterCoolInletPreLow2'
    GenWaterCoolOutletPreLow2='.SC_GenWaterCoolOutletPreLow2'
    GenWaterCoolFan1Alarm='.OC_GenWaterCoolFan1Alarm'
    #AutoControlOfGENGLWCSHeater
    GenWaterCoolInletTempHigh2='.SC_GenWaterCoolInletTempHigh2'
    GenWaterCoolHeaterOnTooLong='.SC_GenWaterCoolHeaterOnTooLong'
    GenWaterCoolInOutPressureDiffHigh='.SC_GenWaterCoolInOutPressureDiffHigh'
    #Auto control of hydraulics pump
    MotorProtection_HydrPump='.SC_MotorProtection_HydrPump'
    HydrSystemOilTemp_High='.SC_HydrSystemOilTemp_High'
    SC_MotorProtection_GearFan = '.SC_MotorProtection_GearFan'
    SC_FaultInputPT100_GearOilSump = '.SC_FaultInputPT100_GearOilSump'
    SC_FaultInputPT100_GearBearingNDE = '.SC_FaultInputPT100_GearBearingNDE'
    #//
    

class Parmeter():
    #额定转速
    rated_power = '.PAR_Gen_RatedPower'
    #额定功率
    rotor_rmp = '.PAR_rSetValueRPMatNominalPower'
    gbx_prduce_low = '.PAR_rGBXOilTempPowerReduction_Low'
    gbx_prduce_high = '.PAR_rGBXOilTempPowerReduction_High'
    #10min停机风速
    minwindspeed_10min = '.PAR_rMinWindSpeed_10min'
    #30S大风切出风速
    maxwindspped_30s = '.PAR_rMaxWindSpeed_30sec'
    #最小启动风速	
    wind_above_start = '.PAR_rWindAboveStart'
    #YLJ
    PAR_rPCH_HubFFTAlertValue = '.PAR_rPCH_HubFFTAlertValue'
    PAR_rPCH_HubFFTAlarmResetValue =  '.PAR_rPCH_HubFFTAlarmResetValue'
    PAR_rPCH_HubFFTDangerValue = '.PAR_rPCH_HubFFTDangerValue'
    PAR_rTempGearbox_HeaterON = '.PAR_rTempGearbox_HeaterON'
    PAR_rGenSpeed_GearboxHeaterON = '.PAR_rGenSpeed_GearboxHeaterON'
    PAR_rTempGearbox_Heater_OFF = '.PAR_rTempGearbox_Heater_OFF'
class Simu():
    enable_simu_allsystem ='.gbSIMU_MAIN_AllTogetherSimulation'
    #SIMU风速
    enable_simu_windspeed = '.gbsimu_FreezeWindSpeed'
    simu_windspeed = '.grsimu_setWindSpeed_1'
    #SIMU风向夹角
    enable_simu_wanedir = '.gbsimu_FreezeWaneDir'
    simu_wanedir = '.grsimu_setWaneDir_1'    
    simu_gearbox_temp = '.grsimu_TempGearOilSump'
    #ylj
    simuPeakAlertBlade1_PCH_Hub = '.gbsimuPeakAlertBlade1_PCH_Hub'
    simuPPAlertBlade1_PCH_Hub = '.gbsimuPPAlertBlade1_PCH_Hub'
    simuPeakAlertBlade2_PCH_Hub = '.gbsimuPeakAlertBlade2_PCH_Hub'
    simuPPAlertBlade2_PCH_Hub = '.gbsimuPPAlertBlade2_PCH_Hub'
    simuPeakAlertBlade3_PCH_Hub = '.gbsimuPeakAlertBlade3_PCH_Hub'
    simuPPAlertBlade3_PCH_Hub = '.gbsimuPPAlertBlade3_PCH_Hub'
    simuPeakDangerBlade1_PCH_Hub = '.gbsimuPeakDangerBlade1_PCH_Hub'
    simuPPDangerBlade1_PCH_Hub = '.gbsimuPPDangerBlade1_PCH_Hub'
    simuPeakDangerBlade2_PCH_Hub = '.gbsimuPeakDangerBlade2_PCH_Hub'
    simuPPDangerBlade2_PCH_Hub = '.gbsimuPPDangerBlade2_PCH_Hub'
    simuPeakDangerBlade3_PCH_Hub = '.gbsimuPeakDangerBlade3_PCH_Hub'
    simuPPDangerBlade3_PCH_Hub = '.gbsimuPPDangerBlade3_PCH_Hub'  
    simuFFT1_DetLevel_PCH_Hub =  '.grsimuFFT1_DetLevel_PCH_Hub'
    simuFFT2_DetLevel_PCH_Hub =  '.grsimuFFT2_DetLevel_PCH_Hub'
    simuCANPCH_Hub_ComErr = '.gbsimuCANPCH_Hub_ComErr'
    #Intern parm
    #//
    #ControlOfGenHeater:
    simu_TempGenStatorU='.grsimu_TempGenStatorU'
    simu_TempGenStatorV='.grsimu_TempGenStatorV'
    simu_TempGenStatorW='.grsimu_TempGenStatorW'
    simu_NacelleGenSpaceHeater='.DIsimu_NacelleGenSpaceHeater'
    #AutoControlOfGENGLWCSFan:
    simu_GLGenWaterCool_InletTemp='.grsimu_GLGenWaterCool_InletTemp'
    simu_GLGenWaterCool_Fan1Start='.DIsimu_GLGenWaterCool_Fan1Start'
    simu_GLGenWaterCool_Fan2Start='.DIsimu_GLGenWaterCool_Fan2Start'
    simu_GLGenWaterCool_Fan3Start='.DIsimu_GLGenWaterCool_Fan3Start'
    #AutoControlOfGENGLWCSHeater:
    simu_GLGenWaterCool_HeaterStart='.DIsimu_GLGenWaterCool_HeaterStart'
    simu_GLGenWaterCool_PumpOn='.DQsimu_GLGenWaterCool_PumpOn'
    #ManualControlOfGENGLWCS
    simu_GLGenWaterCool_ValveClose='.DQsimu_GLGenWaterCool_ValveClose' 
    #Auto control of hydraulics pump
    simu_NacelleHydrPump='.DIsimu_NacelleHydrPump'
    simu_SafetyChainNacelleWECinServiceGeneral='.gbsimu_SafetyChainNacelleWECinServiceGeneral'
    simu_SafetyChainNacelleEmergencySTOP='.gbsimu_SafetyChainNacelleEmergencySTOP'
    simu_TowerSafetyChainTowerEmergencySTOP='.gbsimu_TowerSafetyChainTowerEmergencySTOP'
    #ManualControlOfRotorBrake
    simu_SafetyChainNacelleEmergencySTOP='.gbsimu_SafetyChainNacelleEmergencySTOP'
    simu_NacelleValve1RotorBrakeON_sudden='.DIsimu_NacelleValve1RotorBrakeON_sudden'
    simu_NacelleValve2RotorBrakeON_dimmed='.DIsimu_NacelleValve2RotorBrakeON_dimmed'
    simu_NacelleValve3RotorBrakeOFF_sudden='.DIsimu_NacelleValve3RotorBrakeOFF_sudden'
    simu_NacelleValve4RotorBrakeOFF_dimmed='.DIsimu_NacelleValve4RotorBrakeOFF_dimmed'
    simu_Gen1RotorBrake1='.DIsimu_Gen1RotorBrake1'
    simu_Gen1RotorBrake2='.DIsimu_Gen1RotorBrake2'
    simu_NacelleCloseRotorBrakeManual='.gbsimu_NacelleCloseRotorBrakeManual'
    simu_NacelleWECinServiceManualPitc='.gbsimu_NacelleWECinServiceManualPitch'
    simu_TowerSafetyChainWECinService='.gbsimu_TowerSafetyChainWECinService'
    simu_TowerWECinRepairMode='.gbsimu_TowerWECinRepairMode'
    simu_UnfilHydraulicLoad='.gbsimu_UnfilHydraulicLoad'
    simu_GridOK_ExternalDevice='.gbsimu_GridOK_ExternalDevice'
    #//
     
    #LiuFeng
    simudiConverter_HeatingMode = ".simudiConverter_HeatingMode"
    Pump = ".DQsimu_GLCVTWaterCool_PumpOn" 
    simuConverter_TempHeatSink=".grsimuConverter_TempHeatSink"
    EtherCAT = ".gbsimu_EtherCAT_OK"
    SC_Enable = ".gbsimu_SafetyChainNacelleRelayOverspeed"
    LVRT_Enable = ".simudiConverter_LowVoltageForRideThrough"
    CW = ".gbsimu_YawCW"
    CCW = ".gbsimu_YawCCW"
    #shanyue
    simu_TempGearOiSump='.grsimu_TempGearOiSump'
    simu_TowerLampTest='.gbsimu_TowerLampTest'
    simu_NacelleLampTest='.gbsimu_NacelleLampTest'
    simu_Blade1_EndPos95Deg='.gbsimu_Blade1_EndPos95Deg'
    simu_Blade2_EndPos95Deg='.gbsimu_Blade2_EndPos95Deg'
    simu_Blade3_EndPos95Deg='.gbsimu_Blade3_EndPos95Deg'
    simu_TempOutdoor='.grsimu_TempOutdoor'
    
    
    
    
class Scada():
    #2015r1及之前版本限功率接口
    PowerLimitFromSCADA='.SCADA.GridValues.PAR.Ctrl_PAR_PowerLimitFromSCADA'
    #2015r2版本限功率接口
    PowerLimitFromSCADA='.SCADA.StateMachine.PAR.Ctrl_Par_powerlimitfromscada'
    PAR_iPCH_HubType = '.SCADA.MeasurementSystem.PAR.Ctrl_PAR_iPCH_HubType'
    #SCADA接口 10min停机风速
    scada_minwindspeed_10min = '.SCADA.Meteorology.PAR.Ctrl_PAR_rMinWindSpeed_10min'
    scada_HubEnableBadDataDetect = '.SCADA.MeasurementSystem.PAR.Ctrl_PAR_bPCH_HubEnableBadDataDetect'
    #齿轮箱限功率使能
    gearbox_repower_enbale = '.SCADA.GEARBOX.PAR.Ctrl_PAR_bEnablePowerReduByGearbox'  
    
    
    #Intern parm
    #//
    #ManualControlOfGenHeater
    PAR_bManualControlGenHeater='.SCADA.Generator.PAR.Ctrl_PAR_bManualControlGenHeater'
    #AutoControlOfGENGLWCSFan:
    GenCoolSysType='.SCADA.Generator.PAR.Ctrl_PAR_iGenCoolSysType' 
    #Auto control of hydraulics pump
    HydrPumpControlledBySwitch='.SCADA.Hydraulics.PAR.Ctrl_PAR_bHydrPumpControlledBySwitch'
    SystemPressureMainCircuitSTART_HydrPump='.SCADA.Hydraulics.PAR.Ctrl_PAR_rSystemPressureMainCircuitSTART_HydrPump'
    SystemPressureMainCircuitSTOP_HydrPump='.SCADA.Hydraulics.PAR.Ctrl_PAR_rSystemPressureMainCircuitSTOP_HydrPump'
    GenSpeedBelowMainBrakeON='.SCADA.Generator.PAR.Ctrl_PAR_rGenSpeedBelowMainBrakeON'
    SystemPressureStart_HydrPump='.SCADA.Hydraulics.PAR.Ctrl_PAR_rSystemPressureStart_HydrPump'
    SystemPressureStop_HydrPump='.SCADA.Hydraulics.PAR.Ctrl_PAR_rSystemPressureStop_HydrPump'
    HydraulicType='.SCADA.Hydraulics.PAR.Ctrl_PAR_iHydraulicType'
    #ManualControlOfRotorBrake
    GenSpeedEnableRotorBrake='.SCADA.Generator.PAR.Ctrl_PAR_rGenSpeedEnableRotorBrake'
    UnfilHydraulicLoad='.SCADA.Hydraulics.PAR.Ctrl_PAR_UnfilHydraulicLoad'
    EnableBoxTransSignalMonitor='.SCADA.others.PAR.Ctrl_PAR_bEnableBoxTransSignalMonitor'
    #//

    #LiuFeng
    ConverterType = ".SCADA.Converter.PAR.Ctrl_PAR_iConverterType"
    ConverterCoolingType = ".SCADA.Converter.PAR.Ctrl_PAR_iConverterCoolingType"
    MotorProtection_WCSC_todisable = ".SCADA.Converter.SC.SC_MotorProtection_WCSC_todisable"
    FaultPofibusWCSC_todisable = ".SCADA.Converter.SC.SC_FaultPofibusWCSC_todisable"
    Temp_ON = ".SCADA.Converter.PAR.Ctrl_PAR_rTempWCSOfCon_HeaterON"
    Temp_Off = ".SCADA.Converter.PAR.Ctrl_PAR_rTempWCSOfCon_HeaterOFF"
    Temp_MIN_Par = ".SCADA.Nacelle.PAR.Ctrl_PAR_rTempMIN_Nacelle"
    MainShaftType = ".SCADA.Nacelle.PAR.Ctrl_PAR_iMainShaftType"
    SC_165_1_Enable = ".SCADA.Gearbox.PAR.Ctrl_PAR_rTempHigh_GearOilSump" 
    SC_165_2_Enable =".SCADA.Gearbox.PAR.Ctrl_PAR_rTempHigh_GearOilInlet"
    SC_175_Enable = ".SCADA.Gearbox.PAR.Ctrl_PAR_rTempMAX_GearOilSump"
    GenCoilTempPowerLimitEnable='.SCADA.Generator.PAR.Ctrl_PAR_bGenCoilTempPowerLimitEnable'
    PitchMoveLimit='.SCADA.Pitchsystem.PAR.Ctrl_PAR_rPitchMoveLimit'
    
    WindfarmControlEnable='.SCADA.WFMS.PAR.Ctrl_PAR_bWindfarmControlEnable'
    Force = ".SCADA.Safetychain.PAR.Ctrl_PAR_bForceRemoteResetSafetyChain"
    GearboxRatio='.SCADA.Gearbox.PAR.Ctrl_PAR_rGearboxRatio'
    GenOverSpeedLevel3='.SCADA.Generator.PAR.Ctrl_PAR_rGenOverSpeedLevel3'
    PitchAngleMin_DFIG_RunUp='.SCADA.STATEMACHINE.PAR.Ctrl_PAR_rPitchAngleMin_DFIG_RunUp'
    Disable_SC_1 = ".SCADA.Meteorology.SC.SC_WindTooSmallDetectedByRotor_todisable" 
    Disable_SC_2 = ".SCADA.Meteorology.SC.SC_ConstantSignalAnemometer1_todisable"
    Trundle_1 = ".SCADA.GENERATOR.PAR.Ctrl_PAR_rShutDownSlowForLowPower"
    Trundle_Time = ".SCADA.StateMachine.PAR.Ctrl_PAR_tSpeedSteady_DFIG_RunUp"
    Selftest_Enable = ".SCADA.operation.PAR.Ctrl_PAR_bEnableSelfTest"
    #shanyue
    ManualControlGearOilpump='.SCADA.Gearbox.PAR.Ctrl_PAR_bManualControlGearOilpump'
    ManualControlGearboxFanLS='.SCADA.Gearbox.PAR.Ctrl_PAR_bManualControlGearboxFanLS'
    ManualControlGearboxFanHS='.SCADA.Gearbox.PAR.Ctrl_PAR_bManualControlGearboxFanHS'
    ManualControlGearOilFilter='.SCADA.Gearbox.PAR.Ctrl_PAR_bManualControlGearOilFilter'
    ManualControlHeaterGearOilFilter='.SCADA.Gearbox.PAR.Ctrl_PAR_bManualControlHeaterGearOilFilter'
    ManualControlHeaterGearboxFan='.SCADA.Gearbox.PAR.Ctrl_PAR_bManualControlHeaterGearboxFan'
    ManualControlGearOilpumpHeater='.SCADA.Gearbox.PAR.Ctrl_PAR_bManualControlGearOilpumpHeater'
    ManualControlGearboxHeater='.SCADA.Gearbox.PAR.Ctrl_PAR_bManualControlGearboxHeater'
    ManualControlHeaterWindSensor='.SCADA.Meteorology.PAR.Ctrl_PAR_bManualControlHeaterWindSensor'
	
Basis_varlist = []
Basis_varlist.append(Variable.data_Time)
Basis_varlist.append(Variable.gen_speedPDM1)
Basis_varlist.append(Variable.gen_power)
Basis_varlist.append(Variable.pitch)
Basis_varlist.append(Variable.pitch_set)
Basis_varlist.append(Variable.operation_mode)
Basis_varlist.append(Variable.CVT_ActualTorque)
Basis_varlist.append(Variable.bp_level)
Basis_varlist.append(Variable.Gistate)

test_varlist = []
test_varlist.append(Variable.data_Time)
#风机状态
test_varlist.append(Variable.operation_mode)
#风速
test_varlist.append(Variable.WindSpeed)
#风向
test_varlist.append(Variable.WindDirection)
#发电机转速
test_varlist.append(Variable.gen_speedPDM1)
#风轮转速
test_varlist.append(Variable.RotorSpeedPDM)
#功率
test_varlist.append(Variable.gen_power)
#扭矩
test_varlist.append(Variable.gen_torque)
#变桨角度
test_varlist.append(Variable.PitchAngleBlade1)
test_varlist.append(Variable.PitchAngleBlade2)
test_varlist.append(Variable.PitchAngleBlade3)
#机舱夹角
test_varlist.append(Variable.VaneDirection)
#偏航位置
test_varlist.append(Variable.YawPosition)
#机械刹车动作
test_varlist.append(Variable.DI_NacelleRotorBrakeOpen)
#机舱振动加速度X
test_varlist.append(Variable.OmniDirection_PCH)
#机舱振动加速度Y
test_varlist.append(Variable.ForeaftDirection_PCH)
#电网电压
test_varlist.append(Variable.UL1ForProcess)
test_varlist.append(Variable.UL2ForProcess)
test_varlist.append(Variable.UL3ForProcess)
#电网频率
test_varlist.append(Variable.GridFrequencyForProcess)
