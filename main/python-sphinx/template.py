pkgname = "python-sphinx"
pkgver = "7.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-setuptools",
    "python-flit_core",
    "python-build",
    "python-installer",
]
checkdepends = ["python-pytest", "python-markupsafe"]
depends = [
    "python",
    "python-jinja2",
    "python-docutils",
    "python-pygments",
    "python-snowballstemmer",
    "python-babel",
    "python-alabaster",
    "python-imagesize",
    "python-requests",
    "python-packaging",
    "python-sphinxcontrib-applehelp",
    "python-sphinxcontrib-devhelp",
    "python-sphinxcontrib-htmlhelp",
    "python-sphinxcontrib-jsmath",
    "python-sphinxcontrib-qthelp",
    "python-sphinxcontrib-serializinghtml",
]
pkgdesc = "Python documentation generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://www.sphinx-doc.org/en/master"
source = f"$(PYPI_SITE)/s/sphinx/sphinx-{pkgver}.tar.gz"
sha256 = "7ad02a0677d43cbaab3f9477355a412e449472d3f4693e2df3842e7ccb7ae7c8"
# dependency of pytest, missing other checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")
