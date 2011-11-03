# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/eukdate
# catalog-date 2009-03-17 21:46:26 +0100
# catalog-license lppl
# catalog-version 1.04
Name:		texlive-eukdate
Version:	1.04
Release:	1
Summary:	UK format dates, with weekday
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eukdate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eukdate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eukdate.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eukdate.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package is used to change the format of \today's date,
including the weekday, e.g., "Saturday, 26 June 2008", the 'UK
format', which is preferred in many parts of the world, as
distinct from that which is used in \maketitle of the article
class, "June 26, 2008", the 'US format'.

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
%{_texmfdistdir}/tex/latex/eukdate/eukdate.sty
%doc %{_texmfdistdir}/doc/latex/eukdate/README
%doc %{_texmfdistdir}/doc/latex/eukdate/eukdate.pdf
#- source
%doc %{_texmfdistdir}/source/latex/eukdate/eukdate.dtx
%doc %{_texmfdistdir}/source/latex/eukdate/eukdate.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
