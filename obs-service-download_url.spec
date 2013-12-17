#
# spec file for package obs-service-download_url
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           obs-service-download_url
Summary:        An OBS source service: curl download tool
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            http://openbuildservice.org
Version:        0.1
Release:        0
Source:         download_url
Source1:        download_url.service
Requires:       wget
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It supports downloading files from given URLs via curl

%prep
%setup -q -D -T 0 -n .

%build

%install
mkdir -p %{buildroot}/usr/lib/obs/service
install -m 0755 %{SOURCE0} %{buildroot}/usr/lib/obs/service
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/obs/service

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
