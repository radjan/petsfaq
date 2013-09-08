
ROLE = 'role'
SPECIALTY = 'specialty'
HOSPITAL = 'hospital'
PERSON = 'person'
ACCOUNT = 'account'

SERVICES_MAP = None

#prevent circular import
def _init_service_map():
    from service.role import role_service
    from service.specialty import specialty_service
    from service.hospital import hospital_service
    from service.person import person_service
    from service.account import account_service
    global SERVICES_MAP
    if not SERVICES_MAP:
        SERVICES_MAP = {
            ROLE: role_service,
            SPECIALTY: specialty_service,
            HOSPITAL: hospital_service,
            PERSON: person_service,
            ACCOUNT: account_service,
            }

def get_service(service_name):
    _init_service_map()
    global SERVICES_MAP
    return SERVICES_MAP.get(service_name, None)
