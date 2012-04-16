%define	ver	2.1.0
%define	majver	111
%define	minver	2
%define	pak	pak128

Summary:	A complete Simutrans game data package with 128x128 tiles
Name:		simutrans-%{pak}
Version:	0.%{majver}.%{minver}
Release:	%mkrel 1
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
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_libexecdir}/simutrans
%__cp -pr simutrans/* %{buildroot}%{_libexecdir}/simutrans/

%clean
%__rm -rf %{buildroot}

%files
%{_libexecdir}/simutrans/*

