# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/eukdate
# catalog-date 2009-03-17 21:46:26 +0100
# catalog-license lppl
# catalog-version 1.04
Name:		texlive-eukdate
Version:	1.04
Release:	10
Summary:	UK format dates, with weekday
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eukdate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eukdate.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eukdate.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eukdate.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is used to change the format of \today's date,
including the weekday, e.g., "Saturday, 26 June 2008", the 'UK
format', which is preferred in many parts of the world, as
distinct from that which is used in \maketitle of the article
class, "June 26, 2008", the 'US format'.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eukdate/eukdate.sty
%doc %{_texmfdistdir}/doc/latex/eukdate/README
%doc %{_texmfdistdir}/doc/latex/eukdate/eukdate.pdf
#- source
%doc %{_texmfdistdir}/source/latex/eukdate/eukdate.dtx
%doc %{_texmfdistdir}/source/latex/eukdate/eukdate.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.04-2
+ Revision: 751660
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.04-1
+ Revision: 718383
- texlive-eukdate
- texlive-eukdate
- texlive-eukdate
- texlive-eukdate

