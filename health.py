from trytond.model import fields
from trytond.pool import PoolMeta


class HealthProfessional(metaclass=PoolMeta):
    __name__ = 'gnuhealth.healthprofessional'

    is_healthprof = fields.Function(
        fields.Char('Es médico?'),
        'get_is_healthprof'
    )

    def get_is_healthprof(self, name):
        if self.name:
            return 'Sí' if self.name.is_healthprof else 'No'
        return 'No'
