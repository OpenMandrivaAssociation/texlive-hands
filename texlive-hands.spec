%global tl_name hands
%global tl_revision 13293

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Pointing hand font
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/hands
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hands.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides right- and left-pointing hands in both black-on-white and
white-on-black realisation. The font is distributed as Metafont source.

