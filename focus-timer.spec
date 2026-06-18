Name:           focus-timer
Version:        1.1.2
Release:        1%{?dist}
Summary:        A time management utility based on the Pomodoro Technique

License:        GPLv3+
URL:            https://github.com/focustimerhq/FocusTimer
Source0:        https://github.com/focustimerhq/FocusTimer/archive/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  vala
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  libpeas-devel

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-controller-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(pangocairo)

Requires:       %{name}-data = %{version}-%{release}

%description
Focus Timer (formerly gnome-pomodoro) is a time-management app built 
around the Pomodoro Technique, helping you maintain focus and prevent 
burnout through structured work and break intervals.

%package data
Summary:        Data files for Focus Timer
BuildArch:      noarch
Requires:       glib2

%description data
Data files, icons, desktop integration files, schemas and translations
for Focus Timer.

%prep
%autosetup -n FocusTimer-%{version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang focus-timer

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop || :
appstream-util validate-relax %{buildroot}%{_metainfodir}/*.xml || :

%files -f focus-timer.lang
%license COPYING
%doc README.md
%{_bindir}/focus-timer

%files data
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/focus-timer/
%{_metainfodir}/*.xml
%{_datadir}/knotifications6/io.github.focustimerhq.FocusTimer.notifyrc

%changelog
* Thu Jun 18 2026 Bahram Farahmand <bahram.0098.bf@gmail.com> - 1.1.2-1
- Initial package
