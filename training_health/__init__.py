from trytond.pool import Pool

from . import patient, professional

def register():
    Pool.register(
        patient.Patient,
        professional.Professional,
        module='training_health', type_="model",
    )

