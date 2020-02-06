%define debug_package %{nil}
%define _rpmfilename RPM/%%{NAME}-%%{VERSION}-%%{RELEASE}.systemd.%%{ARCH}.rpm

Name:    hfit
Version: 0.1.6
Release: 1
Summary: Hfit
License: ASL 2.0
URL:     https://github.com/aurimasl/hfit

Source0: https://github.com/aurimasl/hfit/releases/download/v%{version}/hfit-%{version}.linux-amd64.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description

Hfit.

%prep
%setup -q -n hfit-%{version}.linux-amd64

%build
echo

%install
mkdir -vp $RPM_BUILD_ROOT/usr/bin
mkdir -vp $RPM_BUILD_ROOT/usr/lib/systemd/system
mkdir -vp $RPM_BUILD_ROOT/etc/sysconfig
install -m 755 hfit $RPM_BUILD_ROOT/usr/bin/hfit
install -m 644 contrib/hfit.service $RPM_BUILD_ROOT/usr/lib/systemd/system/hfit.service
install -m 644 contrib/hfit.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/hfit

%clean

%post
%systemd_post hfit.service

%preun
%systemd_preun hfit.service

%postun
%systemd_postun_with_restart hfit.service

%files
%defattr(-,root,root,-)
/usr/bin/hfit
/usr/lib/systemd/system/hfit.service
%config(noreplace) /etc/sysconfig/hfit
