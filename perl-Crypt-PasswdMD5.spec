#
# Conditional build:
%bcond_without	tests	# unit tests

%define		pdir	Crypt
%define		pnam	PasswdMD5
Summary:	Crypt::PasswdMD5 Perl module - an interoperable MD5-based crypt() function
Summary(pl.UTF-8):	Moduł Perla Crypt::PasswdMD5 - funkcja crypt() oparta na MD5
Name:		perl-Crypt-PasswdMD5
Version:	1.42
Release:	1
# same as perl (original was BEER-WARE)
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Crypt/%{pdir}-%{pnam}-%{version}.tgz
# Source0-md5:	3a24c20baccc04bb0623e40cc87b9d56
URL:		https://metacpan.org/dist/Crypt-PasswdMD5
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
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
%{_mandir}/man3/Crypt::PasswdMD5.3pm*
