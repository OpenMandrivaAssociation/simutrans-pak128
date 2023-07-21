%define	ver	2.8.2
%define	majver	123
%define	minver	0
%define	pak	pak128

Summary:	A complete Simutrans game data package with 128x128 tiles
Name:		simutrans-%{pak}
Version:	2.8.2
Release:	1
License:	Artistic
Group:		Games/Strategy
URL:		http://www.simutrans.com
BuildArch:	noarch
Source0:	https://downloads.sourceforge.net/project/simutrans/pak128/pak128%20%{version}%20for%20ST%20%{majver}up/simupak128-%{version}-for%{majver}.zip
Provides:	simutrans-pak = %EVRD
Requires:	simutrans

%description
This is a complete data package for Simutrans transport game
with 128x128 tiles. Internal version is %{ver}.

%prep
%setup -q -n simutrans

%install
mkdir -p %{buildroot}%{_datadir}/simutrans
cp -pr pak128 %{buildroot}%{_datadir}/simutrans/

%files
%{_datadir}/simutrans/*
