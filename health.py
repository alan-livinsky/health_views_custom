from trytond.model import fields
from trytond.pool import PoolMeta


class HealthProfessional(metaclass=PoolMeta):
    __name__ = 'gnuhealth.healthprofessional'

    is_healthprof = fields.Function(
        fields.Boolean('Health Prof'),
        'get_is_healthprof'
    )

    def get_is_healthprof(self, name):
        if self.name:
            return bool(self.name.is_healthprof)
        return False
