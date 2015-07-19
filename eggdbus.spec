%define api	1
%define major	0
%define libname	%mklibname %{name} %{api} %{major}
%define devname	%mklibname -d %{name}

Summary:	Experimental D-Bus bindings for GObject
Name:		eggdbus
Version:	0.6
Release:	12
License:	LGPLv2
Group:		System/Libraries
Url:		http://cgit.freedesktop.org/~david/eggdbus
Source0:	http://cgit.freedesktop.org/~david/eggdbus/snapshot/%{name}-%{version}.tar.gz
Patch0:		eggdbus-0.6-automake-1.13.patch

BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkgconfig(dbus-glib-1)

%description
Experimental D-Bus bindings for GObject.

%package -n %{libname}
Group:		System/Libraries
Summary:	Experimental D-Bus bindings for GObject

%description -n %{libname}
Experimental D-Bus bindings for GObject.

This package contains the shared libraries of %{name}.

%package -n %{devname}
Summary:	Development files for EggDBus
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for EggDBus.

%prep
%setup -q
%apply_patches
autoheader
./autogen.sh

%build
%configure2_5x \
	--enable-gtk-doc \
	--disable-static
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/gtk-doc/html/tests

%files -n %{libname}
%{_libdir}/libeggdbus-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/gtk-doc/html/eggdbus
%{_datadir}/man/man1/*
%{_bindir}/*

