%define kernel %(uname -r)
%define patch kpatch-module-add-livepatch
%define installdir /var/lib/kpatch

Name:		%{patch}
Version:	1
Release:	1%{?dist}
Summary:	kpatch livepatch module - Add livepatch to version

Group:		System Environment/Kernel
License:	GPLv2
Source0:	%{patch}-1.tar.gz

%prep
%setup

%description 
Livepatch kernel module. Appends '-livepatch' to /proc/version.

%build
kpatch-build -t vmlinux module-add-livepatch.patch

%install
mkdir -p %{buildroot}/%{installdir}/%{kernel}
cp -f "%{patch}.ko" "%{buildroot}/%{installdir}/%{kernel}"

%files
%{installdir}/%{kernel}/%{patch}.ko
