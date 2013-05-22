%define upstream_name    Unicode-String
%define upstream_version 2.09

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:        %mkrel 7

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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/auto/Unicode/String
%{perl_vendorarch}/Unicode/*.pm
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.90.0-6mdv2012.0
+ Revision: 765799
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.90.0-5
+ Revision: 764322
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.90.0-4
+ Revision: 667409
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.90.0-3mdv2011.0
+ Revision: 564591
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2.90.0-2mdv2011.0
+ Revision: 555208
- rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.90.0-1mdv2010.1
+ Revision: 401993
- rebuild using %%perl_convert_version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.09-5mdv2009.0
+ Revision: 224595
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.09-4mdv2008.1
+ Revision: 151347
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 2.09-3mdv2008.0
+ Revision: 67541
- rebuild

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 2.09-2mdv2008.0
+ Revision: 23250
- rebuild


* Fri Oct 28 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.09-1mdk
- 2.09

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.07-4mdk
- rebuild for new perl

* Thu Aug 14 2003 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 2.07-3mdk
- rebuild for new perl
- drop Prefix tag
- don't use PREFIX
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.07-1mdk
- rebuild for new auto{prov,req}

* Fri Apr 25 2003 Fran�ois Pons <fpons@mandrakesoft.com> 2.07-1mdk
- 2.07.

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.06-5mdk
- rebuild

* Fri Jan 24 2003 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 2.06-4mdk
- Rebuilt

* Tue Aug 06 2002 Guillaume Rousse <g.rousse@linux-mandrake.com> 2.06-3mdk
- rebuild for multi-thread perl

* Wed Jul 10 2002 Pixel <pixel@mandrakesoft.com> 2.06-2mdk
- rebuild for perl 5.8.0

* Fri Mar 08 2002 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 2.06-1mdk
- First MandrakeSoft Package

