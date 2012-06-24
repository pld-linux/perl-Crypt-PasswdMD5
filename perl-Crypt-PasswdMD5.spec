%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	PasswdMD5
Summary:	Crypt-PasswdMD5 perl module
Summary(pl):	Modu� perla Crypt-PasswdMD5
Name:		perl-Crypt-PasswdMD5
Version:	1.2
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt-PasswdMD5 perl module.

%description -l pl
Modu� perla Crypt-PasswdMD5.

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
