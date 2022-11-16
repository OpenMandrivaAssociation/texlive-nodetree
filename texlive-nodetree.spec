Name:		texlive-nodetree
Version:	56742
Release:	1
Summary:	Visualize node lists in a tree view
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/nodetree
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nodetree.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nodetree.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nodetree.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
nodetree is a development package that visualizes the structure
of node lists. nodetree shows its debug informations in the
console output when you compile a LuaTeX file. It uses a
similar visual representation for node lists as the UNIX tree
command for a folder structure.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/luatex/nodetree
%{_texmfdistdir}/tex/luatex/nodetree
%doc %{_texmfdistdir}/doc/luatex/nodetree

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
