#
# Conditional build:
%bcond_without	tests	# unit tests

%define		pdir	MooseX
%define		pnam	NonMoose
Summary:	MooseX::NonMoose - easy subclassing of non-Moose classes
Summary(pl.UTF-8):	MooseX::NonMoose - łatwe podklasy dla klas spoza Moose
Name:		perl-MooseX-NonMoose
Version:	0.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8a226451ba312c21a27376741c302f47
URL:		https://metacpan.org/release/MooseX-NonMoose
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Moose >= 2.00
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Simple >= 0.88
BuildRequires:	perl-Try-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MooseX::NonMoose allows for easily subclassing non-Moose classes with
Moose, taking care of the annoying details connected with doing this,
such as setting up proper inheritance from Moose::Object and
installing (and inlining, at make_immutable time) a constructor that
makes sure things like BUILD methods are called. It tries to be as
non-intrusive as possible - when this module is used, inheriting from
non-Moose classes and inheriting from Moose classes should work
identically, aside from the few caveats mentioned in docs. One of the
goals of this module is that including it in a Moose::Exporter-based
package used across an entire application should be possible, without
interfering with classes that only inherit from Moose modules, or even
classes that don't inherit from anything at all.

%description -l pl.UTF-8
MooseX::NonMoose pozwala na łatwe tworzenie podklas klas spoza Moose
przy użyciu Moose, dbając o irytujące szczegóły z tym związane, takie
jak ustawianie właściwego dziedziczenia po Moose::Object oraz
instalowanie (oraz włączanie w czasie make_immutable) konstruktora,
który zapewnia, że nastąpi wywołanie koniecznych metod, jak BUILD.
Moduł próbuje być możliwie najmniej inwazyjny - kiedy jest używany.
dziedziczenie z klas spoza Moose oraz dziedzieczenie z klas Moose
powinno działać tak samo, poza kilkoma szczegółami opisanymi w
dokumentacji. Jednym z zastosowań tego modułu jest umożliwienie
dołączania go w pakietach opartych na Moose::Exporter, używanych w
całej aplikacji, bez interferencji z klasami dziedziczonymi tylko z
modułów Moose albo klas nie dziedziczących niczego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/NonMoose.pm
%{perl_vendorlib}/MooseX/NonMoose
%{_mandir}/man3/MooseX::NonMoose*.3pm*
