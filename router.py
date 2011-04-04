# Router for multiple database
offline_db_applist = ['runinfo', 'daqinfo', 'pmtinfo']

class DayaBayOfflineRouter(object):
    """DayaBay Offline DB"""
       
    def db_for_read(self, model, **hints):
        if model._meta.app_label in offline_db_applist:
            return 'lbl'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in offline_db_applist:
            return 'lbl'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in offline_db_applist or obj2._meta.app_label in offline_db_applist:
            return True
        return None

    def allow_syncdb(self, db, model):
        if db == 'lbl':
            return model._meta.app_label == 'dummy'
        elif model._meta.app_label in offline_db_applist:
            return False
        return None

class LocalRouter(object):
    """default database"""

    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_syncdb(self, db, model):
        return True
