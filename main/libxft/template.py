pkgname = "libxft"
pkgver = "2.3.8"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "pkgconf", "slibtool", "xorg-util-macros"]
makedepends = [
    "xorgproto",
    "libxrender-devel",
    "freetype-devel",
    "fontconfig-devel",
]
pkgdesc = "X font library"
license = "MIT"
url = "https://xorg.freedesktop.org"
source = f"$(XORG_SITE)/lib/libXft-{pkgver}.tar.gz"
sha256 = "32e48fe2d844422e64809e4e99b9d8aed26c1b541a5acf837c5037b8d9f278a8"
# crashes
hardening = ["!int"]


def post_install(self):
    self.install_license("COPYING")


@subpackage("libxft-devel")
def _(self):
    return self.default_devel()
