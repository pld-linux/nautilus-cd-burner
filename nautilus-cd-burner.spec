Summary:	Extension for Nautilus to write CD
Summary(pl.UTF-8):	Rozszerzenie Nautilusa do zapisu płyt CD
Name:		nautilus-cd-burner
Version:	2.22.0
Release:	1
License:	LGPL v2+/GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-cd-burner/2.22/%{name}-%{version}.tar.bz2
# Source0-md5:	e75c61879a12ab329fd2f3081b7e5d76
Patch0:		%{name}-desktop.patch
URL:		http://www.gnome.org/
Buildrequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	eel-devel >= 2.22.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gnome-mount-devel >= 0.6
BuildRequires:	gtk+2-devel >= 2:2.12.5
BuildRequires:	hal-devel >= 0.5.10
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.22.0
BuildRequires:	nautilus-devel >= 2.22.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,preun):	GConf2
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cdrecord
Requires:	hal-libs >= 0.5.10
Requires:	mkisofs
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus-cd-burner is an extension to Nautilus that makes it easy to
write files to a CD burner.

%description -l pl.UTF-8
Nautilus-cd-burner to rozszerzenie Nautilusa, ułatwiające nagranie
plików na płycie CD.

%package libs
Summary:	nautilus-cd-burner library
Summary(pl.UTF-8):	Biblioteka nautilus-cd-burner
Group:		X11/Libraries
Requires:	glib2 >= 1:2.15.4

%description libs
nautilus-cd-burner library.

%description libs -l pl.UTF-8
Biblioteka nautilus-cd-burner.

%package devel
Summary:	Nautilus-cd-burner include files
Summary(pl.UTF-8):	Pliki nagłówkowe Nautilus-cd-burner
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 1:2.15.4
Requires:	gtk+2-devel >= 2:2.12.5
Requires:	hal-devel >= 0.5.10

%description devel
Nautilus-cd-burner headers files.

%description devel -l pl.UTF-8
Pliki nagłówkowe Nautilus-cd-burner.

%package static
Summary:	Static nautilus-cd-burner library
Summary(pl.UTF-8):	Statyczna biblioteka nautilus-cd-burner
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static nautilus-cd-burner library.

%description static -l pl.UTF-8
Statyczna biblioteka nautilus-cd-burner.

%prep
%setup -q
%patch0 -p1

sed -i -e s#sr@Latn#sr@latin# po/LINGUAS
mv -f po/sr@{Latn,latin}.po

%build
cp -f /usr/share/automake/config.sub .
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--enable-gnome-mount \
	--enable-static \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-2.0/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install nautilus-cd-burner.schemas
%update_desktop_database_post
%update_icon_cache hicolor

%preun
%gconf_schema_uninstall nautilus-cd-burner.schemas

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%post	libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/nautilus-cd-burner
%attr(755,root,root) %{_libdir}/nautilus/extensions-2.0/libnautilus-burn-extension.so
%{_sysconfdir}/gconf/schemas/nautilus-cd-burner.schemas
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/*/apps/*.svg
%{_desktopdir}/nautilus-cd-burner-open-iso.desktop
%{_desktopdir}/nautilus-cd-burner.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-burn.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnautilus-burn.so.4

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilus-burn.so
%{_libdir}/libnautilus-burn.la
%{_includedir}/libnautilus-burn
%{_pkgconfigdir}/libnautilus-burn.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libnautilus-burn.a
