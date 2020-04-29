%global git_revision    7a26f271b78e7a3769fc1f5a627dc11d586cbb53
%global progname        cherrytree
# Package does not provide debug sources
%global debug_package %{nil}
Name:       %{progname}-future
Version:    0.0.1.git%{git_revision}
Release:    1%{?dist}
Summary:    Hierarchical note taking application

License:    GPLv3+
URL:        http://www.giuspen.com/cherrytree/
Source0:    https://github.com/giuspen/cherrytree/archive/%{git_revision}.zip
Patch0:     https://raw.githubusercontent.com/funnelfiasco/copr-cherrytree/master/0001-Fedora-uses-a-newer-gettext.patch

BuildRequires: cpputest-devel
BuildRequires: gcc-c++ libtool autoconf gtkmm30-devel gtksourceviewmm3-devel libxml++-devel
BuildRequires: libsq3-devel gettext-devel gettext intltool python3-lxml libxml2 gspell-devel

# This may be more explicit requires than strictly necessary. It is the result of running ldd on
# the binary and `rpm -q --whatprovides`-ing the results
Requires: atk
Requires: atkmm
Requires: at-spi2-atk
Requires: at-spi2-core
Requires: bzip2-libs
Requires: cairo
Requires: cairo-gobject
Requires: cairomm
Requires: dbus-libs
Requires: enchant2
Requires: expat
Requires: fontconfig
Requires: freetype
Requires: fribidi
Requires: gdk-pixbuf2
Requires: glib2
Requires: glibc
Requires: glibmm24
Requires: graphite2
Requires: gspell
Requires: gtk3
Requires: gtkmm30
Requires: gtksourceview3
Requires: gtksourceviewmm3
Requires: harfbuzz
Requires: libblkid
Requires: libdatrie
Requires: libepoxy
Requires: libffi
Requires: libgcc
Requires: libgcrypt
Requires: libgpg-error
Requires: libmount
Requires: libpng
Requires: libselinux
Requires: libsigc++20
Requires: libstdc++
Requires: libthai
Requires: libwayland-client
Requires: libwayland-cursor
Requires: libwayland-egl
Requires: libX11
Requires: libXau
Requires: libxcb
Requires: libXcomposite
Requires: libXcursor
Requires: libXdamage
Requires: libXext
Requires: libXfixes
Requires: libXi
Requires: libXinerama
Requires: libxkbcommon
Requires: libxml++
Requires: libxml2
Requires: libXrandr
Requires: libXrender
Requires: lz4-libs
Requires: pango
Requires: pangomm
Requires: pcre
Requires: pcre2
Requires: pixman
Requires: sqlite-libs
Requires: systemd-libs
Requires: xz-libs
Requires: zlib

%description
CherryTree is a hierarchical note taking application, featuring rich text and
syntax highlighting, storing all the data (including images) in a single XML
file with extension ".ctd".


%prep
%setup -q -n %{progname}-%{git_revision}
%patch0 -p1

%build
cd future
export PKG_CONFIG_PATH=/usr/lib64/pkgconfig/
./build.sh R

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{progname} %{buildroot}/%{_bindir}/%{progname}

%files
%license license.txt
%{_bindir}/%{progname}

%changelog
* Wed Apr 29 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.0.1.git7a26f27-1
- Initial COPR packaging
