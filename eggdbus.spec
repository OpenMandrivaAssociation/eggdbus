%define api 1
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name

Summary: Experimental D-Bus bindings for GObject
Name: eggdbus
Version: 0.6
Release: %mkrel 1
License: LGPLv2
Group: System/Libraries
URL: http://cgit.freedesktop.org/~david/eggdbus
Source0: http://cgit.freedesktop.org/~david/eggdbus/snapshot/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: dbus-glib-devel
BuildRequires: gtk-doc

%description
Experimental D-Bus bindings for GObject.

%package -n %libname
Group: System/Libraries
Summary: Experimental D-Bus bindings for GObject

%description -n %libname
Experimental D-Bus bindings for GObject.

This package contains the shared libraries of %{name}.

%package -n %develname
Summary: Development files for EggDBus
Group: Development/C
Provides: %name-devel = %version-%release
Requires: %libname = %{version}-%{release}

%description -n %develname
Development files for EggDBus.

%prep
%setup -q
./autogen.sh

%build
%configure2_5x --enable-gtk-doc --disable-static
%make


%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/tests

%clean
rm -rf $RPM_BUILD_ROOT


%files -n %libname
%defattr(-,root,root,-)
%doc AUTHORS 
%{_libdir}/libeggdbus-%api.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/gtk-doc/html/eggdbus
%{_datadir}/man/man1/*
%{_bindir}/*

