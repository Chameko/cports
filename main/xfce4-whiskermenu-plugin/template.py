pkgname = "xfce4-whiskermenu-plugin"
pkgver = "2.9.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "gettext",
    "pkgconf",
]
makedepends = [
    "accountsservice-devel",
    "exo-devel",
    "garcon-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "xfce4-panel-devel",
    "xfconf-devel",
]
pkgdesc = "Xfce application launcher panel plugin"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/panel-plugins/xfce4-whiskermenu-plugin/start"
source = f"$(XFCE_SITE)/panel-plugins/xfce4-whiskermenu-plugin/{pkgver[:-2]}/xfce4-whiskermenu-plugin-{pkgver}.tar.bz2"
sha256 = "e2f28c066709bdcfe30236307026a562ec9aed790f9929a4e40aa411a5c7e3de"
