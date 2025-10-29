%define 	module	intersphinx_registry
Summary:	Convenient utilities and data to write a sphinx config file
Summary(pl.UTF-8):	Wygodne narzędzia i dane do zapisu pliku konfiguracyjnego Sphinksa
Name:		python3-%{module}
Version:	0.2501.23
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/intersphinx_registry/
Source0:	https://files.pythonhosted.org/packages/source/i/intersphinx_registry/%{module}-%{version}.tar.gz
# Source0-md5:	2db90088f486cd061b9c55bf90421262
URL:		https://github.com/Quansight-labs/intersphinx_registry
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.2
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convenient utilities and data to write a sphinx config file.

%description -l pl.UTF-8
Wygodne narzędzia i dane do zapisu pliku konfiguracyjnego Sphinksa.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
