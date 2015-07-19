%define modname	Unicode-String
%define modver	2.09

Summary:	Unicode-String module for perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	17
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Unicode/%{modname}-%{modver}.tar.bz2
BuildRequires:	perl-devel >= 5.8.0
Requires:	perl

%description
These are experimental modules to handle various Unicode issues.  They
were made before perl included native UTF8 support.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/auto/Unicode/String
%{perl_vendorarch}/Unicode/*.pm
%{_mandir}/man3/*

