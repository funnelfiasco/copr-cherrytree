%global git_date 20210616
%global git_rev 2633d5f
%global git_revision    2633d5fd44063d9105a5cd8fd5671ba226676b4c
%global progname        cherrytree
%global srcpkgdir       %{progname}-%{git_revision}
Name:       %{progname}-future
Version:    0.99.37.%{git_date}git%{git_rev}
Release:    1%{?dist}

Summary:    Hierarchical note taking application

License:    GPLv3+
URL:        http://www.giuspen.com/cherrytree/
Source0:    https://github.com/giuspen/cherrytree/archive/%{git_revision}.zip

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gcc-c++ libtool autoconf gtkmm30-devel gtksourceviewmm3-devel libxml++-devel
BuildRequires: libsq3-devel gettext-devel gettext intltool python3-lxml libxml2 gspell-devel
BuildRequires: libcurl-devel uchardet-devel
BuildRequires: fmt-devel
BuildRequires: spdlog-devel

Requires: atk
Requires: atkmm
Requires: at-spi2-atk
Requires: at-spi2-core
Requires: cairo
Requires: cairo-gobject
Requires: cairomm
Requires: enchant2
Requires: expat
Requires: fontconfig
Requires: freetype
Requires: fribidi
Requires: gdk-pixbuf2
Requires: glibc
Requires: glibmm24
Requires: graphite2
Requires: gspell
Requires: gtk3
Requires: gtkmm30
Requires: gtksourceview3
Requires: gtksourceviewmm3
Requires: harfbuzz
Requires: pango
Requires: pangomm
Requires: pcre
Requires: pcre2
Requires: pixman

%description
CherryTree is a hierarchical note taking application, featuring rich text and
syntax highlighting, storing all the data (including images) in a single XML
or SQLite file.


%prep
%setup -q -n %{srcpkgdir}

%build
mkdir build
cd build
export PKG_CONFIG_PATH=/usr/lib64/pkgconfig/
cmake -DBUILD_TESTING=OFF -DCMAKE_BUILD_TYPE=Debug ..
make %{?_smp_mflags}

%install
cmake -DCMAKE_INSTALL_PREFIX="%{buildroot}/usr" -P %{_builddir}/%{srcpkgdir}/build/cmake_install.cmake
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{progname}.desktop
# Put a few things in the places we expect
mkdir -p %{buildroot}%{_datadir}/mime/packages
mv %{buildroot}%{_datadir}/mime-info/* %{buildroot}/%{_datadir}/mime/packages
rmdir %{buildroot}/%{_datadir}/mime-info/

%find_lang %{progname}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
touch --no-create %{_datadir}/mime/packages &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    update-mime-database %{_datadir}/mime &> /dev/null || :
fi


%files -f %{progname}.lang
%license license.txt
%{_bindir}/%{progname}
%dir %{_datadir}/cherrytree
%{_datadir}/cherrytree/data/user-style.xml
%{_datadir}/cherrytree/data/script3.js
%{_datadir}/cherrytree/data/styles3.css
%{_datadir}/cherrytree/language-specs/clisp.lang
%{_datadir}/cherrytree/language-specs/dart.lang
%{_datadir}/cherrytree/language-specs/elixir.lang
%{_datadir}/cherrytree/language-specs/markdown-extra.lang
%{_datadir}/cherrytree/language-specs/nasm.lang
%{_datadir}/cherrytree/icons/ct_home.svg
%{_datadir}/cherrytree/styles/Amy.xml
%{_datadir}/cherrytree/styles/cobalt-darkened.xml
%{_datadir}/cherrytree/styles/classic.xml
%{_datadir}/cherrytree/styles/cobalt.xml
%{_datadir}/cherrytree/styles/kate.xml
%{_datadir}/cherrytree/styles/oblivion.xml
%{_datadir}/cherrytree/styles/solarized-dark.xml
%{_datadir}/cherrytree/styles/solarized-light.xml
%{_datadir}/cherrytree/styles/tango.xml
%{_datadir}/applications/%{progname}.desktop
%{_datadir}/metainfo/com.giuspen.%{progname}.metainfo.xml
%{_datadir}/mime/packages/%{progname}.mime
%{_datadir}/mime/packages/%{progname}.keys
%{_datadir}/icons/hicolor/scalable/apps/%{progname}.svg
%{_mandir}/man1/%{progname}.1.gz


%changelog
* Wed Jun 16 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.38.20210616git2633d5f-1
- Update to version 0.99.38

* Wed May 19 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.37.20210519git6ee5bc4-1
- Update to version 0.99.37

* Thu May 13 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.36.20210513git1e34cc1-1
- Update to latest upstream snapshot
- Includes new translations and keyboard shortcuts

* Sat May 01 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.36.20210501gitef48471-1
- Update to latest upstream snapshot

* Tue Apr 13 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.33.20210413gitc8f974e-1
- Update to latest upstream snapshot
- Updates translations
- Makes headings configurable

* Tue Mar 30 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.33.20210330git68a5ef3-1
- Update to latest upstream snapshot
- Adds support for Korean dialogs

* Tue Mar 23 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.33.20210323gitcdb41a6-1
- Update to version 0.99.33

* Fri Mar 19 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.32.20210319git5c731cd-3
- Address more fedora-review issues

* Fri Mar 19 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.32.20210319git5c731cd-1
- Update to latest upstream snapshot
- Address a few more fedora-review issues

* Thu Mar 18 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.32.20210318git4d58c84-2
- Fixes for fedora-review output

* Thu Mar 18 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.32.20210318git4d58c84-1
- Update to latest upstream snapshot

* Mon Mar 15 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.32.20210315git7bdc5f8-1
- Update to version 0.99.32

* Tue Mar 09 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.31.20210308gitbbe53fa-1
- Update to latest upstream snapshot
- Includes version 0.99.31

* Fri Feb 19 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.30.20210219git277601d-1
- Update to latest upstream snapshot

* Sat Feb 06 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.30.20210206git1f4962e-1
- Update to latest upstream snapshot

* Sat Jan 30 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.30.20210130gitf466dc6-1
- Update to latest upstream snapshot

* Mon Jan 25 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.30.20210125git4ecd0e6-1
- Update to version 0.99.30

* Sat Jan 23 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.29.20210123git2484970-1
- Update to latest upstream snapshot

* Tue Jan 19 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.29.20210118git9cb2d9c-1
- Update to latest upstream snapshot
- Includes version 0.99.29

* Mon Jan 04 2021 Ben Cotton <bcotton@fedoraproject.org> - 0.99.28.20210104git5a77e32-1
- Update to latest upstream snapshot
- Includes version 0.99.28

* Thu Dec 17 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.25.20201217git7fe5cc3-2
- Includes a fix for build failures on Rawhide.

* Thu Dec 17 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.25.20201217git44ad7a6-1
- Update to latest upstream snapshot
- Includes version 0.99.25

* Wed Dec 02 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.24.20201202git890ba12-1
- Update to version 0.99.24

* Wed Nov 18 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.20.20201118git95f358f-1
- Update to latest upstream snapshot

* Tue Nov 17 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.20.20201117git736ca99-1
- Update to latest upstream snapshot
- Includes version 0.99.20

* Wed Nov 11 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.19.20201111gitd61e746-1
- Update to latest upstream snapshot
- Includes version 0.99.19

* Mon Nov 02 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.18.20201106git84ce680-1
- Update to latest upstream snapshot

* Mon Nov 02 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.18.20201102gitdea7e7c-1
- Update to latest upstream snapshot

* Thu Oct 29 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.18.20201029gitfaa68ab-1
- Update to version 0.99.18

* Mon Oct 26 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.17.20201026git6aa84df-1
- Update to latest upstream snapshot
- Includes version 0.99.17

* Fri Oct 16 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.16.20201016git3cc2d92-1
- Update to latest upstream snapshot

* Wed Oct 14 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.15.20201014gite3e08ba-1
- Update to latest upstream snapshot
- Includes support for huge xml files

* Thu Oct 08 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.15.20201008git82b401a-1
- Update to version 0.99.15

* Thu Oct 01 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.14.20201001gitb6a0ac3-1
- Update to version 0.99.14

* Mon Sep 28 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.13.20200928gitc2b7465-1
- Update to version 0.99.13

* Fri Sep 25 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.12.20200925gite164abc-1
- Update to latest upstream snapshot
- Includes 100% translations for: sl, tr

* Thu Sep 24 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.12.20200924git872d59b-1
- Update to latest upstream snapshot

* Wed Sep 23 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.12.20200923gitba29f32-1
- Update to latest upstream snapshot
- Includes 100% translations for: hy, it, pl, ru, sv, uk
- Includes single-file HTML export

* Mon Sep 21 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.12.20200921gitf2cfad1-1
- Update to latest upstream snapshot
- Includes 0.99.12 release
- Includes translations for: cs, nl, hy, it, and sv

* Fri Sep 18 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.11.20200918git370f605-1
- Update to latest upstream snapshot
- Fixes issue where styles are not packaged

* Thu Sep 17 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.11.20200917gita9cc562-1
- Update to latest upstream snapshot
- Adds 'Amy' style for gtksourceview

* Wed Sep 16 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.11.20200916git344ae23-1
- Update to latest upstream snapshot

* Sun Sep 13 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.11.20200913gita562f76-1
- Update to version 0.99.11

* Fri Sep 11 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.10.20200911git9c30668-1
- Update to latest upstream snapshot
- Includes implentation of "reload after external update to ct* file" feature

* Tue Sep 08 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.10.20200908gitecbaada-1
- Update to latest upstream snapshot
- Includes 0.99.10 release

* Tue Sep 01 2020 Ben Cotton <bcotton@fedoraproject.orG> - 0.99.9.20200901gitcc43bb2-1
- Update to latest upstream snapshot

* Mon Aug 24 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.9.20200824git0e5f27a-1
- Update to latest upstream snapshot
- Includes 0.99.9 release

* Tue Aug 18 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.8.20200813git54c529f-1
- Update to latest upstream snapshot
- Includes 0.99.8 release

* Wed Aug 12 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.7.20200812git72ba066-1
- Update to latest upstream snapshot

* Sun Aug 9 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.7.20200809git551237c-1
- Update to latest upstream snapshot
- Includes "future becomes present" (still tagged 0.99.7 in upstream config)

* Thu Aug 6 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.7.20200806git5151d6a-1
- Update to latest upstream snapshot

* Mon Aug 3 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.7.20200803git63db740-1
- Update to latest upstream snapshot
- Includes 0.99.7 release

* Fri Jul 31 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.6.20200731git80f2886-1
- Update to latest upstream snapshot

* Tue Jul 28 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.6.20200728git36c4bc9-1
- Update to latest upstream snapshot

* Mon Jul 20 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.6.20200720git801430e-1
- Update to the latest upstream snapshot
- Includes 0.99.6 release

* Fri Jul 17 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.5.20200717git06242e7-1
- Update to the latest upstream snapshot
- Includes a fix for PDF exports

* Thu Jul 16 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.5.20200716gitbc31203-1
- Update to the latest upstream snapshot
- Includes 0.99.5 release
- Includes support for importing Leo files

* Thu Jul 09 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.4.20200708git088c243-1
- Update to the latest upstream snaphot
- Includes 0.99.4 release

* Wed Jul 01 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.3.20200701gitc94c9df-1
- Missed that upstream bumped the release version. This is only a packaging update.

* Wed Jul 01 2020 Ben Cotton <bcotton@fedoraproject.rog> - 0.99.2.20200701gitc94c9df-1
- Update to latest upstream snapshot

* Wed Jun 24 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.2.20200623git90c4526-1
- Update to latest upstream snapshot
- Includes Pandoc import support
- Includes support for inserting a table of contents
- Includes debuginfo

* Tue Jun 09 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.1.20200609giteb02517-1
- Update to latest upstream snapshot

* Mon Jun 01 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.0.20200601git33f4bc1-1
- Update to latest upstream snapshot
- Includes support for importing markdown and Zim files

* Tue May 26 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.0.20200526git4e15514-1
- Update to latest upstream snapshot
- Includes support for file importing

* Tue May 19 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.0.20200519git11a58ef-1
- Update to latest upstream snapshot

* Mon May 11 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.99.0.20200511git6bac8ac-1
- Update to latest upstream snapshot
- Inludes language support

* Wed May 06 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.0.1.20200506gitc1b48d5-1
- Update to latest upstream snapshot
- Includes fixes for 32-bit compilation
- Includes the ability to skip tests

* Tue May 05 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.0.1.20200505git26afcc6-1
- Update to latest upstream snapshot

* Sun May 03 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.0.1.1b8db2b-1
- Update to latest upstream snapshot

* Fri May 01 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.0.1.20200429git7a26f27-2
- Add desktop niceties

* Wed Apr 29 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.0.1.20200429git7a26f27-1
- Bring the version string closer to Fedora's requirements

* Wed Apr 29 2020 Ben Cotton <bcotton@fedoraproject.org> - 0.0.1.git7a26f27-1
- Initial COPR packaging
