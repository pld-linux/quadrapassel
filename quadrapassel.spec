Summary:	GNOME Tetris
Summary(pl.UTF-8):	Tetris dla GNOME
Name:		quadrapassel
Version:	3.10.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/quadrapassel/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	bc5c70e5fc5951f6c38f750496fc8747
URL:		https://live.gnome.org/Quadrapassel
BuildRequires:	autoconf
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 0.91.6
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	vala >= 2:0.16.0
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Provides:	gnome-games-gnometris
Provides:	gnome-games-quadrapassel = 1:%{version}-%{release}
Obsoletes:	gnome-games-gnometris
Obsoletes:	gnome-games-quadrapassel < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tetris like game.

%description -l pl.UTF-8
Gra podobna do Tetrisa.

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
%{_iconsdir}/HighContrast/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
%{_mandir}/man6/quadrapassel.6*
