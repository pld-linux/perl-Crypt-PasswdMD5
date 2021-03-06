#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Crypt
%define		pnam	PasswdMD5
Summary:	Crypt::PasswdMD5 Perl module - an interoperable MD5-based crypt() function
Summary(pl.UTF-8):	Moduł Perla Crypt::PasswdMD5 - funkcja crypt() oparta na MD5
Name:		perl-Crypt-PasswdMD5
Version:	1.3
Release:	2
# same as perl (original was BEER-WARE)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	368205b1be8c0d4f807afe25d6fbd1ad
URL:		http://search.cpan.org/dist/Crypt-PasswdMD5/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unix_md5_crypt() provides a crypt()-compatible interface to the
rather new MD5-based crypt() function found in modern operating
systems. apache_md5_crypt() provides a function compatible with
Apache's .htpasswd files.

%description -l pl.UTF-8
Funkcja unix_md5_crypt() udostępnia kompatybilny z crypt() interfejs
do dosyć nowej funkcji crypt() opartej na MD5, dostępnej we
współczesnych systemach operacyjnych. Funkcja apache_md5_crypt() jest
kompatybilna z plikami .htpasswd Apache'a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Crypt/PasswdMD5.pm
%{_mandir}/man3/*
