Summary:	Extension for Nautilus to write CD
Summary(pl):	Rozszerzenie Nautilusa do zapisu p�yt CD
Name:		nautilus-cd-burner
Version:	2.7.6
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.7/%{name}-%{version}.tar.bz2
# Source0-md5:	a3bfa5efdd1b745447831a340c6a31e7
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel >= 2.7.91
BuildRequires:	hal-devel >= 0.2.92
BuildRequires:	intltool >= 0.22
BuildRequires:	libglade2-devel >= 1:2.4.0
BuildRequires:	nautilus-devel >= 2.7.4
Requires(post):	/sbin/ldconfig
Requires(post): GConf2 >= 2.7.91
Requires:	cdrtools
Requires:	cdrtools-mkisofs
Requires:	hal >= 0.2.92
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus-cd-burner is an extension to Nautilus that makes it easy to
write files to a CD burner.

%description -l pl
Nautilus-cd-burner to rozszerzenie Nautilusa, u�atwiaj�ce nagranie
plik�w na p�ycie CD.

%package devel
Summary:	Nautilus-cd-burner include files
Summary(pl):	Pliki nag��wkowe Nautilus-cd-burner 
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Nautilus-cd-burner headers files.

%description devel -l pl
Pliki nag��wkowe Nautilus-cd-burner.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
%{__autoconf}
%configure \
	--disable-schemas-install \
	--enable-hal

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-*/modules/*.la

%post
/sbin/ldconfig
%gconf_schema_install

%postun -p /sbin/ldconfig

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
%{_libdir}/libnautilus-burn.so.*.*.*
%{_sysconfdir}/gnome-vfs-2.0/modules/*
%{_sysconfdir}/gconf/schemas/ncb.schemas
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-burn.so
%{_libdir}/libnautilus-burn.la
%{_includedir}/libnautilus-burn
%{_pkgconfigdir}/*
