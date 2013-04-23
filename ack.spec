# TODO:
# - split /usr/share/perl* part into perl-ack subpackage
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
%bcond_with	pty_tests	# do not perform tests requiring a pty
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ack
Summary:	grep-like text finder
Summary(pl.UTF-8):	produkt grepopodobny
Name:		ack
Version:	2.02
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/P/PE/PETDANCE/%{name}-%{version}.tar.gz
# Source0-md5:	9ae2c3939d0f069c6781ee5b6de47c27
Patch0:		%{name}-deps.patch
Patch1:		%{name}-interactive-tests.patch
URL:		http://betterthangrep.com/
%if %{with tests}
BuildRequires:	perl-File-Next >= 1.10
%{?with_pty_tests:BuildRequires:	perl-IO-Tty}
BuildRequires:	perl-Test-Simple >= 0.98
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-perldoc
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ack is designed as a replacement for 99% of the uses of grep.

Ack searches the named input FILEs (or standard input if no files are
named, or the file name - is given) for lines containing a match to
the given PATTERN. By default, ack prints the matching lines.

Ack can also list files that would be searched, without actually
searching them, to let you take advantage of ack's file-type filtering
capabilities.

%description -l pl.UTF-8
ack jest narzędziem podobnym do grepa, zaprojektowanym dla
programistów pracujących z dużymi drzewami różnorodnych plików.

ack jest napisane w czystym Perlu i korzysta z ptęgi wyrażeń
regularnych języka Perl.

%package -n perl-ack
Summary:	ack perl library
Summary(pl.UTF-8):	biblioteka ack dla języka perl
Group:		Development/Languages/Perl

%description -n perl-ack
ack perl library.

%description -n perl-ack -l pl.UTF-8
ack perl library.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p0
%patch1 -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{!?with_pty_tests: RUN_INTERACTIVE=0} %{__make} -j1 test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%attr(755,root,root) %{_bindir}/ack
%{_mandir}/man1/ack.1p*

%files -n perl-ack
%defattr(644,root,root,755)
%{perl_vendorlib}/App/Ack.pm
%{perl_vendorlib}/App/Ack
