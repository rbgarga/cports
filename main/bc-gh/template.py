pkgname = "bc-gh"
pkgver = "5.2.0"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
make_use_env = True
pkgdesc = "Implementation of POSIX bc with GNU extensions"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = "https://git.yzena.com/gavin/bc"
source = f"https://github.com/gavinhoward/bc/releases/download/{pkgver}/bc-{pkgver}.tar.xz"
sha256 = "bb918d67b4fc6fc27634de343069a26c9ad05cf0c1c18cf05add5c821717741e"

def do_configure(self):
    self.do(
        self.chroot_cwd / "configure.sh",
        ["-GM", "-sbc.banner", "-sdc.tty_mode"],
        env = {
            "PREFIX": "/usr",
            "DESTDIR": self.chroot_destdir,
            "EXECSUFFIX": "-gh",
            "HOSTCC": "clang",
            "HOSTCFLAGS": self.get_cflags(shell = True, target = "host"),
        }
    )

def post_install(self):
    self.install_license("LICENSE.md")

    self.install_file("manuals/bc.1", "usr/share/man/man1", name = "bc-gh.1")
    self.install_file("manuals/dc.1", "usr/share/man/man1", name = "dc-gh.1")
