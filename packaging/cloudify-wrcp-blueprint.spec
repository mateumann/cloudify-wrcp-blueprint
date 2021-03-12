%define _tmpdir /tmp/wrcp-blueprint

Name:           cloudify-wrcp-blueprint
Version:        0.0.1
Release:        1%{?dist}
Summary:        Cloudify WRCP Blueprint Add-on
Group:          Applications/Multimedia
License:        Apache 2.0
#URL:            https://github.com/cloudify-cosmo/cloudify-manager-install
Vendor:         Cloudify Platform Ltd.
Packager:       Cloudify Platform Ltd.

BuildRequires:  git
Requires(pre):  cloudify-manager


%description
Cloudify WRCP Blueprint Add-on

%build
echo "Building"
git clone https://github.com/mateumann/cloudify-wrcp-blueprint ${RPM_SOURCE_DIR}/cloudify-wrcp-blueprint
mkdir -p %{buildroot}/qwe
cp -r ${RPM_SOURCE_DIR}/files/* %{buildroot}/
pwd
ls

%install
echo "Installing"
mkdir -p %{buildroot}/asd
cp -r ${RPM_SOURCE_DIR}/files/* %{buildroot}/
pwd
ls

%files
/etc/nginx/conf.d/fileserver-location.cloudify
/opt/cloudify-stage/dist/appData/templates/pages/catalog.json
/opt/manager/resources/windriver/
