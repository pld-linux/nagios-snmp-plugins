Summary:	Plugins for Nagios to monitor remote disk and processes via SNMP
Name:		nagios-snmp-plugins
Version:	1.0
Release:	0.3
Epoch:		0
License:	GPL
Group: 		Applications/System
Source0:	ftp://ftp.hometree.net/pub/nagios-snmp-plugins/%{name}-%{version}.tar.gz
# Source0-md5:	cf70e405718d016debe206d01f54262c
URL:		ftp://ftp.hometree.net/pub/nagios-snmp-plugins/index.html
BuildRequires:	nagios-devel
BuildRequires:	net-snmp-devel
Requires:	nagios
Requires:	net-snmp-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_plugindir	%{_libdir}/nagios/plugins

%description
These plugins allow you to monitor disk space and running processes on
a remote machine via SNMP.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}

install check_snmp_disk $RPM_BUILD_ROOT%{_plugindir}
install check_snmp_proc $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_plugindir}/*
