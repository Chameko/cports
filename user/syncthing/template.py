pkgname = "syncthing"
pkgver = "1.29.2"
pkgrel = 4
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/syncthing/syncthing/lib/build.Version=v{pkgver}",
    "./cmd/stdiscosrv",
    "./cmd/strelaysrv",
    "./cmd/syncthing",
]
make_check_args = [
    "./lib/...",
    "./cmd/stdiscosrv",
    "./cmd/strelaysrv",
    "./cmd/syncthing",
]
hostmakedepends = ["go"]
go_build_tags = ["noupgrade"]
pkgdesc = "Continuous file synchronization program"
license = "MPL-2.0"
url = "https://syncthing.net"
source = f"https://github.com/syncthing/syncthing/archive/v{pkgver}.tar.gz"
sha256 = "6446e52cb5ca6584710c3abd9250e0d9708486d2dc2264f7c869ade169876a57"


def pre_build(self):
    self.do("go", "generate", "github.com/syncthing/syncthing/lib/api/auto")


def post_install(self):
    self.install_license("cmd/strelaysrv/LICENSE", pkgname="syncthing-relaysrv")
    self.install_file("etc/firewall-ufw/syncthing", "etc/ufw/applications.d")
    self.install_file(
        "etc/linux-desktop/*.desktop", "usr/share/applications", glob=True
    )
    self.install_file("etc/linux-sysctl/30-syncthing.conf", "usr/lib/sysctl.d")

    self.install_man("man/*.[157]", glob=True)

    for f in [32, 64, 128, 256, 512]:
        self.install_file(
            f"assets/logo-{f}.png",
            f"usr/share/icons/hicolor/{f}x{f}/apps",
            name="syncthing.png",
        )
    self.install_file(
        "assets/logo-only.svg",
        "usr/share/icons/hicolor/scalable/apps",
        name="syncthing.svg",
    )

    self.install_service(self.files_path / "syncthing.user")


@subpackage("syncthing-relaysrv")
def _(self):
    self.subdesc = "relay server"
    self.license = "MIT"

    return [
        "usr/bin/strelaysrv",
        "usr/share/licenses/syncthing-relaysrv",
        "usr/share/man/man1/strelaysrv.1",
    ]


@subpackage("syncthing-discosrv")
def _(self):
    self.subdesc = "discovery server"

    return ["usr/bin/stdiscosrv", "usr/share/man/man1/stdiscosrv.1"]
