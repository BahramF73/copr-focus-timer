Name:           gnome-shell-extension-focus-timer
Version:        2
Release:        1%{?dist}
Summary:        GNOME Shell extension for Focus Timer

License:        GPLv3+
URL:            https://github.com/focustimerhq/gnome-shell-extension-focus-timer
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(gio-2.0)

Requires:       gnome-shell

%description
GNOME Shell extension for Focus Timer. It adds an indicator to the
GNOME Shell panel and integrates with the Focus Timer application.

%prep
%autosetup -n gnome-shell-extension-focus-timer-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
true

%files
%license COPYING*
%doc README*
%{_datadir}/gnome-shell/extensions/focus-timer@focustimerhq.github.io/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.focus-timer.gschema.xml

%changelog
* Thu Jun 18 2026 Bahram Farahmand <bahram.0098.bf@gmail.com> - 2-1
- Initial package