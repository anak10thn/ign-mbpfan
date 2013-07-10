Summary:IGOS Nusantara Control Panel
Name:mbpfan
Version:1.4
Release:10.7.13
License:GPLv3
Group:System/Kernel
URL:http://igos-nusantara.or.id
Source0:%{name}.tar.bz2
BuildRoot:%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
Fancontrol for macbook pro on IGOS Nusantara
%prep
%setup -q -n %{name}

%install
mkdir -p $RPM_BUILD_ROOT/usr/sbin
make
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/etc/rc.d/init.d
install -m 0755 bin/mbpfan $RPM_BUILD_ROOT/usr/sbin
install -m 0755 mbpfan.conf $RPM_BUILD_ROOT/etc
install -m 0755 mbpfan.init.redhat $RPM_BUILD_ROOT/etc/rc.d/init.d/mbpfan

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir 
/usr/sbin/
/etc/
/etc/rc.d/init.d/
%changelog
* Thu Jul 7 2013 Ibnu Yahya <ibnu.yahya@toroo.org>
- First build for IGOS Nusantara.
