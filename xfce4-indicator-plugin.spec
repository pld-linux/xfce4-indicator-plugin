Summary:	A panel plugin that uses indicator-applet to show new messages
Name:		xfce4-indicator-plugin
Version:	2.4.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-indicator-plugin/2.4/%{name}-%{version}.tar.bz2
# Source0-md5:	ee8a56be1790e6d00481241343da6db5
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-indicator-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+3-devel >= 3.18.0
BuildRequires:	intltool
BuildRequires:	libayatana-indicator-gtk3-devel >= 0.5
BuildRequires:	libtool
BuildRequires:	libxfce4ui-devel >= 4.12.0
BuildRequires:	libxfce4util-devel >= 4.12.0
BuildRequires:	xfce4-dev-tools >= 4.12.0
BuildRequires:	xfce4-panel-devel >= 4.12.0
BuildRequires:	xfconf-devel
Requires:	xfce4-panel >= 4.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A panel plugin that uses indicator-applet to show new messages.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xfce4/panel/plugins/*.la

%{__rm}	-r $RPM_BUILD_ROOT%{_localedir}/{hye,ie}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libindicator-plugin.so
%{_datadir}/xfce4/panel/plugins/indicator.desktop
%{_iconsdir}/hicolor/*x*/apps/xfce4-indicator-plugin.png
%{_iconsdir}/hicolor/scalable/apps/xfce4-indicator-plugin.svg
