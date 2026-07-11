%global tl_name miama
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	The Miama Nueva handwriting font with LaTeX support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/miama
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/miama.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/miama.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/miama.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Miama Nueva is a handwriting / script font with over 1300 glyphs that
supports latin, cyrillic, and greek. It comes complete with LaTeX
support.

