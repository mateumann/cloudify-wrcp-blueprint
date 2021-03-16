Name:           cloudify-wrcp-blueprint
Version:        0.0.1
Release:        1%{?dist}

Summary:        Cloudify WRCP Blueprint Add-on
License:        Apache 2.0
Group:          Applications/Multimedia
Vendor:         Cloudify Platform Ltd.
Packager:       Cloudify Platform Ltd.

Source0:        README.md
Source1:        wrcp-examples.json
Source2:        wrcp.png
Source3:        wrcp.zip
Source4:        catalog.json.patch
Source5:        etc-fileserver-location.cloudify.patch
Source6:        template-fileserver-location.cloudify.patch

Requires:       cloudify-rest-service

%define _windriverdir /opt/manager/resources/windriver
%define _patchesdir   /tmp/wrcp-blueprint-patches

%description
Cloudify WRCP Blueprint Add-on


%prep

%build

%install
mkdir -p %{buildroot}%{_windriverdir}
install -m 644 %{SOURCE0} %{buildroot}%{_windriverdir}
install -m 644 %{SOURCE1} %{buildroot}%{_windriverdir}
install -m 644 %{SOURCE2} %{buildroot}%{_windriverdir}
install -m 644 %{SOURCE3} %{buildroot}%{_windriverdir}
mkdir -p %{buildroot}%{_patchesdir}
install -m 644 %{SOURCE4} %{buildroot}%{_patchesdir}
install -m 644 %{SOURCE5} %{buildroot}%{_patchesdir}
install -m 644 %{SOURCE6} %{buildroot}%{_patchesdir}

%post
cp -a /etc/nginx/conf.d/fileserver-location.cloudify \
      /etc/nginx/conf.d/fileserver-location.cloudify.orig && \
patch -p0 < %{_patchesdir}/etc-fileserver-location.cloudify.patch
cp -a /opt/cloudify/cfy_manager/lib/python3.6/site-packages/cfy_manager/components/nginx/config/fileserver-location.cloudify \
      /opt/cloudify/cfy_manager/lib/python3.6/site-packages/cfy_manager/components/nginx/config/fileserver-location.cloudify.orig && \
patch -p0 < %{_patchesdir}/template-fileserver-location.cloudify.patch
cp -a /opt/cloudify-stage/dist/appData/templates/pages/catalog.json \
      /opt/cloudify-stage/dist/appData/templates/pages/catalog.json.orig && \
patch -p0 < %{_patchesdir}/catalog.json.patch
supervisorctl restart nginx || systemctl restart nginx

%postun
mv /etc/nginx/conf.d/fileserver-location.cloudify.orig \
   /etc/nginx/conf.d/fileserver-location.cloudify
mv /opt/cloudify/cfy_manager/lib/python3.6/site-packages/cfy_manager/components/nginx/config/fileserver-location.cloudify.orig \
   /opt/cloudify/cfy_manager/lib/python3.6/site-packages/cfy_manager/components/nginx/config/fileserver-location.cloudify
mv /opt/cloudify-stage/dist/appData/templates/pages/catalog.json.orig \
   /opt/cloudify-stage/dist/appData/templates/pages/catalog.json
supervisorctl restart nginx || systemctl restart nginx

%files
%{_windriverdir}
%{_patchesdir}
