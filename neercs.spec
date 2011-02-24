Summary:	neercs, a screen replacement
Name:		neercs
Version:	0.1
Release:	1
License:	WTFPL v2
Group:		Applications/Terminal
# git clone git://git.zoy.org/neercs.git
# tar --exclude-vcs -cjf neercs.tar.bz2 neercs
Source0:	%{name}.tar.bz2
# Source0-md5:	0b0e3cca24e86610c8f6d14e07abad4a
URL:		http://caca.zoy.org/wiki/neercs
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libcaca-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
neercs is a work-in-progress libcaca project.

Like GNU screen, it allows you to detach a session from a terminal,
but provides unique features:

- Grabbing a process that you forgot to start inside neercs
- Great screensaver
- 3D rotating cube to switch between full screen terms
- Real time thumbnails of your shells
- Special effects when closing a window
- Various window layouts...

%prep
%setup -q -n %{name}
install -d .auto

%{__sed} -i -e '/SUBDIRS/ s/doc//' Makefile.am

%build
%{__aclocal} -I .auto
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1
cp -p doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog COPYING NOTES README TODO
%attr(755,root,root) %{_bindir}/mini-neercs
%attr(755,root,root) %{_bindir}/neercs
%{_mandir}/man1/neercs.1*
