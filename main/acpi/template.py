pkgname = "acpi"
pkgver = "1.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "ACPI client for battery, power, and thermal readings"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/projects/acpiclient/files/acpiclient"
source = f"$(SOURCEFORGE_SITE)/acpiclient/acpi-{pkgver}.tar.gz"
sha256 = "e64c6e00b53cd797427ea32a160513425b03ed4f077733f71f1f09ff340f230b"
hardening = ["vis", "cfi"]
