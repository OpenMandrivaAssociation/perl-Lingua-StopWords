%define upstream_name    Lingua-StopWords
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Stop words for several languages
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz


BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
In keyword search, it is common practice to suppress a collection of
"stopwords": words such as "the", "and", "maybe", etc. which exist in in a
large number of documents and do not tell you anything important about any
document which contains them. This module provides such "stoplists" in
several languages.

Supported Languages
        |-----------------------------------------------------------|
        | Language   | ISO code | default encoding | also available |
        |-----------------------------------------------------------|
        | Danish     | da       | ISO-8859-1       | UTF-8          | 
        | Dutch      | nl       | ISO-8859-1       | UTF-8          | 
        | English    | en       | ISO-8859-1       | UTF-8          |
        | Finnish    | fi       | ISO-8859-1       | UTF-8          |
        | French     | fr       | ISO-8859-1       | UTF-8          |
        | German     | de       | ISO-8859-1       | UTF-8          | 
        | Hungarian  | hu       | ISO-8859-1       | UTF-8          | 
        | Italian    | it       | ISO-8859-1       | UTF-8          | 
        | Norwegian  | no       | ISO-8859-1       | UTF-8          | 
        | Portuguese | pt       | ISO-8859-1       | UTF-8          | 
        | Spanish    | es       | ISO-8859-1       | UTF-8          | 
        | Swedish    | sv       | ISO-8859-1       | UTF-8          | 
        | Russian    | ru       | KOI8-R           | UTF-8          | 
        |-----------------------------------------------------------|

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


