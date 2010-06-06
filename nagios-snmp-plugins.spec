Summary:	Plugins for Nagios to monitor remote disk and processes via SNMP
Summary(pl.UTF-8):	Wtyczki dla Nagiosa do zdalnego monitorowania dysku i procesów po SNMP
Name:		nagios-snmp-plugins
Version:	1.2
Release:	5
License:	GPL v2
Group:		Networking
Source0:	http://www.softwareforge.de/releases/nagios-snmp-plugins/%{name}-%{version}.tar.gz
# Source0-md5:	54f2b7ad0df22a9c9dcd8c64cb8ef955
Source1:	%{name}.cfg
Patch0:		%{name}-list-formatting.patch
Patch1:		check_snmp_swap.patch
Patch2:		check_snmp_load.patch
URL:		http://henning.schmiedehausen.org/eyewiki/Wiki.jsp?page=NagiosSnmpPlugins
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	nagios-devel
BuildRequires:	net-snmp-devel >= 5.2.1.2
Requires:	nagios-core
Requires:	net-snmp-libs
Obsoletes:	netsaint-snmp-plugins
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/nagios/plugins
%define		plugindir	%{_libdir}/nagios/plugins

%description
These plugins allow you to monitor disk space and running processes on
a remote machine via SNMP.

%description -l pl.UTF-8
Te wtyczki pozwalają na zdalne monitorowanie zajętości dysku i
działajacych procesów po SNMP.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
