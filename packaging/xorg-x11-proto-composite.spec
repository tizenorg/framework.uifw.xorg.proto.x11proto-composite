Name:     xorg-x11-proto-composite
Summary:  X.Org X11 Protocol compositeproto
Version:  0.4.2
Release:  1
Group:    Development/System
License:  MIT
URL:      http://www.x.org
Source0:  %{name}-%{version}.tar.gz
Provides: compositeproto

BuildRequires: pkgconfig
BuildRequires: pkgconfig(xorg-macros)

# some file to be intalled can be ignored when rpm generates packages
%define _unpackaged_files_terminate_build 0

%description
Description: %{summary}

%prep
%setup -q

%build

./autogen.sh
%reconfigure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%remove_docs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*
%{_datadir}/pkgconfig/*

