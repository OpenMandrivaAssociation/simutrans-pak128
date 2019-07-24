%define	ver	2.6
%define	majver	120
%define	minver	0
%define	pak	pak128

Summary:	A complete Simutrans game data package with 128x128 tiles
Name:		simutrans-%{pak}
Version:	2.8.1
Release:	1
License:	Artistic
Group:		Games/Strategy
URL:		http://www.simutrans.com
BuildArch:	noarch
Source0:	https://sourceforge.net/projects/simutrans/files/pak128/pak128%20for%20ST%20120%20%282.6%2C%20completed%20elevated%20tracks%29/pak128-2.6--ST120.zip/download
Provides:	simutrans-pak = %EVRD
Requires:	simutrans

%description
This is a complete data package for Simutrans transport game
with 128x128 tiles. Internal version is %{ver}.

%prep
%setup -q -n pak128

%install
mkdir -p %{buildroot}%{_datadir}/simutrans
cp -pr ../pak128 %{buildroot}%{_datadir}/simutrans/

%files
%{_datadir}/simutrans/*
