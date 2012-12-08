%define api 1
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define develname %mklibname -d %{name}

Summary:	Experimental D-Bus bindings for GObject
Name:		eggdbus
Version:	0.6
Release:	4
License:	LGPLv2
Group:		System/Libraries
URL:		http://cgit.freedesktop.org/~david/eggdbus
Source0:	http://cgit.freedesktop.org/~david/eggdbus/snapshot/%{name}-%{version}.tar.bz2
BuildRequires:	dbus-glib-devel
BuildRequires:	gtk-doc
BuildRequires:	libtool

%description
Experimental D-Bus bindings for GObject.

%package -n %{libname}
Group:		System/Libraries
Summary:	Experimental D-Bus bindings for GObject

%description -n %{libname}
Experimental D-Bus bindings for GObject.

This package contains the shared libraries of %{name}.

%package -n %{develname}
Summary:	Development files for EggDBus
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Development files for EggDBus.

%prep
%setup -q
./autogen.sh

%build
%configure2_5x --enable-gtk-doc --disable-static
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/gtk-doc/html/tests

%files -n %{libname}
%doc AUTHORS
%{_libdir}/libeggdbus-%{api}.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/gtk-doc/html/eggdbus
%{_datadir}/man/man1/*
%{_bindir}/*

%changelog
* Fri May 04 2012 Götz Waschk <waschk@mandriva.org> 0.6-3mdv2012.0
+ Revision: 795873
- remove libtool archive
- yearly rebuild

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6-2
+ Revision: 664127
- mass rebuild

* Mon Nov 23 2009 Götz Waschk <waschk@mandriva.org> 0.6-1mdv2011.0
+ Revision: 469347
- update build deps
- new version
- use git snapshot

* Tue Jul 14 2009 Götz Waschk <waschk@mandriva.org> 0.5-1mdv2010.0
+ Revision: 395803
- import eggdbus


* Tue Jul 14 2009 Götz Waschk <waschk@mandriva.org> 0.5-1mdv2010.0
- port to Mandriva

* Fri Jun 19 2009 David Zeuthen <davidz@redhat.com> - 0.5-1
- Update to 0.5

* Wed May 27 2009 David Zeuthen <davidz@redhat.com> - 0.4-1
- Update to 0.4

* Mon Feb  9 2009 David Zeuthen <davidz@redhat.com> - 0.3-1
- Initial spec file.

