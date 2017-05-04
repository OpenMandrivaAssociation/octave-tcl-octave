%define octpkg tcl-octave

Summary:	Socket implementation of a tcl-octave connection for Octave
Name:		octave-%{octpkg}
Version:	0.1.8
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	Public Domain
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 2.9.7

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Socket implementation of a tcl-octave connection for Octave.

This package is part of unmantained Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
#%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

