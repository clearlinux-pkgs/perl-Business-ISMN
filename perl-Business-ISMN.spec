#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Business-ISMN
Version  : 1.202
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISMN-1.202.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BD/BDFOY/Business-ISMN-1.202.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libb/libbusiness-ismn-perl/libbusiness-ismn-perl_1.131-1.debian.tar.xz
Summary  : 'work with International Standard Music Numbers'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-2.0 GPL-1.0
Requires: perl-Business-ISMN-license = %{version}-%{release}
Requires: perl-Business-ISMN-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Tie::Cycle)

%description
See the tests in the t/ directory for examples until I add some more.

%package dev
Summary: dev components for the perl-Business-ISMN package.
Group: Development
Provides: perl-Business-ISMN-devel = %{version}-%{release}
Requires: perl-Business-ISMN = %{version}-%{release}

%description dev
dev components for the perl-Business-ISMN package.


%package license
Summary: license components for the perl-Business-ISMN package.
Group: Default

%description license
license components for the perl-Business-ISMN package.


%package perl
Summary: perl components for the perl-Business-ISMN package.
Group: Default
Requires: perl-Business-ISMN = %{version}-%{release}

%description perl
perl components for the perl-Business-ISMN package.


%prep
%setup -q -n Business-ISMN-1.202
cd %{_builddir}
tar xf %{_sourcedir}/libbusiness-ismn-perl_1.131-1.debian.tar.xz
cd %{_builddir}/Business-ISMN-1.202
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Business-ISMN-1.202/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Business-ISMN
cp %{_builddir}/Business-ISMN-1.202/LICENSE %{buildroot}/usr/share/package-licenses/perl-Business-ISMN/5001be8844666d7a7450f0ad5dd864fc7e2fa514
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Business-ISMN/11c8cf187a7784cdb888ba426eec64beae98de3d
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Business::ISMN.3
/usr/share/man/man3/Business::ISMN::Data.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Business-ISMN/11c8cf187a7784cdb888ba426eec64beae98de3d
/usr/share/package-licenses/perl-Business-ISMN/5001be8844666d7a7450f0ad5dd864fc7e2fa514

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Business/ISMN.pm
/usr/lib/perl5/vendor_perl/5.34.0/Business/ISMN/Data.pm
