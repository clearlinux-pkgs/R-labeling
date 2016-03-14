#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-labeling
Version  : 0.3
Release  : 16
URL      : http://cran.r-project.org/src/contrib/labeling_0.3.tar.gz
Source0  : http://cran.r-project.org/src/contrib/labeling_0.3.tar.gz
Summary  : Axis Labeling
Group    : Development/Tools
License  : MIT
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n labeling

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library labeling
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library labeling


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/labeling/DESCRIPTION
/usr/lib64/R/library/labeling/INDEX
/usr/lib64/R/library/labeling/LICENSE
/usr/lib64/R/library/labeling/Meta/Rd.rds
/usr/lib64/R/library/labeling/Meta/hsearch.rds
/usr/lib64/R/library/labeling/Meta/links.rds
/usr/lib64/R/library/labeling/Meta/nsInfo.rds
/usr/lib64/R/library/labeling/Meta/package.rds
/usr/lib64/R/library/labeling/NAMESPACE
/usr/lib64/R/library/labeling/R/labeling
/usr/lib64/R/library/labeling/R/labeling.rdb
/usr/lib64/R/library/labeling/R/labeling.rdx
/usr/lib64/R/library/labeling/help/AnIndex
/usr/lib64/R/library/labeling/help/aliases.rds
/usr/lib64/R/library/labeling/help/labeling.rdb
/usr/lib64/R/library/labeling/help/labeling.rdx
/usr/lib64/R/library/labeling/help/paths.rds
/usr/lib64/R/library/labeling/html/00Index.html
/usr/lib64/R/library/labeling/html/R.css
