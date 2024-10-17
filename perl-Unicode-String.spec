%define modname	Unicode-String
%undefine _debugsource_packages

Summary:	Unicode-String module for perl
Name:		perl-%{modname}
Version:	2.10
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Unicode/%{modname}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	perl-Test-Base
BuildRequires:	perl-Test
Requires:	perl

%description
These are experimental modules to handle various Unicode issues.  They
were made before perl included native UTF8 support.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
%make_build test

%install
%make_install

%files
%doc Changes README
%{perl_vendorarch}/auto/Unicode/String
%{perl_vendorarch}/Unicode/*.pm
%{_mandir}/man3/*
