Summary:	Extension for Nautilus to write CD
Summary(pl):	Rozszerzenie Nautilusa do zapisu p³yt CD
Name:		nautilus-cd-burner
Version:	0.6.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	5ea4babfd0284230c5dfc5f9f1ef9d59
Patch0:		%{name}-locale-names.patch
URL:		http://www.gnome.org/
BuildRequires:	gnome-vfs2-devel >= 2.5.90
BuildRequires:	libglade2-devel >= 2.3.2
BuildRequires:	nautilus-devel >= 2.5.90
BuildRequires:	intltool
Requires(post): GConf2 
Requires:	cdrtools
Requires:	cdrtools-mkisofs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus-cd-burner is an extension to Nautilus that makes it easy to
write files to a CD burner.

%description -l pl
Nautilus-cd-burner to rozszerzenie Nautilusa, u³atwiaj±ce nagranie
plików na p³ycie CD.

%prep
%setup -q
%patch0 -p1

mv po/{no,nb}.po

%build
glib-gettextize --copy --force
intltoolize --copy --force
%{__autoconf}
%configure \
	--disable-schemas-install

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}

%post
%gconf_schema_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/nautilus-cd-burner
%attr(755,root,root) %{_libdir}/mapping-daemon
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/*.so
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/lib*.so*
%{_libdir}/gnome-vfs-2.0/modules/*.la
%{_libdir}/nautilus/extensions-1.0/lib*.la
%{_sysconfdir}/gnome-vfs-2.0/modules/*
%{_sysconfdir}/gconf/schemas/ncb.schemas
%{_datadir}/%{name}
