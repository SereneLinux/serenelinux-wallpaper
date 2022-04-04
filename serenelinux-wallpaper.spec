Summary: serenelinux wallpaper
Name: serenelinux-wallpaper
Version: 1.0.2
Release: 1%{?dist}
Group: User Interface/Desktops
BuildArch: noarch
License: NONE
Packager: kokkiemouse
Vendor: INDETAIL

Source0: https://github.com/FascodeNet/serenelinux-wallpaper/archive/master.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
serenelinux wallpaper
%prep
rm -rf $RPM_BUILD_ROOT

%autosetup -n %{name}-master

%build

%install
rm -rf README.md
mkdir -p $RPM_BUILD_ROOT/
cp -arf ./usr $RPM_BUILD_ROOT/

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
/usr/share/backgrounds/
%changelog
