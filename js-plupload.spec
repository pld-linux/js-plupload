%define		ver	%(echo %{version} | tr . _)
%define		plugin	plupload
Summary:	Multiple file upload utility using Flash, Silverlight, Google Gears, HTML5 or BrowserPlus
Name:		js-%{plugin}
Version:	1.5.3
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	https://github.com/downloads/moxiecode/plupload/plupload_%{ver}.zip
# Source0-md5:	7cbc00bbf7b42a995cb84b6a6539b0cb
Source1:	apache.conf
Source2:	lighttpd.conf
URL:		http://www.plupload.com/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	webapps
Requires:	webserver(access)
Suggests:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		plupload
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir		%{_datadir}/%{_webapp}

%description
Plupload is a JavaScript API for dealing with file uploads it supports
features like multiple file selection, file type filtering, request
chunking, client side image scaling and it uses different runtimes to
achieve this such as HTML 5, Silverlight, Flash, Gears and
BrowserPlus.

%package demo
Summary:	Demo for %{plugin}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description demo
Demonstrations and samples for %{plugin}.

%prep
%setup -qc
mv %{_webapp}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}}

cp -a js/* $RPM_BUILD_ROOT%{_appdir}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/lighttpd.conf
cp -p $RPM_BUILD_ROOT%{_sysconfdir}/{apache,httpd}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%doc readme.md changelog.txt
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf
%dir %{_appdir}
%{_appdir}/jquery.plupload.queue
%{_appdir}/jquery.ui.plupload
%{_appdir}/plupload.*js
%{_appdir}/plupload.*swf
%{_appdir}/plupload.*xap

%dir %{_appdir}/i18n
%lang(cs) %{_appdir}/i18n/cs.js
%lang(da) %{_appdir}/i18n/da.js
%lang(de) %{_appdir}/i18n/de.js
%lang(el) %{_appdir}/i18n/el.js
%lang(es) %{_appdir}/i18n/es.js
%lang(et) %{_appdir}/i18n/et.js
%lang(fa) %{_appdir}/i18n/fa.js
%lang(fi) %{_appdir}/i18n/fi.js
%lang(fr) %{_appdir}/i18n/fr.js
%lang(fr_CA) %{_appdir}/i18n/fr-ca.js
%lang(hr) %{_appdir}/i18n/hr.js
%lang(hu) %{_appdir}/i18n/hu.js
%lang(it) %{_appdir}/i18n/it.js
%lang(ja) %{_appdir}/i18n/ja.js
%lang(ko) %{_appdir}/i18n/ko.js
%lang(lv) %{_appdir}/i18n/lv.js
%lang(nl) %{_appdir}/i18n/nl.js
%lang(pl) %{_appdir}/i18n/pl.js
%lang(pt_BR) %{_appdir}/i18n/pt-br.js
%lang(ro) %{_appdir}/i18n/ro.js
%lang(ru) %{_appdir}/i18n/ru.js
%lang(sr) %{_appdir}/i18n/sr.js
%lang(sv) %{_appdir}/i18n/sv.js

%files demo
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
