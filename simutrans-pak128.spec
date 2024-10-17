%define	majver	124
%define	minver	1
%define	pak	pak128

Summary:	A complete Simutrans game data package with 128x128 tiles
Name:		simutrans-%{pak}
Version:	2.9.1
Release:	1
License:	Artistic
Group:		Games/Strategy
URL:		https://www.simutrans.com
BuildArch:	noarch
Source0:	https://downloads.sourceforge.net/project/simutrans/pak128/pak128%20for%20ST%20%20%{majver}.%{minver}up%20%28%{version}%29/simupak128-%{version}.zip
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
