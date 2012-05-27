#
# Conditional build:
%bcond_without	tests # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Fatal
Summary:	Test::Fatal - incredibly simple helpers for testing code with exceptions
Summary(pl.UTF-8):	Test::Fatal - bardzo proste funkcje pomocnicze do kodu testującego z wyjątkami
Name:		perl-Test-Fatal
Version:	0.010
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8052d4160e8d999cbeb574592f26541
URL:		http://search.cpan.org/dist/Test-Fatal/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.31
BuildRequires:	perl-devel >= 1:5.8.7
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Try-Tiny >= 0.07
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Fatal is an alternative to the popular Test::Exception. It does
much less, but should allow greater flexibility in testing
exception-throwing code with about the same amount of typing.

%description -l pl.UTF-8
Test::Fatal to alternatywa dla popularnego Test::Exception. Ten moduł
robi znacznie mniej, ale powinien pozwalać na większą elastyczność
przy testowaniu kodu rzucającego wyjątki przy mniej więcej tej samej
ilości napisanego kodu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/Fatal.pm
%{_mandir}/man3/Test::Fatal.3pm*
