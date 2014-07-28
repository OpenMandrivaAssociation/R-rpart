%global packname  rpart
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.1.8
Release:          1
Summary:          Recursive Partitioning and Regression Trees
Group:            Sciences/Mathematics
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.1-8.tar.gz

Requires:         R-graphics R-stats R-grDevices 

Requires:         R-survival 
BuildRequires:    R-devel Rmath-devel R-graphics R-stats R-grDevices

BuildRequires:   R-survival 
%description
Recursive partitioning for classification, regression and survival trees. 
An implementation of most of the functionality of the 1984 book by
Breiman, Friedman, Olshen and Stone.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
