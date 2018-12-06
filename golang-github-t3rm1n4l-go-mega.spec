# Run tests in check section
%bcond_with check

%global goipath         github.com/t3rm1n4l/go-mega
%global commit          854bf31d998b151cf5f94529c815bc4c67322949

%global common_description %{expand:
A client library in go for mega.co.nz storage service.}

%gometa

Name:           golang-github-t3rm1n4l-go-mega
Version:        0
Release:        0.3%{?dist}
Summary:        A client library in go for mega.co.nz storage service
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%doc README.md


%changelog
* Sat Oct 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20181006git854bf31
- Bump to commit 854bf31d998b151cf5f94529c815bc4c67322949

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git3ba4983
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1-20180530git3ba4983
- First package for Fedora

