%define	ver	2.1.0
%define	majver	111
%define	minver	2
%define	pak	pak128

Summary:	A complete Simutrans game data package with 128x128 tiles
Name:		simutrans-%{pak}
Version:	0.%{majver}.%{minver}
Release:	2
License:	Artistic
Group:		Games/Strategy
URL:		http://www.simutrans.com
BuildArch:	noarch
Source0:	%{pak}-%{ver}--%{majver}.%{minver}.zip
Provides:	simutrans-pak = %{version}
Requires:	simutrans

%description
This is a complete data package for Simutrans transport game
with 128x128 tiles. Internal version is %{ver}.

%prep
%setup -q -c %{name}-%{version}

%install
mkdir -p %{buildroot}%{_libexecdir}/simutrans
cp -pr simutrans/* %{buildroot}%{_libexecdir}/simutrans/

%files
%{_libexecdir}/simutrans/*

%changelog
* Mon Apr 16 2012 Andrey Bondrov <abondrov@mandriva.org> 0.111.2-1
+ Revision: 791369
- New version 2.1.0-111.2

* Fri Dec 09 2011 Andrey Bondrov <abondrov@mandriva.org> 0.111.0-1
+ Revision: 739513
- imported package simutrans-pak128

