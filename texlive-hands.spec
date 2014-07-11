# revision 13293
# category Package
# catalog-ctan /fonts/hands
# catalog-date 2008-10-05 01:10:25 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-hands
Version:	20081005
Release:	8
Summary:	Pointing hand font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/hands
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hands.tar.xz
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
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20081005-2
+ Revision: 752458
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20081005-1
+ Revision: 718596
- texlive-hands
- texlive-hands
- texlive-hands
- texlive-hands

