Name:		texlive-eukdate
Version:	15878
Release:	2
Summary:	UK format dates, with weekday
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eukdate
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eukdate.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eukdate.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eukdate.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
