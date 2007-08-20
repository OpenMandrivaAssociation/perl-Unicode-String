%define realname        Unicode-String

Name:           perl-%{realname}
Version:        2.09
Release:        %mkrel 3
License:        GPL or Artistic
Group:          Development/Perl
Summary:        Unicode-String module for perl
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Unicode/%{realname}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{realname}/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  perl-devel >= 5.8.0
Requires:       perl

%description
These are experimental modules to handle various Unicode issues.  They
were made before perl included native UTF8 support.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/auto/Unicode/String
%{perl_vendorarch}/Unicode/*.pm
%{_mandir}/*/*

