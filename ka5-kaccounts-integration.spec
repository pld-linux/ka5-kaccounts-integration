#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.4
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kaccounts-integration
Summary:	Kaccounts integration
Name:		ka5-%{kaname}
Version:	23.08.4
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	0662519937e19d639a34e68378354035
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 3.20
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdeclarative-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	libaccounts-glib-devel >= 1.21
BuildRequires:	libaccounts-qt5-devel >= 1.13
BuildRequires:	libsignon-qt5-devel >= 8.55
BuildRequires:	ninja
BuildRequires:	qcoro-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Administer web accounts for the sites and services across the Plasma
desktop.

%description -l pl.UTF-8
Zarządzaj kontami internetowymi w środowisku Plazmy.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkaccounts.so.*.*.*
%dir %{_libdir}/qt5/qml/org/kde/kaccounts
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kaccounts/libkaccountsdeclarativeplugin.so
%{_libdir}/qt5/qml/org/kde/kaccounts/qmldir
%dir %{_datadir}/kpackage/kcms/kcm_kaccounts
%dir %{_datadir}/kpackage/kcms/kcm_kaccounts/contents
%dir %{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/AvailableAccounts.qml
%ghost %{_libdir}/libkaccounts.so.2
%dir %{_libdir}/qt5/plugins/kaccounts
%dir %{_libdir}/qt5/plugins/kaccounts/daemonplugins
%{_libdir}/qt5/plugins/kaccounts/daemonplugins/kaccounts_kio_webdav_plugin.so
%{_libdir}/qt5/plugins/kf5/kded/kded_accounts.so
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/AccountDetails.qml
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/MessageBoxSheet.qml
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/RemoveAccountDialog.qml
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/RenameAccountDialog.qml
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_kaccounts.so
%{_datadir}/kpackage/kcms/kcm_kaccounts/contents/ui/main.qml
%{_desktopdir}/kcm_kaccounts.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KAccounts
%{_libdir}/cmake/KAccounts
%{_libdir}/libkaccounts.so
