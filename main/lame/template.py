pkgname = "lame"
pkgver = "3.100"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--enable-nasm", "--enable-shared"]
# broken m4
configure_gen = []
hostmakedepends = ["nasm"]
makedepends = ["ncurses-devel"]
pkgdesc = "Fast, high quality MP3 encoder"
license = "LGPL-2.1-or-later"
url = "https://lame.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/lame/lame-{pkgver}.tar.gz"
sha256 = "ddfe36cab873794038ae2c1210557ad34857a4b6bdc515785d1da9e175b1da1e"
options = ["linkundefver"]


@subpackage("lame-devel")
def _(self):
    return self.default_devel()
