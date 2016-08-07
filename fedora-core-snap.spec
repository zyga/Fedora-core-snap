%global commit0 0bbaadbf629d4a8deb0d627d5801d796ee26af29
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           fedora-core-snap
Version:        1
Release:        1.%{shortcommit0}%{?dist}
Summary:        Tools for constructing the fedora-core snap

Group:          Development/Tools
License:        MIT
URL:            https://github.com/zyga/fedora-core-snap
Source0:        https://github.com/zyga/fedora-core-snap/archive/%{commit0}/%{name}-%{commit0}.tar.gz

Requires:       squashfs-tools
Requires:       /usr/bin/dnf
Requires:       /bin/bash

%description
Tools for constructing the fedora-core snap out of the Fedora archive RPMs.
The tool installs a minimal chroot and makes some trivial modifications to
discard unneeded files. The resulting tree is compressed to a squashfs
filesystem image.

%prep
%setup -q  -n %{name}-%{commit0}

%build
# Nothing to do here

%install
install -d %{buildroot}%{_sbindir}
install -m 0755 mksnap-fedora-core %{buildroot}%{_sbindir}

%files
%license LICENSE
%{_sbindir}/mksnap-fedora-core

%changelog
* Sun Aug 07 2016 Neal Gompa <ngompa13@gmail.com> - 1-1.0bbaadb
- Slight refactor

* Sun Aug 07 2016 Zygmunt Krynicki <me@zygoon.pl> - 1-1
- Initial version of the package