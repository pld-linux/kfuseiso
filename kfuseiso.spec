Summary:	Small set of modules to help access ISO image files in KDE
Summary(pl.UTF-8):	Mały zbiór modułów pomagających przy dostępie do plików obrazów ISO w KDE
Name:		kfuseiso
Version:	20070117
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://ubiz.ru/dm/%{name}-%{version}.tar.bz2
# Source0-md5:	61e717d561c498f883e3bfcb536e0622
Patch0:		kde-ac260-lt.patch
Patch1:		kde-am.patch
URL:		http://www.kde-apps.org/content/show.php?content=46526
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.6.1
BuildRequires:	kdebase-devel
Requires:	fuse-iso
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small set of modules to help access ISO image files in KDE.

%description -l pl.UTF-8
Mały zbiór modułów pomagających przy dostępie do plików obrazów ISO w
KDE.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	applnkutilitiesdir=%{_desktopdir}/kde \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfuseisomount
%attr(755,root,root) %{_libdir}/kde3/kfile_iso_image.so
%{_libdir}/kde3/kfile_iso_image.la
%attr(755,root,root) %{_libdir}/kde3/kio_isomedia.so
%{_libdir}/kde3/kio_isomedia.la
%attr(755,root,root) %{_libdir}/kde3/libiso_image_plugin.so
%{_libdir}/kde3/libiso_image_plugin.la
%{_desktopdir}/kde/kfuseisomount.desktop
%{_datadir}/mimelnk/application/x-iso-image.desktop
%{_datadir}/mimelnk/inode/x-iso-image-mounted.desktop
%{_datadir}/apps/kfuseiso
%{_datadir}/apps/systemview/isomedia.desktop
%{_datadir}/services/isomedia.protocol
%{_datadir}/services/kfile_iso_image.desktop
%{_datadir}/services/iso_image_plugin.desktop
