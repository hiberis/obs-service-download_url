
Name:           obs-service-download_url
License:        GPL v2 or later
Group:          Development/Tools/Building
Summary:        An OBS source service: curl download tool
Version:        0.1
Release:        1
Source:         download_url
Requires:       /usr/bin/curl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It supports downloading files from given URLs via curl

%prep
%setup -q -D -T 0 -n .

%build


%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/obs/service
install -m 0755 %{SOURCE0} $RPM_BUILD_ROOT/usr/lib/obs/service

%files
%defattr(-,root,root)
%dir /usr/lib/obs
/usr/lib/obs/service

