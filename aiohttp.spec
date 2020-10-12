#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aiohttp
Version  : 3.6.3
Release  : 20
URL      : https://files.pythonhosted.org/packages/9d/6c/429faa2d2f73973189ca0cfe141ff703417a5eebe18d78e6b25b70db0a34/aiohttp-3.6.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/9d/6c/429faa2d2f73973189ca0cfe141ff703417a5eebe18d78e6b25b70db0a34/aiohttp-3.6.3.tar.gz
Summary  : Async http client/server framework (asyncio)
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: aiohttp-license = %{version}-%{release}
Requires: aiohttp-python = %{version}-%{release}
Requires: aiohttp-python3 = %{version}-%{release}
Requires: async-timeout
Requires: attrs
Requires: brotlipy
Requires: chardet
Requires: idna-ssl
Requires: multidict
Requires: typing_extensions
Requires: yarl
BuildRequires : async-timeout
BuildRequires : attrs
BuildRequires : brotlipy
BuildRequires : buildreq-distutils3
BuildRequires : chardet
BuildRequires : idna-ssl
BuildRequires : multidict
BuildRequires : typing_extensions
BuildRequires : yarl

%description
Async http client/server framework
        ==================================

%package license
Summary: license components for the aiohttp package.
Group: Default

%description license
license components for the aiohttp package.


%package python
Summary: python components for the aiohttp package.
Group: Default
Requires: aiohttp-python3 = %{version}-%{release}

%description python
python components for the aiohttp package.


%package python3
Summary: python3 components for the aiohttp package.
Group: Default
Requires: python3-core
Provides: pypi(aiohttp)
Requires: pypi(async_timeout)
Requires: pypi(attrs)
Requires: pypi(chardet)
Requires: pypi(multidict)
Requires: pypi(yarl)

%description python3
python3 components for the aiohttp package.


%prep
%setup -q -n aiohttp-3.6.3
cd %{_builddir}/aiohttp-3.6.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602522288
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aiohttp
cp %{_builddir}/aiohttp-3.6.3/LICENSE.txt %{buildroot}/usr/share/package-licenses/aiohttp/2da4a3eea24ffca0a87562a6bff54344c074a108
cp %{_builddir}/aiohttp-3.6.3/vendor/http-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/aiohttp/88b9c8fca2f64284b46f0dd05f37329ae8a7a6a8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/aiohttp/2da4a3eea24ffca0a87562a6bff54344c074a108
/usr/share/package-licenses/aiohttp/88b9c8fca2f64284b46f0dd05f37329ae8a7a6a8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
