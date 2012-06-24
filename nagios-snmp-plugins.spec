Summary:	Plugins for Nagios to monitor remote disk and processes via SNMP
Summary(pl):	Wtyczki dla Nagiosa do zdalnego monitorowania dysku i proces�w po SNMP
Name:		nagios-snmp-plugins
Version:	1.0
Release:	4
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.hometree.net/pub/nagios-snmp-plugins/%{name}-%{version}.tar.gz
# Source0-md5:	cf70e405718d016debe206d01f54262c
Patch0:		%{name}-format-report.patch
URL:		ftp://ftp.hometree.net/pub/nagios-snmp-plugins/index.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	nagios-devel
BuildRequires:	net-snmp-devel >= 5.2.1.2
Requires:	nagios-core
Requires:	net-snmp-libs
Obsoletes:	netsaint-snmp-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_plugindir	%{_libdir}/nagios/plugins

%description
These plugins allow you to monitor disk space and running processes on
a remote machine via SNMP.

%description -l pl
Te wtyczki pozwalaj� na zdalne monitorowanie zaj�to�ci dysku i
dzia�ajacych proces�w po SNMP.

%prep
%setup -q
%patch0 -p1

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
