from django.db import models

class Ad1Lidsensor(models.Model):
    id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField()
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
    class Meta:
        db_table = u'AD1_LidSensor'
        ordering = ['-date_time']
    def __unicode__(self):
        return unicode(self.date_time)

class DbnsEnvPth(models.Model):
    id = models.IntegerField(primary_key=True)
    date_time = models.DateTimeField()
    dbns_pth_p1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_P1', blank=True) # Field name made lowercase.
    dbns_pth_t1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_T1', blank=True) # Field name made lowercase.
    dbns_pth_h1 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_H1', blank=True) # Field name made lowercase.
    dbns_pth_p2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_P2', blank=True) # Field name made lowercase.
    dbns_pth_t2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_T2', blank=True) # Field name made lowercase.
    dbns_pth_h2 = models.DecimalField(decimal_places=2, null=True, max_digits=8, db_column='DBNS_PTH_H2', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'DBNS_ENV_PTH'
        ordering = ['-date_time']
    def __unicode__(self):
        return unicode(self.date_time)
        