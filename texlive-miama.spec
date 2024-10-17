Name:		texlive-miama
Version:	54512
Release:	2
Summary:	The Miama Nueva handwriting font with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/miama
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miama.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miama.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/miama.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Miama Nueva is a handwriting / script font with over 1300
glyphs that supports latin, cyrillic, and greek. It comes
complete with LaTeX support.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/miama
%{_texmfdistdir}/tex/latex/miama
%{_texmfdistdir}/fonts/type1/public/miama
%{_texmfdistdir}/fonts/tfm/public/miama
%{_texmfdistdir}/fonts/opentype/public/miama
%{_texmfdistdir}/fonts/map/dvips/miama
%{_texmfdistdir}/fonts/enc/dvips/miama
%{_texmfdistdir}/fonts/afm/public/miama
%doc %{_texmfdistdir}/doc/fonts/miama

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
