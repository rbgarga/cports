pkgname = "kaccounts-providers"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "intltool",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kaccounts-integration-devel",
    "ki18n-devel",
    "kio-devel",
    "kpackage-devel",
    "libaccounts-qt-devel",
    "qcoro-devel",
    "signond-devel",
]
pkgdesc = "KDE providers for online accounts"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/network/kaccounts-providers"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kaccounts-providers-{pkgver}.tar.xz"
sha256 = "bf400b1aef13f235ffa25741b45a6a2452f063aac4de1fd94a8ffec55fba1e4d"
hardening = ["vis"]


if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
    makedepends += ["qt6-qtwebengine-devel"]
