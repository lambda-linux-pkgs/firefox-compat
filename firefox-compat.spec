%define _buildid .1

#
# https://www.mozilla.org/en-US/firefox/35.0/system-requirements/
#
%global gtk2_version 2.24.22
%global pango_version 1.34.1

#
# Dependencies
#
%global fontconfig_version 2.10.95
%global gdk_pixbuf2_version 2.28.2
%global atk_version 2.8.0
%global hicolor_icon_theme_version 0.12

#
# Others
#
%global dbus_glib_version 0.86
%global libXt_version 1.1.4
%global xorg_x11_xauth_version 1.0.2

Name:           firefox-compat
Version:        1.0
Release:        0%{?_buildid}%{?dist}
Summary:        Meta package to install Firefox dependencies

Group:          Applications/Internet
License:        GPL+
URL:            http://www.mozilla.org/projects/firefox/

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires: gtk2 >= %{gtk2_version}
Requires: pango >= %{pango_version}

Requires: fontconfig >= %{fontconfig_version}
Requires: gdk-pixbuf2 >= %{gdk_pixbuf2_version}
Requires: atk >= %{atk_version}
Requires: hicolor-icon-theme >= %{hicolor_icon_theme_version}

Requires: dbus-glib >= %{dbus_glib_version}
Requires: libXt >= %{libXt_version}
Requires: xorg-x11-xauth >= %{xorg_x11_xauth_version}

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

Meta package to install Firefox dependencies

%prep
exit 0

%build
exit 0

%install
rm -rf %{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)

%changelog