import re

RE_EMAIL = re.compile(r'(?P<username>([a-z0-9\_\.-]+))@(?P<domain>[a-z0-9\_\.-]+)', re.IGNORECASE)


def email_parse(email_address):
    if not RE_EMAIL.match(email_address):
        raise ValueError(f"wrong email: {email_address}")
    else:
        return RE_EMAIL.match(email_address).groupdict()


test_emails = ['jess+ica@gmail.com',
               'daniel-123@gmail.com',
               'edwSDS_fountain@gmail.com',
               'oda^wg@gmail.com',
               'sd.sdff@gmail.com']

for email in test_emails:
    try:
        print(email_parse(email))
    except ValueError as v:
        print(v)
