pkgname = "gst-plugins-rs"
# separate versioning from main gst
pkgver = "0.13.6"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = [
    "cargo",
    "cargo-c",
    "meson",
    "nasm",
    "pkgconf",
]
makedepends = [
    "dav1d-devel",
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "gtk4-devel",
    "libsodium-devel",
    "libwebp-devel",
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "GStreamer rust plugins"
license = "(MIT OR Apache-2.0) AND MPL-2.0 AND LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"https://gitlab.freedesktop.org/gstreamer/gst-plugins-rs/-/archive/{pkgver}.tar.gz"
sha256 = "9d7dd50aebc24e00a39729c88ca2c60b4c58425a6bc884de3248d6506a952410"
# takes forever
options = ["!check"]

if self.profile().wordsize == 32:
    broken = "requires atomic64"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_license("LICENSE-MIT")


@subpackage("gst-plugins-rs-gtk4")
def _(self):
    self.subdesc = "GTK4 sink"
    self.install_if = [self.parent]
    return ["usr/lib/gstreamer-1.0/libgstgtk4.so"]


@subpackage("gst-plugins-rs-devel")
def _(self):
    return self.default_devel()
