#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-labeling
Version  : 0.4.2
Release  : 83
URL      : https://cran.r-project.org/src/contrib/labeling_0.4.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/labeling_0.4.2.tar.gz
Summary  : Axis Labeling
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n labeling
cd %{_builddir}/labeling

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641042690

%install
export SOURCE_DATE_EPOCH=1641042690
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library labeling
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library labeling
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library labeling
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc labeling || :


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
