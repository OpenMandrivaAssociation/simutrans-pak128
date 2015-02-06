%define	ver	2.3.0
%define	majver	112
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
Source0:	http://tenet.dl.sourceforge.net/project/simutrans/pak128/pak128%20for%20%majver-%minver/%{pak}-%{ver}--%{majver}.%{minver}.zip
Provides:	simutrans-pak = %EVRD
Requires:	simutrans

%description
This is a complete data package for Simutrans transport game
with 128x128 tiles. Internal version is %{ver}.

%prep
%setup -q -c %{name}-%{version}

%install
mkdir -p %{buildroot}%{_datadir}/simutrans
cp -pr simutrans/* %{buildroot}%{_datadir}/simutrans/

%files
%{_datadir}/simutrans/*
