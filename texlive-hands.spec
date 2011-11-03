# revision 13293
# category Package
# catalog-ctan /fonts/hands
# catalog-date 2008-10-05 01:10:25 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-hands
Version:	20081005
Release:	1
Summary:	Pointing hand font
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/hands
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hands.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Provides right- and left-pointing hands in both black-on-white
and white-on-black realisation. The font is distributed as
MetaFont source.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/hands/hands.mf
%{_texmfdistdir}/fonts/source/public/hands/handsdef.mf
%{_texmfdistdir}/fonts/source/public/hands/mirror.mf
%{_texmfdistdir}/fonts/source/public/hands/reverse.mf
%{_texmfdistdir}/fonts/source/public/hands/rvmirror.mf
%{_texmfdistdir}/fonts/tfm/public/hands/hands.tfm
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
