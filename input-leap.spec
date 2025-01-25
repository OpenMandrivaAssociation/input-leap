Name:		input-leap
Version:    3.0.2
Release:	1
Source0:	https://github.com/input-leap/input-leap/archive/refs/tags/v%{version}.tar.gz
Summary:	An open source software based KVM
URL:		https://github.com/input-leap/input-leap
License:	GPLv2
Group:	        Networking	
BuildRequires:	cmake
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Linguist)

BuildSystem:	cmake
BuildOption:    -DINPUTLEAP_BUILD_GUI=ON
BuildOption:    -DINPUTLEAP_BUILD_LIBEI=OFF
BuildOption:    -DINPUTLEAP_BUILD_TESTS=OFF
BuildOption:    -DINPUTLEAP_BUILD_X11=ON

%description
Input Leap is a fork of the no longer maintained Barrier. Input Leap allows the
sharing of a mouse and keyboard between multiple computers or even virtual
machines. It is cross platform allowing seamless switching from one computer to
another running a completely different operating system.

%files
%{_bindir}/input-*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/man/man1/input-leap*.1.zst
%{_datadir}/metainfo/*

