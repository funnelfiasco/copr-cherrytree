%define debug_package %{nil}
Name:           cpputest
Version:        3.8
Release:        2%{?dist}
Summary:        CppUTest unit testing and mocking framework for C/C++

License:        BSD
URL:            https://cpputest.github.io/
Source0:        https://github.com/cpputest/cpputest/releases/download/v%{version}/cpputest-%{version}.tar.gz

BuildRequires:  gcc-c++
# Requires:       

%description
CppUTest is a C /C++ based unit xUnit test framework for unit testing
and for test-driving your code. It is written in C++ but is used in C
and C++ projects and frequently used in embedded systems but it works
for any C/C++ project.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Apr 30 2020 Ben Cotton <bcotton@fedoraproject.org> - 3.8-2
- Fix to build on aarch64 and armhfp

* Tue Jun 13 2017 Rob Spanton <rob@adventurousmachines.com
- Update to 3.8

* Wed Jan 14 2015 Rob Spanton <rspanton@zepler.net>
- 
