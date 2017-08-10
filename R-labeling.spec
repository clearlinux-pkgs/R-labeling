#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-labeling
Version  : 0.3
Release  : 37
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
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502407023

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502407023
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library labeling
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library labeling
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library labeling
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/labeling/DESCRIPTION
/usr/lib64/R/library/labeling/INDEX
/usr/lib64/R/library/labeling/LICENSE
/usr/lib64/R/library/labeling/Meta/Rd.rds
/usr/lib64/R/library/labeling/Meta/features.rds
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
