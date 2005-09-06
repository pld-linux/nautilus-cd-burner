Summary:	Extension for Nautilus to write CD
Summary(pl):	Rozszerzenie Nautilusa do zapisu p³yt CD
Name:		nautilus-cd-burner
Version:	2.12.0
Release:	1
License:	LGPL v2+/GPL v2+ 
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus-cd-burner/2.12/%{name}-%{version}.tar.bz2
# Source0-md5:	1647cb0192ced15979a2768dda23346d
URL:		http://www.gnome.org/
Buildrequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	hal-devel >= 0.5.0
BuildRequires:	intltool >= 0.33
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeui-devel >= 2.11.2-2
BuildRequires:	nautilus-devel >= 2.12.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun): GConf2 >= 2.10.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cdrtools
Requires:	cdrtools-mkisofs
Requires:	hal-libs >= 0.5.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus-cd-burner is an extension to Nautilus that makes it easy to
write files to a CD burner.

%description -l pl
Nautilus-cd-burner to rozszerzenie Nautilusa, u³atwiaj±ce nagranie
plików na p³ycie CD.

%package libs
Summary:	nautilus-cd-burner library
Summary(pl):	Biblioteka nautilus-cd-burner
Group:		Libraries

%description libs
nautilus-cd-burner library.

%description libs -l pl
Biblioteka nautilus-cd-burner.

%package devel
Summary:	Nautilus-cd-burner include files
Summary(pl):	Pliki nag³ówkowe Nautilus-cd-burner 
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gtk+2-devel >= 2:2.6.4

%description devel
Nautilus-cd-burner headers files.

%description devel -l pl
Pliki nag³ówkowe Nautilus-cd-burner.

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
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-*/modules/*.{la,a}
rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.{la,a}

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install ncb.schemas

%preun
%gconf_schema_uninstall ncb.schemas

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/nautilus-cd-burner
%attr(755,root,root) %{_libdir}/mapping-daemon
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/*.so
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/lib*.so*
%{_sysconfdir}/gnome-vfs-2.0/modules/*
%{_sysconfdir}/gconf/schemas/ncb.schemas
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-burn.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-burn.so
%{_libdir}/libnautilus-burn.la
%{_includedir}/libnautilus-burn
%{_pkgconfigdir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libnautilus-burn.a
