from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in invoice_qr_generator/__init__.py
from invoice_qr_generator import __version__ as version

setup(
	name="invoice_qr_generator",
	version=version,
	description="It is used to Generate QR code for invoices",
	author="Quantbit Technologies Pvt ltd",
	author_email="contact@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
