
# -*- coding: utf8 -*- 
#parameter for SC-1

class Constant():
    PARMTYPE = "SC1"
    #无刹车
    NO_BP = 0
    #50号刹车
    BP_50 = 50
    #51号刹车
    BP_51 = 51
    #并网发电
    GOP = '.CON_iCAGE_GridOp'  
     #无限功率编号
    GRID_OPER_NO_REDUCE = '.CON_iGridOperationNoRedu'
    #齿轮箱限功率编号
    GRID_OPER_GEARBOX  = '.CON_iGearBoxPowerReduction'
    #PLC AMS地址
    IP = '172.16.43.186.1.1:801'
    #NI设备IP
    NiIP = '172.16.43.81'
    #报告路径
    PATH = '.\Reports'
    
    #198号刹车
    BP_198 = 198   
    #100号刹车
    BP_100 = 100       
    #:dmr>
class Variable():
    #激活SCADA控制，会有500秒倒计时，超时后需重新激活
    SCADA_active = '.gbRemoteActive'
    #叶片角度    
    pitch = '.grpitchangle'
    pitch_set = '.grENVin_Blade1Setpoint'
    #p
    #扭矩
    gen_torque = '.grConverter_GeneratorTorque_Nm'
    gen_torque_set = '.grGenTorqueSetValue'
    #当前功率
    gen_power='.grGenPowerForProcess'
    #当前转速
    gen_speedPDM = '.grGenSpeedForProcess'
    
    #安全链复位
    safety_chain_reset = '.gbsimu_NacelleSafetyChain_RESET'
    softSafetyChain_Tripped = '.gbSoftSafetyChain_Tripped' 
    
    #版本号
    code_build_no ='.gsControlCodeBuildNo'
    
    #刹车等级
    bp_level = '.giBPLevel'
    #50号刹车
    bp_50 = '.RemCmdACK_bTestBP50'
    
    #风机状态
    operation_mode = '.giTurbineOperationMode'
    
    mode_GridOp = '.CON_iCAGE_GridOp'
    mode_Selftest1 = '.CON_iSelftest1'
    mode_Selftest2 = '.CON_iSelftest2'
    mode_Selftest3 = '.CON_iSelftest3'
    mode_Selftest4 = '.CON_iSelftest4'
    mode_bp_50 = '.CON_iBrakeMode50'    
    
    #当前限功率模式
    powerredu_mode = 'PRG_PowerReduction.iPowerReductionMode'
    #一分钟平均油池温度
    temp_gear_oilsump = '.grTempGearOilSump_1min'
    #10min平均风速
    windspeed_10min = '.grWindSpeed_10min'
    windspeed_1s = '.grWindSpeed_30sec'
    
    #变频器扭矩实际值
    CVT_ActualTorque = '.grCVT_ActualTorque'
    #发电机扭矩设定值
    genTorqueSetValue = '.grGenTorqueSetValue'
    #PLC系统时间
    data_Time = '.gsDataTime'
    #实际风速
    windSpeed = '.grWindSpeed'
    #发电机转速 PDM1
    genSpeedPDM1 = '.grGenSpeedPDM1'
    genSpeedPDM = '.grGenSpeedPDM'
    
    #skp:
    
    #机舱柜中齿轮箱的油泵电机保护空开
    nacelleMotorProtGearOilPump = '.gbDI_NacelleMotorProtGearOilPump'
    #齿轮箱冷却风扇断路器状态断开。（gbDI_NacelleMotorProtGearFan=0）
    nacelleMotorProtGearFan = '.gbDI_NacelleMotorProtGearFan'
    #齿轮箱加热器保险丝
    nacelleMotorProtGearHeater = '.gbDI_NacelleMotorProtGearHeater'   
    
    #机舱柜中齿轮箱冷却风扇电机加热器或齿轮箱油泵电机加热器保护空开跳开
    nacelleFuseHeaterGearFanAndOilPump='.gbDI_NacelleFuseHeaterGearFanAndOilPump'
     #机舱柜中齿轮箱油管加热器保护开关跳开 0202043
    nacelleFuseHeaterGearOilPipe= '.gbDI_NacelleFuseHeaterGearOilPipe'
       #齿轮箱入口油温测量PT100传感器故障   0202055
    StatePT100_TempGearOilInlet='.gbStatePT100_TempGearOilInlet'
    #齿轮箱非驱动端轴承PT100传感器输入的状态字节第6位是TRUE或齿轮箱非驱动端轴承1min平均温度不在[-100,500]范围内。0202059
    TempGearBearingNDE='.gbStatePT100_TempGearBearingNDE'
    #齿轮箱驱动端的中间轴温度测量PT100传感器故障0202061
    TempGearBearingInterDE='.gbStatePT100_TempGearBearingInterDE'
    #齿轮箱入口油压传感器输入的状态字节第6位是TRUE。（giStateAIGearOilPressureGBXInlet.6=1）02020065
    
    #齿轮油泵处于运行状态，但齿轮油的温度不低于设定值。0205001 (DQ_NacelleGearOilPumpLS=1 OR DQ_NacelleGearOilPumpHS=1) AND (grTempGearOilSump_10min 
    NacelleGearOilFilterCloggingWarning='.gbDI_NacelleGearOilFilterCloggingWarning'#0触发    
    #齿轮箱滤网阻塞故障不断。(SC_RepFaultGearOilFilterClogged=1)  0205003
    OilFilterCloggingWarning='.gbDI_OilFilterCloggingAlarm'  #0chufa
    
    #齿轮箱滤网阻塞故障不断。(SC_RepFaultGearOilFilterClogged=1)0402013
    PitchBackupMinVolt='.Par_rPitchBackupMinVolt'
    
    PitchBackupMaxVolt='.Par_rPitchBackupMaxVolt'
    #1号轴控柜温度过高故障 sc0402019
    PitchAxisBoxTemp='.Par_rPitchAxisBoxMaxTemp'
    #轴控柜温度过di故障
    PitchAxisBoxMinTemp='.Par_rPitchAxisBoxMinTemp'
    #变桨系统发出内部信息
    PITCH_InfoTcuActive='.di_PITCH_InfoTcuActive'
    #变桨系统发出故障信息0402027
    PITCH_ErrTcuActive='.di_PITCH_ErrTcuActive' 
    #1号桨直流母线电压不正常故障
    PITCH_Blade1DCLinkOK='.di_PITCH_Blade1DCLinkOK'
    PITCH_Blade3DCLinkOK='.di_PITCH_Blade3DCLinkOK'
    #2号桨叶24V电源故障
    PITCH_Blade2_24VSupplyError='.di_PITCH_Blade2_24VSupplyError'
    #主控制与变桨间的通讯故障0402035
    
    #1号变桨电机温度过高故障0402039
    PitchMotorMaxTemp= '.Par_rPitchMotorMaxTemp'  
    PitchMotorMinTemp='.Par_rPitchMotorMinTemp'
    
    PITCH_PCUSafetyLineClosed='.di_PITCH_PCUSafetyLineClosed'
    #超级电容需要维护sc0402051
    PITCH_Backup1MaintenanceRequired='.di_PITCH_Backup1MaintenanceRequired'
    PITCH_Backup2MaintenanceRequired='.di_PITCH_Backup2MaintenanceRequired'
    PITCH_Backup3MaintenanceRequired='.di_PITCH_Backup3MaintenanceRequired'    
    #超级电容自检报警
    PITCH_Backup1Warining='.di_PITCH_Backup1Warining'
    PITCH_Backup2Warining='.di_PITCH_Backup2Warining'
    PITCH_Backup3Warining='.di_PITCH_Backup3Warining'
    #超级电容自检故障
    PITCH_Backup1Error='.di_PITCH_Backup1Error'
    PITCH_Backup2Error='.di_PITCH_Backup2Error'
    PITCH_Backup3Error='.di_PITCH_Backup3Error'
    
    PITCH_LubricationFault='.di_PITCH_LubricationFault'
    #2号桨叶的PM出现故障
    PITCH_Master2Error='.di_PITCH_Master2Error'
    PITCH_Master1CommunicationError='.di_PITCH_Master1CommunicationError'
    PITCH_Master3CommunicationError='.di_PITCH_Master3CommunicationError'
    PITCH_TCUOpenSafetyLine='.di_PITCH_TCUOpenSafetyLine'#71
    PITCH_EmergencyModeByTCU='.di_PITCH_EmergencyModeByTCU'#73
    PITCH_PM2SafetyRun='.di_PITCH_PM2SafetyRun'#75
    PITCH_SafetyRunTimeout='.di_PITCH_SafetyRunTimeout'#77
    PITCH_Blade1GridSupplyError='.di_PITCH_Blade1GridSupplyError'#79
    PITCH_Blade3GridSupplyError='.di_PITCH_Blade3GridSupplyError'
    PITCH_Blade1DCLinkFuseError='.di_PITCH_Blade1DCLinkFuseError'
    PITCH_Blade3DCLinkFuseError='.di_PITCH_Blade3DCLinkFuseError'#85
    PITCH_Blade2DiodeError='.di_PITCH_Blade2DiodeError'
    PITCH_LightningProtectionError='.di_PITCH_LightningProtectionError'
    #轴控柜充电故障0402091
    PITCH_Backup2ChargerError='.di_PITCH_Backup2ChargerError'
    di_PITCH_Axis1HeatingError='.di_PITCH_Axis1HeatingError'
    di_PITCH_Axis3HeatingError='.di_PITCH_Axis3HeatingError'
    di_PITCH_BackupBox2OverTemp='.di_PITCH_BackupBox2OverTemp'
    di_PITCH_BackupBox1UnderTemp='.di_PITCH_BackupBox1UnderTemp'
    di_PITCH_BackupBox3UnderTemp='.di_PITCH_BackupBox3UnderTemp'
    di_PITCH_AxisBox2TempSensorError='.di_PITCH_AxisBox2TempSensorError'
    di_PITCH_BackupBox1TempSensorError='.di_PITCH_BackupBox1TempSensorError'
    di_PITCH_BackupBox3TempSensorError='.di_PITCH_BackupBox3TempSensorError'
    di_PITCH_Motor2TempSensorError='.di_PITCH_Motor2TempSensorError'
    di_PITCH_PM2FanError='.di_PITCH_PM2FanError'
    di_PITCH_HubTempSensorError='.di_PITCH_HubTempSensorError'
    di_PITCH_Backup1SwitchOpen='.di_PITCH_Backup1SwitchOpen'
    di_PITCH_Backup3SwitchOpen='.di_PITCH_Backup3SwitchOpen'
    di_PITCH_AxisBox2ContactorExpireWarning='.di_PITCH_AxisBox2ContactorExpireWarning'
    #中心柜温度过高故障123
    #di_PITCH_CenterBoxOverTemp='.di_PITCH_CenterBoxOverTemp'
    PAR_rPitchLBAMaxTemp='.PAR_rPitchLBAMaxTemp'
    #中心柜温度传感器断线故障125
    di_PITCH_CenterBoxTempSensorError='.di_PITCH_CenterBoxTempSensorError'
    PitchHubMinTemp='.PAR_rPitchHubMinTemp'
    #HVRT level2 警告129
    PITCH_HVRTLevel2='.di_PITCH_HVRTLevel2'
    #变桨系统处于低温预加热模式0402063'
    gbPitchTempCold='.gbPitchTempCold'
    gbDI_NacelleGearOilLevelOK='.gbDI_NacelleGearOilLevelOK'
    #第一批用例完成
    
    #sc0405017齿轮箱低速泵热继跳开 0 chufa
    gbDI_GBXOilPumpMotorLS_Overload='.gbDI_GBXOilPumpMotorLS_Overload'
    #018齿轮箱高速泵热继跳开
    gbDI_GBXOilPumpMotorHS_Overload='.gbDI_GBXOilPumpMotorHS_Overload'
    #齿轮箱中速轴(GSGS)PT100传感器故障  31
    gbStateGearboxBearing_IMS_GSGS_Temp='.gbStateGearboxBearing_IMS_GSGS_Temp'
    #齿轮箱中速轴(GSRS)PT100传感器故障32
    gbStateGearboxBearing_IMS_GSRS_Temp='.gbStateGearboxBearing_IMS_GSRS_Temp'
    #齿轮箱中速轴(RS)PT100传感器故障
    gbStateGearboxBearing_IMS_RS_Temp='.gbStateGearboxBearing_IMS_RS_Temp'
    #齿轮箱高速轴(GSGS)PT100传感器故障34
    gbStateGearboxBearing_HSS_GSGS_Temp='.gbStateGearboxBearing_HSS_GSGS_Temp'
    #齿轮箱高速轴(GSRS)PT100传感器故障35    
    gbStateGearboxBearing_HSS_GSRS_Temp='.gbStateGearboxBearing_HSS_GSRS_Temp'
    #齿轮箱高速轴(RS)PT100传感器故障36
    gbStateGearboxBearing_HSS_RS_Temp='.gbStateGearboxBearing_HSS_RS_Temp'
    #齿轮箱离线精滤器空开跳开39
    gbDI_GBXOfflineFitrationSystemMCB='.gbDI_GBXOfflineFitrationSystemMCB'
    #40齿轮箱油泵加热器空开跳开
    gbDI_GearOilPumpMotorPreheaterMCB='.gbDI_GearOilPumpMotorPreheaterMCB'
    #齿轮箱油泵滤网堵塞41
    gbDI_GearFilterBlocking='.gbDI_GearFilterBlocking'
    #齿轮箱过滤器压差传感器故障45
    gbStateAIGearOilDiffPressureInlineFilter='.gbStateAIGearOilDiffPressureInlineFilter'
    #齿轮箱左扭力臂位置传感器损坏50
    gbStateAI_GBXTorqueArmPositionLeft='.gbStateAI_GBXTorqueArmPositionLeft'
    #齿轮箱左扭力臂位置传感器损坏51
    gbStateAI_GBXTorqueArmPositionRight='.gbStateAI_GBXTorqueArmPositionRight'  
    #齿轮箱暖机超时0205110
    
    #Scada发出50#刹车测试指令 0307005
    RemCmdACK_bTestBP50='.RemCmdACK_bTestBP50'
    #齿轮箱油泵加热器运行0202104
    gbDQ_NacelleGearHeaterOilPump='.gbDQ_NacelleGearHeaterOilPump'
    #电网电压L1相超出上限值 0304002
    grUL1ForProcess='.grUL1ForProcess'
    #电网电压L2相超出上限值 0304003
    grUL2ForProcess='.grUL2ForProcess'
    #电网电压L3相超出上限值 0304004
    grUL3ForProcess='.grUL3ForProcess'
    
    #电网测量设备故障0414001
    gbValidData_RS485_PowerMeasurement='.gbValidData_RS485_PowerMeasurement'
    
    #机舱出口风扇1空开跳开
    gbDI_NacelleOutletFan1MCB='.gbDI_NacelleOutletFan1MCB'
    #机舱出口风扇1热继跳开
    gbDI_NacelleOutletFan1Overload='.gbDI_NacelleOutletFan1Overload'
    #机舱出口风扇2空开跳开
    gbDI_NacelleOutletFan2MCB='.gbDI_NacelleOutletFan2MCB'
     #机舱出口 风扇2热继跳开
    gbDI_NacelleOutletFan2Overload='.gbDI_NacelleOutletFan2Overload'
    #FT加热器空开跳开
    gbDI_FTHeatingMCB='.gbDI_FTHeatingMCB'
    #风向标加热器空开跳开
    gbDI_AnalogWindDirectionHeaterMCB='.gbDI_AnalogWindDirectionHeaterMCB'
    #风速仪加热器空开跳开
    gbDI_AnalogWindSpeedHeaterMCB='.gbDI_AnalogWindSpeedHeaterMCB'
    #机舱出口气流调节器空开跳开
    gbDI_NacelleOutletDamperMCB='.gbDI_NacelleOutletDamperMCB'    
    #机舱入口气流调节器空开跳开
    gbDI_NacelleInletDamperMCB='.gbDI_NacelleInletDamperMCB'
    #机舱加热器空开跳开
    gbDI_NacelleHeaterMCB='.gbDI_NacelleHeaterMCB'
    #航空灯空开跳开
    gbDI_NacelleAviationLightChangeLamp='.gbDI_NacelleAviationLightChangeLamp'
    
    gbDI_NacelleAviationLightOK='.gbDI_NacelleAviationLightOK'    
    #:skp>
    
    #DMR:
    #机舱柜中齿轮箱的油泵电机保护空开
    nacelleMotorProtGearOilPump = '.gbDI_NacelleMotorProtGearOilPump'
    #机舱柜中齿轮箱冷却风扇电机加热器或齿轮箱油泵电机加热器保护空开跳开
    NacelleFuseHeaterGearFanAndOilPump='.gbDI_NacelleFuseHeaterGearFanAndOilPump' 
    #齿轮箱油池油温测量PT100传感器故障
    StatePT100_TempGearOilSump='.gbStatePT100_TempGearOilSump'
    #驱动端轴承温度测量PT100传感器故障
    StatePT100_TempGearBearingDE='.gbStatePT100_TempGearBearingDE'
    #齿轮箱非驱动端中间轴温度测量PT100传感器故障
    StatePT100_TempGearBearingInterNDE='.gbStatePT100_TempGearBearingInterNDE'
    #齿轮箱过滤器入口压力传感器故障
    StateAIGearOilPressureFilterInlet='.gbStateAIGearOilPressureFilterInlet'
    #齿轮箱精滤器保护空开跳开
    NacelleGearOilFilterSwitch='.gbDI_NacelleGearOilFilterSwitch'
    #齿轮箱过滤器阻塞警告
    OilFilterCloggingWarning='.gbDI_OilFilterCloggingWarning'
    #后备最小电源电压
    PitchBackupMinVolt='.PAR_rPitchBackupMinVolt'
    #后备最大电源电压
    PitchBackupMaxVolt='.PAR_rPitchBackupMaxVolt'
    #最大盒温度
    PitchAxisBoxMaxTemp='.PAR_rPitchAxisBoxMaxTemp'
    #2号轴控柜温度过高故障
    PITCH_AxisBox2OverTemp='.di_PITCH_AxisBox2OverTemp'
    #最小盒温度
    PitchAxisBoxMinTemp='.PAR_rPitchAxisBoxMinTemp'
    #变桨系统发出报警信息
    PITCH_WarnTCUActive='.di_PITCH_WarnTCUActive'
    #变桨系统出现内部故障
    PITCH_ErrPCUActive='.di_PITCH_ErrPCUActive'
    #2号桨直流母线电压不正常故障
    PITCH_Blade2DCLinkOK='.di_PITCH_Blade2DCLinkOK'
    #1号桨叶24V电源故障
    PITCH_Blade1_24VSupplyError='.di_PITCH_Blade1_24VSupplyError'
    #3号桨叶24V电源故障
    PITCH_Blade3_24VSupplyError='.di_PITCH_Blade3_24VSupplyError'
    #变桨系统处于低电压穿越模式
    PITCH_LVRT='.di_PITCH_LVRT'
    #最小电机温度
    PitchMotorMinTemp='.PAR_rPitchMotorMinTemp'
    #最大电机温度
    PitchMotorMaxTemp='.PAR_rPitchMotorMaxTemp'    
    #主控先断开了EFC信号
    PITCH_TCUSafetyLineOpened='.di_PITCH_TCUSafetyLineOpened'
    #50:1号超级电容需要维护
    PITCH_Backup1MaintenanceRequired='.di_PITCH_Backup1MaintenanceRequired'
    #变桨自润滑系统电源故障
    PITCH_LubricationON='.di_PITCH_LubricationON'
    #变桨自润滑系统低油位故障
    PITCH_LubricationLowLevel='.di_PITCH_LubricationLowLevel'
    #1号桨叶的PM出现故障
    PITCH_Master1Error='.di_PITCH_Master1Error'
    #3号桨叶的PM出现故障
    PITCH_Master3Error='.di_PITCH_Master3Error'    
    #2号桨叶的PM出现通讯故障
    PITCH_Master2CommunicationError='.di_PITCH_Master2CommunicationError'
    #变桨系统与主控的通讯出现故障
    PITCH_TCU_PCUCommunicationError='.di_PITCH_TCU_PCUCommunicationError'
    #变桨系统先断开EFC信号
    PITCH_PCUOpenSafetyLineFirst='.di_PITCH_PCUOpenSafetyLineFirst'
    #1号桨叶开始自主回桨
    PITCH_PM1SafetyRun='.di_PITCH_PM1SafetyRun'
    #3号桨叶开始自主回桨
    PITCH_PM3SafetyRun='.di_PITCH_PM3SafetyRun'
    #400V进线主接触器2Q1的吸合次数超过了设计寿命报警
    PITCH_GridSupplyContactorExpireWarning='.di_PITCH_GridSupplyContactorExpireWarning'
    #2号桨叶400V电源故障
    PITCH_Blade2GridSupplyError='.di_PITCH_Blade2GridSupplyError'
    #LVRT故障
    PITCH_LVRTError='.di_PITCH_LVRTError'
    #2号轴控柜内1F2失效故障
    PITCH_Blade2DCLinkFuseError='.di_PITCH_Blade2DCLinkFuseError'
    #1号轴控柜内1F1跳开故障
    PITCH_Blade1DiodeError='.di_PITCH_Blade1DiodeError'
    #3号轴控柜内1F1跳开故障
    PITCH_Blade3DiodeError='.di_PITCH_Blade3DiodeError'
    #1号轴控柜充电故障
    PITCH_Backup1ChargerError='.di_PITCH_Backup1ChargerError'
    #3号轴控柜充电故障
    PITCH_Backup3ChargerError='.di_PITCH_Backup3ChargerError'  
    #2号轴控柜加热器故障
    PITCH_Axis2HeatingError='.di_PITCH_Axis2HeatingError'  
    #最大后备电源柜温度
    PitchBackupMaxTemp='.PAR_rPitchBackupMaxTemp'
    #最小哦后备电源柜温度
    PitchBackupMinTemp='.PAR_rPitchBackupMinTemp'
    #1号轴控柜温度传感器断线故障
    AxisBox1TempSensorError='.di_PITCH_AxisBox1TempSensorError'
    #3号轴控柜温度传感器断线故障
    AxisBox3TempSensorError='.di_PITCH_AxisBox3TempSensorError' 
    #2号后备电源柜温度传感器断线故障
    BackupBox2TempSensorError='.di_PITCH_BackupBox2TempSensorError' 
    #1号变桨电机温度传感器断线故障
    Motor1TempSensorError='.di_PITCH_Motor1TempSensorError' 
    #3号变桨电机温度传感器断线故障
    Motor3TempSensorError='.di_PITCH_Motor3TempSensorError' 
    #1号PM的风扇故障
    PITCH_PM1FanError='.di_PITCH_PM1FanError'
    #3号PM的风扇故障
    PITCH_PM3FanError='.di_PITCH_PM3FanError'  
    #2号轴控柜超级电容开关-1Q1断开
    PITCH_Backup2SwitchOpen='.di_PITCH_Backup2SwitchOpen'
    #1号轴控柜内接触器3Q1的吸合次数超过了设计寿命报警
    PITCH_AxisBox1ContactorExpireWarning='.di_PITCH_AxisBox1ContactorExpireWarning'
    #3号轴控柜内接触器3Q1的吸合次数超过了设计寿命报警
    PITCH_AxisBox3ContactorExpireWarning='.di_PITCH_AxisBox3ContactorExpireWarning' 
    #中心柜温度过低故障
    PitchLBAMinTemp='.PAR_rPitchLBAMinTemp'
    #轮毂温度过高警告
    PitchHubMaxTemp='.PAR_rPitchHubMaxTemp'
    #HVRT level1 警告
    PITCH_HVRTLevel1='.di_PITCH_HVRTLevel1' 
    
    #SC02_02_036:机舱柜中发电机冷却风扇保护空开跳开
    NacelleMotorProtGenFan='.gbDI_NacelleMotorProtGenFan'
    #SC02_02_038:机舱柜中发电机空间加热器保护空开跳开
    NacelleMotorProtGenSpaceHeater='.gbDI_NacelleMotorProtGenSpaceHeater'
    #SC02_02_067:发电机定子U相绕组温度测量PT100传感器故障
    StatePT100_TempGenStatorU1='.gbStatePT100_TempGenStatorU1'   
    #SC02_02_069:发电机定子V相绕组温度测量PT100传感器故障
    StatePT100_TempGenStatorV1='.gbStatePT100_TempGenStatorV1'
    #SC02_02_071:发电机定子W相绕组温度测量PT100传感器故障
    StatePT100_TempGenStatorW1='.gbStatePT100_TempGenStatorW1'
    #SC02_02_073:发电机驱动端轴承温度测量PT100传感器故障
    StatePT100_TempGenBearingDE='.gbStatePT100_TempGenBearingDE'
    #SC02_02_074:发电机非驱动端轴承温度测量PT100传感器故障
    StatePT100_TempGenBearingNDE='.gbStatePT100_TempGenBearingNDE'
    #SC02_02_128:机舱柜中发电机水冷系统保护空开跳开
    NacelleMotorProtWCSG='.gbDI_NacelleMotorProtWCSG'
    #SC_02_08_006:发电机碳刷磨损警告
    NacelleGeneratorBrushWastage='.gbDI_NacelleGeneratorBrushWastage' 
    #SC_02_08_007:发电机碳刷磨损警告
    NacelleGeneratorBrushWastage='.gbDI_NacelleGeneratorBrushWastage'     
    #SC02_08_012:发电机定子两相绕组温差大于设定值
    GEN_StatorTempDiffMAX='.PAR_rGEN_StatorTempDiffMAX'    
    #setdelay of SC02_08_012
    SC02_08_012_setdelay = '.gxstatuscode[180].tsetdelay'
    #SC02_08_013:发电机定子UVW相绕组温度过高警告
    TempHigh_GenStator='.PAR_rTempHigh_GenStator'
    #setdelay of SC02_08_013
    SC02_08_013_setdelay = '.gxstatuscode[181].tsetdelay' 
    #SC02_08_014:发电机定子UVW相绕组温度过低警告
    TempLow_GenStator='.PAR_rTempLow_GenStator'
    #setdelay of SC02_08_014
    SC02_08_014_setdelay = '.gxstatuscode[182].tsetdelay' 
    #SC02_08_015:发电机定子UVW绕组温度过高故障
    TempMAX_GenStator='.PAR_rTempMAX_GenStator'
    #setdelay of SC02_08_015
    SC02_08_015_setdelay = '.gxstatuscode[183].tsetdelay' 
    #resetdelay of SC02_08_015
    SC02_08_015_resetdelay = '.gxstatuscode[183].tresetdelay'
    #SC02_08_016:发电机定子UVW相绕组温度过低故障
    TempMIN_GenStator='.PAR_rTempMIN_GenStator'
    #setdelay of SC02_08_016
    SC02_08_016_setdelay = '.gxstatuscode[184].tsetdelay' 
    #resetdelay of SC02_08_016
    SC02_08_016_resetdelay = '.gxstatuscode[184].tresetdelay'  
    #setdelay of SC02_08_017
    SC02_08_017_setdelay = '.gxstatuscode[185].tsetdelay' 
    #setdelay of SC02_08_018
    SC02_08_018_setdelay = '.gxstatuscode[186].tsetdelay'
    #setdelay of SC02_08_019
    SC02_08_019_setdelay = '.gxstatuscode[187].tsetdelay'
    #resetdelay of SC02_08_019
    SC02_08_019_resetdelay = '.gxstatuscode[187].tresetdelay'     
    #setdelay of SC02_08_020
    SC02_08_020_setdelay = '.gxstatuscode[188].tsetdelay'
    #resetdelay of SC02_08_020
    SC02_08_020_resetdelay = '.gxstatuscode[188].tresetdelay' 
    #setdelay of SC02_08_021
    SC02_08_021_setdelay = '.gxstatuscode[189].tsetdelay'   
    #resetdelay of SC02_08_021
    SC02_08_021_resetdelay = '.gxstatuscode[189].tresetdelay'     
    #setdelay of SC02_08_022
    SC02_08_022_setdelay = '.gxstatuscode[190].tsetdelay'
    #resetdelay of SC02_08_022
    SC02_08_022_resetdelay = '.gxstatuscode[190].tresetdelay'      
    #setdelay of SC02_08_023
    SC02_08_023_setdelay = '.gxstatuscode[191].tsetdelay'
    #resetdelay of SC02_08_023
    SC02_08_023_resetdelay = '.gxstatuscode[191].tresetdelay'
    #setdelay of SC02_08_024
    SC02_08_024_setdelay = '.gxstatuscode[192].tsetdelay'
    #resetdelay of SC02_08_024
    SC02_08_024_resetdelay = '.gxstatuscode[192].tresetdelay'     
    #setdelay of SC02_08_025
    SC02_08_025_setdelay = '.gxstatuscode[193].tsetdelay'
    #SC02_08_026:发电机驱动端轴承温度过高警告
    TempHigh_GenBearDE='.PAR_rTempHigh_GenBearDE'
    #setdelay of SC02_08_026
    SC02_08_026_setdelay = '.gxstatuscode[194].tsetdelay'  
    #SC02_08_027:发电机驱动端轴承温度过高警告
    TempLow_GenBearDE='.PAR_rTempLow_GenBearDE'
    #setdelay of SC02_08_027
    SC02_08_027_setdelay = '.gxstatuscode[195].tsetdelay' 
    #resetdelay of SC02_08_027
    SC02_08_027_resetdelay = '.gxstatuscode[195].tresetdelay'
    #SC02_08_028:发电机驱动端轴承温度过高故障
    TempMAX_GenBearDE='.PAR_rTempMAX_GenBearDE'
    #setdelay of SC02_08_028
    SC02_08_028_setdelay = '.gxstatuscode[196].tsetdelay' 
    #resetdelay of SC02_08_028
    SC02_08_028_resetdelay = '.gxstatuscode[196].tresetdelay'
    #SC02_08_029:发电机驱动端轴承温度过低故障
    TempMIN_GenBearDE='.PAR_rTempMIN_GenBearDE'
    #setdelay of SC02_08_029
    SC02_08_029_setdelay = '.gxstatuscode[197].tsetdelay' 
    #resetdelay of SC02_08_029
    SC02_08_029_resetdelay = '.gxstatuscode[197].tresetdelay'    
    #SC02_08_030:发电机非驱动端轴承温度过高警告
    TempHigh_GenBearNDE='.PAR_rTempHigh_GenBearNDE'
    #setdelay of SC02_08_030
    SC02_08_030_setdelay = '.gxstatuscode[198].tsetdelay' 
    #resetdelay of SC02_08_030
    SC02_08_030_resetdelay = '.gxstatuscode[198].tresetdelay'  
    #SC02_08_031:发电机非驱动端轴承温度过低警告
    TempLow_GenBearNDE='.PAR_rTempLow_GenBearNDE'
    #setdelay of SC02_08_031
    SC02_08_031_setdelay = '.gxstatuscode[199].tsetdelay' 
    #resetdelay of SC02_08_031
    SC02_08_031_resetdelay = '.gxstatuscode[199].tresetdelay'
    #SC02_08_032:发电机非驱动端轴承温度过高故障
    TempMAX_GenBearNDE='.PAR_rTempMAX_GenBearNDE'
    #setdelay of SC02_08_032
    SC02_08_032_setdelay = '.gxstatuscode[200].tsetdelay' 
    #resetdelay of SC02_08_032
    SC02_08_032_resetdelay = '.gxstatuscode[200].tresetdelay'  
    #SC02_08_033:发电机非驱动端轴承温度过低故障
    TempMIN_GenBearNDE='.PAR_rTempMIN_GenBearNDE'
    #setdelay of SC02_08_033
    SC02_08_033_setdelay = '.gxstatuscode[201].tsetdelay' 
    #resetdelay of SC02_08_033
    SC02_08_033_resetdelay = '.gxstatuscode[201].tresetdelay' 
    #setdelay of SC02_08_034
    SC02_08_034_setdelay = '.gxstatuscode[202].tsetdelay' 
    #resetdelay of SC02_08_034
    SC02_08_034_resetdelay = '.gxstatuscode[202].tresetdelay' 
    #SC02_08_035:发电机冷却系统入口或出口温度过高警告
    TempHigh_GenCoolingInlet='.PAR_rTempHigh_GenCoolingInlet'
    TempHigh_GenCoolingOutlet='.PAR_rTempHigh_GenCoolingOutlet'
    #setdelay of SC02_08_035
    SC02_08_035_setdelay = '.gxstatuscode[203].tsetdelay'
    #SC02_08_036:发电机冷却系统入口或出口温度过低警告
    TempLow_GenCoolingInlet='.PAR_rTempLow_GenCoolingInlet'
    TempLow_GenCoolingOutlet='.PAR_rTempLow_GenCoolingOutlet'
    #setdelay of SC02_08_036
    SC02_08_036_setdelay = '.gxstatuscode[204].tsetdelay' 
    #SC02_08_037:发电机冷却系统入口或出口温度过高故障
    TempMAX_GenCoolingInlet='.PAR_rTempMAX_GenCoolingInlet'
    TempMAX_GenCoolingOutlet='.PAR_rTempMAX_GenCoolingOutlet'
    #setdelay of SC02_08_037
    SC02_08_037_setdelay = '.gxstatuscode[205].tsetdelay' 
    #resetdelay of SC02_08_037
    SC02_08_037_resetdelay = '.gxstatuscode[205].tresetdelay' 
    #SC02_08_038:发电机冷却系统入口或出口温度过低故障
    TempMIN_GenCoolingInlet='.PAR_rTempMIN_GenCoolingInlet'
    TempMIN_GenCoolingOutlet='.PAR_rTempMIN_GenCoolingOutlet'
    #setdelay of SC02_08_038
    SC02_08_038_setdelay = '.gxstatuscode[206].tsetdelay' 
    #resetdelay of SC02_08_038
    SC02_08_038_resetdelay = '.gxstatuscode[206].tresetdelay'
    #setdelay of SC02_08_039
    SC02_08_039_setdelay = '.gxstatuscode[207].tsetdelay' 
    #SC02_08_002:发电机30秒平均功率高于上限值
    MaxPower30sec='.PAR_rMaxPower30sec'
    #SC02_08_042:发电机冷却系统入口PT100传感器故障
    StatePT100_TempGenCoolingInlet='.gbStatePT100_TempGenCoolingInlet'
    #resetdelay of SC02_08_042
    SC02_08_042_resetdelay = '.gxstatuscode[208].tresetdelay'
    #SC02_08_043:发电机冷却系统出口PT100传感器故障
    StatePT100_TempGenCoolingOutlet='.gbStatePT100_TempGenCoolingOutlet'
    #resetdelay of SC02_08_043
    SC02_08_043_resetdelay = '.gxstatuscode[209].tresetdelay'
    #SC02_08_100:发电机定子温度低于露点温度
    TempNacelle='.grTempNacelle' 
    #setdelay of SC02_08_100
    SC02_08_100_setdelay = '.gxstatuscode[210].tsetdelay'
    #SC04_06_002:发电机U相温度信号2错误，报警不停机
    StatePT100_TempGenStatorU2='.gbStatePT100_TempGenStatorU2'
    #SC04_06_005:发电机V相温度信号1错误，报警不停机
    StatePT100_TempGenStatorV1='.gbStatePT100_TempGenStatorV1'
    #SC04_06_006:发电机V相温度信号2错误，报警不停机
    StatePT100_TempGenStatorV2='.gbStatePT100_TempGenStatorV2'
    #SC04_06_009:发电机W相温度信号1错误，报警不停机
    StatePT100_TempGenStatorW1='.gbStatePT100_TempGenStatorW1'
    #SC04_06_010:发电机W相温度信号2错误，报警不停机
    StatePT100_TempGenStatorW2='.gbStatePT100_TempGenStatorW2'
    #SC04_06_035:发电机空水冷却器漏水警告
    GENWaterLeakWarning1='.gbDI_GENWaterLeakWarning1'
    GENWaterLeakWarning2='.gbDI_GENWaterLeakWarning2'
    #SC04_06_036:发电机润滑系统警告
    GENLubricationWarning='.gbDI_GENLubricationWarning'
    #SC02_08_117:发电机水冷主循环泵或电加热器或三通阀开关跳闸
    GLGenWaterCool_PumpHeaterValve_PowerSupply='.gbDI_GLGenWaterCool_PumpHeaterValve_PowerSupply'
    #SC02_08_118:发电机水冷供水温度传感器TT01 故障
    StatePT100_GLGenWaterCoolInlet='.gbStatePT100_GLGenWaterCoolInlet'
    #SC02_08_122:发电机水冷供水温度过高故障
    WCSGENInletTempHigh2='.PAR_rWCSGENInletTempHigh2'
    #SC02_08_124:发电机水冷回水温度高
    WCSGENOutletTempHigh='.PAR_rWCSGENOutletTempHigh'
    #SC02_08_125:发电机水冷供水压力过高故障
    WCSGENInletPreHigh2='.PAR_rWCSGENInletPreHigh2'
    #SC02_08_128:发电机水冷供水压力过低故障
    WCSGENInletPreLow2='.PAR_rWCSGENInletPreLow2'
    #SC02_08_130:发电机水冷回水压力过低故障
    WCSGENOutletPreLow2='.PAR_rWCSGENOutletPreLow2'
    #SC02_08_133:发电机水冷入口、出口压差过大故障
    GenWaterCoolInOutPressureDiffHigh='.PAR_rGenWaterCoolInOutPressureDiffHigh'
    #SC02_08_134:发电机水冷入口、出口压差过低故障
    GenWaterCoolInOutPressureDiffLow='.PAR_rGenWaterCoolInOutPressureDiffLow'
    GLGenWaterCool_PumpOn='.gbDI_GLGenWaterCool_PumpOn'
    #SC02_08_136:发电机水冷加热器加热时间过长
    GLGenWaterCool_HeaterOn='.gbDI_GLGenWaterCool_HeaterOn'
    #setdelay of SC02_08_136:
    SC02_08_136_setdelay='.gxSTATUSCODE[806].tSetDelay'
    #SC04_08_005:冷却系统循环泵1低速电机手动模式开启
    CS_Pump1LowManualControlMode='.RemCmdACK_bEnableCS_Pump1LowManualControlMode'
    #SC04_08_006:冷却系统循环泵2低速电机手动模式开启
    CS_Pump2LowManualControlMode='.RemCmdACK_bEnableCS_Pump2LowManualControlMode'
    #SC04_08_007:冷却系统循环泵1低速电机强制模式开启
    CS_Pump1LowForceControlMode='.RemCmdACK_bEnableCS_Pump1LowForceControlMode'
    #SC04_08_008:冷却系统循环泵2低速电机强制模式开启
    CS_Pump2LowForceControlMode='.RemCmdACK_bEnableCS_Pump2LowForceControlMode'
    #SC04_08_009:冷却系统循环泵1高速电机手动模式开启
    CS_Pump1HighManualControlMode='.RemCmdACK_bEnableCS_Pump1HighManualControlMode'
    #SC04_08_010:冷却系统循环泵2高速电机手动模式开启
    CS_Pump2HighManualControlMode='.RemCmdACK_bEnableCS_Pump2HighManualControlMode'
    #SC04_08_011:冷却系统循环泵1高速电机强制模式开启
    CS_Pump1HighForceControlMode='.RemCmdACK_bEnableCS_Pump1HighForceControlMode'
    #SC04_08_012:冷却系统循环泵2高速电机强制模式开启
    CS_Pump2HighForceControlMode='.RemCmdACK_bEnableCS_Pump2HighForceControlMode'
    #SC04_08_013:冷却系统发电机出口温度过高
    Temp_CS_GENOutletHigh='.PAR_rTemp_CS_GENOutletHigh'
    #SC04_08_014:冷却系统(入口或出口)压力低报警
    Pre_CS_LowWarning='.PAR_rPre_CS_LowWarning'
    #SC04_08_015:冷却系统(入口或出口)压力低故障
    Pre_CS_LowError='.PAR_rPre_CS_LowError'
    #SC04_08_016:冷却系统泵出口PT100故障
    StateAI_CS_PumpOutletTemp='.gbStateAI_CS_PumpOutletTemp'
    #SC04_08_017:冷却系统发电机出口PT100故障
    StateAI_CS_GENOutletTemp='.gbStateAI_CS_GENOutletTemp'
    #SC04_08_018:冷却系统齿轮箱出口PT100故障
    StateAI_CS_GBXOutletTemp='.gbStateAI_CS_GBXOutletTemp'
    #SC04_08_019:冷却系统循环泵压力侧压力传感器故障
    StateAI_CS_PumpOutletPressure='.gbStateAI_CS_PumpOutletPressure'
    #SC04_08_020:冷却系统循环泵吸入侧压力传感器故障
    StateAI_CS_PumpInletPressure='.gbStateAI_CS_PumpInletPressure'
    #SC04_08_021:水冷循环泵1低速热继触发
    CS_Pump1Low_OverloadOK='.gbDI_CS_Pump1Low_OverloadOK'
    #SC04_08_022:水冷循环泵2低速热继触发
    CS_Pump2Low_OverloadOK='.gbDI_CS_Pump2Low_OverloadOK'
    #SC04_08_023:水冷循环泵1高速热继触发
    CS_Pump1High_OverloadOK='.gbDI_CS_Pump1High_OverloadOK'
    #SC04_08_024:水冷循环泵2高速热继触发
    CS_Pump2High_OverloadOK='.gbDI_CS_Pump2High_OverloadOK'
    #SC04_08_025:水冷循环泵1空开跳开
    CS_Pump1MCBOK='.gbDI_CS_Pump1MCBOK'
    #SC04_08_026:水冷循环泵2空开跳开
    CS_Pump2MCBOK='.gbDI_CS_Pump2MCBOK'
    #SC04_08_027:冷却系统齿轮箱出口温度过高
    Temp_CS_GBXOutletHigh='.PAR_rTemp_CS_GBXOutletHigh'
    #SC04_08_031:塔底水冷泵1MCB跳开
    TCS_Pump1MCB='.gbDI_TCS_Pump1MCB'
    #SC04_08_032:塔底水冷泵2MCB跳开
    TCS_Pump2MCB='.gbDI_TCS_Pump2MCB'
    #SC04_08_035:塔底水冷泵2无压力故障
    TCS_PumpMINPressureErr='.PAR_rTCS_PumpMINPressureErr'
    #SC04_08_037:塔底水冷加热器MCB跳开
    TCS_CVTHeaterMCB='.gbDI_TCS_CVTHeaterMCB'
    #SC04_08_038:塔底水冷进水口水温过低警告
    TCS_WaterInletTempLowWarning='.PAR_rTCS_WaterInletTempLowWarning'
    #SC04_08_039:塔底水冷进水口PT100故障
    StateAI_TCS_WaterCoolingInletTemp='.gbStateAI_TCS_WaterCoolingInletTemp'
    #SC04_08_042:塔底水冷塔内风扇1MCB跳开
    TCS_InsideCoolerFan1MCB='.gbDI_TCS_InsideCoolerFan1MCB'
    #SC04_08_043:塔底水冷塔内风扇2MCB跳开
    TCS_InsideCoolerFan2MCB='.gbDI_TCS_InsideCoolerFan2MCB'
    #SC04_08_046:塔底冷却器1风扇A过载
    TCS_Cooler1FanAOverload='.gbDI_TCS_Cooler1FanAOverload'
    #SC04_08_047:塔底冷却器1风扇B过载
    TCS_Cooler1FanBOverload='.gbDI_TCS_Cooler1FanBOverload'
    #SC04_08_048:塔底冷却器2风扇A过载
    TCS_Cooler2FanAOverload='.gbDI_TCS_Cooler2FanAOverload'
    #SC04_08_049:塔底冷却器2风扇B过载
    TCS_Cooler2FanBOverload='.gbDI_TCS_Cooler2FanBOverload'
    #SC04_08_050:塔底冷却器3风扇A过载
    TCS_Cooler3FanAOverload='.gbDI_TCS_Cooler3FanAOverload'
    #SC04_08_051:塔底冷却器3风扇B过载
    TCS_Cooler3FanBOverload='.gbDI_TCS_Cooler3FanBOverload'
    #SC04_08_052:塔底冷却器4风扇A过载
    TCS_Cooler4FanAOverload='.gbDI_TCS_Cooler4FanAOverload'
    #SC04_08_053:塔底冷却器4风扇B过载
    TCS_Cooler4FanBOverload='.gbDI_TCS_Cooler4FanBOverload'
    #SC04_08_054:塔底冷却器1风扇 MCB跳开
    TCS_Cooler1Fans_MCB='.gbDI_TCS_Cooler1Fans_MCB'
    #SC04_08_055:塔底冷却器2风扇 MCB跳开
    TCS_Cooler2Fans_MCB='.gbDI_TCS_Cooler2Fans_MCB'
    #SC04_08_056:塔底冷却器3风扇 MCB跳开
    TCS_Cooler3Fans_MCB='.gbDI_TCS_Cooler3Fans_MCB'
    #SC04_08_057:塔底冷却器4风扇 MCB跳开
    TCS_Cooler4Fans_MCB='.gbDI_TCS_Cooler4Fans_MCB'    
     #:dmr>   
     
class  Sc():    
    shutdown_lowwindspeed = '.SC_ShutDownWindspeed_10minMin'
    motorProtection_GearOilPump = '.SC_MotorProtection_GearOilPump'
    motorProtection_GearFan ='.SC_MotorProtection_GearFan'
    nacelleFuseGearboxHeater = '.SC_NacelleFuseGearboxHeater'    
    
    #机舱柜中齿轮箱冷却风扇电机加热器或齿轮箱油泵电机加热器保护空开跳开
    nacelleFuseMotorHeater_GearFanAndOilPump='.SC_NacelleFuseMotorHeater_GearFanAndOilPump'    
    #机舱柜中齿轮箱油管加热器保护开关跳开 0202043
    nacelleFuseHeater_GearOilPipe='.SC_NacelleFuseHeater_GearOilPipe' 
    #齿轮箱入口油温测量PT100传感器故障   0202055
    faultInputPT100_GearOilInlet='.SC_FaultInputPT100_GearOilInlet'
    #齿轮箱非驱动端轴承PT100传感器输入的状态字节第6位是TRUE或齿轮箱非驱动端轴承1min平均温度不在[-100,500]范围内。0202059
    faultInputPT100_GearBearingNDE='.SC_FaultInputPT100_GearBearingNDE'
    #齿轮箱驱动端的中间轴温度测量PT100传感器故障0202061
    FaultInputPT100_GearBearingInterDE='.SC_FaultInputPT100_GearBearingInterDE'
    #齿轮箱入口油压传感器输入的状态字节第6位是TRUE。（giStateAIGearOilPressureGBXInlet.6=1）02020065
    FaultAI_GearOilPressureGBXInlet='.SC_FaultAI_GearOilPressureGBXInlet'
    
    #齿轮油泵处于运行状态，但齿轮油的温度不低于设定值。0205001 (DQ_NacelleGearOilPumpLS=1 OR DQ_NacelleGearOilPumpHS=1) AND (grTempGearOilSump_10min 
    GearOilFilterClogged_Warning='SC_GearOilFilterClogged_Warning'
    #齿轮箱滤网阻塞故障不断。(SC_RepFaultGearOilFilterClogged=1)  02005003
    GearOilFilterClogged_STOP='.SC_GearOilFilterClogged_STOP'
    
    #齿轮箱滤网阻塞故障不断。(SC_RepFaultGearOilFilterClogged=1)0402013
    UndervoltageBackupAxis1='.SC_UndervoltageBackupAxis1'
    
    UndervoltageBackupAxis3='.SC_UndervoltageBackupAxis3'#015 
    
    #2号桨叶后备电源电压过高故障
    OvervoltageBackupAxis2='.SC_OvervoltageBackupAxis2'   
        
    #1号轴控柜温度过高故障 0402019 sc
    OvertemperatureAxisBox1='.Sc_OvertemperatureAxisBox1'
    #3号轴控柜温度过高故障 0402021 sc
    OvertemperatureAxisBox3='.Sc_OvertemperatureAxisBox3'
    OvertemperatureAxisBox2='.Sc_OvertemperatureAxisBox2'
    #号轴控柜温度过低故障
    UndertemperatureAxisBox1='.Sc_UndertemperatureAxisBox1'
    UndertemperatureAxisBox2='.Sc_UndertemperatureAxisBox2'
    UndertemperatureAxisBox3='.Sc_UndertemperatureAxisBox3'
    #变桨系统发出内部信息
    InfoTcuActive='.SC_InfoTcuActive'
    #变桨系统发出故障信息0402027
    ErrTcuActive='.SC_ErrTcuActive'
    #1号桨直流母线电压不正常故障
    Blade1DCLinkVoltageNotOK='.Sc_Blade1DCLinkVoltageNotOK'
    Blade2DCLinkVoltageNotOK='.Sc_Blade2DCLinkVoltageNotOK'
    Blade3DCLinkVoltageNotOK='.Sc_Blade3DCLinkVoltageNotOK'
    #2号桨叶24V电源故障
    SupplyAxis2='.SC_24VSupplyAxis2'
    #主控制与变桨间的通讯故障0402035
    PitchCommunicationError='.SC_PitchCommunicationError'
    #变桨电机温度过高故障0402039
    OvertemperatureMotorAxis1='.SC_OvertemperatureMotorAxis1'
    OvertemperatureMotorAxis3='.SC_OvertemperatureMotorAxis3'
    #2号变桨电机温度过低故障
    UndertemperatureMotorAxis2='.SC_UndertemperatureMotorAxis2'
    #变桨系统断开EFC反馈信号0402045
    PcuOpenSafetychain='.SC_PcuOpenSafetychain'
    #超级电容sc0402051
    Axis1BackupMaintenanceRequired='.SC_Axis1BackupMaintenanceRequired'
    Axis2BackupMaintenanceRequired='.SC_Axis2BackupMaintenanceRequired'
    Axis3BackupMaintenanceRequired='.SC_Axis3BackupMaintenanceRequired'
    #超级电容自检报警
    Axis1backupTestWarning='.SC_Axis1backupTestWarning'
    Axis2backupTestWarning='.SC_Axis2backupTestWarning'
    Axis3backupTestWarning='.SC_Axis3backupTestWarning'
    #超级电容自检故障
    Axis1backupTestError='.SC_Axis1backupTestError'
    Axis2backupTestError='.SC_Axis2backupTestError'
    Axis3backupTestError='.SC_Axis3backupTestError'
    
    LubricationSystemFault='.SC_LubricationSystemFault'
    #2号桨叶的PM出现故障
    PitchMasterAxis2error='.SC_PitchMasterAxis2error'
    CommunicationErrorPitchMasterAxis1='.SC_CommunicationErrorPitchMasterAxis1'
    CommunicationErrorPitchMasterAxis3='.SC_CommunicationErrorPitchMasterAxis3'
    SafetyLineTCUOpen='.SC_SafetyLineTCUOpen'
    EmmergencyModeCommandFromTCUViaFieldbus='.SC_EmmergencyModeCommandFromTCUViaFieldbus'
    SafetyRunStartedAutonomousByPitchmasterAxis2='.SC_SafetyRunStartedAutonomousByPitchmasterAxis2'
    SafetyRunTimeout='.SC_SafetyRunTimeout'
    GridSupplyErrorAxis1='.SC_GridSupplyErrorAxis1'#79
    GridSupplyErrorAxis3='.SC_GridSupplyErrorAxis3'
    DClinkFuseErrorAxis1='.SC_DClinkFuseErrorAxis1'
    DClinkFuseErrorAxis3='.SC_DClinkFuseErrorAxis3'
    DiodeMonitoringAxis2='.SC_DiodeMonitoringAxis2'
    Mainsupplycontactoropen='.SC_Mainsupplycontactoropen'#89
    #轴控柜充电故障0402091
    SC_ErrorChargerAxis2='.SC_ErrorChargerAxis2'
    SC_ErrorHeatingAxis1='.SC_ErrorHeatingAxis1'
    SC_ErrorHeatingAxis3='.SC_ErrorHeatingAxis3'
    SC_OvertemperatureBackupBox2='.SC_OvertemperatureBackupBox2'
    SC_UndertemperatureBackupBox1='.SC_UndertemperatureBackupBox1'
    SC_UndertemperatureBackupBox3='.SC_UndertemperatureBackupBox3'    
    SC_WireBreakTemperatureAxisBox2='.SC_WireBreakTemperatureAxisBox2'
    SC_WireBreakTemperatureBackupBox1='.SC_WireBreakTemperatureBackupBox1'
    SC_WireBreakTemperatureBackupBox3='.SC_WireBreakTemperatureBackupBox3'
    SC_WireBreakTemperatureMotorAxis2='.SC_WireBreakTemperatureMotorAxis2'
    #SC_WireBreakTemperatureMotorAxis2='.SC_WireBreakTemperatureMotorAxis2'
    SC_WireBreakTemperatureHub='.SC_WireBreakTemperatureHub'
    SC_ErrorFanPitchmasterAxis2='.SC_ErrorFanPitchmasterAxis2'
    SC_BackupSwitchopenaxis1='.SC_BackupSwitchopenaxis1'
    SC_BackupSwitchopenaxis3='.SC_BackupSwitchopenaxis3'#119
    SC_ContactorCyclesDCSupplyAxis2='.SC_ContactorCyclesDCSupplyAxis2'
    #中心柜温度过高故障123
    SC_OvertemperatureLBA='.SC_OvertemperatureLBA'
    #中心柜温度传感器断线故障#0402125
    SC_WireBreakTemperatureLBA='.SC_WireBreakTemperatureLBA'
    #轮毂温度过低警告127
    SC_UndertemperatureHub='.SC_UndertemperatureHub'
    #HVRT level2 警告129
    SC_HVRTLevel2detected='.SC_HVRTLevel2detected'
    #变桨系统处于低温预加热模式0402063
    SC_PitchHeatingMode='.SC_PitchHeatingMode'
    #主控制与变桨间的通讯故障0402035
    '.SC_PitchCommunicationError'
    #齿轮箱油池油位警告重复出现
    SC_RepFaultGearOilLevel='.SC_RepFaultGearOilLevel'
    #齿轮箱油池油位警告0205004
    SC_GearOilLevel_Warning='.SC_GearOilLevel_Warning'
    #齿轮箱油压高于上限值
    SC_GBXFilterOilPressure_MAX_STOP='.SC_GBXFilterOilPressure_MAX_STOP'
    #齿轮箱油池温度过高警告
    SC_TempGearOilSump_high='.SC_TempGearOilSump_high'
    SC_TempGearOilSump_low='.SC_TempGearOilSump_low'
     #齿轮箱油箱1分钟平均温度高于最高值或齿轮箱油温10分钟平均温度超过高温值达30分钟以上。(grTempGearOilSump_10min > PAR_rTempHigh_GearOilSump)
    SC_TempGearOilSump_MAX='.SC_TempGearOilSump_MAX'
    #齿轮箱油箱10分钟平均温度高于最低限值。grTempGearOilSump_10min < PAR_rTempMIN_GearOilSump)18
    SC_TempGearOilSump_MIN='.SC_TempGearOilSump_MIN'
    #齿轮箱入口10分钟平均油温高于设定值。(grTempGearOilInlet_10min > PAR_rTempHigh_GearOilInlet)19
    SC_TempGearOilInlet_high='.SC_TempGearOilInlet_high'
    #齿轮箱入口10分钟平均油温低于设定值。(grTempGearOilInlet_10min < PAR_rTempLow_GearOilInlet) 
    SC_TempGearOilInlet_low='.SC_TempGearOilInlet_low'
    #齿轮箱入口10分钟平均油温高于最高限值或高于设定值达30分钟之久。（grTempGearOilInlet_10min > PAR_rTempMAX_GearOilInlet OR bSTOP_DelayWarningElapsed=1）
    SC_TempGearOilInlet_MAX='.SC_TempGearOilInlet_MAX'
     #齿轮箱入口10分钟平均油温低于最低限值。(grTempGearOilInlet_10min < PAR_rTempMIN_GearOilInlet)  22
    SC_TempGearOilInlet_MIN='.SC_TempGearOilInlet_MIN'
    #齿轮箱油箱温度过高或过低的故障重复出现。(gbRepeat_02_05_015=1 OR gbRepeat_02_05_016=1)27
    SC_RepFaultTempGearOilSump='.SC_RepFaultTempGearOilSump'
    #齿轮箱驱动端轴承1分钟温度过高。(grTempGearBearingDE_1min > PAR_rTempHigh_GearBearingDE)28
    SC_TempGearBearingDE_high='.SC_TempGearBearingDE_high'
    #30齿轮箱驱动端轴承1分钟平均温度高于最高限值或高于设定值达30分钟之久。#grTempGearBearingDE_1min > PAR_rTempMAX_GearBearingDE OR bSTOP_DelayWarningElapsed=1
    SC_TempGearBearingDE_MAX='.SC_TempGearBearingDE_MAX'
    #33#齿轮箱非驱动端轴承10分钟平均温度高于设定值。(grTempGearBearingNDE_10min > PAR_rTempHigh_GearBearingNDE)
    SC_TempGearBearingNDE_high='.SC_TempGearBearingNDE_high'
    #35#齿轮箱非驱动端轴承1分钟平均油温高于上限值或10min平均油温高于设定值达30分钟之久。
    SC_TempGearBearingNDE_MAX='.SC_TempGearBearingNDE_MAX'    
    ##38齿轮箱驱动端轴承入口温度过高警告grTempGearBearinginterDE_1min > PAR_rTempHigh_GearBearinginterDE    
    SC_TempGearBearingInterDE_high='.SC_TempGearBearingInterDE_high'
    #39齿轮箱驱动端入口温度过高故障grTempGearBearinginterDE_1min > PAR_rTempMAX_GearBearinginterDE
    SC_TempGearBearingInterDE_MAX='.SC_TempGearBearingInterDE_MAX'
    #齿轮箱驱动端轴承入口温度过高警告41
    SC_TempGearBearingInterNDE_high='.SC_TempGearBearingInterNDE_high'
    #42 齿轮箱驱动端轴承入口温度过高故障 t119
    SC_TempGearBearingInterNDE_MAX='.SC_TempGearBearingInterNDE_MAX'
    #齿轮箱过滤器的油温过高SC_GearOilFilter_TempHigh
    SC_GearOilFilter_TempHigh='.SC_GearOilFilter_TempHigh'
    #45齿轮箱精滤器堵塞  giGearOilFilterOffLine_PresureHighCount>=3
    
    #sc0405017齿轮箱低速泵热继跳开
    SC_GBXOilPumpMotorLS_Overload='.SC_GBXOilPumpMotorLS_Overload'
    #018齿轮箱高速泵热继跳开
    SC_GBXOilPumpMotorHS_Overload='.SC_GBXOilPumpMotorHS_Overload'
    #20齿轮箱油入口压力过低故障
    SC_GBXOilInletPressureTooLow='.SC_GBXOilInletPressureTooLow'
    #齿轮箱中速轴(GSGS)温度高警告
    SC_GBXBearingIMS_GSGS_TempHigh='.SC_GBXBearingIMS_GSGS_TempHigh'
    #22齿轮箱中速轴(GSGS)温度高故障
    SC_GBXBearingIMS_GSGS_TempMax='.SC_GBXBearingIMS_GSGS_TempMax'
    #齿轮箱中速轴(GSRS)温度高警告 23
    SC_GBXBearingIMS_GSRS_TempHigh='.SC_GBXBearingIMS_GSRS_TempHigh'
    #齿轮箱中速轴(GSRS)温度高故障24
    SC_GBXBearingIMS_GSRS_TempMax='.SC_GBXBearingIMS_GSRS_TempMax'
    #齿轮箱中速轴(RS)温度高警告25
    SC_GBXBearingIMS_RS_TempHigh='.SC_GBXBearingIMS_RS_TempHigh'
    #齿轮箱高速轴(GSGS)温度高警告27
    SC_GBXBearingHSS_GSGS_TempHigh='.SC_GBXBearingHSS_GSGS_TempHigh'
    #齿轮箱高速轴(GSRS)温度高警告29
    SC_GBXBearingHSS_GSRS_TempHigh='.SC_GBXBearingHSS_GSRS_TempHigh'
    #齿轮箱中速轴(GSGS)PT100传感器故障  31
    SC_FaultAIAI_Gearbox_Bearing_IMS_GSGS_Temp='.SC_FaultAIAI_Gearbox_Bearing_IMS_GSGS_Temp'
    #齿轮箱中速轴(RS)温度高故障26
    SC_GBXBearingIMS_RS_TempMax='.SC_GBXBearingIMS_RS_TempMax'
    #齿轮箱高速轴(GSGS)温度高故障28
    SC_GBXBearingHSS_GSGS_TempMax='.SC_GBXBearingHSS_GSGS_TempMax'
    #齿轮箱高速轴(GSRS)温度高故障30
    SC_GBXBearingHSS_GSRS_TempMax='.SC_GBXBearingHSS_GSRS_TempMax'
    #齿轮箱中速轴(GSRS)PT100传感器故障32
    SC_FaultAIAI_Gearbox_Bearing_IMS_GSRS_Temp='.SC_FaultAIAI_Gearbox_Bearing_IMS_GSRS_Temp'
    #齿轮箱中速轴(RS)PT100传感器故障
    SC_FaultAIAI_Gearbox_Bearing_IMS_RS_Temp='.SC_FaultAIAI_Gearbox_Bearing_IMS_RS_Temp'
    #齿轮箱高速轴(GSGS)PT100传感器故障34
    SC_FaultAIAI_Gearbox_Bearing_HSS_GSGS_Temp='.SC_FaultAIAI_Gearbox_Bearing_HSS_GSGS_Temp'
    #齿轮箱高速轴(GSRS)PT100传感器故障35   
    SC_FaultAIAI_Gearbox_Bearing_HSS_GSRS_Temp='.SC_FaultAIAI_Gearbox_Bearing_HSS_GSRS_Temp'
    #齿轮箱高速轴(RS)PT100传感器故障
    SC_FaultAIAI_Gearbox_Bearing_HSS_RS_Temp='.SC_FaultAIAI_Gearbox_Bearing_HSS_RS_Temp'
    #齿轮箱高速轴(RS)温度高警告37
    SC_GBXBearingHSS_RS_TempHigh='.SC_GBXBearingHSS_RS_TempHigh'
    #SC_GBXBearingHSS_RS_TempMax38
    SC_GBXBearingHSS_RS_TempHigh='.SC_GBXBearingHSS_RS_TempHigh'
    #齿轮箱离线精滤器空开跳开39
    SC_GBXOfflineFitrationSystemMCB='.SC_GBXOfflineFitrationSystemMCB'
    #40齿轮箱油泵加热器空开跳开
    SC_GearOilPumpMotorPreheaterMCB='.SC_GearOilPumpMotorPreheaterMCB'
    #齿轮箱油泵滤网堵塞41
    SC_GearFilterPumpClogging='.SC_GearFilterPumpClogging'
    OC_NoMonitoringOfGearOilFilter='.OC_NoMonitoringOfGearOilFilter'
    #齿轮箱过滤器压差传感器故障
    SC_FaultAI_GearOilDiffPressureInlineFilter='.SC_FaultAI_GearOilDiffPressureInlineFilter'
    #齿轮箱入口压力过高故障47
    SC_GBXOilInletPressure_MAX_Stop='.SC_GBXOilInletPressure_MAX_Stop'
    #齿轮箱入口压力过高或过低故障重复出现 46
    
    #齿轮箱弹性支撑达到极限载荷报警48
    SC_GBXSupportGetsExtremeLoadWarning='.SC_GBXSupportGetsExtremeLoadWarning'
    #齿轮箱弹性支撑失效报警49
    SC_GBXSupportFailureWarning='.SC_GBXSupportFailureWarning'
    #齿轮箱左扭力臂位置传感器损坏50
    SC_FaultAI_GBXTorqueArmPositionLeft='.SC_FaultAI_GBXTorqueArmPositionLeft'
    #齿轮箱右扭力臂位置传感器损坏51
    SC_FaultAI_GBXTorqueArmPositionRight='.SC_FaultAI_GBXTorqueArmPositionRight'
    #齿轮箱驱动端轴承温度过于过高设定值或低于过低设定值故障重复出现 0205032
    SC_RepFaultTempGearBearingDE='.SC_RepFaultTempGearBearingDE'
    #齿轮箱非驱动端轴承温度高于过高设定值或低于过低设定值故障重复出现
    SC_RepFaultTempGearBearingNDE='.SC_RepFaultTempGearBearingNDE'
    #齿轮箱暖机超时0205110
    SC_GearboxHeatingModeTimeout='.SC_GearboxHeatingModeTimeout'
    #Scada发出50#刹车测试指令 0307005
    SC_TestBrakeProgram50='.SC_TestBrakeProgram50'
    #齿轮箱油泵加热器运行0202104
    #发电机10分钟平均功率高于上限值0208001
    SC_GenMaxPower10min='.SC_GenMaxPower10min'
    #发电机30秒平均功率高于上限值002
    SC_GenMaxPower30s='.SC_GenMaxPower30s'
    #发电机1秒平均功率高于上限值
    SC_GenMaxPower1s='.SC_GenMaxPower1s'
    #发电机10分钟平均功率高于上限值故障重复出现04
    SC_RepFaultGenMaxPower10min='.SC_RepFaultGenMaxPower10min'
    #外部设备测得发电机功率与变频器测得的差异大于设定值09
    
    #发电机30秒平均功率高于上限值故障重复出现40
    SC_RepFaultGenMaxPower30s='.SC_RepFaultGenMaxPower30s'
    #发电机1秒平均功率高于上限值故障重复出现41
    SC_RepFaultGenMaxPower1s='.SC_RepFaultGenMaxPower1s'
    #外部设备测得发电机功率与变频器测得的差异大于设定值0208009
    SC_DevicePowerUnequalGenPower='.SC_DevicePowerUnequalGenPower'
    #电网电压L1相超出上限值 0304002
    SC_GridVoltageL1_high='.SC_GridVoltageL1_high'
    #电网电压L2相超出上限值 0304003
    SC_GridVoltageL2_high='.SC_GridVoltageL2_high'
    #电网电压L3相超出上限值 0304004
    SC_GridVoltageL3_high='.SC_GridVoltageL3_high'
    #电网电压过高故障重复出现005
    SC_RepFaultGridVoltageHigh='.SC_RepFaultGridVoltageHigh'
    #电网电压L1相超出下限值
    SC_GridVoltageL1_low='.SC_GridVoltageL1_low'
    #电网电压L2相超出下限值
    SC_GridVoltageL2_low='.SC_GridVoltageL2_low'
    #电网电压L3相超出下限值
    SC_GridVoltageL3_low='.SC_GridVoltageL3_low'
    #电网电压过高故障重复出现009
    SC_RepFaultGridVoltageLow='.SC_RepFaultGridVoltageLow'
    #电网频率过高10
    SC_GridFrequencyHigh='.SC_GridFrequencyHigh'
    #电网频率过低11
    SC_GridFrequencyLow='.SC_GridFrequencyLow'
    #电网频率过高过低故障重复出现
    SC_RepFaultGridFrequency='.SC_RepFaultGridFrequency'
    #掉网故障0304018
    SC_GridLost_PowerFailure='.SC_GridLost_PowerFailure'
    #电网频率高于上限值20
    SC_GridFrequencyMax='.SC_GridFrequencyMax'
    #电网频率低于下限值21
    SC_GridFrequencyMin='.SC_GridFrequencyMin'
    #电网三相电流不平衡0304200
    SC_GridCurrentAsymmetric='.SC_GridCurrentAsymmetric'
    #电网测量设备故障0414001
    SC_PowerMeasurementUnit_Fail='.SC_PowerMeasurementUnit_Fail'
    #机舱温度过高警告0203001
    SC_TempNacelle_high='.SC_TempNacelle_high'
    #机舱温度过低警告0203002
    SC_TempNacelle_low='.SC_TempNacelle_low'
    #机舱温度过高故障0203003
    SC_TempNacelle_max='.SC_TempNacelle_max'
    #机舱温度过低故障0203004
    SC_TempNacelle_min='.SC_TempNacelle_min'
    #机舱温度过高或过低警告重复出现05
    SC_RepFaultTempNacelle='.SC_RepFaultTempNacelle'
    #舱外环境温度过高警告02 11 016
    SC_TempOutdoor_high='.SC_TempOutdoor_high'
    #舱外环境温度过低警告
    SC_TempOutdoor_low='.SC_TempOutdoor_low'
    #舱外环境温度过高故障
    SC_TempOutdoor_MAX='.SC_TempOutdoor_MAX'
    #舱外环境温度过低故障
    SC_TempOutdoor_MIN='.SC_TempOutdoor_MIN'
    #舱外环境温度过高或过低警告重复出现
    SC_RepFault_TempOutdoor='.SC_RepFault_TempOutdoor'
    #1秒平均风速高于上限值
    SC_ShutDownWindspeed_1sMax='.SC_ShutDownWindspeed_1sMax'
    #30秒平均风速高于上限值
    SC_ShutDownWindspeed_30sMax='.SC_ShutDownWindspeed_30sMax'
    #10平均风速高于上限值
    SC_ShutDownWindspeed_10minMax='.SC_ShutDownWindspeed_10minMax'
    #风速过低停机
    SC_ShutDownWindspeed_10minMin='.SC_ShutDownWindspeed_10minMin'
    #风速过高，不能手动变桨和手动操作风机
    SC_WindSpeedTooHighForManualModeOrService='.SC_WindSpeedTooHighForManualModeOrService'
    #机舱前后振动带通滤波值报警50
    SC_BandFilter_NacelleVibrationForaftAlarm='.SC_BandFilter_NacelleVibrationForaftAlarm'
    #机舱前后振动带通滤波值停机
    SC_BandFilter_NacelleVibrationForaftFault='.SC_BandFilter_NacelleVibrationForaftFault'
    #机舱前后振动带通滤波值报警重复出现
    SC_RepeatBandFilter_NacelleVibrationForaftAlarm='.SC_RepeatBandFilter_NacelleVibrationForaftAlarm'
    #机舱左右振动带通滤波值报警
    SC_BandFilter_NacelleVibrationSideSideAlarm='.SC_BandFilter_NacelleVibrationSideSideAlarm'
    #机舱左右振动带通滤波值停机
    SC_BandFilter_NacelleVibrationSideSideFault='.SC_BandFilter_NacelleVibrationSideSideFault'
    #机舱左右振动带通滤波值报警重复出现  55
    SC_RepeatBandFilter_NacelleVibrationSideSideAlarm='.SC_RepeatBandFilter_NacelleVibrationSideSideAlarm'
    #机舱出口风扇1空开跳开0409016
    SC_NacelleOutletFan1MCB='.SC_NacelleOutletFan1MCB'
    #机舱出口风扇1热继跳开
    SC_NacelleOutletFan1Overload='.SC_NacelleOutletFan1Overload'
    #机舱出口风扇2空开跳开
    SC_NacelleOutletFan2MCB='.SC_NacelleOutletFan2MCB'
     #机舱出口风扇2热继跳开
    SC_NacelleOutletFan2Overload='.SC_NacelleOutletFan2Overload'
    #FT加热器空开跳开
    SC_FTHeaterMCB='.SC_FTHeaterMCB'
    #风向标加热器空开跳开
    SC_AnalogWindDirectionHeaterMCB='.SC_AnalogWindDirectionHeaterMCB'
    #风速仪加热器空开跳开
    SC_AnalogWindSpeedHeaterMCB='.SC_AnalogWindSpeedHeaterMCB'
    #机舱出口气流调节器空开跳开
    SC_NacelleOutletDamperMCB='.SC_NacelleOutletDamperMCB'
    #机舱入口气流调节器空开跳开
    SC_NacelleInletDamperMCB='.SC_NacelleInletDamperMCB'
    #机舱加热器空开跳开
    SC_NacelleHeaterMCB='.SC_NacelleHeaterMCB'
    #航空灯空开跳开
    SC_AviationLightMCB='.SC_AviationLightMCB'
    
    #:skp>
    
    #dmr:
    NacelleFuseMotorHeater_GearFanAndOilPump='.SC_NacelleFuseMotorHeater_GearFanAndOilPump'
    FaultInputPT100_GearOilSump='.SC_FaultInputPT100_GearOilSump'
    FaultInputPT100_GearBearingDE='.SC_FaultInputPT100_GearBearingDE'
    FaultInputPT100_GearBearingInterNDE='.SC_FaultInputPT100_GearBearingInterNDE'
    FaultAI_GearOilPressureFilterInlet='.SC_FaultAI_GearOilPressureFilterInlet'
    GearOilFilter_Overload='.SC_GearOilFilter_Overload'
    GearOilFilterClogged_Warning='.SC_GearOilFilterClogged_Warning'
    RepFaultGearOilFilterClogged='.SC_RepFaultGearOilFilterClogged'
    UndervoltageBackupAxis2='.SC_UndervoltageBackupAxis2'
    OvervoltageBackupAxis1='.SC_OvervoltageBackupAxis1'
    OvervoltageBackupAxis3='.SC_OvervoltageBackupAxis3'
    OvertemperatureAxisBox2='.SC_OvertemperatureAxisBox2'
    UndertemperatureAxisBox1='.SC_UndertemperatureAxisBox1'
    UndertemperatureAxisBox3='.SC_UndertemperatureAxisBox3'
    WarnTcuActive='.SC_WarnTcuActive'
    ErrPcuActive='.SC_ErrPcuActive'
    Blade2DCLinkVoltageNotOK='.SC_Blade2DCLinkVoltageNotOK'
    SupplyAxis1='.SC_24VSupplyAxis1'
    SupplyAxis3='.SC_24VSupplyAxis3'
    PitchInLVRT='.SC_PitchInLVRT'
    OvertemperatureMotorAxis2='.SC_OvertemperatureMotorAxis2'
    UndertemperatureMotorAxis1='.SC_UndertemperatureMotorAxis1'
    UndertemperatureMotorAxis3='.SC_UndertemperatureMotorAxis3'
    TcuOpenSafetychainFirst='.SC_TcuOpenSafetychainFirst'
    #50:Axis1BackupMaintenanceRequired='.SC_Axis1BackupMaintenanceRequired'
    LubricationFuseError='.SC_LubricationFuseError'
    LubricationLowLevel='.SC_LubricationLowLevel'
    PitchMasterAxis1error='.SC_PitchMasterAxis1error'
    PitchMasterAxis3error='.SC_PitchMasterAxis3error'
    CommunicationErrorPitchMasterAxis2='.SC_CommunicationErrorPitchMasterAxis2'
    CommunicationErrorTCU='.SC_CommunicationErrorTCU'
    PCUOpensSafetyLineFirst='.SC_PCUOpensSafetyLineFirst'
    SafetyRunStartedAutonomousByPitchmasterAxis1='.SC_SafetyRunStartedAutonomousByPitchmasterAxis1'
    SafetyRunStartedAutonomousByPitchmasterAxis3='.SC_SafetyRunStartedAutonomousByPitchmasterAxis3'
    ContactorCyclesGridSupplyAxis='.SC_ContactorCyclesGridSupplyAxis'
    GridSupplyErrorAxis2='.SC_GridSupplyErrorAxis2'
    LVRTError='.SC_LVRTError'
    DCLinkFuseErrorAxis2='.SC_DCLinkFuseErrorAxis2'
    DiodeMonitoringAxis1='.SC_DiodeMonitoringAxis1'
    DiodeMonitoringAxis3='.SC_DiodeMonitoringAxis3'
    ErrorChargerAxis1='.SC_ErrorChargerAxis1'
    ErrorChargerAxis3='.SC_ErrorChargerAxis3'
    ErrorHeatingAxis2='.SC_ErrorHeatingAxis2'
    OvertemperatureBackupBox1='.SC_OvertemperatureBackupBox1'
    OvertemperatureBackupBox3='.SC_OvertemperatureBackupBox3'
    UndertemperatureBackupBox2='.SC_UndertemperatureBackupBox2'
    WireBreakTemperatureAxisBox1='.SC_WireBreakTemperatureAxisBox1'
    WireBreakTemperatureAxisBox3='.SC_WireBreakTemperatureAxisBox3'
    WireBreakTemperatureBackupBox2='.SC_WireBreakTemperatureBackupBox2'
    WireBreakTemperatureMotorAxis1='.SC_WireBreakTemperatureMotorAxis1'
    WireBreakTemperatureMotorAxis3='.SC_WireBreakTemperatureMotorAxis3'
    ErrorFanPitchmasterAxis1='.SC_ErrorFanPitchmasterAxis1'
    ErrorFanPitchmasterAxis3='.SC_ErrorFanPitchmasterAxis3'
    BackupSwitchopenaxis2='.SC_BackupSwitchopenaxis2'
    ContactorCyclesDCSupplyAxis1='.SC_ContactorCyclesDCSupplyAxis1'
    ContactorCyclesDCSupplyAxis3='.SC_ContactorCyclesDCSupplyAxis3'
    UndertemperatureLBA='.SC_UndertemperatureLBA'
    OvertemperatureHub='.SC_OvertemperatureHub'
    HVRTdetected='.SC_HVRTdetected'
    
    #Generator
    #SC02_02_036:
    MotorProtection_GenFanExternal='.SC_MotorProtection_GenFanExternal'
    #SC02_02_038:
    NacelleFuseGenSpaceHeater='.SC_NacelleFuseGenSpaceHeater'
    #SC02_02_067：
    FaultInputPT100_GeneratorStatorU='.SC_FaultInputPT100_GeneratorStatorU'
    #SC02_02_069:
    FaultInputPT100_GeneratorStatorV='.SC_FaultInputPT100_GeneratorStatorV'
    #SC02_02_071:
    FaultInputPT100_GeneratorStatorW='.SC_FaultInputPT100_GeneratorStatorW'
    #SC02_02_073:
    FaultInputPT100_GeneratorBearingDE='.SC_FaultInputPT100_GeneratorBearingDE'    
    #SC02_02_074:
    FaultInputPT100_GeneratorBearingNDE='.SC_FaultInputPT100_GeneratorBearingNDE'
    #SC02_02_128:
    MotorProtection_WCSG='.SC_MotorProtection_WCSG'
    #SC02_08_006:
    GeneratorBrushesWaste_Warning='.SC_GeneratorBrushesWaste_Warning'
    #SC02_08_007:
    GeneratorBrushesWaste_STOP='.SC_GeneratorBrushesWaste_STOP' 
    #SC02_08_012:
    GEN_StatorTempDiffExceedLimit='.SC_GEN_StatorTempDiffExceedLimit'
    #SC02_08_013:
    TempGenStatorU_high='.SC_TempGenStatorU_high'
    #SC02_08_014:
    TempGenStatorU_low='.SC_TempGenStatorU_low'
    #SC02_08_015:
    TempGenStatorU_MAX='.SC_TempGenStatorU_MAX'
    #SC02_08_016:
    TempGenStatorU_min='.SC_TempGenStatorU_min'
    #SC02_08_017:
    TempGenStatorV_high='.SC_TempGenStatorV_high'
    #SC02_08_018:
    TempGenStatorV_low='.SC_TempGenStatorV_low'
    #SC02_08_019:
    TempGenStatorV_MAX='.SC_TempGenStatorV_MAX'    
    #SC02_08_020:
    TempGenStatorV_MIN='.SC_TempGenStatorV_MIN'  
    #SC02_08_021:
    TempGenStatorW_high='.SC_TempGenStatorW_high'
    #SC02_08_022:
    TempGenStatorW_low='.SC_TempGenStatorW_low'
    #SC02_08_023:
    TempGenStatorW_MAX='.SC_TempGenStatorW_MAX'    
    #SC02_08_024:
    TempGenStatorW_MIN='.SC_TempGenStatorW_MIN'
    #SC02_08_025:
    RepFaultTempGenStator='.SC_RepFaultTempGenStator'
    #SC02_08_026:
    TempGenBearingDE_high='.SC_TempGenBearingDE_high'
    #SC02_08_027:
    TempGenBearingDE_low='.SC_TempGenBearingDE_low'
    #SC02_08_028:
    TempGenBearingDE_MAX='.SC_TempGenBearingDE_MAX'
    #SC02_08_029:
    TempGenBearingDE_MIN='.SC_TempGenBearingDE_MIN'
    #SC02_08_030:
    TempGenBearingNDE_high='.SC_TempGenBearingNDE_high'
    #SC02_08_031:
    TempGenBearingNDE_low='.SC_TempGenBearingNDE_low'
    #SC02_08_032:
    TempGenBearingNDE_MAX='.SC_TempGenBearingNDE_MAX'
    #SC02_08_033:
    TempGenBearingNDE_MIN='.SC_TempGenBearingNDE_MIN'
    #SC02_08_034:
    RepFaultTempGenBearing='.SC_RepFaultTempGenBearing'
    #SC02_08_035:
    TempGenCoolingInletOrOutlet_high='.SC_TempGenCoolingInletOrOutlet_high'
    #SC02_08_036:
    TempGenCoolingInletOrOutlet_low='.SC_TempGenCoolingInletOrOutlet_low'
    #SC02_08_037:
    TempGenCoolingInletOrOutlet_MAX='.SC_TempGenCoolingInletOrOutlet_MAX'
    #SC02_08_038:
    TempGenCoolingInletOrOutlet_MIN='.SC_TempGenCoolingInletOrOutlet_MIN'
    #SC02_08_039:
    RepFaultTempGenCoolingInletOrOutlet='.SC_RepFaultTempGenCoolingInletOrOutlet'
    #SC02_08_002:
    GenMaxPower30s='.SC_GenMaxPower30s'
    #SC02_08_042:
    FaultPT100_GenCoolingInlet='.SC_FaultPT100_GenCoolingInlet'
    #SC02_08_043:
    FaultPT100_GenCoolingOutlet='.SC_FaultPT100_GenCoolingOutlet'
    #SC02_08_100:
    TempGenStatorDewShortCircui='.SC_TempGenStatorDewShortCircuit'
    #SC04_06_001:
    TempGenStatorU1Error='.SC_TempGenStatorU1Error'
    #SC04_06_002:
    TempGenStatorU2Error='.SC_TempGenStatorU2Error'
    #SC04_06_005:
    TempGenStatorV1Error='.SC_TempGenStatorV1Error'
    #SC04_06_006:
    TempGenStatorV2Error='.SC_TempGenStatorV2Error'
    #SC04_06_009:
    TempGenStatorW1Error='.SC_TempGenStatorW1Error'
    #SC04_06_010:
    TempGenStatorW2Error='.SC_TempGenStatorW2Error'
    #SC04_06_035:
    GENWaterLeakWarning='.SC_GENWaterLeakWarning'
    #SC04_06_036:
    GENLubricationWarning='.SC_GENLubricationWarning'
    #SC02_08_117:
    GenWaterCoolPumpAlarm='.SC_GenWaterCoolPumpAlarm'
    #SC02_08_118:
    GLGenWaterCoolInletPT100Fault='.SC_GLGenWaterCoolInletPT100Fault'
    #SC02_08_122:
    GLGenWaterCoolInletTempHigh2='.SC_GLGenWaterCoolInletTempHigh2'
    #SC02_08_124:
    GLGenWaterCoolOutletTempHigh='.SC_GLGenWaterCoolOutletTempHigh'
    #SC02_08_125:
    GLGenWaterCoolInletPreHigh2='.SC_GLGenWaterCoolInletPreHigh2'
    #SC02_08_128:
    GLGenWaterCoolInletPreLow2='.SC_GLGenWaterCoolInletPreLow2'
    #SC02_08_130:
    GLGenWaterCoolOutletPreLow2='.SC_GLGenWaterCoolOutletPreLow2'
    #SC02_08_133:
    GenWaterCoolInOutPressureDiffHigh='.SC_GenWaterCoolInOutPressureDiffHigh'
    #SC02_08_134:
    GenWaterCoolInOutPressureDiffLow='.SC_GenWaterCoolInOutPressureDiffLow'
    #SC02_08_136:
    GenWaterCoolHeaterOnTooLong='.SC_GenWaterCoolHeaterOnTooLong'
    #SC04_08_005:
    CS_Pump1LowControlManualMode='.SC_CS_Pump1LowControlManualMode'
    #SC04_08_006:
    CS_Pump2LowControlManualMode='.SC_CS_Pump2LowControlManualMode'
    #SC04_08_007:
    CS_Pump1LowControlForcelMode='.SC_CS_Pump1LowControlForcelMode'
    #SC04_08_008:
    CS_Pump2LowControlForcelMode='.SC_CS_Pump2LowControlForcelMode'
    #SC04_08_009:
    CS_Pump1HighControlManualMode='.SC_CS_Pump1HighControlManualMode'
    #SC04_08_010:
    CS_Pump2HighControlManualMode='.SC_CS_Pump2HighControlManualMode'
    #SC04_08_011:
    CS_Pump1HighControlForcelMode='.SC_CS_Pump1HighControlForcelMode'
    #SC04_08_012:
    CS_Pump2HighControlForcelMode='.SC_CS_Pump2HighControlForcelMode'
    #SC04_08_013:
    CS_GENOutletTempHighWarining='.SC_CS_GENOutletTempHighWarining'
    #SC04_08_014:
    CS_PreLowWaringing='.SC_CS_PreLowWaringing'
    #SC04_08_015:
    CS_PreLowError='.SC_CS_PreLowError'
    #SC04_08_016:
    CS_PumpOutputTempSensorFault='.SC_CS_PumpOutputTempSensorFault'
    #SC04_08_017:
    CS_GENOutletTempSensorFault='.SC_CS_GENOutletTempSensorFault'
    #SC04_08_018:
    CS_GBXOutletTempSensorFault='.SC_CS_GBXOutletTempSensorFault'
    #SC04_08_019:
    CS_PumpOutletPreSensorFault='.SC_CS_PumpOutletPreSensorFault'
    #SC04_08_020:
    CS_PumpInletPreSensorFault='.SC_CS_PumpInletPreSensorFault'
    #SC04_08_021:
    CS_Pump1LowOverload='.SC_CS_Pump1LowOverload'
    #SC04_08_022:
    CS_Pump2LowOverload='.SC_CS_Pump2LowOverload'
    #SC04_08_023:
    CS_Pump1HighOverload='.SC_CS_Pump1HighOverload'
    #SC04_08_024:
    CS_Pump2HighOverload='.SC_CS_Pump2HighOverload'
    #SC04_08_025:
    CS_Pump1MCB='.SC_CS_Pump1MCB'
    #SC04_08_026:
    CS_Pump2MCB='.SC_CS_Pump2MCB'
    #SC04_08_027:
    CS_GBXOutletTempHighWarining='.SC_CS_GBXOutletTempHighWarining'
    #SC04_08_031:
    TCS_Pump1_MCB='.SC_TCS_Pump1_MCB'
    #SC04_08_032:
    TCS_Pump2_MCB='.SC_TCS_Pump2_MCB'
    #SC04_08_033:
    TCS_Pumps_MCB='.SC_TCS_Pumps_MCB'
    #SC04_08_035:
    TCSPump2Failure_NoPressure='.SC_TCSPump2Failure_NoPressure'
    #SC04_08_037:
    TCS_Heater_MCB='.SC_TCS_Heater_MCB'
    #SC04_08_038:
    TCS_InletWaterTempLow_Warning='.SC_TCS_InletWaterTempLow_Warning'
    #SC04_08_039:
    TCS_InletWaterPT100Fault='.SC_TCS_InletWaterPT100Fault'
    #SC04_08_042:
    TCS_InsideFan1_MCB='.SC_TCS_InsideFan1_MCB'
    #SC04_08_043:
    TCS_InsideFan2_MCB='.SC_TCS_InsideFan2_MCB'
    #SC04_08_046:
    TCS_Cooler1FanA_Overload='.SC_TCS_Cooler1FanA_Overload'
    #SC04_08_047:
    TCS_Cooler1FanB_Overload='.SC_TCS_Cooler1FanB_Overload'
    #SC04_08_048:
    TCS_Cooler2FanA_Overload='.SC_TCS_Cooler2FanA_Overload'
    #SC04_08_049:
    TCS_Cooler2FanB_Overload='.SC_TCS_Cooler2FanB_Overload'
    #SC04_08_050:
    TCS_Cooler3FanA_Overload='.SC_TCS_Cooler3FanA_Overload'
    #SC04_08_051:
    TCS_Cooler3FanB_Overload='.SC_TCS_Cooler3FanB_Overload'
    #SC04_08_052:
    TCS_Cooler4FanA_Overloa='.SC_TCS_Cooler4FanA_Overload'
    #SC04_08_053:
    TCS_Cooler4FanB_Overload='.SC_TCS_Cooler4FanB_Overload'
    #SC04_08_054:
    TCS_Cooler1Fans_MCB='.SC_TCS_Cooler1Fans_MCB'
    #SC04_08_055:
    TCS_Cooler2Fans_MCB='.SC_TCS_Cooler2Fans_MCB'
    #SC04_08_056:
    TCS_Cooler3Fans_MCB='.SC_TCS_Cooler3Fans_MCB'
    #SC04_08_057:
    TCS_Cooler4Fans_MCB='.SC_TCS_Cooler4Fans_MCB'    
    #:dmr>
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
class Scada():
    #SCADA接口 10min停机风速
    minwindspeed_10min = '.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rMinWindSpeed_10min'
    #SCADA接口 SCADA限功率
    powerLimitFromSCADA = '.SCADA.TurbineStateMachine.Process.Ctrl_grPowerLimitFromSCADA'    
    #齿轮箱类型
    par_igearboxtype = ".SCADA.Gearbox.Parameter.Ctrl_PAR_iGearBoxType"
    
    EnableFuseHeater_GearOilPipe='.SCADA.Gearbox.Parameter.Ctrl_PAR_bGBX_EnableFuseHeater_GearOilPipe'
    bWinergyGearboxOilInletNoPT100='.SCADA.Gearbox.Parameter.Ctrl_PAR_bWinergyGearboxOilInletNoPT100'
    vPAR_rTempGearOilFilterMonitor='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempGearOilFilterMonitor'
    tDelayGearOilFilterClogged_STOP='.SCADA.Gearbox.Parameter.Ctrl_PAR_tDelayGearOilFilterClogged_STOP'
    
    Par_rPitchBackupMinVolt='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchBackupMinVolt'
    Par_rPitchBackupMaxVolt='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchBackupMaxVolt'
    #1号轴控柜温度过高故障 sc0402019
    Par_rPitchAxisBoxMaxTemp='.SCADA.PitchSystem.Parameter.Ctrl_Par_rPitchAxisBoxMaxTemp'
    #号轴控柜温度过低故障
    Par_rPitchAxisBoxMinTemp='.SCADA.PitchSystem.Parameter.Ctrl_Par_rPitchAxisBoxMinTemp'
    #1号变桨电机温度过高故障0402039
    Par_rPitchMotorMaxTemp='.SCADA.PitchSystem.Parameter.Ctrl_Par_rPitchMotorMaxTemp'
    Par_rPitchMotorMinTemp='.SCADA.PitchSystem.Parameter.Ctrl_Par_rPitchMotorMinTemp'
    #中心柜温度过高故障0402123
    PAR_rPitchLBAMaxTemp='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchLBAMaxTemp'
    #中心柜温度传感器断线故障125
    #'.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchLBAMaxTemp'
    #轮毂温度过低警告0402127
    PAR_rPitchHubMinTemp='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchHubMinTemp'
    PAR_tDelayGearOilLevel_Warning='.SCADA.Gearbox.Parameter.Ctrl_PAR_tDelayGearOilLevel_Warning'
    PAR_rTempGearOillevelmoniter='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempGearOillevelmoniter'
    PAR_rGearOilpressure_Max='.SCADA.Gearbox.Parameter.Ctrl_PAR_rGearOilpressure_Max'
    PAR_rTempHigh_GearOilSump='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempHigh_GearOilSump'
    #齿轮箱油箱10分钟平均温度低于设定值。(grTempGearOilSump_10min < PAR_rTempLow_GearOilSump)
    PAR_rTempLow_GearOilSump='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempLow_GearOilSump'
    #齿轮箱油箱1分钟平均温度高于最高值或齿轮箱油温10分钟平均温度超过高温值达30分钟以上。(grTempGearOilSump_10min > PAR_rTempHigh_GearOilSump) 
    PAR_rTempMAX_GearOilSump='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempMAX_GearOilSump'
    #齿轮箱油箱10分钟平均温度高于最低限值。grTempGearOilSump_10min < PAR_rTempMIN_GearOilSump)
    PAR_rTempMIN_GearOilSump='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempMIN_GearOilSump'
    #齿轮箱入口10分钟平均油温高于设定值。(grTempGearOilInlet_10min > PAR_rTempHigh_GearOilInlet)
    PAR_rTempHigh_GearOilInlet='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempHigh_GearOilInlet' 
    #齿轮箱入口10分钟平均油温低于设定值。(grTempGearOilInlet_10min < PAR_rTempLow_GearOilInlet)   20
    PAR_rTempLow_GearOilInlet='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempLow_GearOilInlet' 
    par_bwinergygearboxoilinletnopt100='.SCADA.Gearbox.Parameter.Ctrl_PAR_bWinergyGearboxOilinletNoPT100'
    #齿轮箱入口10分钟平均油温高于最高限值或高于设定值达30分钟之久。（grTempGearOilInlet_10min > PAR_rTempMAX_GearOilInlet OR bSTOP_DelayWarningElapsed=1）
    PAR_rTempMAX_GearOilInlet='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempMAX_GearOilInlet'
    #齿轮箱入口10分钟平均油温低于最低限值。(grTempGearOilInlet_10min < PAR_rTempMIN_GearOilInlet)  22
    PAR_rTempMIN_GearOilInlet='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempMIN_GearOilInlet'
    #齿轮箱驱动端轴承1分钟温度过高。(grTempGearBearingDE_1min > PAR_rTempHigh_GearBearingDE)28
    PAR_rTempHigh_GearBearingDE='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempHigh_GearBearingDE'
    #30齿轮箱驱动端轴承1分钟平均温度高于最高限值或高于设定值达30分钟之久。#grTempGearBearingDE_1min > PAR_rTempMAX_GearBearingDE OR bSTOP_DelayWarningE
    PAR_rTempMAX_GearBearingDE='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempMAX_GearBearingDE '
    #33#齿轮箱非驱动端轴承10分钟平均温度高于设定值。(grTempGearBearingNDE_10min > PAR_rTempHigh_GearBearingNDE)
    PAR_rTempHigh_GearBearingNDE='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempHigh_GearBearingNDE'
    #35#齿轮箱非驱动端轴承1分钟平均油温高于上限值或10min平均油温高于设定值达30分钟之久。
    PAR_rTempMAX_GearBearingNDE='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempMAX_GearBearingNDE'    
    #38 齿轮箱驱动端轴承入口温度过高警告grTempGearBearinginterDE_1min > PAR_rTempHigh_GearBearinginterDE 
    PAR_rTempHigh_GearBearinginterDE='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempHigh_GearBearinginterDE'
    #39齿轮箱驱动端轴承入口温度过高故障grTempGearBearinginterDE_1min > PAR_rTempMAX_GearBearinginterDE
    PAR_rTempMAX_GearBearinginterDE='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempMAX_GearBearinginterDE'
    #41 齿轮箱驱动端轴承入口温度过高警告t118 
    PAR_rTempHigh_GearBearinginterNDE='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempHigh_GearBearinginterNDE'
    #42 齿轮箱驱动端轴承入口温度过高故障 t119
    PAR_rTempMax_GearBearinginterNDE='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempMax_GearBearinginterNDE'
    #齿轮箱过滤器的油温过高43
    PAR_bGBX_OilFilter_Enable='.SCADA.Gearbox.Parameter.Ctrl_PAR_bGBX_OilFilter_Enable'
    PAR_rGBX_OilFilter_StopTemp='.SCADA.Gearbox.Parameter.Ctrl_PAR_rGBX_OilFilter_StopTemp'
    #45齿轮箱精滤器堵塞  giGearOilFilterOffLine_PresureHighCount>=3
    #20齿轮箱油入口压力过低故障
    PAR_rGearOilPressure_MIN_PumpLS='.SCADA.Gearbox.Parameter.Ctrl_PAR_rGearOilPressure_MIN_PumpLS'
    #齿轮箱中速轴(GSGS)温度高警告21
    PAR_rTempGBXBearingiMSHigh='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempGBXBearingiMSHigh'
    #22齿轮箱中速轴(GSGS)温度高故障 26
    PAR_rTempGBXBearingiMSMax='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempGBXBearingiMSMax'
    #齿轮箱中速轴(GSRS)温度高警告 23
    #齿轮箱高速轴(GSGS)温度高警告27
    PAR_rTempGBXBearingHSSHigh='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempGBXBearingHSSHigh'
    #齿轮箱高速轴(GSGS)温度高故障28
    PAR_rTempGBXBearingHSSMax='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempGBXBearingHSSMax'
        #  0405041  shi OC_NoMonitoringOfGearOilFilter  =0
    PAR_rTempGearOilFilterMonitor='.SCADA.Gearbox.Parameter.Ctrl_PAR_rTempGearOilFilterMonitor'
    #齿轮箱入口压力过高故障47
    PAR_rGearOilPressure_MAX='.SCADA.Gearbox.Parameter.Ctrl_PAR_rGearOilPressure_MAX'
    #齿轮箱弹性支撑达到极限载荷报警48
    PAR_rGBXTorqueArmPositionWarming='.SCADA.Gearbox.Parameter.Ctrl_PAR_rGBXTorqueArmPositionWarming'
    PAR_rGBXTorqueArmPositionNormal='.SCADA.Gearbox.Parameter.Ctrl_PAR_rGBXTorqueArmPositionNormal'
    #齿轮箱弹性支撑失效报警49
    PAR_rGBXTorqueArmPositionAlarm='.SCADA.Gearbox.Parameter.Ctrl_PAR_rGBXTorqueArmPositionAlarm'
    #Scada发出50#刹车测试指令 0307005
    RemCmdACK_bTestBP50='.RemCmdACK_bTestBP50'
    #齿轮箱过滤器压力过大0205044
    PRG_SC02_05_044_bEnable='PRG_SC02_05_044.bEnable'
    #发电机10分钟平均功率高于上限值0208001
    PAR_rMaxPower10min='.SCADA.GridMeasurement.Parameter.Ctrl_PAR_rMaxPower10min'
    #发电机30秒平均功率高于上限值002
    PAR_rMaxPower30sec='.SCADA.GridMeasurement.Parameter.Ctrl_PAR_rMaxPower30sec'
    #发电机1秒平均功率高于上限值   3 
    PAR_rMaxPower1sec='.SCADA.GridMeasurement.Parameter.Ctrl_PAR_rMaxPower1sec'
    #发电机10分钟平均功率高于上限值故障重复出现04
    
    #外部设备测得发电机功率与变频器测得的差异大于设定值09    
    #外部设备测得发电机功率与变频器测得的差异大于设定值0208009
    PAR_rPower100msDiffMax='.SCADA.GridMeasurement.Parameter.Ctrl_PAR_rPower100msDiffMax'
    
    PAR_iConverterType=	'.SCADA.ConverterContainer.Parameter.Ctrl_PAR_iConverterType'
    #电网电压L1相超出上限值
    #PAR_rsimuCVT_GridVoltage='.SCADA.ConverterContainer.Parameter.Ctrl_PAR_rsimuCVT_GridVoltage'
    
    #电网频率过高10
    PAR_rGridFrequencyHigh_Hz	='.SCADA.GridMeasurement.Parameter.Ctrl_PAR_rGridFrequencyHigh_Hz'
    #电网频率过低11
    PAR_rGridFrequencyLow_Hz='.SCADA.GridMeasurement.Parameter.Ctrl_PAR_rGridFrequencyLow_Hz'
    #掉网故障0304018
    PAR_rVoltageForGridLost_Volt='.SCADA.GridMeasurement.Parameter.Ctrl_PAR_rVoltageForGridLost_Volt'
    #电网频率高于上限值20
    PAR_rGridFrequencyMAX_Hz='.SCADA.GridMeasurement.Parameter.Ctrl_PAR_rGridFrequencyMAX_Hz'
    #电网频率di于xia限值21
    PAR_rGridFrequencyMIN_Hz='.SCADA.GridMeasurement.Parameter.Ctrl_PAR_rGridFrequencyMIN_Hz'    
    #电网三相电流不平衡0304200
    PAR_rMaxCurrentDiff_A='.SCADA.GridMeasurement.Parameter.Ctrl_PAR_rMaxCurrentDiff_A'
    #机舱温度过高警告0203001
    PAR_rTempHigh_Nacelle='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rTempHigh_Nacelle'
    #机舱温度过低警告0203002
    PAR_rTempLow_Nacelle='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rTempLow_Nacelle'
    #机舱温度过高故障0203003
    PAR_rTempMAX_Nacelle='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rTempMAX_Nacelle'
    #机舱温度过低故障0203004
    PAR_rTempMIN_Nacelle='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rTempMIN_Nacelle'
    #机舱温度过高或过低警告重复出现05
    
    #舱外环境温度过高警告02 11 016
    PAR_rTempHigh_Outdoor='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rTempHigh_Outdoor'
    #舱外环境温度过低警告17
    PAR_rTempLow_Outdoor='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rTempLow_Outdoor'
    #舱外环境温度过高故障18
    PAR_rTempOutdoorOutOfSpecMAX='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rTempOutdoorOutOfSpecMAX'
    #舱外环境温度过低故障
    PAR_rTempOutdoorOutOfSpecMIN='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rTempOutdoorOutOfSpecMIN'
    #1秒平均风速高于上限值
    PAR_rMaxWindSpeed_1sec='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rMaxWindSpeed_1sec'
    #30秒平均风速高于上限值
    PAR_rMaxWindSpeed_30sec='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rMaxWindSpeed_30sec'
    #10平均风速高于上限值
    PAR_rMaxWindSpeed_10min='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rMaxWindSpeed_10min'
    #风速过低停机
    PAR_rMinWindSpeed_10min='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rMinWindSpeed_10min'
    #风速过高，不能手动变桨和手动操作风机
    PAR_rMaxWindForManualModeOrService='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rMaxWindForManualModeOrService'
    #机舱前后振动带通滤波值报警       
    PAR_rBandFilterNacelleForaftVibrationAlarm='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rBandFilterNacelleForaftVibrationAlarm'
    #机舱前后振动带通滤波值停机
    PAR_rBandFilterNacelleForaftVibrationFault='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rBandFilterNacelleForaftVibrationFault'
    #机舱左右振动带通滤波值报警
    PAR_rBandFilterNacelleSideSideVibrationAlarm='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rBandFilterNacelleSideSideVibrationAlarm'
    #机舱左右振动带通滤波值停机
    PAR_rBandFilterNacelleSideSideVibrationFault='.SCADA.NacelleSystem.Parameter.Ctrl_PAR_rBandFilterNacelleSideSideVibrationFault'
    
    SC_GBXBearingIMS_RS_TempMax_todisable='.SCADA.Gearbox.SC.SC_GBXBearingIMS_RS_TempMax_todisable'                     #SC04_05_026
    SC_GBXBearingIMS_GSRS_TempMax_todisable='.SCADA.Gearbox.SC.SC_GBXBearingIMS_GSRS_TempMax_todisable'                 #SC04_05_024 
    SC_GBXBearingIMS_GSGS_TempMax_todisable='.SCADA.Gearbox.SC.SC_GBXBearingIMS_GSGS_TempMax_todisable'                 #SC04_05_022 
    SC_GBXBearingHSS_GSGS_TempMax='.SCADA.Gearbox.SC.SC_GBXBearingHSS_GSGS_TempMax_todisable'                           #SC04_05_028
    SC_ErrTcuActive_todisable0='.SCADA.PitchSystem.SC.SC_ErrTcuActive_todisable'                                        #SC04_02_027
    SC_Axis2backupTestError_todisable0='.SCADA.PitchSystem.SC.SC_Axis2backupTestError_todisable'                            #SC04_02_057
    SC_CVT_MinInterval_TwiceCharge_Waiting0='.SCADA.ConverterContainer.SC.SC_CVT_MinInterval_TwiceCharge_Waiting_todisable' #SC04_12_026
    SC_Safety_Loop_Open_todisable0='.SCADA.SafetySystem.SC.SC_Safety_Loop_Open_todisable'                                       #0401001 禁用
    SC_Blade1_EndPos91Deg_todisable='.SCADA.Pitchsystem.SC.SC_Blade1_EndPos91Deg_todisable'                                 #SC01_05_011
    SC_Blade2_EndPos91Deg_todisable='.SCADA.Pitchsystem.SC.SC_Blade2_EndPos91Deg_todisable'                                 #SC01_05_031
    SC_Blade3_EndPos91Deg_todisable='.SCADA.Pitchsystem.SC.SC_Blade3_EndPos91Deg_todisable'                                 #SC01_05_051
    SC_AllBlades_EndPos91Or95_todisable='.SCADA.Pitchsystem.SC.SC_AllBlades_EndPos91Or95_todisable'                         #SC01_05_063
    OC_NoMonitoringOfGearOilFilter_todisable='.SCADA.GearBox.SC.OC_NoMonitoringOfGearOilFilter_todisable'                   #SC02_05_100
    SC_DevicePowerUnequalGenPower_todisable='.SCADA.GridMeasurement.SC.SC_DevicePowerUnequalGenPower_todisable'             #SC02_08_009
    SC_GBXSupportFailureWarning_todisable='.SCADA.Gearbox.SC.SC_GBXSupportFailureWarning_todisable'                         #SC04_05_049
    SC_DevicePowerUnequalGenPower009='.SCADA.GridMeasurement.SC.SC_DevicePowerUnequalGenPower_todisable'
    #:skp>
    
    
    #dmr:
    #齿轮箱过滤器温度监控
    par_rTempGearOilFilterMonitor= ".SCADA.Gearbox.Parameter.Ctrl_PAR_rTempGearOilFilterMonitor"
    #最小后备电源电压
    Par_rPitchBackupMinVolt='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchBackupMinVolt'
    #最大后备电源电压
    Par_rPitchBackupMaxVolt='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchBackupMaxVolt'
    #最大盒温度
    Par_rPitchAxisBoxMaxTemp='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchAxisBoxMaxTemp'
    #最小盒温度
    Par_rPitchAxisBoxMinTemp='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchAxisBoxMinTemp'
    #最大电机温度
    Par_rPitchMotorMaxTemp='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchMotorMaxTemp'
    #最小电机温度
    Par_rPitchMotorMinTemp='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchMotorMinTemp'
    #后备电源柜最大温度
    Par_rPitchBackupMaxTemp='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchBackupMaxTemp'
    #后备电源柜最小温度
    Par_rPitchBackupMinTemp='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchBackupMinTemp'
    #中心柜最小温度
    Par_rPitchLBAMinTemp='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchLBAMinTemp'
    #轮毂最高温度
    Par_rPitchHubMaxTemp='.SCADA.PitchSystem.Parameter.Ctrl_PAR_rPitchHubMaxTemp' 
    #机舱柜中发电机冷却风扇保护空开跳开
    Par_iGenType='.SCADA.Generator.Parameter.Ctrl_PAR_iGenType'
    #SC02_02_007：
    PAR_tWarningToSTOP_GeneratorBrushes='.SCADA.Generator.Parameter.Ctrl_PAR_tWarningToSTOP_GeneratorBrushes'
    #SC02_08_012:发电机定子两相绕组温差大于设定值
    PAR_rGEN_StatorTempDiffMAX='.SCADA.Generator.Parameter.Ctrl_PAR_rGEN_StatorTempDiffMAX'
    #SC02_08_013:发电机定子U相绕组温度过高警告
    PAR_rTempHigh_GenStator='.SCADA.Generator.Parameter.Ctrl_PAR_rTempHigh_GenStator' 
    #SC02_08_014:发电机定子U相绕组温度过低警告
    PAR_rTempLow_GenStator='.SCADA.Generator.Parameter.Ctrl_PAR_rTempLow_GenStator' 
    #SC02_08_015:发电机定子U相绕组温度过高故障
    PAR_rTempMAX_GenStator='.SCADA.Generator.Parameter.Ctrl_PAR_rTempMAX_GenStator'
    #SC02_08_016:发电机定子U相绕组温度过低故障
    PAR_rTempMIN_GenStator='.SCADA.Generator.Parameter.Ctrl_PAR_rTempMIN_GenStator'
    
    #SC02_08_026:发电机驱动端轴承温度过高警告
    PAR_rTempHigh_GenBearDE='.SCADA.Generator.Parameter.Ctrl_PAR_rTempHigh_GenBearDE'
    #SC02_08_027:发电机驱动端轴承温度过低警告
    PAR_rTempLow_GenBearDE='.SCADA.Generator.Parameter.Ctrl_PAR_rTempLow_GenBearDE'
    #SC02_08_028:发电机驱动端轴承温度过高故障
    PAR_rTempMAX_GenBearDE='.SCADA.Generator.Parameter.Ctrl_PAR_rTempMAX_GenBearDE'
    #SC02_08_029:发电机驱动端轴承温度过低故障
    PAR_rTempMIN_GenBearDE='.SCADA.Generator.Parameter.Ctrl_PAR_rTempMIN_GenBearDE'
    #SC02_08_030:发电机非驱动端轴承温度过高警告
    PAR_rTempHigh_GenBearNDE='.SCADA.Generator.Parameter.Ctrl_PAR_rTempHigh_GenBearNDE'
    #SC02_08_031:发电机非驱动端轴承温度过低警告
    PAR_rTempLow_GenBearNDE='.SCADA.Generator.Parameter.Ctrl_PAR_rTempLow_GenBearNDE'
    #SC02_08_032:发电机非驱动端轴承温度过高故障
    PAR_rTempMAX_GenBearNDE='.SCADA.Generator.Parameter.Ctrl_PAR_rTempMAX_GenBearNDE'
    #SC02_08_033:发电机非驱动端轴承温度过低故障
    PAR_rTempMIN_GenBearNDE='.SCADA.Generator.Parameter.Ctrl_PAR_rTempMIN_GenBearNDE' 
    #SC02_08_035:发电机冷却系统入口或出口温度过高警告
    PAR_rTempHigh_GenCoolingInlet='.SCADA.Generator.Parameter.Ctrl_PAR_rTempHigh_GenCoolingInlet'
    PAR_rTempHigh_GenCoolingOutlet='.SCADA.Generator.Parameter.Ctrl_PAR_rTempHigh_GenCoolingOutlet'
    PAR_bGenWithTempInOutlet='.SCADA.Generator.Parameter.Ctrl_PAR_bGenWithTempInOutlet'
    #SC02_08_036:发电机冷却系统入口或出口温度过低警告
    PAR_rTempLow_GenCoolingInlet='.SCADA.Generator.Parameter.Ctrl_PAR_rTempLow_GenCoolingInlet' 
    PAR_rTempLow_GenCoolingOutlet='.SCADA.Generator.Parameter.Ctrl_PAR_rTempLow_GenCoolingOutlet'
    #SC02_08_037:发电机冷却系统入口或出口温度过高故障
    PAR_rTempMAX_GenCoolingInlet='.SCADA.Generator.Parameter.Ctrl_PAR_rTempMAX_GenCoolingInlet'
    PAR_rTempMAX_GenCoolingOutlet='.SCADA.Generator.Parameter.Ctrl_PAR_rTempMAX_GenCoolingOutlet'
    #SC02_08_038:发电机冷却系统入口或出口温度过低故障
    PAR_rTempMIN_GenCoolingInlet='.SCADA.Generator.Parameter.Ctrl_PAR_rTempMIN_GenCoolingInlet'
    PAR_rTempMIN_GenCoolingOutlet='.SCADA.Generator.Parameter.Ctrl_PAR_rTempMIN_GenCoolingOutlet'
    #SC02_08_002:发电机30秒平均功率高于上限值
    PAR_rMaxPower30sec='.SCADA.GridMeasurement.Parameter.Ctrl_PAR_rMaxPower30sec'
    #SC02_08_122:发电机水冷供水温度过高故障
    PAR_rWCSGENInletTempHigh2='.SCADA.Generator.Parameter.Ctrl_PAR_rWCSGENInletTempHigh2'
    #SC02_08_124:发电机水冷回水温度高
    PAR_rWCSGENOutletTempHigh='.SCADA.Generator.Parameter.Ctrl_PAR_rWCSGENOutletTempHigh'
    #SC02_08_125:发电机水冷供水压力过高故障
    WCSGENInletPreHigh2='.SCADA.Generator.Parameter.Ctrl_PAR_rWCSGENInletPreHigh2'
    #SC02_08_128:发电机水冷供水压力过低故障
    PAR_rWCSGENInletPreLow2='.SCADA.Generator.Parameter.Ctrl_PAR_rWCSGENInletPreLow2'
    #SC02_08_130:发电机水冷回水压力过低故障
    PAR_rWCSGENOutletPreLow2='.SCADA.Generator.Parameter.Ctrl_PAR_rWCSGENOutletPreLow2'
    #SC02_08_133:发电机水冷入口、出口压差过大故障
    PAR_rGenWaterCoolInOutPressureDiffHigh='.SCADA.Generator.Parameter.Ctrl_PAR_rGenWaterCoolInOutPressureDiffHigh'
    #SC02_08_134:发电机水冷入口、出口压差过低故障
    PAR_rGenWaterCoolInOutPressureDiffLow='.SCADA.Generator.Parameter.Ctrl_PAR_rGenWaterCoolInOutPressureDiffLow'
    #SC04_08_005:冷却系统循环泵1低速电机手动模式开启
    CS_Pump1LowManualControlMode='.SCADA.CoolingSystem.RemoteCommand.RemCmd_bEnableCS_Pump1LowManualControlMode'
    #SC04_08_006:冷却系统循环泵2低速电机手动模式开启
    CS_Pump2LowManualControlMode='.SCADA.CoolingSystem.RemoteCommand.RemCmd_bEnableCS_Pump2LowManualControlMode'
    #SC04_08_007:冷却系统循环泵1低速电机强制模式开启
    CS_Pump1LowForceControlMode='.SCADA.CoolingSystem.RemoteCommand.RemCmd_bEnableCS_Pump1LowForceControlMode'
    #SC04_08_008:冷却系统循环泵2低速电机强制模式开启
    CS_Pump2LowForceControlMode='.SCADA.CoolingSystem.RemoteCommand.RemCmd_bEnableCS_Pump2LowForceControlMode'
    #SC04_08_009:冷却系统循环泵1高速电机手动模式开启
    CS_Pump1HighManualControlMode='.SCADA.CoolingSystem.RemoteCommand.RemCmd_bEnableCS_Pump1HighManualControlMode'
    #SC04_08_010:冷却系统循环泵2高速电机手动模式开启
    CS_Pump2HighManualControlMode='.SCADA.CoolingSystem.RemoteCommand.RemCmd_bEnableCS_Pump2HighManualControlMode'
    #SC04_08_011:冷却系统循环泵1高速电机强制模式开启
    CS_Pump1HighForceControlMode='.SCADA.CoolingSystem.RemoteCommand.RemCmd_bEnableCS_Pump1HighForceControlMode'
    #SC04_08_012:冷却系统循环泵2高速电机强制模式开启
    CS_Pump2HighForceControlMode='.SCADA.CoolingSystem.RemoteCommand.RemCmd_bEnableCS_Pump2HighForceControlMode'    
    #SC04_08_013:冷却系统发电机出口温度过高
    PAR_rTemp_CS_GENOutletHigh='.SCADA.CoolingSystem.Parameter.Ctrl_PAR_rTemp_CS_GENOutletHigh'
    #SC04_08_014:冷却系统(入口或出口)压力低报警
    PAR_rPre_CS_LowWarning='.SCADA.CoolingSystem.Parameter.Ctrl_PAR_rPre_CS_LowWarning'
    #SC04_08_015:冷却系统(入口或出口)压力低故障
    PAR_rPre_CS_LowError='.SCADA.CoolingSystem.Parameter.Ctrl_PAR_rPre_CS_LowError'
    #SC04_08_027:冷却系统齿轮箱出口温度过高
    PAR_rTemp_CS_GBXOutletHigh='.SCADA.CoolingSystem.Parameter.Ctrl_PAR_rTemp_CS_GBXOutletHigh'
    #SC04_08_035:塔底水冷泵2无压力故障
    PAR_rTCS_PumpMINPressureErr='.SCADA.CoolingSystem.Parameter.Ctrl_PAR_rTCS_PumpMINPressureErr'
    #SC04_08_038:塔底水冷进水口水温过低警告
    PAR_rTCS_WaterInletTempLowWarning='.SCADA.CoolingSystem.Parameter.Ctrl_PAR_rTCS_WaterInletTempLowWarning'
    
    #禁用：
    #SC02_08_122:
    GLGenWaterCoolInletTempHigh2_todisable='.SCADA.Generator.SC.SC_GLGenWaterCoolInletTempHigh2_todisable'
    #SC04_08_015:
    PreLowError_todisable='.SCADA.CoolingSystem.SC.SC_CS_PreLowError_todisable'
    #SC04_08_060:
    TCS_Pump2_ON_todisable='.SCADA.CoolingSystem.SC.OC_TCS_Pump2_ON_todisable'
    #SC04_09_035:
    WindIrisData_NotValid_todisable='.SCADA.NacelleSystem.SC.SC_WindIrisData_NotValid_todisable'    
     #:dmr>   
    
class Simu():
    enable_simu_allsystem ='.gbSIMU_MAIN_AllTogetherSimulation'
    #SIMU风速
    enable_simu_windspeed = '.gbsimu_FreezeWindSpeed'
    simu_windspeed = '.grsimu_setWindSpeed_1'
    #SIMU风向夹角
    #enable_simu_wanedir = '.gbsimu_FreezeWaneDir'
    #simu_wanedir = '.grsimu_setWaneDir_1'    
    simu_gearbox_temp = '.grsimu_TempGearOilSump'    
    #U相定子1min平均温度
    simu_genstatorU_temp = '.grsimu_TempGenStatorU1'
    #机舱柜中齿轮箱的油泵电机保护空开仿真
    simu_nacelleMotorProtGearOilPump = '.gbsimu_NacelleMotorProtGearOilPump'    
 
    #齿轮箱冷却风扇断路器状态断开。（gbDI_NacelleMotorProtGearFan=0）    
    simu_nacelleMotorProtGearFan='.gbsimu_NacelleMotorProtGearFan'
    #齿轮箱加热器保险丝
    simu_nacelleMotorProtGearHeater = '.gbsimu_NacelleMotorProtGearHeater'
    
    
    #机舱柜中齿轮箱冷却风扇电机加热器或齿轮箱油泵电机加热器保护空开跳开
    nacelleFuseHeaterGearFanAndOilPump='.gbsimu_NacelleFuseHeaterGearFanAndOilPump'
    #机舱柜中齿轮箱油管加热器保护开关跳开 0202043
    nacelleFuseHeaterGearOilPipe ='.simuDI_NacelleFuseHeaterGearOilPipe'
       #齿轮箱入口油温测量PT100传感器故障   0202055
    tempGearOillnlet='.grsimu_TempGearOilinlet'
    #齿轮箱非驱动端轴承PT100传感器输入的状态字节第6位是TRUE或齿轮箱非驱动端轴承1min平均温度不在[-100,500]范围内。0202059
    TempGearBearingNDE= '.grsimu_TempGearBearingNDE'    
    #齿轮箱驱动端的中间轴温度测量PT100传感器故障0202061
    TempGearBearingInterDE='.grsimu_TempGearBearingInterDE'
    #齿轮箱入口油压传感器输入的状态字节第6位是TRUE。（giStateAIGearOilPressureGBXInlet.6=1）02020065
    
    #齿轮油泵处于运行状态，但齿轮油的温度不低于设定值。(DQ_NacelleGearOilPumpLS=1 OR DQ_NacelleGearOilPumpHS=1) AND (grTempGearOilSump_10min 
    OilFilterClogged_Warning='.gbsimu_OilFilterClogging_Warning'#0触发
     #齿轮箱滤网阻塞故障不断。(SC_RepFaultGearOilFilterClogged=1)  02005003
    OilFilterCloggingAlarm='.gbsimu_OilFilterCloggingAlarm'
    #变桨系统发出内部信息 #变桨系统发出故障信息0402027
    simu_CANFromPitch2_TxPDO4_0='.aqsimu_CANFromPitch2_TxPDO4_0'
    #1号桨直流母线电压不正常故障
    simu_PITCH_Blade1DCLinkOK='.dqsimu_PITCH_Blade1DCLinkOK'
    simu_PITCH_Blade3DCLinkOK='.dqsimu_PITCH_Blade3DCLinkOK'
    #2号桨叶24V电源故障
    simu_CANFromPitch2_TxPDO7_2='.aqsimu_CANFromPitch2_TxPDO7_2'
    
    PITCH_PCUSafetyLineClosed='.dqsimu_PITCH_PCUSafetyLineClosed'
    PITCH_Backup2MaintenanceRequired='.dqsimu_PITCH_Backup2MaintenanceRequired'
    PITCH_Backup1MaintenanceRequired='.dqsimu_PITCH_Backup1MaintenanceRequired'
    PITCH_Backup3MaintenanceRequired='.dqsimu_PITCH_Backup3MaintenanceRequired'
    PITCH_Backup1Warining='.dqsimu_PITCH_Backup1Warining' 
    PITCH_Backup2Warining='.dqsimu_PITCH_Backup2Warining' 
    PITCH_Backup3Warining='.dqsimu_PITCH_Backup3Warining' 
    #超级电容自检故障
    PITCH_Backup1Error='.dqsimu_PITCH_Backup1Error'
    PITCH_Backup2Error='.dqsimu_PITCH_Backup2Error'
    PITCH_Backup3Error='.dqsimu_PITCH_Backup3Error'
    
    PITCH_LubricationFault='.dqsimu_PITCH_LubricationFault'
    #2号桨叶的PM出现故障
    simu_CANFromPitch2_TxPDO7_0='.aqsimu_CANFromPitch2_TxPDO7_0'
    simu_CANFromPitch2_TxPDO7_2='.aqsimu_CANFromPitch2_TxPDO7_2'
    simu_CANFromPitch2_TxPDO7_4='.aqsimu_CANFromPitch2_TxPDO7_4'
    simu_CANFromPitch2_TxPDO7_6='.aqsimu_CANFromPitch2_TxPDO7_6'
    simu_CANFromPitch2_TxPDO8_0='.aqsimu_CANFromPitch2_TxPDO8_0'
    simu_CANFromPitch2_TxPDO8_2='.aqsimu_CANFromPitch2_TxPDO8_2'
    simu_CANFromPitch2_TxPDO8_4='.aqsimu_CANFromPitch2_TxPDO8_4'
    NacelleGearOilLevelOK='.gbsimu_NacelleGearOilLevelOK'
    #第一批用例完成
    
    #sc0405017齿轮箱低速泵热继跳开  0
    simu_GBXOilPumpMotorLS_Overload='.gbsimu_GBXOilPumpMotorLS_Overload'
    #018齿轮箱高速泵热继跳开
    simu_GBXOilPumpMotorHS_Overload='.gbsimu_GBXOilPumpMotorHS_Overload'
    #20齿轮箱油入口压力过低故障
    #齿轮箱中速轴(GSGS)PT100传感器故障  31
    grsimu_GearboxBearing_IMS1_Temp='.grsimu_GearboxBearing_IMS1_Temp'
    #齿轮箱中速轴(GSRS)PT100传感器故障32
    grsimu_GearboxBearing_IMS2_Temp='.grsimu_GearboxBearing_IMS2_Temp'
    #齿轮箱中速轴(RS)PT100传感器故障33
    grsimu_GearboxBearing_IMS3_Temp='.grsimu_GearboxBearing_IMS3_Temp'
    #齿轮箱高速轴(GSGS)PT100传感器故障34
    grsimu_GearboxBearing_HSS1_Temp='.grsimu_GearboxBearing_HSS1_Temp'
    #齿轮箱高速轴(GSRS)PT100传感器故障35    
    grsimu_GearboxBearing_HSS2_Temp='.grsimu_GearboxBearing_HSS2_Temp'
    #齿轮箱高速轴(RS)PT100传感器故障36
    #齿轮箱高速轴(RS)温度高警告37
    #齿轮箱离线精滤器空开跳开39
    gbsimu_GBXOfflineFitrationSystemMCB='.gbsimu_GBXOfflineFitrationSystemMCB'
    #40齿轮箱油泵加热器空开跳开
    gbsimu_GearOilPumpMotorPreheaterMCB='.gbsimu_GearOilPumpMotorPreheaterMCB'
    #齿轮箱油泵滤网堵塞41
    gbsimu_GearFilterBlocking='.gbsimu_GearFilterBlocking'
    #齿轮箱过滤器压差传感器故障45
    grsimu_GearOilDiffPressureInlineFilter  ='.grsimu_GearOilDiffPressureInlineFilter'
    #齿轮箱左扭力臂位置传感器损坏50
    grsimu_GBXTorqueArmPositionLeft='.grsimu_GBXTorqueArmPositionLeft'
    #齿轮箱左扭力臂位置传感器损坏51
    grsimu_GBXTorqueArmPositionRight='.grsimu_GBXTorqueArmPositionRight'    
    #齿轮箱油泵加热器运行0202104
    #电网电压L1相超出上限值 0304002, 3,4
    PAR_rsimuCVT_GridVoltage='.PAR_rsimuCVT_GridVoltage'
    #电网频率过高10
    #外部设备测得发电机功率与变频器测得的差异大于设定值
    gbsimuCVT_ForceStateValueEnable='.gbsimuCVT_ForceStateValueEnable'
    gbsimuCVT_Rdy_REF_ForceValue='.gbsimuCVT_Rdy_REF_ForceValue'
    
    #机舱出口风扇1空开跳开0409016
    gbsimu_NacelleOutletFan1MCB='.gbsimu_NacelleOutletFan1MCB'
    #机舱出口风扇1热继跳开
    gbsimu_NacelleOutletFan1Overload='.gbsimu_NacelleOutletFan1Overload'
    #机舱出口风扇2空开跳开
    gbsimu_NacelleOutletFan2MCB='.gbsimu_NacelleOutletFan2MCB'
    #机舱出口风扇2热继跳开
    gbsimu_NacelleOutletFan2Overload='.gbsimu_NacelleOutletFan2Overload'
    #FT加热器空开跳开
    gbsimu_FTHeatingMCB='.gbsimu_FTHeatingMCB'
    #风向标加热器空开跳开
    gbsimu_AnalogWindDirectionHeaterMCB='.gbsimu_AnalogWindDirectionHeaterMCB'
    #风速仪加热器空开跳开
    gbsimu_AnalogWindSpeedHeaterMCB='.gbsimu_AnalogWindSpeedHeaterMCB'
    #机舱出口气流调节器空开跳开
    gbsimu_NacelleOutletDamperMCB='.gbsimu_NacelleOutletDamperMCB'
    #机舱入口气流调节器空开跳开
    gbsimu_NacelleInletDamperMCB='.gbsimu_NacelleInletDamperMCB'
    #机舱加热器空开跳开
    gbsimu_NacelleHeaterMCB='.gbsimu_NacelleHeaterMCB'
    #航空灯空开跳开
    gbsimu_NacelleAviationLightChangeLamp='.gbsimu_NacelleAviationLightChangeLamp'
    
    gbsimu_NacelleAviationLightOK='.gbsimu_NacelleAviationLightOK'    
    #:skp>

    #dmr:
    #机舱柜中齿轮箱冷却风扇电机加热器或齿轮箱油泵电机加热器保护空开跳开仿真
    simu_NacelleFuseHeaterGearFanAndOilPump='.gbsimu_NacelleFuseHeaterGearFanAndOilPump'
    #齿轮箱油池油温测量PT100传感器故障仿真
    simu_TempGearOilSump='.grsimu_TempGearOilSump'
    #驱动端轴承温度测量PT100传感器故障仿真
    simu_TempGearBearingDE='.grsimu_TempGearBearingDE'
    #齿轮箱非驱动端中间轴温度测量PT100传感器故障仿真
    simu_TempGearBearingInterNDE='.grsimu_TempGearBearingInterNDE'
    #齿轮箱过滤器入口压力传感器故障仿真
    simu_GearOilPressureFilterInlet='.grsimu_GearOilPressureFilterInlet'
    #齿轮箱精滤器保护空开跳开仿真
    simu_NacelleGearOilFilterSwitch='.gbsimu_NacelleGearOilFilterSwitch'
    #齿轮箱过滤器阻塞警告仿真
    simu_OilFilterCloggingWarning='.gbsimu_OilFilterCloggingWarning'
    #变桨系统出现内部故障仿真
    simu_CANFromPitch2_TxPDO4_0='.aqsimu_CANFromPitch2_TxPDO4_0'
    #桨直流母线电压不正常故障仿真
    simu_PITCH_Blade2DCLinkOK='.dqsimu_PITCH_Blade2DCLinkOK'
    #桨叶24V电源故障仿真
    simu_CANFromPitch2_TxPDO7_2='.aqsimu_CANFromPitch2_TxPDO7_2'
    #变桨系统处于低电压穿越模式仿真
    simu_PITCH_PCUSafetyLineClosed='.dqsimu_PITCH_PCUSafetyLineClosed'
    #变桨系统处于低电压穿越模式仿真
    simu_CANFromPitch2_TxPDO4_2='.aqsimu_CANFromPitch2_TxPDO4_2'
    #变桨系统处于低电压穿越模式仿真
    simu_CANFromPitch2_TxPDO8_0='.aqsimu_CANFromPitch2_TxPDO8_0'
    #50:1号超级电容需要维护仿真
    simu_CANFromPitch2_TxPDO4_4='.aqsimu_CANFromPitch2_TxPDO4_4'
    #变桨自润滑系统电源故障仿真
    simu_PITCH_LubricationON='.dqsimu_PITCH_LubricationON'
    #变桨自润滑系统低油位故障仿真
    simu_PITCH_LubricationLowLevel='.dqsimu_PITCH_LubricationLowLevel'
    #桨叶的PM出现故障仿真
    simu_CANFromPitch2_TxPDO7_0='.aqsimu_CANFromPitch2_TxPDO7_0'
    #400V进线主接触器2Q1的吸合次数超过了设计寿命报警仿真
    simu_CANFromPitch2_TxPDO8_2='.aqsimu_CANFromPitch2_TxPDO8_2'
    #桨叶400V电源故障仿真
    simu_CANFromPitch2_TxPDO7_2='.aqsimu_CANFromPitch2_TxPDO7_2'
    #轴控柜充电故障仿真
    simu_CANFromPitch2_TxPDO7_4='.aqsimu_CANFromPitch2_TxPDO7_4'
    #轴控柜温度传感器断线故障仿真
    simu_CANFromPitch2_TxPDO7_6='.aqsimu_CANFromPitch2_TxPDO7_6'
    #变桨电机温度传感器断线故障仿真
    simu_CANFromPitch2_TxPDO8_0='.aqsimu_CANFromPitch2_TxPDO8_0'
    #HVRT level1 警告仿真
    simu_CANFromPitch2_TxPDO8_4='.aqsimu_CANFromPitch2_TxPDO8_4' 
    
    
    #SC01_02_036:机舱柜中发电机冷却风扇保护空开跳开仿真
    simu_NacelleMotorProtGenFan='.gbsimu_NacelleMotorProtGenFan'
    #SC02_02_038:机舱柜中发电机空间加热器保护空开跳开仿真
    simu_NacelleMotorProtGenSpaceHeater='.gbsimu_NacelleMotorProtGenSpaceHeater'
    #SC02_02_067:发电机定子U相绕组PT100传感器输入的状态字节第6位是TRUE或发电机定子U相绕组1min平均温度不在[-100,500]范围内
    simu_TempGenStatorU1='.grsimu_TempGenStatorU1'
    #SC02_02_069:发电机定子V相绕组PT100传感器输入的状态字节第6位是TRUE或发电机定子V相绕组1min平均温度不在[-100,500]范围内
    simu_TempGenStatorV1='.grsimu_TempGenStatorV1'    
    #SC02_02_071:发电机定子W相绕组PT100传感器输入的状态字节第6位是TRUE或发电机定子V相绕组1min平均温度不在[-100,500]范围内
    simu_TempGenStatorW1='.grsimu_TempGenStatorW1' 
    #SC02_02_073:发电机驱动端轴承温度测量PT100传感器故障
    simu_TempGenBearingDE='.grsimu_TempGenBearingDE'
    #SC02_02_074:发电机非驱动端轴承温度测量PT100传感器故障
    simu_TempGenBearingNDE='.grsimu_TempGenBearingNDE' 
    #SC02_02_128:机舱柜中发电机水冷系统保护空开跳开
    simu_NacelleMotorProtWCSG='.DQsimu_NacelleMotorProtWCSG'
    #SC_02_08_006:发电机碳刷磨损警告
    simu_NacelleGeneratorBrushWastage='.gbsimu_NacelleGeneratorBrushWastage'
    #SC02_08_042:发电机冷却系统入口PT100传感器故障
    simu_TempGenCoolingInlet='.grsimu_TempGenCoolingInlet'
    #SC02_08_043:发电机冷却系统出口PT100传感器故障
    simu_TempGenCoolingOutlet='.grsimu_TempGenCoolingOutlet'
    #SC02_08_100:发电机定子温度低于露点温度
    simu_TempNacelle='.grsimu_TempNacelle'  
    #SC04_06_001:发电机U相温度信号1错误，报警不停机
    simu_TempGenStatorU1='.grsimu_TempGenStatorU1'
    #SC04_06_002:发电机U相温度信号2错误，报警不停机
    simu_TempGenStatorU2='.grsimu_TempGenStatorU2'
    #SC04_06_005:发电机V相温度信号1错误，报警不停机
    simu_TempGenStatorV1='.grsimu_TempGenStatorV1'
    #SC04_06_006:发电机V相温度信号2错误，报警不停机
    simu_TempGenStatorV2='.grsimu_TempGenStatorV2'
    #SC04_06_009:发电机W相温度信号1错误，报警不停机
    simu_TempGenStatorW1='.grsimu_TempGenStatorW1'
    #SC04_06_010:发电机W相温度信号2错误，报警不停机
    simu_TempGenStatorW2='.grsimu_TempGenStatorW2'
    #SC04_06_035:发电机空水冷却器漏水警告
    simu_GENWaterLeakWarning1='.gbsimu_GENWaterLeakWarning1'
    simu_GENWaterLeakWarning2='.gbsimu_GENWaterLeakWarning2'
    #SC04_06_036:发电机润滑系统警告
    simu_GENLubricationWarning='.gbsimu_GENLubricationWarning'
    #SC02_08_117:发电机水冷主循环泵或电加热器或三通阀开关跳闸
    simu_GLGenWaterCool_PumpHeaterValve_PowerSupply='.gbsimu_GLGenWaterCool_PumpHeaterValve_PowerSupply'
    #SC02_08_118:发电机水冷供水温度传感器TT01 故障
    simuAI_GLGenWaterCool_InletTemp='.grsimuAI_GLGenWaterCool_InletTemp'
    #SC02_08_134:发电机水冷入口、出口压差过低故障
    simu_GLGenWaterCool_PumpOn='.DQsimu_GLGenWaterCool_PumpOn'
    #SC02_08_136:发电机水冷加热器加热时间过长
    simu_GLGenWaterCool_HeaterOn='.DQsimu_GLGenWaterCool_HeaterOn'
    #SC04_08_016:冷却系统泵出口PT100故障
    simu_PumpOutletTemp='.grsimu_PumpOutletTemp'
    #SC04_08_017:冷却系统发电机出口PT100故障
    simu_GENOutletTemp='.grsimu_GENOutletTemp'
    #SC04_08_018:冷却系统齿轮箱出口PT100故障
    simu_GBXOutletTemp='.grsimu_GBXOutletTemp'
    #SC04_08_019:冷却系统循环泵压力侧压力传感器故障
    simu_PumpOutletPressure='.grsimu_PumpOutletPressure'
    #SC04_08_020:冷却系统循环泵吸入侧压力传感器故障
    simu_PumpInletPressure='.grsimu_PumpInletPressure'
    #SC04_08_021:水冷循环泵1低速热继触发
    simu_CS_Pump1Low_OverloadOK='.gbsimu_CS_Pump1Low_OverloadOK'
    #SC04_08_022:水冷循环泵2低速热继触发
    simu_CS_Pump2Low_OverloadOK='.gbsimu_CS_Pump2Low_OverloadOK'
    #SC04_08_023:水冷循环泵1高速热继触发
    simu_CS_Pump1High_OverloadOK='.gbsimu_CS_Pump1High_OverloadOK'
    #SC04_08_024:水冷循环泵2高速热继触发
    simu_CS_Pump2High_OverloadOK='.gbsimu_CS_Pump2High_OverloadOK'
    #SC04_08_025:水冷循环泵1空开跳开
    simu_CS_Pump1MCBOK='.gbsimu_CS_Pump1MCBOK'
    #SC04_08_026:水冷循环泵2空开跳开
    simu_CS_Pump2MCBOK='.gbsimu_CS_Pump2MCBOK'
    #SC04_08_031:塔底水冷泵1MCB跳开
    simu_TCS_Pump1MCB='.gbsimu_TCS_Pump1MCB'
    #SC04_08_032:塔底水冷泵2MCB跳开
    simu_TCS_Pump2MCB='.gbsimu_TCS_Pump2MCB'
    #SC04_08_037:塔底水冷加热器MCB跳开
    simu_TCS_CVTHeaterMCB='.gbsimu_TCS_CVTHeaterMCB'
    #SC04_08_039:塔底水冷进水口PT100故障
    simu_TCS_WaterCoolingInletTemp='.grsimu_TCS_WaterCoolingInletTemp'
    #SC04_08_042:塔底水冷塔内风扇1MCB跳开
    simu_TCS_InsideCoolerFan1MCB='.gbsimu_TCS_InsideCoolerFan1MCB'
    #SC04_08_043:塔底水冷塔内风扇2MCB跳开
    simu_TCS_InsideCoolerFan2MCB='.gbsimu_TCS_InsideCoolerFan2MCB'
    #SC04_08_046:塔底冷却器1风扇A过载
    simu_TCS_Cooler1FanAOverload='.gbsimu_TCS_Cooler1FanAOverload'
    #SC04_08_047:塔底冷却器1风扇B过载
    simu_TCS_Cooler1FanBOverload='.gbsimu_TCS_Cooler1FanBOverload'
    #SC04_08_048:塔底冷却器2风扇A过载
    simu_TCS_Cooler2FanAOverload='.gbsimu_TCS_Cooler2FanAOverload'
    #SC04_08_049:塔底冷却器2风扇B过载
    simu_TCS_Cooler2FanBOverload='.gbsimu_TCS_Cooler2FanBOverload'
    #SC04_08_050:塔底冷却器3风扇A过载
    simu_TCS_Cooler3FanAOverload='.gbsimu_TCS_Cooler3FanAOverload'
    #SC04_08_051:塔底冷却器3风扇B过载
    simu_TCS_Cooler3FanBOverload='.gbsimu_TCS_Cooler3FanBOverload'
    #SC04_08_052:塔底冷却器4风扇A过载
    simu_TCS_Cooler4FanAOverload='.gbsimu_TCS_Cooler4FanAOverload'
    #SC04_08_053:塔底冷却器4风扇B过载
    simu_TCS_Cooler4FanBOverload='.gbsimu_TCS_Cooler4FanBOverload'
    #SC04_08_054:塔底冷却器1风扇 MCB跳开
    simu_TCS_Cooler1Fans_MCB='.gbsimu_TCS_Cooler1Fans_MCB'
    #SC04_08_055:塔底冷却器2风扇 MCB跳开
    simu_TCS_Cooler2Fans_MCB='.gbsimu_TCS_Cooler2Fans_MCB'
    #SC04_08_056:塔底冷却器3风扇 MCB跳开
    simu_TCS_Cooler3Fans_MCB='.gbsimu_TCS_Cooler3Fans_MCB'
    #SC04_08_057:塔底冷却器4风扇 MCB跳开
    simu_TCS_Cooler4Fans_MCB='.gbsimu_TCS_Cooler4Fans_MCB'  

    #:dmr>


Basis_varlist = [Variable.data_Time,Variable.windSpeed,   #基础的录播数据列表
                 Variable.genSpeedPDM,Variable.gen_power,
                 '.grParameterEnvision_11',Variable.pitch,Variable.pitch_set,
                 Variable.operation_mode,Variable.bp_level,
                 Variable.gen_torque,Variable.gen_torque_set,'.grProcessorLoad_Percent']

