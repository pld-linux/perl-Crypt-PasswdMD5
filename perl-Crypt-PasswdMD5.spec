%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	PasswdMD5
Summary:	Crypt::PasswdMD5 Perl module
Summary(cs):	Modul Crypt::PasswdMD5 pro Perl
Summary(da):	Perlmodul Crypt::PasswdMD5
Summary(de):	Crypt::PasswdMD5 Perl Modul
Summary(es):	Módulo de Perl Crypt::PasswdMD5
Summary(fr):	Module Perl Crypt::PasswdMD5
Summary(it):	Modulo di Perl Crypt::PasswdMD5
Summary(ja):	Crypt::PasswdMD5 Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Crypt::PasswdMD5 ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Crypt::PasswdMD5
Summary(pl):	Modu³ Perla Crypt::PasswdMD5
Summary(pt):	Módulo de Perl Crypt::PasswdMD5
Summary(pt_BR):	Módulo Perl Crypt::PasswdMD5
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Crypt::PasswdMD5
Summary(sv):	Crypt::PasswdMD5 Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Crypt::PasswdMD5
Summary(zh_CN):	Crypt::PasswdMD5 Perl Ä£¿é
Name:		perl-Crypt-PasswdMD5
Version:	1.2
Release:	6
License:	BEER-WARE (free)
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::PasswdMD5 perl module.

%description -l cs
Modul Crypt::PasswdMD5 pro Perl.

%description -l da
Perlmodul Crypt::PasswdMD5.

%description -l de
Crypt::PasswdMD5 Perl Modul.

%description -l es
Módulo de Perl Crypt::PasswdMD5.

%description -l fr
Module Perl Crypt::PasswdMD5.

%description -l it
Modulo di Perl Crypt::PasswdMD5.

%description -l ja
Crypt::PasswdMD5 Perl ¥â¥¸¥å¡¼¥ë

%description -l ko
Crypt::PasswdMD5 ÆÞ ¸ðÁÙ.

%description -l no
Perlmodul Crypt::PasswdMD5.

%description -l pl
Modu³ perla Crypt::PasswdMD5.

%description -l pt
Módulo de Perl Crypt::PasswdMD5.

%description -l pt_BR
Módulo Perl Crypt::PasswdMD5.

%description -l ru
íÏÄÕÌØ ÄÌÑ Perl Crypt::PasswdMD5.

%description -l sv
Crypt::PasswdMD5 Perlmodul.

%description -l uk
íÏÄÕÌØ ÄÌÑ Perl Crypt::PasswdMD5.

%description -l zh_CN
Crypt::PasswdMD5 Perl Ä£¿é

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Crypt/PasswdMD5.pm
%{_mandir}/man3/*
