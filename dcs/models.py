from django.db import models

# abstract model for all dcs tables
class DcsModel(models.Model):
    id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField()
    class Meta:
        abstract = True
        ordering = ['-date_time']
    def __unicode__(self):
        return unicode(self.date_time)


# abstract model for AD lid sensor tables
class AbstractAdLidsensor(DcsModel):
    ultrasonic_gdls = models.IntegerField(null=True, db_column='Ultrasonic_GdLS', blank=True) # Field name made lowercase.
    ultrasonic_ls = models.IntegerField(null=True, db_column='Ultrasonic_LS', blank=True) # Field name made lowercase.
    temp_gdls = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Temp_GdLS', blank=True) # Field name made lowercase.
    temp_ls = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Temp_LS', blank=True) # Field name made lowercase.
    tiltx_sensor1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Tiltx_Sensor1', blank=True) # Field name made lowercase.
    tilty_sensor1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Tilty_Sensor1', blank=True) # Field name made lowercase.
    tiltx_sensor2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Tiltx_Sensor2', blank=True) # Field name made lowercase.
    tilty_sensor2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Tilty_Sensor2', blank=True) # Field name made lowercase.
    tiltx_sensor3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Tiltx_Sensor3', blank=True) # Field name made lowercase.
    tilty_sensor3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Tilty_Sensor3', blank=True) # Field name made lowercase.
    capacitance_gdls = models.IntegerField(null=True, db_column='Capacitance_GdLS', blank=True) # Field name made lowercase.
    capacitance_temp_gdls = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Capacitance_Temp_GdLS', blank=True) # Field name made lowercase.
    capacitance_ls = models.IntegerField(null=True, db_column='Capacitance_LS', blank=True) # Field name made lowercase.
    capacitance_temp_ls = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Capacitance_Temp_LS', blank=True) # Field name made lowercase.
    capacitance_mo = models.IntegerField(null=True, db_column='Capacitance_MO', blank=True) # Field name made lowercase.
    capacitance_temp_mo = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Capacitance_Temp_MO', blank=True) # Field name made lowercase.
    ps_output_v = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='PS_Output_V', blank=True) # Field name made lowercase.
    ps_output_i = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='PS_Output_I', blank=True) # Field name made lowercase.
    sensorstatus = models.IntegerField(null=True, db_column='SensorStatus', blank=True) # Field name made lowercase.
    class Meta(DcsModel.Meta):
        abstract = True
        
class Ad1Lidsensor(AbstractAdLidsensor):
    class Meta(AbstractAdLidsensor.Meta):
        db_table = u'AD1_LidSensor'

class Ad2Lidsensor(AbstractAdLidsensor):
    class Meta(AbstractAdLidsensor.Meta):
        db_table = u'AD2_LidSensor'


class DbnsRpcGas101(DcsModel):
    flow_rate_isobutane = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    flow_rate_argon = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    flow_rate_r134a = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    flow_rate_sf6 = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    flow_rate_total = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    flow_rate_branch_1 = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    flow_rate_branch_2 = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    pressure_isobutane = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    pressure_argon = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    pressure_r134a = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    pressure_sf6 = models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)
    class Meta(DcsModel.Meta):
        db_table = u'DBNS_RPC_GAS_101'

       
class DbnsIowTemp(DcsModel):
    dbns_iw_temp_pt1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_IW_Temp_PT1', blank=True) # Field name made lowercase.
    dbns_iw_temp_pt2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_IW_Temp_PT2', blank=True) # Field name made lowercase.
    dbns_iw_temp_pt3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_IW_Temp_PT3', blank=True) # Field name made lowercase.
    dbns_iw_temp_pt4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_IW_Temp_PT4', blank=True) # Field name made lowercase.
    dbns_ow_temp_pt1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_OW_Temp_PT1', blank=True) # Field name made lowercase.
    dbns_ow_temp_pt2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_OW_Temp_PT2', blank=True) # Field name made lowercase.
    dbns_ow_temp_pt3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_OW_Temp_PT3', blank=True) # Field name made lowercase.
    dbns_ow_temp_pt4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_OW_Temp_PT4', blank=True) # Field name made lowercase.
    class Meta(DcsModel.Meta):
        db_table = u'DBNS_IOW_Temp'

                    
class DbnsEnvPth(DcsModel):
    dbns_pth_p1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_P1', blank=True) # Field name made lowercase.
    dbns_pth_t1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_T1', blank=True) # Field name made lowercase.
    dbns_pth_h1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_H1', blank=True) # Field name made lowercase.
    dbns_pth_p2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_P2', blank=True) # Field name made lowercase.
    dbns_pth_t2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_T2', blank=True) # Field name made lowercase.
    dbns_pth_h2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_H2', blank=True) # Field name made lowercase.
    class Meta(DcsModel.Meta):
        db_table = u'DBNS_ENV_PTH'

# abstract model for VMR crate tables
class AbstractVme(DcsModel):
    voltage_5v = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Voltage_5V', blank=True) # Field name made lowercase.
    current_5v = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Current_5V', blank=True) # Field name made lowercase.
    voltage_n5v2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Voltage_N5V2', blank=True) # Field name made lowercase.
    current_n5v2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Current_N5V2', blank=True) # Field name made lowercase.
    voltage_12v = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Voltage_12V', blank=True) # Field name made lowercase.
    current_12v = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Current_12V', blank=True) # Field name made lowercase.
    voltage_n12v = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Voltage_N12V', blank=True) # Field name made lowercase.
    current_n12v = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Current_N12V', blank=True) # Field name made lowercase.
    voltage_3v3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Voltage_3V3', blank=True) # Field name made lowercase.
    current_3v3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Current_3V3', blank=True) # Field name made lowercase.
    temperature1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Temperature1', blank=True) # Field name made lowercase.
    temperature2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Temperature2', blank=True) # Field name made lowercase.
    temperature3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Temperature3', blank=True) # Field name made lowercase.
    temperature4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Temperature4', blank=True) # Field name made lowercase.
    temperature5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Temperature5', blank=True) # Field name made lowercase.
    temperature6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Temperature6', blank=True) # Field name made lowercase.
    temperature7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Temperature7', blank=True) # Field name made lowercase.
    temperature8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Temperature8', blank=True) # Field name made lowercase.
    fantemperature = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='FanTemperature', blank=True) # Field name made lowercase.
    fanspeed = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='Fanspeed', blank=True) # Field name made lowercase.
    powerstatus = models.IntegerField(null=True, db_column='PowerStatus', blank=True) # Field name made lowercase.
    class Meta(DcsModel.Meta):
        abstract = True

class DbnsAd1Vme(AbstractVme):
    class Meta(AbstractVme.Meta):
        db_table = u'DBNS_AD1_VME'

class DbnsAd2Vme(AbstractVme):
    class Meta(AbstractVme.Meta):
        db_table = u'DBNS_AD2_VME'

class DbnsIWVme(AbstractVme):
    class Meta(AbstractVme.Meta):
        db_table = u'DBNS_IW_VME'

class DbnsOWVme(AbstractVme):
    class Meta(AbstractVme.Meta):
        db_table = u'DBNS_OW_VME'        

class DbnsRPCVme(AbstractVme):
    class Meta(AbstractVme.Meta):
        db_table = u'DBNS_RPC_VME'


class DbnsMuonPmtHvVmon(DcsModel):
    dciu3g = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU3G', blank=True) # Field name made lowercase.
    dciu3f = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU3F', blank=True) # Field name made lowercase.
    dciu3e = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU3E', blank=True) # Field name made lowercase.
    dciu3d = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU3D', blank=True) # Field name made lowercase.
    dciu3c = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU3C', blank=True) # Field name made lowercase.
    dciu3b = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU3B', blank=True) # Field name made lowercase.
    dciu3a = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU3A', blank=True) # Field name made lowercase.
    dciu39 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU39', blank=True) # Field name made lowercase.
    dciu38 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU38', blank=True) # Field name made lowercase.
    dciu37 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU37', blank=True) # Field name made lowercase.
    dciu36 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU36', blank=True) # Field name made lowercase.
    dciu35 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU35', blank=True) # Field name made lowercase.
    dciu34 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU34', blank=True) # Field name made lowercase.
    dciu33 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU33', blank=True) # Field name made lowercase.
    dciu32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU32', blank=True) # Field name made lowercase.
    dciu31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU31', blank=True) # Field name made lowercase.
    dciu24 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU24', blank=True) # Field name made lowercase.
    dciu23 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU23', blank=True) # Field name made lowercase.
    dciu22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU22', blank=True) # Field name made lowercase.
    dciu21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU21', blank=True) # Field name made lowercase.
    dciu11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIU11', blank=True) # Field name made lowercase.
    dcih42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIH42', blank=True) # Field name made lowercase.
    dcih41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIH41', blank=True) # Field name made lowercase.
    dcih32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIH32', blank=True) # Field name made lowercase.
    dcih31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIH31', blank=True) # Field name made lowercase.
    dcih22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIH22', blank=True) # Field name made lowercase.
    dcih21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIH21', blank=True) # Field name made lowercase.
    dcih12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIH12', blank=True) # Field name made lowercase.
    dcih11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIH11', blank=True) # Field name made lowercase.
    dcig72 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIG72', blank=True) # Field name made lowercase.
    dcig63 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIG63', blank=True) # Field name made lowercase.
    dcig61 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIG61', blank=True) # Field name made lowercase.
    dcig52 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIG52', blank=True) # Field name made lowercase.
    dcig43 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIG43', blank=True) # Field name made lowercase.
    dcig41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIG41', blank=True) # Field name made lowercase.
    dcig32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIG32', blank=True) # Field name made lowercase.
    dcig23 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIG23', blank=True) # Field name made lowercase.
    dcig21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIG21', blank=True) # Field name made lowercase.
    dcig12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIG12', blank=True) # Field name made lowercase.
    dcif42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIF42', blank=True) # Field name made lowercase.
    dcif41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIF41', blank=True) # Field name made lowercase.
    dcif32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIF32', blank=True) # Field name made lowercase.
    dcif31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIF31', blank=True) # Field name made lowercase.
    dcif22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIF22', blank=True) # Field name made lowercase.
    dcif21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIF21', blank=True) # Field name made lowercase.
    dcif12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIF12', blank=True) # Field name made lowercase.
    dcif11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIF11', blank=True) # Field name made lowercase.
    dcie76 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE76', blank=True) # Field name made lowercase.
    dcie74 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE74', blank=True) # Field name made lowercase.
    dcie72 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE72', blank=True) # Field name made lowercase.
    dcie67 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE67', blank=True) # Field name made lowercase.
    dcie65 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE65', blank=True) # Field name made lowercase.
    dcie63 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE63', blank=True) # Field name made lowercase.
    dcie61 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE61', blank=True) # Field name made lowercase.
    dcie56 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE56', blank=True) # Field name made lowercase.
    dcie54 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE54', blank=True) # Field name made lowercase.
    dcie52 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE52', blank=True) # Field name made lowercase.
    dcie47 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE47', blank=True) # Field name made lowercase.
    dcie45 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE45', blank=True) # Field name made lowercase.
    dcie43 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE43', blank=True) # Field name made lowercase.
    dcie41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE41', blank=True) # Field name made lowercase.
    dcie36 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE36', blank=True) # Field name made lowercase.
    dcie34 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE34', blank=True) # Field name made lowercase.
    dcie32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE32', blank=True) # Field name made lowercase.
    dcie27 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE27', blank=True) # Field name made lowercase.
    dcie25 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE25', blank=True) # Field name made lowercase.
    dcie23 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE23', blank=True) # Field name made lowercase.
    dcie21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE21', blank=True) # Field name made lowercase.
    dcie16 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE16', blank=True) # Field name made lowercase.
    dcie14 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE14', blank=True) # Field name made lowercase.
    dcie12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIE12', blank=True) # Field name made lowercase.
    dcid42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCID42', blank=True) # Field name made lowercase.
    dcid41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCID41', blank=True) # Field name made lowercase.
    dcid32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCID32', blank=True) # Field name made lowercase.
    dcid31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCID31', blank=True) # Field name made lowercase.
    dcid22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCID22', blank=True) # Field name made lowercase.
    dcid21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCID21', blank=True) # Field name made lowercase.
    dcid12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCID12', blank=True) # Field name made lowercase.
    dcid11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCID11', blank=True) # Field name made lowercase.
    dcic72 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIC72', blank=True) # Field name made lowercase.
    dcic63 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIC63', blank=True) # Field name made lowercase.
    dcic61 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIC61', blank=True) # Field name made lowercase.
    dcic52 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIC52', blank=True) # Field name made lowercase.
    dcic43 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIC43', blank=True) # Field name made lowercase.
    dcic41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIC41', blank=True) # Field name made lowercase.
    dcic32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIC32', blank=True) # Field name made lowercase.
    dcic23 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIC23', blank=True) # Field name made lowercase.
    dcic21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIC21', blank=True) # Field name made lowercase.
    dcic12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIC12', blank=True) # Field name made lowercase.
    dcib42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIB42', blank=True) # Field name made lowercase.
    dcib41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIB41', blank=True) # Field name made lowercase.
    dcib32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIB32', blank=True) # Field name made lowercase.
    dcib31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIB31', blank=True) # Field name made lowercase.
    dcib22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIB22', blank=True) # Field name made lowercase.
    dcib21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIB21', blank=True) # Field name made lowercase.
    dcib12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIB12', blank=True) # Field name made lowercase.
    dcib11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIB11', blank=True) # Field name made lowercase.
    dcia76 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA76', blank=True) # Field name made lowercase.
    dcia74 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA74', blank=True) # Field name made lowercase.
    dcia72 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA72', blank=True) # Field name made lowercase.
    dcia67 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA67', blank=True) # Field name made lowercase.
    dcia65 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA65', blank=True) # Field name made lowercase.
    dcia63 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA63', blank=True) # Field name made lowercase.
    dcia61 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA61', blank=True) # Field name made lowercase.
    dcia56 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA56', blank=True) # Field name made lowercase.
    dcia54 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA54', blank=True) # Field name made lowercase.
    dcia52 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA52', blank=True) # Field name made lowercase.
    dcia47 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA47', blank=True) # Field name made lowercase.
    dcia45 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA45', blank=True) # Field name made lowercase.
    dcia43 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA43', blank=True) # Field name made lowercase.
    dcia41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA41', blank=True) # Field name made lowercase.
    dcia36 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA36', blank=True) # Field name made lowercase.
    dcia34 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA34', blank=True) # Field name made lowercase.
    dcia32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA32', blank=True) # Field name made lowercase.
    dcia27 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA27', blank=True) # Field name made lowercase.
    dcia25 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA25', blank=True) # Field name made lowercase.
    dcia23 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA23', blank=True) # Field name made lowercase.
    dcia21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA21', blank=True) # Field name made lowercase.
    dcia16 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA16', blank=True) # Field name made lowercase.
    dcia14 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA14', blank=True) # Field name made lowercase.
    dcia12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DCIA12', blank=True) # Field name made lowercase.
    dviu26 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIU26', blank=True) # Field name made lowercase.
    dviu25 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIU25', blank=True) # Field name made lowercase.
    dviu24 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIU24', blank=True) # Field name made lowercase.
    dviu23 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIU23', blank=True) # Field name made lowercase.
    dviu22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIU22', blank=True) # Field name made lowercase.
    dviu21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIU21', blank=True) # Field name made lowercase.
    dviu11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIU11', blank=True) # Field name made lowercase.
    dvohf3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOHF3', blank=True) # Field name made lowercase.
    dvohf1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOHF1', blank=True) # Field name made lowercase.
    dvogf1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOGF1', blank=True) # Field name made lowercase.
    dvoff3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOFF3', blank=True) # Field name made lowercase.
    dvoff1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOFF1', blank=True) # Field name made lowercase.
    dvoef3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOEF3', blank=True) # Field name made lowercase.
    dvoef2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOEF2', blank=True) # Field name made lowercase.
    dvoef1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOEF1', blank=True) # Field name made lowercase.
    dvodf3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVODF3', blank=True) # Field name made lowercase.
    dvodf1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVODF1', blank=True) # Field name made lowercase.
    dvocf1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOCF1', blank=True) # Field name made lowercase.
    dvobf3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOBF3', blank=True) # Field name made lowercase.
    dvobf1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOBF1', blank=True) # Field name made lowercase.
    dvoaf3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOAF3', blank=True) # Field name made lowercase.
    dvoaf2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOAF2', blank=True) # Field name made lowercase.
    dvoaf1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOAF1', blank=True) # Field name made lowercase.
    dvoh42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOH42', blank=True) # Field name made lowercase.
    dvoh41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOH41', blank=True) # Field name made lowercase.
    dvoh32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOH32', blank=True) # Field name made lowercase.
    dvoh31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOH31', blank=True) # Field name made lowercase.
    dvoh22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOH22', blank=True) # Field name made lowercase.
    dvoh21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOH21', blank=True) # Field name made lowercase.
    dvoh12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOH12', blank=True) # Field name made lowercase.
    dvoh11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOH11', blank=True) # Field name made lowercase.
    dvih42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIH42', blank=True) # Field name made lowercase.
    dvih41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIH41', blank=True) # Field name made lowercase.
    dvih32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIH32', blank=True) # Field name made lowercase.
    dvih31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIH31', blank=True) # Field name made lowercase.
    dvih22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIH22', blank=True) # Field name made lowercase.
    dvih21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIH21', blank=True) # Field name made lowercase.
    dvih12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIH12', blank=True) # Field name made lowercase.
    dvih11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIH11', blank=True) # Field name made lowercase.
    dvog41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOG41', blank=True) # Field name made lowercase.
    dvog31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOG31', blank=True) # Field name made lowercase.
    dvog21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOG21', blank=True) # Field name made lowercase.
    dvog11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOG11', blank=True) # Field name made lowercase.
    dvig42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIG42', blank=True) # Field name made lowercase.
    dvig41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIG41', blank=True) # Field name made lowercase.
    dvig32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIG32', blank=True) # Field name made lowercase.
    dvig31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIG31', blank=True) # Field name made lowercase.
    dvig22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIG22', blank=True) # Field name made lowercase.
    dvig21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIG21', blank=True) # Field name made lowercase.
    dvig12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIG12', blank=True) # Field name made lowercase.
    dvig11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIG11', blank=True) # Field name made lowercase.
    dvof42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOF42', blank=True) # Field name made lowercase.
    dvof41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOF41', blank=True) # Field name made lowercase.
    dvof32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOF32', blank=True) # Field name made lowercase.
    dvof31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOF31', blank=True) # Field name made lowercase.
    dvof22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOF22', blank=True) # Field name made lowercase.
    dvof21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOF21', blank=True) # Field name made lowercase.
    dvof12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOF12', blank=True) # Field name made lowercase.
    dvof11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOF11', blank=True) # Field name made lowercase.
    dvif42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIF42', blank=True) # Field name made lowercase.
    dvif41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIF41', blank=True) # Field name made lowercase.
    dvif32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIF32', blank=True) # Field name made lowercase.
    dvif31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIF31', blank=True) # Field name made lowercase.
    dvif22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIF22', blank=True) # Field name made lowercase.
    dvif21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIF21', blank=True) # Field name made lowercase.
    dvif12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIF12', blank=True) # Field name made lowercase.
    dvif11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIF11', blank=True) # Field name made lowercase.
    dvoe43 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE43', blank=True) # Field name made lowercase.
    dvoe42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE42', blank=True) # Field name made lowercase.
    dvoe41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE41', blank=True) # Field name made lowercase.
    dvoe33 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE33', blank=True) # Field name made lowercase.
    dvoe32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE32', blank=True) # Field name made lowercase.
    dvoe31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE31', blank=True) # Field name made lowercase.
    dvoe23 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE23', blank=True) # Field name made lowercase.
    dvoe22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE22', blank=True) # Field name made lowercase.
    dvoe21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE21', blank=True) # Field name made lowercase.
    dvoe13 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE13', blank=True) # Field name made lowercase.
    dvoe12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE12', blank=True) # Field name made lowercase.
    dvoe11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOE11', blank=True) # Field name made lowercase.
    dvie44 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE44', blank=True) # Field name made lowercase.
    dvie43 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE43', blank=True) # Field name made lowercase.
    dvie42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE42', blank=True) # Field name made lowercase.
    dvie41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE41', blank=True) # Field name made lowercase.
    dvie34 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE34', blank=True) # Field name made lowercase.
    dvie33 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE33', blank=True) # Field name made lowercase.
    dvie32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE32', blank=True) # Field name made lowercase.
    dvie31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE31', blank=True) # Field name made lowercase.
    dvie24 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE24', blank=True) # Field name made lowercase.
    dvie23 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE23', blank=True) # Field name made lowercase.
    dvie22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE22', blank=True) # Field name made lowercase.
    dvie21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE21', blank=True) # Field name made lowercase.
    dvie14 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE14', blank=True) # Field name made lowercase.
    dvie13 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE13', blank=True) # Field name made lowercase.
    dvie12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE12', blank=True) # Field name made lowercase.
    dvie11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIE11', blank=True) # Field name made lowercase.
    dvod42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOD42', blank=True) # Field name made lowercase.
    dvod41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOD41', blank=True) # Field name made lowercase.
    dvod32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOD32', blank=True) # Field name made lowercase.
    dvod31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOD31', blank=True) # Field name made lowercase.
    dvod22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOD22', blank=True) # Field name made lowercase.
    dvod21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOD21', blank=True) # Field name made lowercase.
    dvod12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOD12', blank=True) # Field name made lowercase.
    dvod11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOD11', blank=True) # Field name made lowercase.
    dvid42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVID42', blank=True) # Field name made lowercase.
    dvid41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVID41', blank=True) # Field name made lowercase.
    dvid32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVID32', blank=True) # Field name made lowercase.
    dvid31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVID31', blank=True) # Field name made lowercase.
    dvid22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVID22', blank=True) # Field name made lowercase.
    dvid21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVID21', blank=True) # Field name made lowercase.
    dvid12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVID12', blank=True) # Field name made lowercase.
    dvid11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVID11', blank=True) # Field name made lowercase.
    dvoc41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOC41', blank=True) # Field name made lowercase.
    dvoc31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOC31', blank=True) # Field name made lowercase.
    dvoc21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOC21', blank=True) # Field name made lowercase.
    dvoc11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOC11', blank=True) # Field name made lowercase.
    dvic42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIC42', blank=True) # Field name made lowercase.
    dvic41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIC41', blank=True) # Field name made lowercase.
    dvic32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIC32', blank=True) # Field name made lowercase.
    dvic31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIC31', blank=True) # Field name made lowercase.
    dvic22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIC22', blank=True) # Field name made lowercase.
    dvic21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIC21', blank=True) # Field name made lowercase.
    dvic12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIC12', blank=True) # Field name made lowercase.
    dvic11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIC11', blank=True) # Field name made lowercase.
    dvob42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOB42', blank=True) # Field name made lowercase.
    dvob41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOB41', blank=True) # Field name made lowercase.
    dvob32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOB32', blank=True) # Field name made lowercase.
    dvob31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOB31', blank=True) # Field name made lowercase.
    dvob22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOB22', blank=True) # Field name made lowercase.
    dvob21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOB21', blank=True) # Field name made lowercase.
    dvob12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOB12', blank=True) # Field name made lowercase.
    dvob11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOB11', blank=True) # Field name made lowercase.
    dvib42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIB42', blank=True) # Field name made lowercase.
    dvib41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIB41', blank=True) # Field name made lowercase.
    dvib32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIB32', blank=True) # Field name made lowercase.
    dvib31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIB31', blank=True) # Field name made lowercase.
    dvib22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIB22', blank=True) # Field name made lowercase.
    dvib21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIB21', blank=True) # Field name made lowercase.
    dvib12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIB12', blank=True) # Field name made lowercase.
    dvib11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIB11', blank=True) # Field name made lowercase.
    dvoa43 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA43', blank=True) # Field name made lowercase.
    dvoa42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA42', blank=True) # Field name made lowercase.
    dvoa41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA41', blank=True) # Field name made lowercase.
    dvoa33 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA33', blank=True) # Field name made lowercase.
    dvoa32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA32', blank=True) # Field name made lowercase.
    dvoa31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA31', blank=True) # Field name made lowercase.
    dvoa23 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA23', blank=True) # Field name made lowercase.
    dvoa22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA22', blank=True) # Field name made lowercase.
    dvoa21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA21', blank=True) # Field name made lowercase.
    dvoa13 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA13', blank=True) # Field name made lowercase.
    dvoa12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA12', blank=True) # Field name made lowercase.
    dvoa11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVOA11', blank=True) # Field name made lowercase.
    dvia44 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA44', blank=True) # Field name made lowercase.
    dvia43 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA43', blank=True) # Field name made lowercase.
    dvia42 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA42', blank=True) # Field name made lowercase.
    dvia41 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA41', blank=True) # Field name made lowercase.
    dvia34 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA34', blank=True) # Field name made lowercase.
    dvia33 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA33', blank=True) # Field name made lowercase.
    dvia32 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA32', blank=True) # Field name made lowercase.
    dvia31 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA31', blank=True) # Field name made lowercase.
    dvia24 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA24', blank=True) # Field name made lowercase.
    dvia23 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA23', blank=True) # Field name made lowercase.
    dvia22 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA22', blank=True) # Field name made lowercase.
    dvia21 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA21', blank=True) # Field name made lowercase.
    dvia14 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA14', blank=True) # Field name made lowercase.
    dvia13 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA13', blank=True) # Field name made lowercase.
    dvia12 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA12', blank=True) # Field name made lowercase.
    dvia11 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DVIA11', blank=True) # Field name made lowercase.
    class Meta(DcsModel.Meta):
        db_table = u'DBNS_MUON_PMT_HV_Vmon'

# abstract model for AD PMT HV tables
class AbstractAdHv(DcsModel):
    l8c3r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C3R8', blank=True) # Field name made lowercase.
    l8c3r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C3R7', blank=True) # Field name made lowercase.
    l8c3r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C3R6', blank=True) # Field name made lowercase.
    l8c3r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C3R5', blank=True) # Field name made lowercase.
    l8c3r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C3R4', blank=True) # Field name made lowercase.
    l8c3r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C3R3', blank=True) # Field name made lowercase.
    l8c3r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C3R2', blank=True) # Field name made lowercase.
    l8c3r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C3R1', blank=True) # Field name made lowercase.
    l8c2r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C2R8', blank=True) # Field name made lowercase.
    l8c2r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C2R7', blank=True) # Field name made lowercase.
    l8c2r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C2R6', blank=True) # Field name made lowercase.
    l8c2r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C2R5', blank=True) # Field name made lowercase.
    l8c2r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C2R4', blank=True) # Field name made lowercase.
    l8c2r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C2R3', blank=True) # Field name made lowercase.
    l8c2r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C2R2', blank=True) # Field name made lowercase.
    l8c2r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C2R1', blank=True) # Field name made lowercase.
    l8c1r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C1R8', blank=True) # Field name made lowercase.
    l8c1r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C1R7', blank=True) # Field name made lowercase.
    l8c1r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C1R6', blank=True) # Field name made lowercase.
    l8c1r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C1R5', blank=True) # Field name made lowercase.
    l8c1r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C1R4', blank=True) # Field name made lowercase.
    l8c1r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C1R3', blank=True) # Field name made lowercase.
    l8c1r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C1R2', blank=True) # Field name made lowercase.
    l8c1r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L8C1R1', blank=True) # Field name made lowercase.
    l7c3r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C3R8', blank=True) # Field name made lowercase.
    l7c3r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C3R7', blank=True) # Field name made lowercase.
    l7c3r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C3R6', blank=True) # Field name made lowercase.
    l7c3r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C3R5', blank=True) # Field name made lowercase.
    l7c3r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C3R4', blank=True) # Field name made lowercase.
    l7c3r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C3R3', blank=True) # Field name made lowercase.
    l7c3r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C3R2', blank=True) # Field name made lowercase.
    l7c3r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C3R1', blank=True) # Field name made lowercase.
    l7c2r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C2R8', blank=True) # Field name made lowercase.
    l7c2r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C2R7', blank=True) # Field name made lowercase.
    l7c2r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C2R6', blank=True) # Field name made lowercase.
    l7c2r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C2R5', blank=True) # Field name made lowercase.
    l7c2r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C2R4', blank=True) # Field name made lowercase.
    l7c2r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C2R3', blank=True) # Field name made lowercase.
    l7c2r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C2R2', blank=True) # Field name made lowercase.
    l7c2r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C2R1', blank=True) # Field name made lowercase.
    l7c1r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C1R8', blank=True) # Field name made lowercase.
    l7c1r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C1R7', blank=True) # Field name made lowercase.
    l7c1r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C1R6', blank=True) # Field name made lowercase.
    l7c1r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C1R5', blank=True) # Field name made lowercase.
    l7c1r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C1R4', blank=True) # Field name made lowercase.
    l7c1r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C1R3', blank=True) # Field name made lowercase.
    l7c1r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C1R2', blank=True) # Field name made lowercase.
    l7c1r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L7C1R1', blank=True) # Field name made lowercase.
    l6c3r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C3R8', blank=True) # Field name made lowercase.
    l6c3r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C3R7', blank=True) # Field name made lowercase.
    l6c3r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C3R6', blank=True) # Field name made lowercase.
    l6c3r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C3R5', blank=True) # Field name made lowercase.
    l6c3r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C3R4', blank=True) # Field name made lowercase.
    l6c3r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C3R3', blank=True) # Field name made lowercase.
    l6c3r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C3R2', blank=True) # Field name made lowercase.
    l6c3r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C3R1', blank=True) # Field name made lowercase.
    l6c2r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C2R8', blank=True) # Field name made lowercase.
    l6c2r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C2R7', blank=True) # Field name made lowercase.
    l6c2r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C2R6', blank=True) # Field name made lowercase.
    l6c2r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C2R5', blank=True) # Field name made lowercase.
    l6c2r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C2R4', blank=True) # Field name made lowercase.
    l6c2r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C2R3', blank=True) # Field name made lowercase.
    l6c2r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C2R2', blank=True) # Field name made lowercase.
    l6c2r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C2R1', blank=True) # Field name made lowercase.
    l6c1r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C1R8', blank=True) # Field name made lowercase.
    l6c1r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C1R7', blank=True) # Field name made lowercase.
    l6c1r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C1R6', blank=True) # Field name made lowercase.
    l6c1r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C1R5', blank=True) # Field name made lowercase.
    l6c1r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C1R4', blank=True) # Field name made lowercase.
    l6c1r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C1R3', blank=True) # Field name made lowercase.
    l6c1r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C1R2', blank=True) # Field name made lowercase.
    l6c1r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L6C1R1', blank=True) # Field name made lowercase.
    l5c3r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C3R8', blank=True) # Field name made lowercase.
    l5c3r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C3R7', blank=True) # Field name made lowercase.
    l5c3r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C3R6', blank=True) # Field name made lowercase.
    l5c3r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C3R5', blank=True) # Field name made lowercase.
    l5c3r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C3R4', blank=True) # Field name made lowercase.
    l5c3r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C3R3', blank=True) # Field name made lowercase.
    l5c3r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C3R2', blank=True) # Field name made lowercase.
    l5c3r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C3R1', blank=True) # Field name made lowercase.
    l5c2r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C2R8', blank=True) # Field name made lowercase.
    l5c2r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C2R7', blank=True) # Field name made lowercase.
    l5c2r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C2R6', blank=True) # Field name made lowercase.
    l5c2r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C2R5', blank=True) # Field name made lowercase.
    l5c2r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C2R4', blank=True) # Field name made lowercase.
    l5c2r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C2R3', blank=True) # Field name made lowercase.
    l5c2r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C2R2', blank=True) # Field name made lowercase.
    l5c2r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C2R1', blank=True) # Field name made lowercase.
    l5c1r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C1R8', blank=True) # Field name made lowercase.
    l5c1r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C1R7', blank=True) # Field name made lowercase.
    l5c1r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C1R6', blank=True) # Field name made lowercase.
    l5c1r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C1R5', blank=True) # Field name made lowercase.
    l5c1r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C1R4', blank=True) # Field name made lowercase.
    l5c1r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C1R3', blank=True) # Field name made lowercase.
    l5c1r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C1R2', blank=True) # Field name made lowercase.
    l5c1r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L5C1R1', blank=True) # Field name made lowercase.
    l4c3r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C3R8', blank=True) # Field name made lowercase.
    l4c3r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C3R7', blank=True) # Field name made lowercase.
    l4c3r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C3R6', blank=True) # Field name made lowercase.
    l4c3r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C3R5', blank=True) # Field name made lowercase.
    l4c3r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C3R4', blank=True) # Field name made lowercase.
    l4c3r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C3R3', blank=True) # Field name made lowercase.
    l4c3r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C3R2', blank=True) # Field name made lowercase.
    l4c3r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C3R1', blank=True) # Field name made lowercase.
    l4c2r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C2R8', blank=True) # Field name made lowercase.
    l4c2r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C2R7', blank=True) # Field name made lowercase.
    l4c2r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C2R6', blank=True) # Field name made lowercase.
    l4c2r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C2R5', blank=True) # Field name made lowercase.
    l4c2r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C2R4', blank=True) # Field name made lowercase.
    l4c2r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C2R3', blank=True) # Field name made lowercase.
    l4c2r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C2R2', blank=True) # Field name made lowercase.
    l4c2r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C2R1', blank=True) # Field name made lowercase.
    l4c1r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C1R8', blank=True) # Field name made lowercase.
    l4c1r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C1R7', blank=True) # Field name made lowercase.
    l4c1r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C1R6', blank=True) # Field name made lowercase.
    l4c1r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C1R5', blank=True) # Field name made lowercase.
    l4c1r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C1R4', blank=True) # Field name made lowercase.
    l4c1r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C1R3', blank=True) # Field name made lowercase.
    l4c1r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C1R2', blank=True) # Field name made lowercase.
    l4c1r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L4C1R1', blank=True) # Field name made lowercase.
    l3c3r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C3R8', blank=True) # Field name made lowercase.
    l3c3r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C3R7', blank=True) # Field name made lowercase.
    l3c3r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C3R6', blank=True) # Field name made lowercase.
    l3c3r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C3R5', blank=True) # Field name made lowercase.
    l3c3r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C3R4', blank=True) # Field name made lowercase.
    l3c3r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C3R3', blank=True) # Field name made lowercase.
    l3c3r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C3R2', blank=True) # Field name made lowercase.
    l3c3r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C3R1', blank=True) # Field name made lowercase.
    l3c2r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C2R8', blank=True) # Field name made lowercase.
    l3c2r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C2R7', blank=True) # Field name made lowercase.
    l3c2r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C2R6', blank=True) # Field name made lowercase.
    l3c2r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C2R5', blank=True) # Field name made lowercase.
    l3c2r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C2R4', blank=True) # Field name made lowercase.
    l3c2r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C2R3', blank=True) # Field name made lowercase.
    l3c2r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C2R2', blank=True) # Field name made lowercase.
    l3c2r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C2R1', blank=True) # Field name made lowercase.
    l3c1r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C1R8', blank=True) # Field name made lowercase.
    l3c1r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C1R7', blank=True) # Field name made lowercase.
    l3c1r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C1R6', blank=True) # Field name made lowercase.
    l3c1r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C1R5', blank=True) # Field name made lowercase.
    l3c1r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C1R4', blank=True) # Field name made lowercase.
    l3c1r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C1R3', blank=True) # Field name made lowercase.
    l3c1r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C1R2', blank=True) # Field name made lowercase.
    l3c1r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L3C1R1', blank=True) # Field name made lowercase.
    l2c3r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C3R8', blank=True) # Field name made lowercase.
    l2c3r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C3R7', blank=True) # Field name made lowercase.
    l2c3r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C3R6', blank=True) # Field name made lowercase.
    l2c3r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C3R5', blank=True) # Field name made lowercase.
    l2c3r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C3R4', blank=True) # Field name made lowercase.
    l2c3r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C3R3', blank=True) # Field name made lowercase.
    l2c3r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C3R2', blank=True) # Field name made lowercase.
    l2c3r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C3R1', blank=True) # Field name made lowercase.
    l2c2r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C2R8', blank=True) # Field name made lowercase.
    l2c2r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C2R7', blank=True) # Field name made lowercase.
    l2c2r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C2R6', blank=True) # Field name made lowercase.
    l2c2r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C2R5', blank=True) # Field name made lowercase.
    l2c2r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C2R4', blank=True) # Field name made lowercase.
    l2c2r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C2R3', blank=True) # Field name made lowercase.
    l2c2r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C2R2', blank=True) # Field name made lowercase.
    l2c2r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C2R1', blank=True) # Field name made lowercase.
    l2c1r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C1R8', blank=True) # Field name made lowercase.
    l2c1r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C1R7', blank=True) # Field name made lowercase.
    l2c1r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C1R6', blank=True) # Field name made lowercase.
    l2c1r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C1R5', blank=True) # Field name made lowercase.
    l2c1r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C1R4', blank=True) # Field name made lowercase.
    l2c1r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C1R3', blank=True) # Field name made lowercase.
    l2c1r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C1R2', blank=True) # Field name made lowercase.
    l2c1r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L2C1R1', blank=True) # Field name made lowercase.
    l1c3r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C3R8', blank=True) # Field name made lowercase.
    l1c3r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C3R7', blank=True) # Field name made lowercase.
    l1c3r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C3R6', blank=True) # Field name made lowercase.
    l1c3r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C3R5', blank=True) # Field name made lowercase.
    l1c3r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C3R4', blank=True) # Field name made lowercase.
    l1c3r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C3R3', blank=True) # Field name made lowercase.
    l1c3r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C3R2', blank=True) # Field name made lowercase.
    l1c3r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C3R1', blank=True) # Field name made lowercase.
    l1c2r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C2R8', blank=True) # Field name made lowercase.
    l1c2r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C2R7', blank=True) # Field name made lowercase.
    l1c2r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C2R6', blank=True) # Field name made lowercase.
    l1c2r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C2R5', blank=True) # Field name made lowercase.
    l1c2r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C2R4', blank=True) # Field name made lowercase.
    l1c2r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C2R3', blank=True) # Field name made lowercase.
    l1c2r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C2R2', blank=True) # Field name made lowercase.
    l1c2r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C2R1', blank=True) # Field name made lowercase.
    l1c1r8 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C1R8', blank=True) # Field name made lowercase.
    l1c1r7 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C1R7', blank=True) # Field name made lowercase.
    l1c1r6 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C1R6', blank=True) # Field name made lowercase.
    l1c1r5 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C1R5', blank=True) # Field name made lowercase.
    l1c1r4 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C1R4', blank=True) # Field name made lowercase.
    l1c1r3 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C1R3', blank=True) # Field name made lowercase.
    l1c1r2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C1R2', blank=True) # Field name made lowercase.
    l1c1r1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='L1C1R1', blank=True) # Field name made lowercase.
    class Meta(DcsModel.Meta):
        abstract = True

                
class DbnsAd1Hv(AbstractAdHv):
    class Meta(AbstractAdHv.Meta):
        db_table = u'DBNS_AD1_HV'

class DbnsAd2Hv(AbstractAdHv):
    class Meta(AbstractAdHv.Meta):
        db_table = u'DBNS_AD2_HV'

    
class DbnsRpcHvVmon(DcsModel):
    dbns_fo00n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO00N', blank=True) # Field name made lowercase.
    dbns_fo01n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO01N', blank=True) # Field name made lowercase.
    dbns_fo02n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO02N', blank=True) # Field name made lowercase.
    dbns_fo03n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO03N', blank=True) # Field name made lowercase.
    dbns_fo04n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO04N', blank=True) # Field name made lowercase.
    dbns_fo05n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO05N', blank=True) # Field name made lowercase.
    dbns_fo06n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO06N', blank=True) # Field name made lowercase.
    dbns_fo07n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO07N', blank=True) # Field name made lowercase.
    dbns_fo08n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO08N', blank=True) # Field name made lowercase.
    dbns_fo09n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO09N', blank=True) # Field name made lowercase.
    dbns_fo10n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO10N', blank=True) # Field name made lowercase.
    dbns_fo11n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO11N', blank=True) # Field name made lowercase.
    dbns_fo12n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO12N', blank=True) # Field name made lowercase.
    dbns_fo13n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO13N', blank=True) # Field name made lowercase.
    dbns_fo14n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO14N', blank=True) # Field name made lowercase.
    dbns_fo15n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO15N', blank=True) # Field name made lowercase.
    dbns_fo16n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO16N', blank=True) # Field name made lowercase.
    dbns_fo17n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO17N', blank=True) # Field name made lowercase.
    dbns_fo18n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO18N', blank=True) # Field name made lowercase.
    dbns_fo19n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO19N', blank=True) # Field name made lowercase.
    dbns_fo20n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO20N', blank=True) # Field name made lowercase.
    dbns_fo21n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO21N', blank=True) # Field name made lowercase.
    dbns_fo22n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO22N', blank=True) # Field name made lowercase.
    dbns_fo23n = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO23N', blank=True) # Field name made lowercase.
    dbns_fo00p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO00P', blank=True) # Field name made lowercase.
    dbns_fo01p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO01P', blank=True) # Field name made lowercase.
    dbns_fo02p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO02P', blank=True) # Field name made lowercase.
    dbns_fo03p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO03P', blank=True) # Field name made lowercase.
    dbns_fo04p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO04P', blank=True) # Field name made lowercase.
    dbns_fo05p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO05P', blank=True) # Field name made lowercase.
    dbns_fo06p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO06P', blank=True) # Field name made lowercase.
    dbns_fo07p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO07P', blank=True) # Field name made lowercase.
    dbns_fo08p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO08P', blank=True) # Field name made lowercase.
    dbns_fo09p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO09P', blank=True) # Field name made lowercase.
    dbns_fo10p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO10P', blank=True) # Field name made lowercase.
    dbns_fo11p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO11P', blank=True) # Field name made lowercase.
    dbns_fo12p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO12P', blank=True) # Field name made lowercase.
    dbns_fo13p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO13P', blank=True) # Field name made lowercase.
    dbns_fo14p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO14P', blank=True) # Field name made lowercase.
    dbns_fo15p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO15P', blank=True) # Field name made lowercase.
    dbns_fo16p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO16P', blank=True) # Field name made lowercase.
    dbns_fo17p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO17P', blank=True) # Field name made lowercase.
    dbns_fo18p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO18P', blank=True) # Field name made lowercase.
    dbns_fo19p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO19P', blank=True) # Field name made lowercase.
    dbns_fo20p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO20P', blank=True) # Field name made lowercase.
    dbns_fo21p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO21P', blank=True) # Field name made lowercase.
    dbns_fo22p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO22P', blank=True) # Field name made lowercase.
    dbns_fo23p = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_FO23P', blank=True) # Field name made lowercase.
    class Meta(DcsModel.Meta):
        db_table = u'DBNS_RPC_HV_Vmon'
                              