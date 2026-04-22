from trytond.model import fields
from trytond.pool import PoolMeta


class HealthProfessional(metaclass=PoolMeta):
    __name__ = 'gnuhealth.healthprofessional'

    is_doctor_display = fields.Function(
        fields.Char('Es un medico?'),
        'get_is_doctor_display'
    )

    def get_is_doctor_display(self, name):
        if self.name and self.name.is_healthprof:
            return 'si'
        return 'no'
