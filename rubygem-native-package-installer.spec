# debugsource generator messes up
%global _empty_manifest_terminate_build 0

Summary:	Ruby package installer
Name:		rubygem-native-package-installer
Version:	1.1.1
Release:	2
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		https://rubygems.org/gems/native-package-installer
Source0:	http://rubygems.org/gems/native-package-installer-%{version}.gem
BuildRequires:  rubygem-pkg-config
BuildRequires:	ruby-devel

%description
A package installtion aid

%prep
%autosetup -p1 -n %{gem_name}-%{version}%{?prerelease}

%build
%gem_build

%install
%gem_install

%files
%gem_files
