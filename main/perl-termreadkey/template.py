pkgname = "perl-termreadkey"
pkgver = "2.38"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for simple terminal control"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/TermReadKey"
source = f"$(CPAN_SITE)/Term/TermReadKey-{pkgver}.tar.gz"
sha256 = "5a645878dc570ac33661581fbb090ff24ebce17d43ea53fd22e105a856a47290"
