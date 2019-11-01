%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

%define pygtk_version 2.8.0
%define pygobject_version 2.15.2
%define gtksourceview_version 2.3.0

Name:           pygtksourceview
Version:        2.10.1
Release:        21%{?dist}
Summary:        Python bindings for gtksourceview

# No version specified.
License:        LGPLv2+
URL:            http://download.gnome.org/sources/pygtksourceview/
#VCS: git:git://git.gnome.org/pygtksourceview
Source0:        https://download.gnome.org/sources/pygtksourceview/2.10/pygtksourceview-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  gtk-doc
BuildRequires:  gtksourceview2-devel >= %{gtksourceview_version}
BuildRequires:  pygobject2-devel >= %{pygobject_version}
BuildRequires:  pygtk2-devel >= %{pygtk_version}
BuildRequires:  python2-devel

%description
The %{name} package contains Python bindings for the gtksourceview
library.

%package devel
Summary: Development files for using %{name} in Python programs
Requires: %{name} = %{version}-%{release}
Requires: %{name}-doc = %{version}-%{release}
Requires: gtksourceview2-devel >= %{gtksourceview_version}
Requires: pkgconfig
Requires: pygtk2-devel >= %{pygtk_version}

%description devel
This package contains files required to build Python programs that
use the %{name} bindings.

%package doc
Summary: Documentation files for %{name}

%description doc
This package contains documentation files for %{name}.

%prep
%setup -q

%build
%configure
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

#rm $RPM_BUILD_ROOT%{python_sitearch}/gtksourceview2.la

%files
%doc COPYING AUTHORS README NEWS
%{python2_sitearch}/*

%files devel
%{_datadir}/pygtk/2.0/defs/gtksourceview2.defs
%{_libdir}/pkgconfig/pygtksourceview-2.0.pc

%files doc
%{_datadir}/gtk-doc/html/pygtksourceview2

%changelog
* Fri Nov 01 2019 Ben Cotton <bcotton@fedoraproject.org> - 2.10.1-21
- Move to COPR

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.10.1-18
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-13
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.10.1-4
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Apr 18 2010 Matthias Clasen <mclasen@redhat.com> - 2.10.1-1
- Update to 2.10.1

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.10.0-1
- Update 2.10.0

* Mon Feb 22 2010 Matthias Clasen <mclasen@redhat.com> - 2.9.2-1
- Update to 2.9.2

* Tue Jan 19 2010 Matthew Barnes <mbarnes@redhat.com> - 2.9.1-2
- Add gtk-doc build requirement.

* Sat Dec  5 2009 Matthias Clasen <mclasen@redhat.com> - 2.9.1-1
- Update to 2.9.1

* Wed Sep 23 2009 Matthias Clasen <mclasen@redhat.com> - 2.8.0-1
- Update to 2.8.0

* Mon Aug 17 2009 Matthias Clasen <mclasen@redhat.com> - 2.7.0-1
- Update to 2.7.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 31 2009 Matthias Clasen <mclasen@redhat.com> - 2.6.0-1
- Update to 2.6.0

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.4.0-2
- Rebuild for Python 2.6

* Sun Sep 21 2008 Matthias Clasen <mclasen@redhat.com> - 2.4.0-1
- Update to 2.4.0

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.0-2
- fix license tag

* Mon Mar 10 2008 Matthias Clasen <mclasen@redhat.com> - 2.2.0-1
- Update to 2.2.0

* Wed Feb  6 2008 Matthias Clasen <mclasen@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Tue Jan 22 2008 Matthew Barnes <mbarnes@redhat.com> - 2.1.0-2.fc9
- Fix a typo.

* Mon Jan 21 2008 Matthew Barnes <mbarnes@redhat.com> - 2.1.0-1.fc9
- Update to 2.1.0

* Fri Oct 26 2007 Matthew Barnes <mbarnes@redhat.com> - 2.0.0-2.fc9
- Add subpackage pygtksourceview-doc (bug #342991).

* Mon Sep 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.0.0-1
- Update to 2.0.0

* Tue Sep 11 2007 Matthew Barnes <mbarnes@redhat.com> - 1.90.5-1
- Update to 1.90.5

* Tue Sep  4 2007 Matthias Clasen <mclasen@redhat.com> - 1.90.4-1
- Update to 1.90.4

* Wed Aug  1 2007 Matthias Clasen <mclasen@redhat.com> - 1.90.3-1
- Update to 1.90.3

* Tue Jul 10 2007 Matthias Clasen <mclasen@redhat.com> - 1.90.2-2
- Rebuild against the gtksourceview2 package

* Fri Jul 06 2007 Matthew Barnes <mbarnes@redhat.com> - 1.90.2-1.fc8
- Update to 1.90.2
- Bump gtksourceview requirement to 1.90.2.

* Tue Jul 03 2007 Florian La Roche <laroche@redhat.com> 1.90.1-3
- fix macro typo

* Tue Jun 26 2007 Matthias Clasen <mclasen@redhat.com> 1.90.1-2
- Incorporate package review feedback

* Mon Jun 25 2007 Matthias Clasen <mclasen@redhat.com> 1.90.1-1
- Initial package
