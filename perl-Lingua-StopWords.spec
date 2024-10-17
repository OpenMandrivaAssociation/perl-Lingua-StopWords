%define upstream_name    Lingua-StopWords
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Stop words for several languages
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 654247
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 471176
- import perl-Lingua-StopWords


* Sun Nov 29 2009 cpan2dist 0.09-1mdv
- initial mdv release, generated with cpan2dist
