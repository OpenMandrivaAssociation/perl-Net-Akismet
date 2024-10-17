%define	upstream_name	 Net-Akismet
%define	upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    3

Summary:	Perl interface to Akismet - comment and trackback spam fighter 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/N/NI/NIKOLAY/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(LWP::UserAgent)
Buildrequires:	perl-devel
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Net::Akismet is a Perl interface to Akismet, a comment and trackback
spam fighter.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%{perl_vendorlib}/Net/Akismet.pm
%{_mandir}/*/*


%changelog
* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 409303
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.05-2mdv2009.0
+ Revision: 268621
- rebuild early 2009.0 package (before pixel changes)

* Sat Jun 07 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.0
+ Revision: 216586
- update to new version 0.05

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.03-1mdv2008.1
+ Revision: 140692
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.0
+ Revision: 75228
- update to new version 0.03

* Sat Aug 11 2007 Olivier Blin <oblin@mandriva.com> 0.02-1mdv2008.0
+ Revision: 61932
- buildrequire perl(LWP::UserAgent) for tests
- initial perl-Net-Akismet release
- Create perl-Net-Akismet

