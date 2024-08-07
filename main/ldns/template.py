pkgname = "ldns"
pkgver = "1.8.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--with-drill",
    "--with-examples",
    "--disable-dane-ta-usage",
    "--with-trust-anchor=/etc/dns/root.key",
]
hostmakedepends = [
    "automake",
    "dnssec-anchors",
    "perl",
    "pkgconf",
    "slibtool",
]
makedepends = ["libpcap-devel", "openssl-devel", "dnssec-anchors"]
pkgdesc = "Modern DNS/DNSSEC library"
subdesc = "utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.nlnetlabs.nl/projects/ldns"
source = f"http://www.nlnetlabs.nl/downloads/ldns/ldns-{pkgver}.tar.gz"
sha256 = "838b907594baaff1cd767e95466a7745998ae64bc74be038dccc62e2de2e4247"
# no check target
options = ["!check"]


def init_configure(self):
    self.configure_args += [f"--with-ssl={self.profile().sysroot / 'usr'}"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("libldns")
def _lib(self):
    self.depends = ["dnssec-anchors"]

    return self.default_libs()


@subpackage("libldns-devel")
def _devel(self):
    self.depends += ["openssl-devel"]

    return self.default_devel()
