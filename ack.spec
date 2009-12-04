%include	/usr/lib/rpm/macros.perl
Summary:	grep-like tool
Summary(pl.UTF-8):	produkt grepopodobny
Name:		ack
Version:	1.90
Release:	1
License:	GPL
Group:		Applications
Source0:	http://betterthangrep.com/%{name}-standalone
# Source0-md5:	d15d059166beff6103d2401aa2d783c7
URL:		http://betterthangrep.com/
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov
Suggests:	perl-perldoc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ack is a tool like grep, designed for programmers with large trees of
heterogeneous source code.

ack is written purely in Perl, and takes advantage of the power of
Perl's regular expressions.

%description -l pld.UTF-8
ack jest narzędziem podobnym do grepa, zaprojektowanym dla
programistów pracujących z dużymi drzewami różnorodnych plików.

ack jest napisane w czystym Perlu i korzysta z ptęgi wyrażeń
regularnych języka Perl.

%prep
%setup -q -c -T

%build
pod2man %{SOURCE0} > ack.1
pod2text %{SOURCE0} > ack.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a ack.1 $RPM_BUILD_ROOT%{_mandir}/man1/ack.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ack.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/ack.1*
