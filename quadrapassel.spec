Summary:	Quadrapassel - Tetris-like game for GNOME
Summary(pl.UTF-8):	Quadrapassel - podobna do Tetrisa gra dla GNOME
Name:		quadrapassel
Version:	3.12.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/quadrapassel/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	811bf8a8d30c245ec4a1ec599a115b76
URL:		https://wiki.gnome.org/Apps/Quadrapassel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 0.91.6
BuildRequires:	gettext-tools
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	vala >= 2:0.16.0
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	clutter >= 1.0.0
Requires:	clutter-gtk >= 0.91.6
Requires:	gtk+3 >= 3.10.0
Requires:	hicolor-icon-theme
Requires:	libcanberra-gtk3 >= 0.26
Requires:	librsvg >= 2.32.0
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
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/quadrapassel
%{_datadir}/appdata/quadrapassel.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.quadrapassel.gschema.xml
%{_datadir}/quadrapassel
%{_desktopdir}/quadrapassel.desktop
%{_iconsdir}/HighContrast/*/apps/quadrapassel.png
%{_iconsdir}/hicolor/*/apps/quadrapassel.png
%{_iconsdir}/hicolor/scalable/apps/quadrapassel.svg
%{_mandir}/man6/quadrapassel.6*
