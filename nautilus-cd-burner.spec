# Conditional build
%bcond_without	hal	# disable HAL support
#
Summary:	Extension for Nautilus to write CD
Summary(pl):	Rozszerzenie Nautilusa do zapisu p³yt CD
Name:		nautilus-cd-burner
Version:	2.8.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	894f58d4dafdd74426cbc6734de5b023
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel >= 2.7.92
%{?with_hal:BuildRequires:	hal-devel >= 0.2.98}
BuildRequires:	intltool >= 0.22
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	nautilus-devel >= 2.8.0
Requires(post): GConf2 >= 2.7.92
Requires:	cdrtools
Requires:	cdrtools-mkisofs
%{?with_hal:Requires:	hal >= 0.2.98}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus-cd-burner is an extension to Nautilus that makes it easy to
write files to a CD burner.

%description -l pl
Nautilus-cd-burner to rozszerzenie Nautilusa, u³atwiaj±ce nagranie
plików na p³ycie CD.

%package devel
Summary:	Nautilus-cd-burner include files
Summary(pl):	Pliki nag³ówkowe Nautilus-cd-burner 
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.4.0

%description devel
Nautilus-cd-burner headers files.

%description devel -l pl
Pliki nag³ówkowe Nautilus-cd-burner.

%package libs
Summary:	nautilus-cd-burner library
Summary(pl):	Biblioteka nautilus-cd-burner
Group:		Libraries

%description libs
nautilus-cd-burner library.

%description libs -l pl
Biblioteka nautilus-cd-burner.

%package static
Summary:	Static nautilus-cd-burner library
Summary(pl):	Statyczna biblioteka nautilus-cd-burner
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nautilus-cd-burner library.

%description static -l pl
Statyczna biblioteka nautilus-cd-burner.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure \
	--enable-static \
	--disable-schemas-install \
	--%{?with_hal:en}%{!?with_hal:dis}able-hal

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-*/modules/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.a

%post
%gconf_schema_install

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/nautilus-cd-burner
%attr(755,root,root) %{_libdir}/mapping-daemon
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/*.so
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/lib*.so*
%{_libdir}/nautilus/extensions-1.0/lib*.la
%{_sysconfdir}/gnome-vfs-2.0/modules/*
%{_sysconfdir}/gconf/schemas/ncb.schemas
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-burn.so
%{_libdir}/libnautilus-burn.la
%{_includedir}/libnautilus-burn
%{_pkgconfigdir}/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-burn.so.*.*.*

%files static
%defattr(644,root,root,755)
%{_libdir}/libnautilus-burn.a
