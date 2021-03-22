# Wind River Cloud Platform Blueprint package

This is a source for the `cloudify-wrcp-blueprint` RPM package.  The purpose of this package is having a WRCP blueprint “baked in” a Cloudify installation at Wind River.

## Repository contents

`packaging/cloudify-wrcp-blueprint.spec`    RPM `.spec` file (a recipe for a RPM package)

### Wind River files

`README.md` is a file which is going to be used as a description for the Wind-River-Cloud-Platform blueprint (displayed when the user clicks the small letter `i` to the bottom left of the blueprint tile in the UI).

`wrcp-examples.json`    is a file used by Cloudify Web UI to display the *WRCP Blueprints* catalog tile.

`wrcp.png`  an image/logo used in the *WRCP Blueprints* catalog tile.

`wrcp.zip`  a packed WRCP blueprint – a `.zip` file containing **a WRCP blueprint**.  Currently the `blueprint.yaml` file inside the `wrcp.zip` is a copy of https://github.com/cloudify-cosmo/cloudify-starlingx-plugin/blob/master/examples/blueprint.yaml.

### Patches

`catalog.json.patch`    A patch that upon RPM installation is going to be applied onto `/opt/cloudify-stage/dist/appData/templates/pages/catalog.json` file which describes the contents of *Cloudify Catalog* tab in the Cloudify Web UI.

`etc-fileserver-location.cloudify.patch`    Another patch that will be applied onto `/etc/nginx/conf.d/fileserver-location.cloudify` file to make the contents of `/opt/manager/resources/windriver/` available as `http(s)://[MANAGER_IP]/resources/windriver/` without authorization requirement.

`template-fileserver-location.cloudify.patch`    Very similar to the `etc-fileserver-location.cloudify.patch` but applied onto `/opt/cloudify/cfy_manager/lib/python3.6/site-packages/cfy_manager/components/nginx/config/fileserver-location.cloudify` in order to change this configuration template.


## Usage

### Build process

These files shall be used in standard RPM build process.  See the `.circleci/config.yml` for build process configuration example.

### Installation

The package shall be installed on a machine where the Cloudify Manager already exists.  This requirement is embedded in the `.spec` file itself, and will prevent the installation unless the `cloudify-rest-service` package is already installed.

The contents of the three files modified during the installation is archived in the `.orig` files.  It is used during uninstallation process to restore previous state of the system.

#### Example commands

```
$ sudo yum install cloudify-manager-install-*.rpm
$ cfy_manager install
$ sudo yum install cloudify-wrcp-blueprint-*.rpm
```

### Uninstallation

The uninstallation process tries restoring three original copies of modified files:

 * `/etc/nginx/conf.d/fileserver-location.cloudify.orig`
 * `/opt/cloudify/cfy_manager/lib/python3.6/site-packages/cfy_manager/components/nginx/config/fileserver-location.cloudify.orig`
 * `/opt/cloudify-stage/dist/appData/templates/pages/catalog.json.orig`
 
