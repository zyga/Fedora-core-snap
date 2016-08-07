%global commit 0bbaadbf629d4a8deb0d627d5801d796ee26af29
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           fedora-core-snap
Version:        0
Release:        1.git%{shortcommit}%{?dist}
Summary:        Tools for constructing the fedora-core snap

Group:          Development/Tools
License:        MIT
URL:            https://github.com/zyga/fedora-core-snap
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildArch:      noarch
Requires:       squashfs-tools

%description
Tools for constructing the fedora-core snap out of the Fedora archive RPMs.
The tool installs a minimal chroot and makes some trivial modifications to
discard unneeded files. The resulting tree is compressed to a squashfs
filesystem image.

%prep
%autosetup -n %{name}-%{commit}

%build
# Nothing to do here

%install
install -d %{buildroot}%{_sbindir}
install -p -m 0755 mksnap-fedora-core %{buildroot}%{_sbindir}

%files
%license LICENSE
%{_sbindir}/mksnap-fedora-core

%changelog
* Sun Aug 07 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0-1.0bbaadb
- More spec cleanups and fixes

* Sun Aug 07 2016 Neal Gompa <ngompa13@gmail.com> - 1-1.0bbaadb
- Slight refactor

* Sun Aug 07 2016 Zygmunt Krynicki <me@zygoon.pl> - 1-1
- Initial version of the package