%global git_date 20200503
%global git_rev 1b8db2b
%global git_revision    1b8db2b6f1d135f319db46b6ae512478f9c038b1
%global progname        cherrytree
%global srcpkgdir	%{progname}-%{git_revision}
# Package does not provide debug sources
%global debug_package %{nil}
Name:       %{progname}-future
Version:    0.0.1.%{git_date}git%{git_rev}
Release:    1%{?dist}

Summary:    Hierarchical note taking application

License:    GPLv3+
URL:        http://www.giuspen.com/cherrytree/
Source0:    https://github.com/giuspen/cherrytree/archive/%{git_revision}.zip
#Patch0:     https://raw.githubusercontent.com/funnelfiasco/copr-cherrytree/master/0001-Fedora-uses-a-newer-gettext.patch

BuildRequires: cmake
BuildRequires: cpputest-devel
BuildRequires: desktop-file-utils
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
%setup -q -n %{srcpkgdir}

%build
mkdir build
cd build
export PKG_CONFIG_PATH=/usr/lib64/pkgconfig/
cmake ../future
make

%install
cmake -DCMAKE_INSTALL_PREFIX="%{buildroot}/usr" -P %{_builddir}/%{srcpkgdir}/build/cmake_install.cmake
# Put a few things in the places we expect
mkdir -p %{buildroot}%{_datadir}/mime/packages
mv %{buildroot}%{_datadir}/mime-info/* %{buildroot}/%{_datadir}/mime/packages
rmdir %{buildroot}/%{_datadir}/mime-info/


%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
touch --no-create %{_datadir}/mime/packages &>/dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    update-mime-database %{_datadir}/mime &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :


%files
%license license.txt
%{_bindir}/%{progname}
%dir %{_datadir}/cherrytree
%{_datadir}/cherrytree/data/script3.js
%{_datadir}/cherrytree/data/styles3.css
%{_datadir}/cherrytree/language-specs/clisp.lang
%{_datadir}/cherrytree/language-specs/markdown-extra.lang
%{_datadir}/applications/%{progname}.desktop
%{_datadir}/metainfo/%{progname}.metainfo.xml
%{_datadir}/mime/packages/%{progname}.mime
%{_datadir}/mime/packages/%{progname}.keys
%{_datadir}/icons/hicolor/scalable/apps/%{progname}.svg
%{_mandir}/man1/%{progname}.1.gz


%changelog
* Sun May 03 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.0.1.1b8db2b-1
- Update to latest upstream snapshot

* Fri May 01 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.0.1.20200429git7a26f27-2
- Add desktop niceties

* Wed Apr 29 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.0.1.20200429git7a26f27-1
- Bring the version string closer to Fedora's requirements

* Wed Apr 29 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.0.1.git7a26f27-1
- Initial COPR packaging
