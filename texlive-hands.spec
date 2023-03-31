Name:		texlive-hands
Version:	13293
Release:	2
Summary:	Pointing hand font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/hands
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hands.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides right- and left-pointing hands in both black-on-white
and white-on-black realisation. The font is distributed as
MetaFont source.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/hands/hands.mf
%{_texmfdistdir}/fonts/source/public/hands/handsdef.mf
%{_texmfdistdir}/fonts/source/public/hands/mirror.mf
%{_texmfdistdir}/fonts/source/public/hands/reverse.mf
%{_texmfdistdir}/fonts/source/public/hands/rvmirror.mf
%{_texmfdistdir}/fonts/tfm/public/hands/hands.tfm

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
