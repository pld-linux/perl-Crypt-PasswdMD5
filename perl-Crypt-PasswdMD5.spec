%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	PasswdMD5
Summary:	Crypt::PasswdMD5 -- an interoperable MD5-based crypt() function
Summary(pl):	Modu³ Perla Crypt::PasswdMD5 - funkcja crypt() oparta na MD5
Name:		perl-Crypt-PasswdMD5
Version:	1.2
Release:	8
License:	BEER-WARE (free)
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unix_md5_crypt() provides a crypt()-compatible interface to the
rather new MD5-based crypt() function found in modern operating
systems. apache_md5_crypt() provides a function compatible with
Apache's .htpasswd files.

%description -l pl
Funkcja unix_md5_crypt() udostêpnia kompatybilny z crypt() interfejs
do dosyæ nowej funkcji crypt() opartej na MD5, dostêpnej we
wspó³czesnych systemach operacyjnych. Funkcja apache_md5_crypt() jest
kompatybilna z plikami .htpasswd Apache'a.

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
