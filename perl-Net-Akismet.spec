%define	upstream_name	 Net-Akismet
%define	upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl interface to Akismet - comment and trackback spam fighter 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
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
