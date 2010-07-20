%define upstream_name    Unicode-String
%define upstream_version 2.09

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 2

Summary:        Unicode-String module for perl
License:        GPL+ or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}/
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Unicode/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-devel >= 5.8.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
Requires:       perl

%description
These are experimental modules to handle various Unicode issues.  They
were made before perl included native UTF8 support.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
