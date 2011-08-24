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
                              