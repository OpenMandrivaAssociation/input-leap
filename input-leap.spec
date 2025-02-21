Name:		input-leap
Version:    3.0.2~0.20250125.1
Release:	1
# The version below is for use with a realeased version
#Source0:	https://github.com/input-leap/input-leap/archive/refs/tags/v%%{version}.tar.gz
# Hash version used to address an issue that was causing segfaults with version 3.0.2 
Source0:    https://github.com/input-leap/input-leap/archive/545548a0b59ca866a425c0d1513b99eb8a6b02df.tar.gz
Summary:	An open source software based KVM (no video)
URL:		https://github.com/input-leap/input-leap
License:	GPLv2
Group:	        Networking	
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:	cmake >= 3
BuildRequires:  pkgconfig(ice) 
BuildRequires:  pkgconfig(libei-1.0) >= 0.99.1
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  librsvg

BuildSystem:	cmake
BuildOption:    -DINPUTLEAP_BUILD_X11=ON
BuildOption:    -DINPUTLEAP_BUILD_LIBEI=ON
BuildOption:    -DINPUTLEAP_BUILD_TESTS=OFF

%description
Input Leap is a fork of the no longer maintained Barrier. Input Leap allows the
sharing of a mouse and keyboard between multiple computers or even virtual
machines. It is cross platform allowing seamless switching from one computer to
another running a completely different operating system.

%prep
%setup -C 

%install
%buildsystem_cmake_install

# Deal with icon's
for d in 16 32 48 64 72 128 256 
do
	install -dm 0754 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	rsvg-convert -f png -h ${d} -w ${d} %{builddir}/%{name}-%{version}/res/io.github.input_leap.input-leap.svg \
			-o %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/input-leap.png
done
install -D -p -m 0644 %{builddir}/%{name}-%{version}/res/io.github.input_leap.input-leap.desktop %{buildroot}%{_datadir}/applications/io.github.input_leap.input-leap.desktop

# Get list of other icons that need converted
files=$(ls %{builddir}/%{name}-%{version}/res/icons/*.svg)

for x in $files
do
fname=$(basename ${x} .svg)
    for d in 16 32 48 64 72 128 256
    do
    echo "${x} ${d} x ${d}"
	install -dm 0754 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
 	rsvg-convert -f png -h ${d} -w ${d} ${x} \
			-o %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/${fname}.png
    done
done

%files
%{_bindir}/input-*
%{_datadir}/applications/*
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_datadir}/man/man1/input-leap*.1.zst
%{_datadir}/metainfo/*
%{_iconsdir}/hicolor/*/apps/*.png
%license LICENSE
