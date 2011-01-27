Summary:	Plugins for Nagios to monitor remote disk and processes via SNMP
Summary(pl.UTF-8):	Wtyczki dla Nagiosa do zdalnego monitorowania dysku i procesów po SNMP
Name:		nagios-snmp-plugins
Version:	1.3
Release:	2
License:	GPL v2
Group:		Networking
#Source0:	http://github.com/glensc/nagios-snmp-plugins/tarball/master#/%{name}-%{version}.tgz
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	6d9d8c2ea166f0a22bb2502da28ab3ca
Source1:	%{name}.cfg
URL:		http://github.com/glensc/nagios-snmp-plugins
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	net-snmp-devel >= 5.2.1.2
Requires:	nagios-core
Requires:	net-snmp-libs
Obsoletes:	netsaint-snmp-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_libdir}/nagios/plugins

%description
These plugins allow you to monitor on a remote machine via SNMP:
- disk space
- running processes
- system load
- swap usage

%description -l pl.UTF-8
Te wtyczki pozwalają na zdalne monitorowanie zajętości dysku i
działajacych procesów po SNMP.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--bindir=%{plugindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{plugindir}}
%{__sed} -e 's,@plugindir@,%{plugindir},' %{SOURCE1} > $RPM_BUILD_ROOT%{_sysconfdir}/%{name}.cfg
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.cfg
%attr(755,root,root) %{plugindir}/*
