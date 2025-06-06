pkgname = "binutils-aarch64-none-elf"
_trip = pkgname.removeprefix("binutils-")
pkgver = "2.44"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    f"--target={_trip}",
    f"--with-sysroot=/usr/{_trip}",
    "--prefix=/usr",
    "--sbindir=/usr/bin",
    "--libdir=/usr/lib",
    "--mandir=/usr/share/man",
    "--infodir=/usr/share/info",
    "--without-debuginfod",
    "--with-system-zlib",
    "--with-mmap",
    "--with-pic",
    "--disable-install-libbfd",
    "--disable-multilib",
    "--disable-werror",
    "--disable-shared",
    "--disable-gold",
    "--disable-nls",
    "--enable-default-hash-style=gnu",
    "--enable-deterministic-archives",
    "--enable-64-bit-bfd",
    "--enable-threads",
    "--enable-plugins",
    "--enable-relro",
]
# requires specific version of autoconf
configure_gen = []
hostmakedepends = ["flex", "texinfo"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "GNU binutils for AArch64 bare metal targets"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/binutils"
source = f"$(GNU_SITE)/binutils/binutils-{pkgver}.tar.xz"
sha256 = "ce2017e059d63e67ddb9240e9d4ec49c2893605035cd60e92ad53177f4377237"
# resistance is futile
options = ["!check", "!lto", "linkundefver"]

if self.profile().cross:
    configure_args += [
        f"--host={self.profile().triplet}",
        f"--with-build-sysroot={self.profile().sysroot}",
    ]


def post_install(self):
    # fix up hardlinks
    for f in (self.destdir / f"usr/{_trip}/bin").iterdir():
        self.uninstall(f"usr/bin/{_trip}-{f.name}")
        self.install_link(
            f"usr/bin/{_trip}-{f.name}", f"../{_trip}/bin/{f.name}"
        )
    # this is also a hardlink
    self.uninstall(f"usr/{_trip}/bin/ld")
    self.install_link(f"usr/{_trip}/bin/ld", "ld.bfd")
    # remove unnecessary dupe
    self.uninstall("usr/lib")
    # collides with binutils proper
    self.uninstall("usr/share/info")
