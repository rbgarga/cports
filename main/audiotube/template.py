pkgname = "audiotube"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
_deps = [
    "kirigami-addons",
    "python-ytmusicapi",
    "yt-dlp",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    *_deps,
]
makedepends = [
    "futuresql-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "ki18n-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kwindowsystem-devel",
    "python-devel",
    "python-pybind11-devel",
    "qcoro-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
]
depends = [*_deps]
pkgdesc = "KDE Youtube Music player"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/audiotube"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/audiotube-{pkgver}.tar.xz"
sha256 = "1bd42686a3725669a6ed46a18ae94200858834710f0dcee621ea164349b80816"
# only test needs net
options = ["!check"]
