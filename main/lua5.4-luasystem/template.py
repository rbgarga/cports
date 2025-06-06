pkgname = "lua5.4-luasystem"
pkgver = "0.6.2"
pkgrel = 0
build_style = "makefile"
make_use_env = True
makedepends = ["lua5.4-devel"]
pkgdesc = "Platform independent system calls for Lua"
license = "MIT"
url = "http://lunarmodules.github.io/luasystem"
source = f"https://github.com/lunarmodules/luasystem/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fc7b9e3d74f74a39bae585b9bb2d1b25e75e50be9981948ccafe1aafdace49ea"
# no tests
options = ["!check"]


def init_configure(self):
    cfl = self.get_cflags(shell=True)
    ldfl = self.get_ldflags(shell=True)
    fl = [
        "prefix=/usr",
        "LUA_VERSION=5.4",
        "CC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("CC"),
        f"MYCFLAGS={cfl}",
        f"MYLDFLAGS={cfl} {ldfl}",
        f"LUAINC_linux={self.profile().sysroot}/usr/include/lua5.4",
    ]
    self.make_build_args += fl
    self.make_install_args += fl


def post_install(self):
    self.install_file("system/init.lua", "usr/share/lua/5.4", name="system.lua")
    self.install_license("LICENSE.md")
