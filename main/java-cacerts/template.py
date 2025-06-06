pkgname = "java-cacerts"
pkgver = "1.0"
pkgrel = 1
depends = ["p11-kit"]
pkgdesc = "Script to update Java cacerts store"
license = "custom:none"
url = "https://chimera-linux.org"
# no tests
options = ["!check"]


def install(self):
    self.install_file(
        self.files_path / "java-cacerts",
        "etc/ca-certificates/update.d",
        mode=0o755,
    )
