import datetime

from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import Pool


class Patient(ModelSQL, ModelView):
    "Patient"
    __name__ = 'training_health.patient'

    code = fields.Char('Code', required=True)
    name = fields.Char('Name', required=True)
    birth_date = fields.Date('Birth Date')
    active = fields.Boolean('Active')
    notes = fields.Text('Observations')

    # Relación Many2One
    professional = fields.Many2One('training_health.professional',
        'Professional')

    age = fields.Function(fields.Integer('Age'), 'get_age')

    @staticmethod
    def default_active():
        return True

    def get_age(self, name):
        if not self.birth_date:
            return None
        today = datetime.date.today()
        years = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month,
                self.birth_date.day):
            years -= 1
        return years

    def get_rec_name(self, name):
        return '[%s] %s' % (self.code, self.name)
