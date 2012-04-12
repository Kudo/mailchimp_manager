from setuptools import setup, find_packages

version = __import__('mailchimp_manager').__version__

setup(
    name = 'mailchimp_manager',
    version = version,
    description = 'MailChimp Manager',
    author = 'Kudo Chien',
    url = 'http://github.com/Kudo/mailchimp_manager',
    packages = find_packages(),
    zip_safe=False,
)
