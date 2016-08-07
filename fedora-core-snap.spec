Name:		fedora-core-snap
Version:	1
Release:	1%{?dist}
Summary:	Tools for constructing the fedora-core snap

Group:		Development/Tools
License:	MIT
URL:		https://github.com/zyga/fedora-core-snap
Source0:	.

Requires:	squashfs-tools
Requires:   dnf
Requires:   bash

%description
Tools for constructing the fedora-core snap out of the Fedora archive RPMs.
The tool installs a minimal chroot and makes some trivial modifications to
discard unneeded files. The resulting tree is compressed to a squashfs
filesystem image.

%prep
%setup -q

%build
:

%install
install -d %{buildroot}%{_sbindir}
install -m 0755 mksnap-fedora-core %{buildroot}%{_sbindir}

%files
%doc LICENSE

%changelog
* Sun Aug 07 2016 Zygmunt Krynicki <me@zygoon.pl> - 1-1
- Initial version of the package
