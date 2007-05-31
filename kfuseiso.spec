#
# TODO:
# - pl descryption
#
Summary:	Small set of modules to help access ISO image files in KDE
Name:		kfuseiso
Version:	20070117
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ubiz.ru/dm/%{name}-%{version}.tar.bz2
# Source0-md5:	61e717d561c498f883e3bfcb536e0622
Patch0:		kde-ac260-lt.patch
Patch1:		kde-am.patch
URL:		http://www.kde-apps.org/content/show.php?content=46526
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-devel
Requires:	fuse-iso
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small set of modules to help access ISO image files in KDE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/kfuseisomount.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde

install -D $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/kfuseiso/index.cache.bz2 $RPM_BUILD_ROOT%{_kdedocdir}/en/kfuseiso/index.cache.bz2
install -D $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/kfuseiso/index.docbook $RPM_BUILD_ROOT%{_kdedocdir}/en/kfuseiso/index.docbook
rm -f $RPM_BUILD_ROOT%{_datadir}/doc/HTML/en/kfuseiso/index.{cache.bz2,docbook}

%find_lang %{name} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfuseisomount
%attr(755,root,root) %{_libdir}/kde3/kfile_iso_image.so
%attr(755,root,root) %{_libdir}/kde3/kfile_iso_image.la
%attr(755,root,root) %{_libdir}/kde3/kio_isomedia.so
%attr(755,root,root) %{_libdir}/kde3/kio_isomedia.la
%attr(755,root,root) %{_libdir}/kde3/libiso_image_plugin.so
%attr(755,root,root) %{_libdir}/kde3/libiso_image_plugin.la
%{_desktopdir}/kde/kfuseisomount.desktop
%{_datadir}/mimelnk/application/x-iso-image.desktop
%{_datadir}/mimelnk/inode/x-iso-image-mounted.desktop
%{_datadir}/apps/kfuseiso/media.directory
%{_datadir}/apps/kfuseiso/mount.desktop
%{_datadir}/apps/systemview/isomedia.desktop
%{_datadir}/services/isomedia.protocol
%{_datadir}/services/kfile_iso_image.desktop
%{_datadir}/services/iso_image_plugin.desktop
