Summary:	Quadrapassel - Tetris-like game for GNOME
Summary(pl.UTF-8):	Quadrapassel - podobna do Tetrisa gra dla GNOME
Name:		quadrapassel
Version:	3.36.05
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/quadrapassel/3.36/%{name}-%{version}.tar.xz
# Source0-md5:	773b76f66e081cb51160afcdd3b28014
URL:		https://wiki.gnome.org/Apps/Quadrapassel
BuildRequires:	appstream-glib
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 0.91.6
BuildRequires:	cogl-devel >= 1.0
BuildRequires:	gettext-tools
BuildRequires:	gsound-devel >= 1.0.2
BuildRequires:	gtk+3-devel >= 3.12.0
BuildRequires:	libmanette-devel >= 0.2.0
BuildRequires:	librsvg-devel >= 1:2.32.0
BuildRequires:	meson
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.12
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.24.0
BuildRequires:	vala-gsound >= 1.0.2
BuildRequires:	vala-libmanette >= 0.2.0
BuildRequires:	vala-librsvg >= 1:2.32.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	clutter >= 1.0.0
Requires:	clutter-gtk >= 0.91.6
Requires:	gsound >= 1.0.2
Requires:	gtk+3 >= 3.12.0
Requires:	hicolor-icon-theme
Requires:	libmanette >= 0.2.0
Requires:	librsvg >= 1:2.32.0
Provides:	gnome-games-gnometris
Provides:	gnome-games-quadrapassel = 1:%{version}-%{release}
Obsoletes:	gnome-games-gnometris
Obsoletes:	gnome-games-quadrapassel < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quadrapassel comes from the classic falling-block game, Tetris. The
goal of the game is to create complete horizontal lines of blocks,
which will disappear. 

%description -l pl.UTF-8
Quadrapassel wywodzi się z Tetrisa - klasycznej gry ze spadającymi
blokami. Celem jest tworzenie zapełnionych blokami poziomych rzędów,
które wtedy znikają.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md TODO.md
%attr(755,root,root) %{_bindir}/quadrapassel
%{_datadir}/glib-2.0/schemas/org.gnome.Quadrapassel.gschema.xml
%{_datadir}/metainfo/org.gnome.Quadrapassel.appdata.xml
%{_datadir}/quadrapassel
%{_desktopdir}/org.gnome.Quadrapassel.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Quadrapassel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Quadrapassel-symbolic.svg
%{_mandir}/man6/quadrapassel.6*
