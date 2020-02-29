%{!?version: %define version 0.0}

Name:           eucalyptus-awscli-plugin
Version:        %{version}
Release:        0%{?build_id:.%build_id}%{?dist}
Summary:        Eucalyptus plugin for AWS CLI

License:        BSD
URL:            https://github.com/corymbia/eucalyptus-awscli-plugin
Source0:        %{tarball_basedir}.tar.xz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       awscli >= 1.11.0
Requires:       python2


%description
An AWS CLI plugin to enable Eucalyptus service endpoints via configuration.


%prep
%setup -q -n %{tarball_basedir}


%build
python2 setup.py build


%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%{python_sitelib}/*


%changelog
* Thu Feb 20 2020 Steve Jones <steve.jones@appscale.com>
- Created
