Summary:	Extension for Nautilus to write CD
Summary(pl):	Rozszerzenie Nautilusa do zapisu p�yt CD
Name:		nautilus-cd-burner
Version:	0.3.2
Release:	3
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.3/%{name}-%{version}.tar.bz2
URL:		http://www.gnome.org/
BuildRequires:	gnome-vfs2-devel >= 2.2.0
BuildRequires:	nautilus-devel >= 2.2.0
Requires:	cdrtools
Requires:	cdrtools-mkisofs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus-cd-burner is an extension to Nautilus that makes it easy to
write files to a CD burner.

%description -l pl
Nautilus-cd-burner to rozszerzenie Nautilusa, u�atwiaj�ce nagranie
plik�w na p�ycie CD.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/nautilus-cd-burner
%attr(755,root,root) %{_libdir}/mapping-daemon
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/*.so
%{_libdir}/gnome-vfs-2.0/modules/*.la
%{_sysconfdir}/gnome-vfs-2.0/modules/*
%{_datadir}/%{name}
