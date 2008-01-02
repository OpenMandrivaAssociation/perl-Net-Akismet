%define	module	Net-Akismet
%define	name	perl-%{module}
%define	version	0.03
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl interface to Akismet - comment and trackback spam fighter 
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/N/NI/NIKOLAY/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildRoot:	%{_tmppath}/%{name}-%{version}
Buildrequires:	perl-devel
BuildRequires:	perl(LWP::UserAgent)
Requires:	perl 
Buildarch:	noarch

%description
Net::Akismet is a Perl interface to Akismet, a comment and trackback
spam fighter.

%prep
%setup -q -n %{module}-%{version}

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
