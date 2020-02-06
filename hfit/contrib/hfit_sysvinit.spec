%define debug_package %{nil}
%define _rpmfilename RPM/%%{NAME}-%%{VERSION}-%%{RELEASE}.sysvinit.%%{ARCH}.rpm

Name:		hfit
Version:	0.1.6
Release:	1
Summary:	Hfit.
Group:		System Environment/Daemons
License:	See the LICENSE file at github.
URL:		https://github.com/aurimasl/hfit
Source0:        https://github.com/aurimasl/hfit/releases/download/v%{version}/hfit-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:       daemonize
AutoReqProv:	No

%description

Hfit.

%prep
%setup -q -n hfit-%{version}.linux-amd64

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/etc/init.d
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig
install -m 755 hfit $RPM_BUILD_ROOT/usr/bin/hfit
install -m 755 contrib/hfit.init $RPM_BUILD_ROOT/etc/init.d/hfit
install -m 644 contrib/hfit.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/hfit

%clean



%files
%defattr(-,root,root,-)
/usr/bin/hfit
/etc/init.d/hfit
%config(noreplace) /etc/sysconfig/hfit
