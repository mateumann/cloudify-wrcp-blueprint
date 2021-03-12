%define _tmpdir /tmp/wrcp-blueprint
%define _patchesdir /tmp/wrcp-blueprint-patches

Name:           cloudify-wrcp-blueprint
Version:        0.0.1
Release:        1%{?dist}
Summary:        Cloudify WRCP Blueprint Add-on
Group:          Applications/Multimedia
License:        Apache 2.0
Vendor:         Cloudify Platform Ltd.
Packager:       Cloudify Platform Ltd.

BuildRequires:  git
Requires:       cloudify-rest-service


%description
Cloudify WRCP Blueprint Add-on

%prep
rm -rf %{_tmpdir}

%build
git clone https://github.com/mateumann/cloudify-wrcp-blueprint %{_tmpdir}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_patchesdir}
cp -r %{_tmpdir}/files/* %{buildroot}
cp -r %{_tmpdir}/patches/* %{buildroot}%{_patchesdir}

%clean
rm -rf %{buildroot}
rm -rf %{_tmpdir}

%post
cp -a /etc/nginx/conf.d/fileserver-location.cloudify \
      /etc/nginx/conf.d/fileserver-location.cloudify.orig && \
patch -p0 < %{_patchesdir}/fileserver-location.cloudify.patch && \
cp -a /opt/cloudify-stage/dist/appData/templates/pages/catalog.json \
      /opt/cloudify-stage/dist/appData/templates/pages/catalog.json.orig && \
patch -p0 < %{_patchesdir}/catalog.json.patch && \
rm -rf %{_patchesdir}
supervisorctl restart nginx || systemctl restart nginx

%files
/opt/manager/resources/windriver/
%{_patchesdir}
