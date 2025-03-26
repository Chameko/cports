pkgname = "libcap"
pkgver = "2.75"
pkgrel = 0
build_style = "makefile"
make_build_args = ["GOLANG=no"]
make_install_args = [
    "PKGCONFIGDIR=/usr/lib/pkgconfig",
    "SBINDIR=/usr/bin",
    "LIBDIR=/usr/lib",
    "exec_prefix=/usr",
    "RAISE_SETFCAP=no",
]
make_check_target = "test"
make_use_env = True
hostmakedepends = ["pkgconf", "perl"]
makedepends = ["attr-devel", "linux-headers"]
pkgdesc = "POSIX.1e capabilities suite"
license = "GPL-2.0-only"
url = "http://sites.google.com/site/fullycapable"
source = (
    f"$(KERNEL_SITE)/libs/security/linux-privs/libcap2/libcap-{pkgver}.tar.xz"
)
sha256 = "de4e7e064c9ba451d5234dd46e897d7c71c96a9ebf9a0c445bc04f4742d83632"


def init_configure(self):
    eargs = [
        "CC=" + self.get_tool("CC"),
        "BUILD_CC=" + self.get_tool("CC", target="host"),
    ]
    self.make_build_args += eargs
    self.make_check_args += eargs


@subpackage("libcap-devel")
def _(self):
    self.depends += ["linux-headers"]
    return self.default_devel()


@subpackage("libcap-progs")
def _(self):
    return self.default_progs()
