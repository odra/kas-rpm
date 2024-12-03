Name:           kas
Version:        4.5
Release:        1%{?dist}
Summary:        Setup tool for bitbake based projects
License:        MIT
URL:            https://github.com/siemens/kas
Source:         %{url}/archive/refs/tags/%{version}.tar.gz
 
BuildArch:      noarch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: help2man

# kas direct dependencies
Requires: python3-pyyaml
Requires: python3-distro
Requires: python3-jsonschema
Requires: python3-kconfiglib
Requires: python3-GitPython
Requires: python3-cached_property
# bitbake dependencies
Requires: tar
Requires: gawk
Requires: wget
Requires: git
Requires: diffstat
Requires: unzip
Requires: texinfo
Requires: gcc
Requires: chrpath
Requires: socat
Requires: cpio
Requires: python3-pexpect
Requires: xz-libs
Requires: net-tools
Requires: python3-jinja2
Requires: mesa-libGL
Requires: sdl12-compat-devel
Requires: python3-subunit
Requires: zstd
Requires: lz4
Requires: lz4-libs
Requires: file
Requires: libacl-devel
Requires: glibc-langpack-en
Requires: which
Requires: g++
Requires: patch
Requires: hostname
Requires: rpcgen
Requires: bzip2
Requires: perl-Thread-Queue
Requires: perl-File-Compare
Requires: perl-FindBin
Requires: perl-open

%global _help2man() PYTHONPATH='%{buildroot}%{python3_sitelib}' help2man --version-string='%{version}' --no-discard-stderr  --no-info --name=%1 --output=%{buildroot}%{_mandir}/man1/%1.1 %{buildroot}%{_bindir}/%1

%global _description %{expand:
This tool provides an easy mechanism to setup bitbake based
projects.

The OpenEmbedded tooling support starts at step 2 with bitbake. The
downloading of sources and then configuration has to be done by
hand. Usually, this is explained in a README. Instead kas is using a
project configuration file and does the download and configuration
phase.

Key features provided by the build tool:

* clone and checkout bitbake layers
* create default bitbake settings (machine, arch, ...)
* launch minimal build environment, reducing risk of host contamination
* initiate bitbake build process

## SECURITY NOTICE

At this stage, kas does not validate the integrity of fetched repositories.
Make sure to only pull from trusted sources to ensure that the selected
revisions are the expected ones, specifically when using mirrors.
}

%description %_description

%prep
%autosetup -n kas-%{version}

%build
%py3_build

%check
echo todo

%install
%py3_install

install -d '%{buildroot}%{_mandir}/man1'

%_help2man kas

%files
%doc README.rst
%license LICENSE
%{_bindir}/kas
%{_bindir}/kas-container
%{python3_sitelib}/kas-%{version}-py%{python3_version}.egg-info/PKG-INFO
%{python3_sitelib}/kas-%{version}-py%{python3_version}.egg-info/PKG-INFO
%{python3_sitelib}/kas-%{version}-py%{python3_version}.egg-info/SOURCES.txt
%{python3_sitelib}/kas-%{version}-py%{python3_version}.egg-info/dependency_links.txt
%{python3_sitelib}/kas-%{version}-py%{python3_version}.egg-info/entry_points.txt
%{python3_sitelib}/kas-%{version}-py%{python3_version}.egg-info/top_level.txt
%{python3_sitelib}/kas-%{version}-py%{python3_version}.egg-info/requires.txt
%pycached %{python3_sitelib}/kas/__init__.py
%pycached %{python3_sitelib}/kas/__main__.py
%pycached %{python3_sitelib}/kas/__version__.py
%pycached %{python3_sitelib}/kas/attestation.py
%pycached %{python3_sitelib}/kas/config.py
%pycached %{python3_sitelib}/kas/configschema.py
%pycached %{python3_sitelib}/kas/context.py
%pycached %{python3_sitelib}/kas/includehandler.py
%pycached %{python3_sitelib}/kas/kas.py
%pycached %{python3_sitelib}/kas/kasusererror.py
%pycached %{python3_sitelib}/kas/libcmds.py
%pycached %{python3_sitelib}/kas/libkas.py
%pycached %{python3_sitelib}/kas/plugins/__init__.py
%pycached %{python3_sitelib}/kas/plugins/build.py
%pycached %{python3_sitelib}/kas/plugins/checkout.py
%pycached %{python3_sitelib}/kas/plugins/dump.py
%pycached %{python3_sitelib}/kas/plugins/for_all_repos.py
%pycached %{python3_sitelib}/kas/plugins/menu.py
%pycached %{python3_sitelib}/kas/plugins/shell.py
%pycached %{python3_sitelib}/kas/repos.py
%{python3_sitelib}/kas/schema-kas.json
%{_mandir}/man1/kas.1*


%changelog
* Fri Dec 03 2024 Leonardo Rossetti <lrossett@redhat.com> - 4.5-1
- initial spec file
