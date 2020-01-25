#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	MooseX
%define		pnam	NonMoose
Summary:	MooseX::NonMoose - easy subclassing of non-Moose classes
Name:		perl-MooseX-NonMoose
Version:	0.22
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	08627b8575835e64b44e82424df27a8f
URL:		http://search.cpan.org/dist/MooseX-NonMoose/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::Fatal)
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Moose >= 1.15
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
identically, aside from the few caveats mentioned below. One of the
goals of this module is that including it in a Moose::Exporter-based
package used across an entire application should be possible, without
interfering with classes that only inherit from Moose modules, or even
classes that don't inherit from anything at all.

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
%{perl_vendorlib}/MooseX/*.pm
%{perl_vendorlib}/MooseX/NonMoose
%{_mandir}/man3/*
