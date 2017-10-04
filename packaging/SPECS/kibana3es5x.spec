
Name:		kibana3es5x
Version:	%{__version}
Release:	%{__release}
Summary:	Kibana is a browser based analytics and search interface for Elasticsearch that was developed primarily to view Logstash event data.
Group:		Productivity/Visualization
License:	Apache-2.0
URL:		https://www.elastic.co/guide/en/kibana/3.0/kibana-guide.html
Source0:	%{name}-%{version}.tgz
BuildArchitectures: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildRequires:  tar
AutoReqProv: no

%description
Kibana is an open source (Apache Licensed), browser based analytics and search interface to Logstash and other timestamped data sets stored in ElasticSearch. With those in place Kibana is a snap to setup and start using (seriously). Kibana strives to be easy to get started with, while also being flexible and powerful

%define _install_dir /opt
%define _www_dir kibana3-es5.5

%prep
%setup -qc

%install
mkdir -vp $RPM_BUILD_ROOT%{_install_dir}
%{__cp} -r $RPM_BUILD_DIR/%{name}-%{version}/src $RPM_BUILD_ROOT%{_install_dir}/%{_www_dir}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
%{_install_dir}/%{_www_dir}
#%config(noreplace) %{_install_dir}/config.js  TODO?

%changelog
* Fri Jul 14 2017 Yaroslav 'Baya' Boychuk <baya@andatra.kiev.ua>
- first LovaCrafts RPM-Release
