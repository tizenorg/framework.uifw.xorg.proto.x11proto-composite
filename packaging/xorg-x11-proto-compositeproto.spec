
Name:       xorg-x11-proto-compositeproto
Summary:    X.Org X11 Protocol compositeproto
Version:    0.4.2
Release:    1
Group:      Development/System
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/proto/compositeproto-%{version}.tar.gz
Provides:   compositeproto
BuildRequires: pkgconfig(xorg-macros)


%description
Description: %{summary}



%prep
%setup -q -n %{name}-%{version}


%build

%reconfigure --disable-static \
    --libdir=%{_datadir}

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install


%clean
rm -rf %{buildroot}






%files
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/composite.h
%{_includedir}/X11/extensions/compositeproto.h
%{_datadir}/pkgconfig/compositeproto.pc
%doc %{_datadir}/doc/compositeproto


