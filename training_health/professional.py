from trytond.model import ModelSQL, ModelView, fields
from trytond.pyson import Eval


class Professional(ModelSQL, ModelView):
    "Professional"
    __name__ = 'training_health.professional'

    name = fields.Char('Name', required=True)
    license_number = fields.Char('License Number', required=True,
        help="Matrícula profesional")
    specialty = fields.Char('Specialty')
    state = fields.Selection([
            ('active', 'Active'),
            ('inactive', 'Inactive'),
            ('suspended', 'Suspended'),
            ], 'State', required=True)
    start_date = fields.Date('Start Date', required=True,
        help="Fecha de ingreso")

    # Relación inversa, definida como One2Many hacia training_health.patient
    patients = fields.One2Many('training_health.patient', 'professional',
        'Patients')

    @staticmethod
    def default_state():
        return 'active'

    def get_rec_name(self, name):
        return '%s (%s)' % (self.name, self.license_number)
